# Luminous Dynamics

**Sovereign computing, verifiable intelligence, simulation, and human-centered coordination.**

Luminous Dynamics develops open-source software and research systems for operating computing infrastructure, building adaptive computational systems, modeling physical environments, and coordinating people and institutions.

Our work spans systems engineering, cognitive architecture, privacy-preserving verification, simulation, decentralized coordination, and geospatial applications. We are research-led and claim-disciplined: project pages distinguish implemented capabilities from prototypes, experiments, planned work, and open research questions.

Our guiding principles are **truth, dignity, flourishing, and sovereignty**.

## Portfolio

The portfolio is organized around complementary platforms. They are independently useful projects; integrations are developed selectively and should not be assumed to exist merely because projects appear in the same portfolio.

### Sovereign computing and operations

#### [Luminous Platform](https://github.com/Luminous-Dynamics/luminous-platform) — NixOS infrastructure operations

A composable NixOS platform focused on observable system state, explicit authorization, controlled changes, verification, and recovery.

- [Nixward](https://github.com/Luminous-Dynamics/nixward) — NixOS management, machine contracts, system observation, and an evidence-bound change lifecycle.
- [Sovereign Boot](https://github.com/Luminous-Dynamics/sovereign-boot) — boot lifecycle and recovery components. Disabled by default; host enablement remains subject to the repository's qualification gates.
- [Luminous Edge](https://github.com/Luminous-Dynamics/luminous-edge) — flake composition for supported platform modules.
- [Nix Signature Policy](https://github.com/Luminous-Dynamics/nix-signature-policy) — a separate reference implementation for composable, downgrade-resistant Nix signature authorization policy.

**Status:** Active engineering. Component maturity, compatibility, and safety gates are documented in their respective repositories. Do not interpret the platform overview as a production-readiness or security-audit claim.

#### [Xenia](https://github.com/Luminous-Dynamics/xenia-peer) — consent-first remote sessions

Peer-to-peer remote-session software with an application layer ([xenia-peer](https://github.com/Luminous-Dynamics/xenia-peer)) and a separate sealed wire protocol ([xenia-wire](https://github.com/Luminous-Dynamics/xenia-wire)).

**Status:** Pre-alpha. End-to-end exercised capabilities are documented, but the project explicitly does not claim a completed security review or production readiness.

### Cognitive systems

#### [Symthaea](https://github.com/Luminous-Dynamics/symthaea) — experimental cognitive architecture

Research into hyperdimensional computing, continuous-time dynamics, active inference, memory, verifiable computation, and privacy-preserving proofs.

Symthaea investigates measurable computational properties and selected verifiable state transitions. It does **not** claim to prove machine consciousness, establish AGI, or confer regulatory compliance.

Start with its [evidence table](https://github.com/Luminous-Dynamics/symthaea#evidence-table), [honest status](https://github.com/Luminous-Dynamics/symthaea/blob/main/docs/HONEST_STATUS.md), and reproduction instructions.

### Simulation and physical systems

#### [Symtropy](https://github.com/Luminous-Dynamics/symtropy) — N-dimensional mathematics and physics

A Rust simulation substrate for N-dimensional geometry, rigid-body dynamics, collision handling, state coupling, and research experiments. Its permissively licensed core crates and AGPL-licensed research/application crates have different licensing terms; consult the repository before incorporating components.

Performance figures in the README are project-reported measurements and should be compared using equivalent workloads and independently reproducible methods.

### Decentralized coordination

#### [Mycelix](https://github.com/Luminous-Dynamics/mycelix) — civic, commons, and institutional coordination

A Holochain-based research and application ecosystem for identity, credentials, consent, governance, education, commons, mutual aid, and other coordination domains.

The repository's maturity matrix distinguishes live application surfaces from pre-alpha backend work and incomplete multi-agent testing. [Pulse](https://mail.mycelix.net) and [Praxis](https://praxis.mycelix.net) have live application surfaces; consult the Mycelix README for their current source, deployment, and integration caveats. A passing unit test or a defined data schema is not evidence of production readiness.

Related work includes [Mycelix Health](https://github.com/Luminous-Dynamics/mycelix-health), which remains research-stage and is not represented as a clinically deployed or compliant health-record system.

### Spatial and planetary applications

#### [Sol Atlas](https://github.com/Luminous-Dynamics/sol-atlas-leptos) — planetary energy and infrastructure visualization

A Rust, Leptos, WebAssembly, and WebGL2 application for interactive planetary visualization, energy and infrastructure layers, and scenario exploration.

- [Open the demo](https://atlas.luminousdynamics.io)
- [Project demonstration notes](https://github.com/Luminous-Dynamics/sol-atlas-leptos/blob/main/DEMO.md)

The current application uses bundled static data by default. Optional data integrations are feature-gated. Scenario timelines, planned infrastructure, and simulated layers must not be interpreted as live measurements or operational forecasts without source, timestamp, and validation evidence.

## Research laboratories and enabling components

- [Spark Engine](https://github.com/Luminous-Dynamics/spark-engine) — a physics-honest toolkit for investigating reported lattice-confinement-fusion anomalies and designing discriminating experiments. It is a research tool, **not a fusion power source**.
- [Kitsune2 DTN transport](https://github.com/Luminous-Dynamics/kitsune2-transport-dtn) — a proof-of-concept BPv7 delay-tolerant transport for Kitsune2. Its README documents demonstrated delivery conditions and remaining untested cases.
- [scap downstream fixes](https://github.com/Luminous-Dynamics/scap) — a deliberately maintained downstream fork for Xenia; upstream attribution and the upstream contribution are documented in that repository.

Other repositories contain supporting libraries, prototypes, historical work, and experiments. Check each repository's archive flag, README, license, and current maturity notes before treating it as an active product.

## How the platforms relate

The portfolio has a shared direction, not a claim of one finished integrated system:

- **Luminous Platform** manages and protects computing environments.
- **Symthaea** investigates adaptive cognition and verifiable computation.
- **Symtropy** provides mathematical and physical simulation capabilities.
- **Mycelix** supports identity, provenance, consent, and distributed coordination.
- **Sol Atlas** provides spatial visualization and scenario context.
- **Xenia** explores consent-bound remote sessions.

A proposed common evidence layer can connect inputs, versions, execution records, verification results, authorization, and outcomes. Each integration must be implemented and tested before it is described as available.

## Evidence and maturity standards

We aim to make the state of each project inspectable.

- **Active engineering** means development is ongoing; it does not mean production-ready.
- **Pre-alpha / prototype** means important product, compatibility, security, or deployment work remains.
- **Research** means hypotheses and experimental results require appropriate validation.
- **Archived** means the repository is historical and should not be presented as a current product.

Where possible, project documentation should provide exact reproduction commands, pinned versions, benchmark methodology, baselines, negative controls, known limitations, and independent-review status. Security, medical, legal, and regulatory claims require the relevant external evaluation; they are not inferred from tests or architectural intent.

### Shared evaluation resources

- [Cross-portfolio benchmark programme](https://github.com/Luminous-Dynamics/.github/blob/main/benchmarks/README.md) — workload-specific baselines, correctness gates, negative controls, and reporting requirements.
- [Luminous Evidence Result Profile 0.1](https://github.com/Luminous-Dynamics/.github/tree/main/standards/evidence/v0.1) — an experimental, interoperable result-predicate proposal designed to reuse in-toto/SLSA and domain standards rather than replace them.

These are drafts and evaluation plans, not certifications or claims that all projects already emit compliant evidence packages.

## Collaboration

We welcome technically grounded contributions, independent benchmark reproduction, research collaboration, design partners, and deployment feedback.

Start with the README and issue tracker of the specific project. For commercial use, check the applicable repository and crate licenses; licensing terms can differ across components.

## Structural Love

Luminous Dynamics is guided by **Structural Love**:

> Love is the disciplined, joyful co-creation of becoming, bounded by truth, consent, repair, and irreducible dignity.

Its ten principles are:

1. **Love is rigorous, playful, co-creative becoming.**
2. **Love is attention without possession.**
3. **Love is power under consent.**
4. **Love is truth with care.**
5. **Love is difference without domination.**
6. **Love is repair over discard.**
7. **Love is abundance within limits.**
8. **Love is freedom with responsibility.**
9. **Love is joy with accountability.**
10. **Love is irreducible dignity.**

These principles inform how we design systems, conduct research, govern shared infrastructure, and work with the people affected by our technology.
