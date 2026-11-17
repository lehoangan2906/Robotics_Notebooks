# Learning Roadmaps Overview

This directory holds the learning-roadmap design for `Robotics_Notebooks`.

## Roadmap design principles

- Ultimate goal: full-stack robotics engineer
- Current entry point: robot motion-control algorithm engineer
- Current focus: motion control, reinforcement learning, imitation learning, humanoid robots

## Main roadmap (core)

- **[Main roadmap: Motion Control → Physical AI Full-Stack Growth Path](motion-control.md)** (Physical AI & Robot Learning)  
  Covers the full sequence of stages: L−1 prologue → L0–L6 trunk → L7 exit → L8–L12 Physical AI extension. It spans the classical-control trunk of humanoid motion control (LIP/ZMP → Centroidal → MPC → TSID/WBC), the RL/IL extensions and hands-on sim2real, then goes up to Transformer / motion generation (Diffusion · Flow Matching · DiT) / VLA (π0 · GR00T) / world models (Cosmos), and down to real-robot deployment with ONNX / ROS2 / real-time buses.

## Depth roadmaps (pick one by goal and go deep)

The main roadmap favors "get the trunk working first". The thirty depth roadmaps below are **each independent**, branch off from some stage of the main roadmap, and can be read on their own.

Ordering: sorted by the **historical order of each direction's starting milestone** (consistent with the homepage buttons and the README). The earlier a direction appears, the deeper its theoretical foundation; the later it appears, the more it depends on learning methods and compute:

