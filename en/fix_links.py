"""Point each relative link in en/**/*.md at the English page if it exists, else the Chinese original.

Idempotent: rerun after each translation batch so links switch over as pages get translated.
"""

import os
import re
import sys

EN = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(EN)
LINK = re.compile(r"\]\((<?)([^)\s>#]*)(#[^)\s>]*)?(>?)\)")
HREF = re.compile(r'(\bhref=")([^"#]*)(#[^"]*)?"')
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")
_slugs = {}


def slugs(path):
    """GitHub-style heading anchors of a file: {slug: line_no} and {line_no: slug}.

    en/ translations keep line N = translation of line N, so the same line number maps an anchor across languages.
    """
    if path not in _slugs:
        by_slug, by_line, seen, fence = {}, {}, {}, False
        with open(path, encoding="utf-8") as f:
            for i, line in enumerate(f):
                if line.lstrip().startswith("```"):
                    fence = not fence
                for explicit in re.findall(r'\b(?:id|name)="([^"]+)"', line):
                    by_slug.setdefault(explicit, i)
                m = None if fence else HEADING.match(line)
                if not m:
                    continue
                text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", m.group(1))
                slug = re.sub(r"[^\w\- ]", "", text.strip().lower()).replace(" ", "-")
                n = seen.get(slug, 0)
                seen[slug] = n + 1
                slug = f"{slug}-{n}" if n else slug
                by_slug[slug], by_line[i] = i, slug
        _slugs[path] = (by_slug, by_line)
    return _slugs[path]


def map_anchor(anchor, target_abs):
    """Rewrite an anchor written against the Chinese original to the English file's heading on the same line."""
    if not anchor or not target_abs.startswith(EN + os.sep) or not target_abs.endswith(".md"):
        return anchor
    orig = os.path.join(ROOT, os.path.relpath(target_abs, EN))
    if not os.path.exists(orig) or anchor[1:] in slugs(target_abs)[0]:
        return anchor
    line = slugs(orig)[0].get(anchor[1:])
    return "#" + slugs(target_abs)[1].get(line, anchor[1:]) if line is not None else anchor


def resolve(file_dir, target):
    abs_t = os.path.normpath(os.path.join(file_dir, target))
    rel = os.path.relpath(abs_t, EN if abs_t.startswith(EN + os.sep) else ROOT)
    if rel.startswith(".."):
        return target
    for cand in (os.path.join(EN, rel), os.path.join(ROOT, rel)):
        if os.path.exists(cand):
            return os.path.relpath(cand, file_dir)
    return target


def fix(path):
    d = os.path.dirname(path)
    with open(path, encoding="utf-8") as f:
        s = f.read()

    def sub(m):
        lt, target, anchor, gt = m.groups()
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or not (target or anchor):
            return m.group(0)
        new_t = resolve(d, target) if target else ""
        anchor = map_anchor(anchor, os.path.normpath(os.path.join(d, new_t)) if new_t else path)
        return f"]({lt}{new_t}{anchor or ''}{gt})"

    def sub_href(m):
        target, anchor = m.group(2), m.group(3)
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or not (target or anchor):
            return m.group(0)
        new_t = resolve(d, target) if target else ""
        anchor = map_anchor(anchor, os.path.normpath(os.path.join(d, new_t)) if new_t else path)
        return f'{m.group(1)}{new_t}{anchor or ""}"'

    new = HREF.sub(sub_href, LINK.sub(sub, s))
    if new != s:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
    broken = []
    for _, t, a, _ in LINK.findall(new):
        if re.match(r"^[a-z][a-z0-9+.-]*:", t) or not (t or a):
            continue
        tp = os.path.normpath(os.path.join(d, t)) if t else path
        if not os.path.exists(tp):
            broken.append(t)
        elif a and tp.endswith(".md") and a[1:] not in slugs(tp)[0]:
            broken.append(t + a)
    return broken


total = 0
for root, _, files in os.walk(EN):
    for name in files:
        if name.endswith(".md"):
            p = os.path.join(root, name)
            for t in fix(p):
                total += 1
                print(f"BROKEN {os.path.relpath(p, ROOT)} -> {t}")
print(f"broken links: {total}")
sys.exit(1 if total else 0)
