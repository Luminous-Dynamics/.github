# Luminous Dynamics Benchmark Programme

**Status:** Research and product-evaluation plan, 2 November 2026. Targets below are proposed gates, not achieved results.

## Benchmark philosophy

We want to improve on the state of the art by producing better outcomes under declared constraints—not by selecting favorable metrics or comparing unlike workloads.

Every public result should include:

- Exact repository, commit, release, and build configuration.
- Dataset, workload, split, and input digests.
- Hardware, OS, compiler/runtime, driver, and power mode.
- Baselines, tuning budget, and command lines.
- At least 5 warm-up runs and 30 measured repetitions when the workload permits; publish raw samples and confidence intervals.
- p50, p95, p99 where meaningful; throughput; peak memory; energy per completed task when measurable.
- Accuracy or correctness criteria, not performance alone.
- Negative controls and failure-injection cases.
- A machine-readable result artifact plus human-readable analysis.
- Explicit non-comparable, missing, and unverified conditions.

For noisy or expensive experiments, publish the sampling plan and stopping rule before observing results. Report medians and uncertainty intervals; do not silently discard outliers. Use paired comparisons on identical hardware and workloads. Do not compare a microbenchmark to an end-to-end system benchmark.

## Portfolio-wide outcome metrics

1. **Cost per accepted outcome** — full compute, energy, operator time, and service costs divided by outcomes that passed predeclared quality checks.
2. **Evidence latency** — time from input capture to independently verifiable result.
3. **Reproducibility rate** — fraction of sampled runs reproduced within a predeclared bitwise or numerical tolerance.
4. **False-accept rate** — invalid or adversarial cases incorrectly accepted; must have explicit denominator and confidence interval.
5. **Recovery time and blast radius** — time and scope needed to return to a known-good state after injected failures.
6. **Human burden** — operator review time, intervention count, and override rate.
7. **Energy per useful result** — measured joules per accepted task, not per token, tick, or simulation step alone.

## Project benchmark matrix

### Luminous Platform / Nixward / Sovereign Boot

