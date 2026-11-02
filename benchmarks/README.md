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

**Comparators:** Native NixOS generations and rollback, deploy-rs, Colmena, Morph, Comin, Bento, and appropriate managed fleet tooling. Compare the same host count, network conditions, configuration, change size, and rollback scenario. These systems have different scopes; document feature gaps rather than forcing a single composite ranking.

**Workloads:** Single-host and multi-host configuration change; drift detection; partial network partition; stale lockfile/input; invalid authorization; interrupted activation; failed health check; disk pressure; host reboot during transition; rollback and recovery.

**Metrics:** Change success, p50/p95 transition time, recovery time, false-positive drift rate, operator interventions, exact input reproducibility, and unauthorized mutation count.

**Hard gates:** Zero unauthorized mutations in the test corpus; every injected denial remains denied; no promotion when post-change verification fails; recovery returns to an identified generation or declares unrecovered state. A zero observed false-accept count is not a proof of zero risk—publish test count and confidence bounds.

**Target direction:** At parity on ordinary deployment speed, materially better evidence completeness, policy-denial behavior, and measured recovery on failure-injection workloads. Avoid trading safety for speed.

### Symthaea

**Comparators:** Task-appropriate conventional ML models, strong small language models, HDC baselines, standard continual-learning algorithms, and task-specific hand-engineered baselines. Include a strong model when semantics require it; do not compare unlike tasks.

**Workloads:** HDC associative recall; compositional binding/unbinding; temporal sequence prediction; continual learning with task/domain shifts; calibration under OOD inputs; constrained-device inference; adversarial and corrupted memory queries.

**Metrics:** Task quality, energy per accepted task, p50/p95 latency, peak RAM/VRAM, model size, update cost, forgetting (e.g. average accuracy drop on prior tasks), calibration error, OOD risk-coverage, and recovery from corrupted memory.

**Hard gates:** Dataset and split digests pinned; leakage audit; baseline tuning budget disclosed; no consciousness or AGI conclusion inferred from task metrics; claims about privacy proofs include proof verification and leakage assumptions.

**Target direction:** Find workload regimes where HDC + liquid dynamics has a measured cost-quality advantage at matched accuracy or a quality advantage at matched energy/latency. If it does not, narrow the claim to the workloads where it does.

### Mycelix

**Comparators:** Centralized relational services, conventional signed event logs, W3C VC 2.0 implementations, OpenID4VCI/OpenID4VP implementations where relevant, and Holochain-native patterns.

**Workloads:** Credential issue/hold/present/revoke; concurrent writes; peer restart/rejoin; DHT validation; conflicting claims; colluding peers; stale or replayed data; permission changes; data export and recovery.

**Metrics:** p50/p95 operation latency, write throughput, storage/replication cost, revocation propagation time, false accept/reject rates, privacy leakage surface, recovery success, and interoperability-conformance cases.

**Hard gates:** Invalid signatures, revoked credentials, malformed entries, and unauthorized reads are rejected. Multi-agent tests are required for claims about DHT validation. Unit-test counts alone do not establish distributed correctness.

**Standards direction:** Map credential functions to W3C VC Data Model 2.0 and evaluate W3C/OpenID conformance rather than inventing a competing credential format. Track VC Data Model 2.1 as a Working Draft separately; do not call a draft Recommendation.

### Symtropy

**Comparators:** Analytic reference solutions first; then Rapier, MuJoCo, Jolt, Box2D, and PhysX where dimensions, collision primitives, solver settings, and workloads overlap. Do not compare N-dimensional capabilities to 3D competitors as if they were the same scope.

**Workloads:** Free motion; collision stacks; joint chains/grids; high-speed CCD; frictional contacts; resting contact stability; deterministic replay; variable mass ratios; 2D/3D shared scenes; dimension-specific tests where competitors cannot participate.

**Metrics:** Relative position/velocity error, momentum and energy drift where conserved, constraint residual, penetration depth, contact stability, deterministic replay agreement, p50/p95 step time, throughput, allocations, and energy per simulated second.

**Hard gates:** Physics correctness and stability thresholds are specified before timing. Performance claims require matched settings, machine, and workload. Numerical divergence across versions is reported with tolerances; contact systems can amplify tiny differences.

**Target direction:** Match established engines on common scenes while offering measured advantages in generic N-dimensional and application-defined state-coupling workloads. Never claim global superiority from a narrow microbenchmark.

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

**Standards direction:** Follow NIST FIPS 203/204/205 as applicable; make algorithm agility explicit; record exact parameter sets and wire versions. PQC claims require interoperability tests and review.

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

- [SPEC CPU 2026](https://www.spec.org/cpu2026/) for standardized CPU throughput/time and optional energy measurements.
- [MuJoCo computation and reproducibility](https://mujoco.readthedocs.io/en/stable/computation.html) for simulator determinism caveats.
- [Rapier performance comparisons](https://godot.rapier.rs/docs/documentation/performance/) for matched-scene physics step-time reporting.
- [NIST PQC standards and migration](https://www.nist.gov/pqc) for post-quantum algorithm selection and migration planning.
- [OpenID4VP / OpenID4VCI conformance](https://openid.net/openid4vp-and-openid4vci-conformance-tests-are-complete-and-open-for-self-certification/) for verifiable credential interoperability.
- [W3C VC Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/) for credential semantics.
- [OGC AI-ready geospatial data building blocks](https://docs.ogc.org/techpaper/26-050/26-050.html) for interoperable inputs, outputs, catalogs, vocabularies, and lineage.
- [SPEC CPU 2026 overview](https://open.spec.org/cpu2026/docs/overview.html) for the limits of CPU-only metrics.

These are reference points, not proof that a Luminous Dynamics project conforms to them.