- [If your goal is PCB design (zero circuit background → first board → schematic → layout → debugging → power / high-speed / EMC → mass production)](depth-pcb-design.md) — go from never having drawn a board to independently delivering robot driver boards, sensor boards, and main-controller carrier boards (starting point: Eisler's printed-circuit patent, 1936)
- [If your goal is teleoperation (humanoid whole-body teleoperation + finger teleoperation → demonstration data / real-time takeover)](depth-teleoperation.md) — let a human control a humanoid in real time and collect high-quality demonstration data (starting point: Goertz master–slave manipulator teleoperation, 1954)
- [If your goal is rocket landing control (powered-descent guidance → lossless convexification → 6-DoF successive convexification → attitude and thrust vectoring → navigation and onboard solvers → full-profile recovery)](depth-rocket-landing.md) — make a rocket return autonomously and land upright on a designated spot (starting point: Apollo Lunar Module powered-descent guidance, 1969)
- [If your goal is torque-controlled motor design (specs → electromagnetic/thermal → FOC torque loop → joint module)](depth-torque-motor-design.md) — take a joint motor from task specs all the way to an acceptance-tested torque-loop module (starting point: field-oriented control FOC, 1971)
- [If your goal is classical model-based control (LIP/ZMP → MPC → WBC)](depth-classical-control.md) — systematically master the model-based humanoid control trunk (starting point: ZMP criterion, 1972)
- [If your goal is whole-humanoid hardware design (spec budget → mechanical → electrical → communication → system acceptance)](depth-humanoid-hardware-design.md) — turn a task requirement into a complete robot that powers on, runs control, and can be delivered (starting point: WABOT-1 full-scale humanoid, 1973)
- [If your goal is safe control (CLF / CBF / Safe RL)](depth-safe-control.md) — add provable safety constraints (starting point: CLF, 1983)
- [If your goal is RSI (recursive self-improvement)](depth-rsi.md) — have "the improvement mechanism itself" improved automatically, and apply that loop to real-robot policies (starting point: EURISKO self-modifying heuristics, 1983)
- [If your goal is contact-rich manipulation](depth-contact-manipulation.md) — do fine-grained contact tasks such as assembly, insertion/removal, and bimanual coordination (starting point: impedance control, 1985)
- [If your goal is navigation (SLAM → Nav2 → VLN → navigation VLA)](depth-navigation.md) — let the robot know where it is and where to go (starting point: probabilistic SLAM, 1986)
- [If your goal is model architecture (backbone family tree → perception encoders → action heads → multimodal foundations → scaled deployment)](depth-model-architecture.md) — know which network a policy should use, how wide and deep, and how actions are output (starting point: backpropagation, 1986)
- [If your goal is imitation learning and skill transfer](depth-imitation-learning.md) — learn skills from human demonstration data (starting point: behavior cloning, 1988)
- [If your goal is RL motion control](depth-rl-locomotion.md) — drive humanoid locomotion with reinforcement learning (starting point: Q-learning, 1989)
- [If your goal is Loco-Manipulation (mobile manipulation)](depth-loco-manipulation.md) — let the robot manipulate while walking (starting point: coordinated control of mobile manipulators, 1994)
- [If your goal is humanoid soccer (omnidirectional walking → perceptive kicking → multi-robot tactics)](depth-humanoid-soccer.md) — let robots chase the ball, shoot, and play a full match (starting point: first RoboCup, 1997)
- [If your goal is motion retargeting (human motion → robot reference trajectories)](depth-motion-retargeting.md) — turn human/animal motion capture and video motion into executable references for humanoids or quadrupeds (starting point: Gleicher motion retargeting, 1998)
- [If your goal is humanoid swarm performance (synchronized group dance → formation moves → group stunts)](depth-humanoid-swarm-performance.md) — have a group of humanoids dance together on stage, change formations, and perform coordinated stunts (starting point: 540 Alpha 1S robots dancing at the CCTV Spring Festival Gala, 2016)
- [If your goal is cross-embodiment transfer (embodiment-gap profiling → unified interface → morphology-aware architectures → multi-embodiment co-training → human→robot transfer → new-embodiment adaptation)](depth-cross-embodiment.md) — let one policy adapt to different embodiments, so swapping grippers, robot models, or morphologies doesn't require retraining from scratch (starting point: Devin et al. modular multi-robot policy transfer, ICRA 2017)
- [If your goal is Sim2Real (domain-gap profiling → actuator alignment → robust training → real-robot deployment)](depth-sim2real.md) — reliably move a policy trained in simulation onto a real robot (starting point: domain randomization DR, 2017)
- [If your goal is humanoid boxing (motion tracking → latent-space skills → adversarial self-play)](depth-humanoid-boxing.md) — have two humanoids spar in a ring like humans (starting point: MuJoCo humanoid adversarial self-play, 2017)
- [If your goal is ICL (embodied in-context learning)](depth-icl.md) — let a robot perform a new task after reading a single demonstration, without touching the weights (starting point: One-Shot Imitation Learning, NeurIPS 2017)
- [If your goal is BFM (humanoid behavior foundation models)](depth-bfm.md) — control a humanoid's whole body with a single checkpoint (starting point: DeepMimic motion-tracking lineage, 2018)
- [If your goal is embodied model evaluation (cognition → world models → policy success rate → motion-control metrics → sim↔real calibration)](depth-embodied-eval.md) — prove or disprove whether an embodied model (including motion-control models such as locomotion / whole-body tracking) is actually good (starting point: RLBench standardized visual manipulation benchmark suite, 2019)
- [If your goal is perceptive locomotion](depth-perceptive-locomotion.md) — let the robot look at the terrain to climb stairs, cross obstacles, and do parkour (starting point: the 2020s wave of perceptive policies)
- [If your goal is motion generation (text/multimodal → humanoid motion)](depth-motion-generation.md) — use generative models to create human/humanoid motion (starting point: MDM diffusion motion generation, 2022)
- [Diffusion & Flow Matching policies](depth-robotics-diffusion-dit-flow.md) — read DP / DiT-Block / RDT / π₀ / GR00T / Dita following the evolution of action-denoising mechanisms (starting point: Diffusion Policy, 2023)
- [If your goal is VLA (vision-language-action models)](depth-vla.md) — let the robot understand instructions and do the work (starting point: RT-2 establishing VLA, 2023)
- [If your goal is Real2Sim (simulatability criteria → geometry/appearance reconstruction → physical properties and articulation → scene/episode twins → retraining and evaluation)](depth-real2sim.md) — compress the real world into trainable / evaluable simulation assets (starting point: large-scale 3D Gaussian Splatting reconstruction, 2023)
- [If your goal is embodied data (pyramid tiers → collection → cleaning and annotation → format aggregation → augmentation and synthesis → mixture flywheel)](depth-embodied-data.md) — build a deliverable data-supply pipeline for embodied models (starting point: Open X-Embodiment cross-embodiment data aggregation, 2023)
- [If your goal is WAM (world–action models)](depth-wam.md) — let a policy explicitly predict how the world will change before it acts (starting point: formalization in the World Action Models survey, 2026)

Note: the main roadmap's **L−1 panorama layer**, **L7 exit layer**, and **L8–L12 Physical AI extension layers** provide a full-stack bird's-eye view; directions such as navigation, perceptive locomotion, and hardware are entered via the existing depth roadmaps above. For role entry points and portfolio planning aimed at people with mechanical, electrical, testing, and manufacturing backgrounds, see the [Humanoid Engineering Practitioner Entry sub-roadmap](../../wiki/roadmaps/humanoid-practitioner-entry-roadmap.md).