**Comparators:** Native NixOS generations and rollback, deploy-rs, Colmena, Morph, Comin, Bento, and appropriate managed fleet tooling. The NixOS Wiki lists these as current deployment options; their feature scopes differ, so use capability matrices and matched scenarios rather than forcing a single scalar ranking. [NixOS operations tools](https://wiki.nixos.org/wiki/Applications).

**Workloads:** Single-host and multi-host configuration change; drift detection; partial network partition; stale lockfile/input; invalid authorization; interrupted activation; failed health check; disk pressure; host reboot during transition; rollback and recovery.

**Metrics:** Change success, p50/p95 transition time, recovery time, false-positive drift rate, operator interventions, exact input reproducibility, and unauthorized mutation count.

**Hard gates:** Zero unauthorized mutations in the test corpus; every injected denial remains denied; no promotion when post-change verification fails; recovery returns to an identified generation or declares unrecovered state. A zero observed false-accept count is not a proof of zero risk—publish test count and confidence bounds.

**Target direction:** At parity on ordinary deployment speed, materially better evidence completeness, policy-denial behavior, and measured recovery on failure-injection workloads. Avoid trading safety for speed.

The focused [ITOPS Autonomy Boundary Benchmark v0.1](https://github.com/Luminous-Dynamics/luminous-platform/tree/main/benchmarks/itops-autonomy-boundary-v0.1) is the domain-specific protocol for agentic IT operations. It records agent decisions, runtime-gate behavior, independent participant-side effects, service observations, human handoff, and resource use. It now includes a 20-case candidate scenario catalog, a JSON Schema, and a small Rust catalog linter that checks cross-field safety invariants and emits the exact corpus digest. The catalog is still marked candidate/not frozen; the linter is not an agent runner, and no public benchmark measurements or SOTA claims exist yet.

### Symthaea

**Comparators:** Task-appropriate conventional ML models, strong small language models, HDC baselines, standard continual-learning algorithms, and task-specific hand-engineered baselines. Include a strong model when semantics require it; do not compare unlike tasks. HDC is an active research area, not a demonstrated universal replacement for deep learning; the 2026 survey literature discusses both efficiency opportunities and architecture limitations.

**Workloads:** HDC associative recall; compositional binding/unbinding; temporal sequence prediction; continual learning with task/domain shifts; calibration under OOD inputs; constrained-device inference; adversarial and corrupted memory queries. Add realistic online/continual task sequences where later tasks depend on earlier experience; include [Continual Learning Bench 1.0](https://sky.cs.berkeley.edu/project/continual-learning-bench/) as a candidate external task source, subject to its license and harness compatibility.

**Metrics:** Task quality, energy per accepted task, p50/p95 latency, peak RAM/VRAM, model size, update cost, forgetting (e.g. average accuracy drop on prior tasks), calibration error, OOD risk-coverage, and recovery from corrupted memory.

**Hard gates:** Dataset and split digests pinned; leakage audit; baseline tuning budget disclosed; no consciousness or AGI conclusion inferred from task metrics; claims about privacy proofs include proof verification and leakage assumptions.

**Target direction:** Find workload regimes where HDC + liquid dynamics has a measured cost-quality advantage at matched accuracy or a quality advantage at matched energy/latency. If it does not, narrow the claim to the workloads where it does.

**SOTA interpretation:** A 2026 survey reviews HDC architectures, performance, efficiency and known limitations; it is a research map, not a leaderboard. Our claim should be a workload-specific Pareto improvement, independently reproduced, with ablations for HDC-only, liquid dynamics-only, hybrid, and conventional baselines. Report where the model loses as well as where it wins.

### Mycelix

**Comparators:** Centralized relational services, conventional signed event logs, W3C VC Data Model 2.0 implementations, W3C Data Integrity implementations with a named cryptosuite, OpenID4VCI/OpenID4VP implementations where relevant, and Holochain-native patterns.

**Workloads:** Credential issue/hold/present/revoke; concurrent writes; peer restart/rejoin; DHT validation; conflicting claims; colluding peers; stale or replayed data; permission changes; data export and recovery. Add explicit credential mutation cases for each signed field, wrong issuer key, wrong verification method, unsupported algorithm, hybrid signature with one invalid component, pure-PQC signatures that only pass structural parsing, unavailable/stale revocation source, and status-list index/resource substitution.

**Metrics:** p50/p95 operation latency, write throughput, storage/replication cost, revocation propagation time, false accept/reject rates, privacy leakage surface, recovery success, credential-size overhead, verifier implementation interoperability, and conformance-suite coverage.

**Hard gates:**
- Invalid signatures, revoked credentials, malformed entries, expired credentials, unauthorized reads, and unsupported algorithms are rejected or explicitly returned as unsupported/inconclusive.
- Every security-relevant field consumed by a verifier is cryptographically bound under the declared proof profile; one-field-at-a-time mutation tests must fail.
- A hybrid credential is not valid unless all required signature components are cryptographically verified. A pure-PQC signature must not be treated as verified merely because its tagged encoding or length is correct.
- Revocation/status unknown, unavailable, malformed, or stale beyond policy limits cannot be treated as active.
- Multi-agent tests are required for claims about DHT validation. Unit-test counts alone do not establish distributed correctness.
- External interoperability claims require an independent resolver/verifier and the relevant W3C / OpenID conformance tests. VC-shaped JSON and a self-issued cryptosuite label are not conformance evidence.

**Standards direction:** Map credential semantics to W3C VC Data Model 2.0 and select a published W3C Data Integrity cryptosuite or another interoperable proof format. Specify and independently test the `did:mycelix` method and resolver. Use W3C Bitstring Status List only when the status-list resource and verification path are actually implemented; otherwise describe Mycelix's Holochain status registry as a native mechanism. Implement OpenID4VCI issuance and OpenID4VP presentation adapters after the underlying credential, DID, and key-lifecycle semantics are stable. Run the OpenID Foundation conformance suites for the exact role and profile. See the [Mycelix Identity Interoperability and Assurance Roadmap](https://github.com/Luminous-Dynamics/mycelix/blob/main/docs/identity/INTEROPERABILITY_AND_ASSURANCE.md).
 
### Symtropy

**Comparators:** Analytic reference solutions first. Then use scope-matched comparisons against:
- [Rapier](https://rapier.rs/docs/): Rust-native 2D/3D engine with collision, joints, soft bodies, snapshots, and optional cross-platform determinism.
- [MuJoCo](https://mujoco.readthedocs.io/en/stable/computation.html): robotics/contact simulation with a mature articulated-body model and documented same-version/same-architecture reproducibility caveats.
- [Jolt Physics](https://github.com/jrouwe/JoltPhysics) and Box2D for appropriate game/interactive workloads.
- [NVIDIA PhysX 5](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/docs/GPURigidBodies.html): CPU and optional CUDA GPU rigid-body simulation, articulations, and additional particle/deformable paths.
- [Newton](https://github.com/newton-physics/newton): the open-source GPU-accelerated physics simulation engine initiated by Disney Research, Google DeepMind, and NVIDIA; it builds on NVIDIA Warp and integrates MuJoCo Warp. Track its release maturity and runtime dependencies separately.

Only compare overlapping dimensions, collision primitives, solver settings, and workloads. Do not compare Symtropy's N-dimensional capabilities to 3D competitors as if they were the same scope. Conversely, do not use a competitor's missing N-D feature to avoid common-scene accuracy and speed comparisons.

**Workloads:** Free motion; collision stacks; joint chains/grids; high-speed CCD; frictional contacts; resting contact stability; deterministic replay; variable mass ratios; 2D/3D shared scenes; dimension-specific tests where competitors cannot participate. Add common robot manipulation tasks where MuJoCo / PhysX / Newton are meaningful comparators, and report solver/model differences explicitly.

**Metrics:** Relative position/velocity error, momentum and energy drift where conserved, constraint residual, penetration depth, contact stability, deterministic replay agreement, p50/p95 step time, throughput, allocations, and energy per simulated second.

**Hard gates:** Physics correctness and stability thresholds are specified before timing. Performance claims require matched settings, machine, and workload. Numerical divergence across versions is reported with tolerances; contact systems can amplify tiny differences.

**Target direction:** Match established engines on common scenes while offering measured advantages in generic N-dimensional and application-defined state-coupling workloads. Never claim global superiority from a narrow microbenchmark.

**Competitive thesis:** The likely differentiation is not "faster than MuJoCo/PhysX at all 3D physics." It is a reusable N-dimensional substrate and generic state-coupling interfaces that conventional 3D engines do not primarily target. The benchmark must separately establish (a) 2D/3D correctness and performance parity, (b) N-D correctness against analytical references, and (c) useful state-coupled behavior with a held-out application task. If these cannot be shown, narrow the product thesis.

### Sol Atlas

**Comparators:** QGIS, PostGIS, GeoServer, MapLibre-based applications, OGC SensorThings implementations, and domain-specific energy planning tools.

**Workloads:** Geospatial load/query/export; time-series overlays; mixed-resolution datasets; missing and stale records; coordinate transformations; source updates; scenario recomputation; mobile/low-power rendering.

**Metrics:** Data provenance coverage, feature completeness, positional error against reference data, temporal staleness, query p50/p95, render frame time, memory, time-to-first-useful-view, and reproducible scenario exports.

**Hard gates:** Every dataset layer declares source, license, retrieval/update time, CRS, units, and observed/estimated/modeled/planned/simulated status. Planned and simulated assets cannot be shown as observed operational facts. No decision-support claim without domain validation.

**Standards direction:** Use OGC APIs and concepts where practical. Map inputs, model outputs, and lineage; avoid forcing heterogeneous domain data into one schema.

### Xenia

**Comparators:** RustDesk, MeshCentral, Apache Guacamole, SSH/administration channels, and protocol-level test harnesses. Compare threat models and supported platforms, not just frame rate.

**Workloads:** Handshake interoperability; replay/reordering; packet loss; key rotation; operator revocation; lost operator device; host identity change; consent denial; malicious viewer; screen-capture lifecycle; long-duration sessions.

**Metrics:** Handshake and rekey latency, bandwidth, p50/p95 frame latency, recovery after transport loss, revoked-operator rejection, replay rejection, consent-state correctness, and resource use.

**Hard gates:** No production positioning before independent cryptographic and application security review. A working handshake does not establish secure end-to-end product behavior.

**Standards direction:** Follow NIST FIPS 203/204/205 as applicable; make algorithm agility explicit; record exact parameter sets and wire versions. PQC claims require interoperability tests and review. Include a migration plan informed by [NIST IR 8547 (October 2026)](https://csrc.nist.gov/pubs/ir/8547/final): inventory quantum-vulnerable primitives, define hybrid migration profiles, and test downgrade / algorithm-confusion paths. A post-quantum algorithm in a handshake does not make the entire remote-session product quantum-safe.

### Spark Engine

**Comparators:** Prioritized expert-designed experiment plans, random/space-filling designs, and alternative Bayesian experimental-design baselines.

**Workloads:** Synthetic problems with known ground truth; historical data replay; model misspecification; uncertain measurement noise; fixed budgets and censored outcomes.

**Metrics:** Information gained per dollar, probability of selecting the correct hypothesis, calibration (Brier/log score), regret versus oracle design, robustness to prior misspecification, and decision sensitivity.

**Hard gates:** The tool must preserve skeptical nulls, model alternatives, and physical constraints. An anomaly model is not evidence of net energy gain or a practical energy source.

## Proposed result and release tiers

- **Tier 0 — Local diagnostic:** exploratory; no external performance claim.
- **Tier 1 — Reproducible internal result:** pinned workload, raw output, and script.
- **Tier 2 — Independent replication:** separate operator or environment repeats the result.
- **Tier 3 — External review:** domain expert, security reviewer, or laboratory reviews method and evidence.
- **Tier 4 — Operationally validated:** real deployment/customer outcomes with ongoing monitoring and incident handling.

A release must display the highest tier actually achieved for each claim. A project-wide badge is misleading when evidence varies by feature.

## Public reporting template

Every benchmark report should include:

1. Claim and exact scope.
2. Hypothesis and predeclared pass/fail thresholds.
3. Baselines and tuning protocol.
4. Hardware/software/dataset digests.
5. Commands and run manifest.
6. Raw result files and aggregation script.
7. Statistical uncertainty and failure cases.
8. Negative controls.
9. Known limitations and non-comparable results.
10. Independent reviewer and replication status.

## Industry reference points

- [ITBench](https://proceedings.mlr.press/v267/jha25a.html) for multi-domain IT automation tasks (SRE, CISO, and FinOps). The ICML 2025 paper describes 102 scenarios in its paper release; later public benchmark snapshots report 94 scenarios. Pin the exact corpus/version before comparing scores.
- [ITBench-AA](https://artificialanalysis.ai/evaluations/itbench-aa) for independent SRE-agent evaluation on Kubernetes incident root-cause tasks. This is a useful diagnostic baseline, not a substitute for end-to-end mutation and recovery checks.
- [EnterpriseOps-Gym](https://proceedings.mlr.press/v306/malay26a.html) for stateful enterprise agent planning: the ICML 2026 paper describes 1,150 expert-curated tasks across eight domains, 164 database tables, and 512 tools.
- [OpenID4VP / OpenID4VCI HAIP conformance](https://openid.net/openid4vp-and-openid4vci-conformance-tests-are-complete-and-open-for-self-certification/) for identity issuance/presentation interoperability; the OpenID Foundation announced completed suites and self-certification in August 2026.
- [W3C Digital Credentials API Working Draft (15 October 2026)](https://www.w3.org/TR/2026/WD-digital-credentials-20261015/) for browser-mediated credential presentation/issuance integration. It is a Working Draft, not a final Recommendation.
- [NIST IR 8547: Transition to Post-Quantum Cryptography Standards (October 2026)](https://csrc.nist.gov/pubs/ir/8547/final) for enterprise migration planning to standardized PQC algorithms and key-establishment schemes.
- [IETF Internet-Draft: Benchmarking Methodology for AI Agents in Network Operations](https://datatracker.ietf.org/doc/draft-contreras-bpm-ai-agent-benchmarking/) for a vendor-independent network-operations agent methodology (draft-00, 2 November 2026; not an Internet Standard).
- [SPEC CPU 2026](https://www.spec.org/cpu2026/) for standardized CPU throughput/time and optional energy measurements. Its 52 benchmarks across four speed/rate suites include optional energy reporting; it is a CPU/memory/compiler benchmark, not an end-to-end application or infrastructure benchmark. Public SPEC results must follow the suite's run rules and report the configuration; SPEC's rules treat a result as an empirical observation with archived configuration and validated outputs.
- [MuJoCo computation and reproducibility](https://mujoco.readthedocs.io/en/stable/computation.html) for simulator determinism caveats.
- [Rapier performance comparisons](https://godot.rapier.rs/docs/documentation/performance/) for matched-scene physics step-time reporting.
- [Hyper-dimensional computing architectures for AI applications: a comprehensive survey](https://doi.org/10.1016/j.rineng.2026.109589), March 2026, for HDC architecture, performance opportunities, and limitations.
- [Continual Learning Bench 1.0](https://sky.cs.berkeley.edu/project/continual-learning-bench/), May 2026, for dependent, online task sequences where systems are expected to adapt during evaluation.
- [NIST PQC standards and migration](https://www.nist.gov/pqc) for post-quantum algorithm selection and migration planning.
- [OpenID4VP / OpenID4VCI conformance](https://openid.net/openid4vp-and-openid4vci-conformance-tests-are-complete-and-open-for-self-certification/) for verifiable credential interoperability.
- [W3C VC Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/) for credential semantics.
- [OGC AI-ready geospatial data building blocks](https://docs.ogc.org/techpaper/26-050/26-050.html) for interoperable inputs, outputs, catalogs, vocabularies, and lineage.
- [SPEC CPU 2026 overview](https://open.spec.org/cpu2026/docs/overview.html) for the limits of CPU-only metrics.

These are reference points, not proof that a Luminous Dynamics project conforms to them.
