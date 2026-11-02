# Luminous Dynamics — Portfolio Commercialization and Investor Blueprint

**Version:** 0.1  
**Prepared:** 2 November 2026  
**Status:** Working strategy; hypotheses require customer validation.  
**Purpose:** A source-of-truth narrative for product sequencing, external partnerships, funding fit, and investor diligence. This document does not claim product-market fit, customers, revenue, independent validation, or market size unless a separately linked source establishes it.

## 1. Investment thesis

Luminous Dynamics develops open and composable software and research systems for:

- operating computing infrastructure with explicit authority and recoverable changes;
- investigating adaptive cognition and verifiable computation;
- simulating physical and embodied systems;
- coordinating identity, credentials, consent, and institutions;
- exploring spatial and planetary systems through geospatial visualization.

The portfolio is intentionally broad, but the commercial strategy should not ask one investor to finance every research programme at once. Each funding request must identify a buyer, a problem, a product boundary, a measurable result, an adoption route, and a milestone that changes the next financing decision.

**Working company thesis:** build sovereign and verifiable systems that help organizations make consequential digital and physical decisions with clearer authority, better evidence, and more recoverable operations.

This thesis is stronger than a collection of unrelated repositories, but the portfolio must demonstrate interoperability rather than simply claim it.

## 2. Portfolio architecture

The projects have different roles and maturity levels. A portfolio label is not a product-readiness badge.

| Portfolio layer | Projects | Role | Current commercialization posture |
|---|---|---|---|
| Sovereign computing and operations | Luminous Platform, Nixward, Sovereign Boot, Luminous Edge, Nix Signature Policy | Manage, authorize, verify, and recover computing environments | **Lead commercial hypothesis:** bounded NixOS operations workflows |
| Consent-bound remote operations | Xenia / xenia-peer / xenia-wire | Remote sessions, consent, operator roles, and cryptographic session transport | Pre-alpha; protocol and security review before product positioning |
| Cognitive systems | Symthaea | HDC, continuous-time dynamics, active inference, memory, and verifiable computation research | Research platform; commercialize only workload-specific measured capabilities |
| Simulation and physical systems | Symtropy | N-dimensional mathematics and rigid-body simulation with state-coupling extensions | Developer SDK / research substrate; not a complete FEA, CAD, or industrial digital-twin suite |
| Decentralized coordination | Mycelix | Holochain identity, credentials, consent, governance, commons, and applications | Focus on one or two deployed workflows; cluster maturity is mixed |
| Spatial and planetary applications | Sol Atlas | Geospatial visualization and scenario exploration | Demonstrator / product discovery; current bundled data is not an authoritative live operations feed |
| Research laboratories | Spark Engine, Mycelix Health research, Terra Preta and other projects | Scientific and application research | Research grants, labs, and domain partnerships; separate from core enterprise software revenue |

### Shared infrastructure

The proposed Evidence Spine is a cross-project design direction, not a fifth standalone platform or a finished product. Its first scope should be small:

- exact subject, code, input, and dataset identity;
- execution and version provenance;
- explicit check results and negative controls;
- uncertainty, limitations, and data classification;
- authorization evidence for consequential actions;
- a reproducible result package.

The experimental [Luminous Evidence Result Profile 0.1](https://github.com/Luminous-Dynamics/.github/tree/main/standards/evidence/v0.1) is intended to reuse in-toto / SLSA envelopes and domain standards. It is a draft; schema-valid data is not proof of truth or authorization.

## 3. Commercial beachhead hypothesis

### Candidate A — Luminous Platform: evidence-bound NixOS operations

**Initial ideal customer profile:** teams already operating NixOS or evaluating it for reproducible infrastructure—research compute teams, specialist infrastructure operators, managed NixOS service providers, and technology organizations with high change-control requirements.

**Pain hypothesis:** configuration changes are operationally consequential. Operators need to know exactly what was proposed, what inputs were approved, whether authorization matches the target and action, whether the change took effect, and how to recover when the outcome is uncertain.

**Product hypothesis:** combine Nixward's observe / plan / validate / authorize / snapshot / apply / verify / recover lifecycle with Luminous Edge's composable NixOS integration and qualified Sovereign Boot components where appropriate.

**Why investigate this first:** it has a comparatively narrow buyer profile, a concrete workflow, and an existing deployment ecosystem to integrate with. A customer can evaluate the value in a bounded environment without adopting the wider Luminous portfolio.

**Competitive alternatives:** native NixOS generations and rollback; deploy-rs, Colmena, Morph, Comin, Bento, and managed fleet tooling. These products have different scopes. The opportunity is not to claim a blanket replacement; it is to prove added value in exact-scope authorization, evidence completeness, failure reconciliation, and recovery.

**Pilot proposition:** one customer-controlled, non-production NixOS environment; a small set of authorized configuration changes; failure injection; independently observed final state; documented rollback/recovery. The pilot should compare against the customer's current workflow.

**Pass criteria:** zero unauthorized committed effects in the frozen test corpus; no retry while an earlier side effect is unresolved; no promotion after failed post-change checks; recovery behavior evidenced; operator time and intervention count measured.

**Commercial model hypothesis:** paid deployment assessment, paid pilot, annual support / enterprise integration, and later managed fleet services. Confirm actual buyer budget and willingness to pay before setting price.

### Candidate B — Symthaea: workload-specific verified computation

**Initial buyer hypotheses:** research labs, constrained-device developers, privacy-preserving computation teams, and organizations with a narrow workload where HDC / liquid dynamics may offer a cost-quality advantage.

**Product boundary:** do not sell “consciousness” or “AGI.” Sell a measured capability: for example, an associative retrieval / compositional binding kernel, a verifiable state-transition primitive, or a constrained continual-learning component.

**Competitive alternatives:** strong task-specific small language models, conventional ML, HDC / vector-symbolic baselines, and established ZK proof stacks. Compare matched tasks, accuracy, energy, latency, model size, calibration, and tuning budget.

**Pass criteria:** a workload-specific Pareto improvement reproduced by an independent operator; leakage controls; matched compute; ablations for HDC-only, liquid-dynamics-only, hybrid, and conventional baselines. If the advantage is limited, narrow the product scope.

**Commercial model hypothesis:** SDK licensing / support, deployment integration, or research contracts. Determine which capabilities customers actually pay to use.

### Candidate C — Symtropy: N-dimensional physics and state-coupled simulation

**Initial buyer hypotheses:** simulation and game developers, embodied-AI research labs, robotics teams investigating novel state-coupling, and scientific visualization developers.

**Product boundary:** a Rust simulation SDK and research substrate. Do not position it as a replacement for Ansys, COMSOL, MuJoCo, or PhysX; the current repository does not establish a complete industrial engineering suite.

**Competitive alternatives:** Rapier, MuJoCo, Jolt, Box2D, PhysX, Newton, and analytic reference solutions where workloads overlap.

**Pass criteria:** (1) 2D/3D correctness and parity tests on common workloads; (2) N-dimensional correctness against analytic references; (3) a held-out application task showing that generic state-coupling is useful beyond a demonstration. Report numerical error and stability before runtime speed.

**Commercial model hypothesis:** permissively licensed core adoption, paid support / integration, and research partnerships for advanced extensions. Keep the AGPL research-extension license boundary explicit.

### Candidate D — Mycelix: a focused institutional workflow

**Initial buyer hypotheses:** education providers, cooperatives, mutual-aid groups, civic institutions, and organizations needing privacy-preserving credentials or coordination.

**Product boundary:** select one application with a clear user, workflow, deployment owner, and operational budget. Pulse and Praxis are candidate application surfaces, but their source / deployment and maturity caveats must be reconciled with actual usage and builds before a production pitch.

**Identity boundary:** the current `did:mycelix` method and credential records are custom / standards-shaped. The current public code has incomplete VC signature field coverage, partial / structural PQC verification paths, and an experimental DASTARK data-model crate. The [Identity Interoperability and Assurance Roadmap](https://github.com/Luminous-Dynamics/mycelix/blob/main/docs/identity/INTEROPERABILITY_AND_ASSURANCE.md) is the acceptance plan. Do not sell W3C / EUDI / eIDAS conformance before independent interoperability and conformance tests.

**Pass criteria:** a working multi-agent deployment; external participant usage; successful credential issue / present / revoke / recover paths; privacy and threat-model review; interop tests; measurable time/cost improvement over the existing process.

**Commercial model hypothesis:** institutional deployment, managed hosting / support, workflow integration, and service contracts. Avoid token economics or broad “CivOS replacement” claims as the initial sales motion.

### Candidate E — Sol Atlas: geospatial scenario exploration

**Initial buyer hypotheses:** energy planners, infrastructure researchers, municipal teams, and organizations exploring asset dependencies or scenario alternatives.

**Product boundary:** current interactive visualization and scenario explorer. Bundled static datasets and modeled / planned layers are not live operational measurements. An industry pilot needs source, license, observation time, CRS, units, uncertainty, and validation for each layer.

**Competitive alternatives:** QGIS, PostGIS, GeoServer, MapLibre applications, OGC APIs, and sector-specific planning systems.

**Pass criteria:** a real customer workflow; source / provenance coverage; position and temporal error; scenario reproducibility; improved planning time or data quality compared to the customer's current method.

**Commercial model hypothesis:** paid data integration / visualization pilot, then site or asset portfolio subscription and services if a recurring workflow emerges.

### Candidate F — Xenia: consent-first remote sessions

**Initial buyer hypotheses:** infrastructure operators and support teams requiring bounded, consent-driven remote access.

**Product boundary:** pre-alpha protocol and application. Working end-to-end components are not an independent security audit or production-ready product.

**Competitive alternatives:** RustDesk, MeshCentral, Apache Guacamole, SSH / administrative channels, and established remote-support products.

**Pass criteria:** external cryptographic review; interoperability across independently implemented clients; replay / revocation / key-rotation / consent tests; supported-platform matrix; bandwidth and latency measurements; incident-response process.

**Commercial model hypothesis:** only after security and platform qualification—enterprise licensing / support and integration. Do not monetize the security promise before review.

## 4. Funding strategy by project type

Funding should match the work:

| Capital type | Appropriate use | Evidence required |
|---|---|---|
| Customer-funded pilot | Luminous Platform, Symtropy SDK, Sol Atlas workflow, focused Mycelix apps | Buyer, scoped problem, acceptance criteria, deployment plan, costed statement of work |
| Commercial angel / pre-seed | Product engineering, support, security review, sales, and initial deployments | Paid pilot or strong design-partner evidence, product boundary, unit economics hypothesis, founder / continuity plan |
| Non-dilutive research funding | Symthaea, novel simulation, Spark Engine, Terra Preta, privacy/identity research | Research question, methodology, falsifiable hypothesis, milestones, independent evaluation path |
| Strategic partnership | Utilities, research labs, engineering firms, NixOS service providers, universities, identity / wallet implementers | A specific workflow and mutual contribution; not a vague MoU |
| Impact / philanthropic capital | Mycelix commons, civic coordination, accessible infrastructure | Measurable beneficiary outcome, governance, privacy and consent, adoption evidence |

A single “fund all projects” capital request obscures risk and use of proceeds. Use project-specific work packages under one coherent company thesis.

## 5. Shared evidence and moat strategy

Potential defensibility should be demonstrated through:

1. **Operational data and integrations:** deployments and connectors that reduce customer changeover cost.
2. **Verification infrastructure:** independent evidence and domain-specific correctness predicates.
3. **Workflow fit:** lower human intervention and lower cost per accepted outcome.
4. **Interoperability:** usable APIs and standards alignment, not a closed proprietary trust silo.
5. **Accumulated validation:** reproducible benchmark suites, failure corpora, and independent reviews.

Code volume, language choice, cryptographic algorithm names, model architecture novelty, and repository count are not moats by themselves.

### Cross-portfolio measures

- cost per accepted outcome;
- evidence latency;
- independent reproducibility rate;
- false-accept rate with denominators / confidence interval;
- recovery time and blast radius;
- human review burden;
- energy per useful result;
- external integration and adoption.

The [benchmark programme](https://github.com/Luminous-Dynamics/.github/blob/main/benchmarks/README.md) defines project-specific comparators, baselines, and hard gates. The [ITOPS Autonomy Boundary protocol](https://github.com/Luminous-Dynamics/luminous-platform/tree/main/benchmarks/itops-autonomy-boundary-v0.1) adds independent participant-effect and service-state oracles for operational agents.

## 6. Customer discovery and product selection

Do not choose a lead product by founder enthusiasm or number of commits. Score each product only after interviews and proof:

| Dimension | Question |
|---|---|
| Urgency | How often does this problem occur, and what happens if it is not solved? |
| Budget owner | Who can approve spending? |
| Existing spend | Which tool, service, staff time, or incident budget is already used? |
| Switching cost | What must be replaced or integrated? |
| Measurable value | What observable metric changes after a pilot? |
| Deployment friction | Security, procurement, regulatory, integration, and training requirements? |
| Repeatability | Can the same product work for another buyer without bespoke engineering? |
| Retention | Will the workflow recur, and what creates an ongoing budget? |

### Interview evidence to capture

For each prospect, record the role, organization type, workflow, frequency, current workaround, annual cost range (if voluntarily disclosed), authority / procurement path, data/security constraints, willingness to pilot, paid-pilot conditions, and explicit reasons for declining.

Do not count informal interest, GitHub stars, compliments, letters of intent without a budget owner, or unpriced pilots as revenue.

### Proposed 30-day discovery targets

These are operating targets, not current traction:

- 15–20 structured conversations for the leading product hypothesis;
- at least 5 conversations with budget owners or direct procurement influencers;
- 3 design-partner candidates with an identified workflow and data / environment;
- 1 priced pilot proposal with measurable acceptance criteria;
- explicit reasons for rejecting the other beachhead candidates.

If the evidence does not support Luminous Platform as the lead, change the priority. The strategy is designed to be falsifiable.

## 7. Commercial promotion gates

| Stage | Required proof | Allowed public statement |
|---|---|---|
| R0 — Research | Reproducible internal experiment and limitations | Research / prototype |
| R1 — Demonstrator | Working demo with pinned inputs and known boundaries | Demonstrator available |
| R2 — Design partner | Real workflow, named stakeholder role, agreed success criteria | Design-partner evaluation |
| R3 — Paid pilot | Signed scope, payment, measurable pre/post results | Paid pilot with stated scope |
| R4 — Production deployment | Support, security, recovery, monitoring, and operational ownership | Production deployment for named scope |
| R5 — Repeatable product | Repeat customers, predictable delivery cost, retention, support economics | Commercial product with documented evidence |

No project inherits a higher stage merely because another project is mature.

## 8. Investor diligence package

The minimum package should include:

- company and cap-table / IP ownership records;
- product portfolio and maturity matrix;
- one lead product brief and buyer workflow;
- demo and exact-version reproduction instructions;
- independent benchmark reports and negative controls;
- security / privacy / operational risk register;
- license and dependency matrix;
- customer interview and paid-pilot evidence;
- 18–24 month use-of-funds model tied to milestones;
- founder / team continuity and hiring plan;
- explicit list of research claims, open risks, and retractions.

Do not publish a top-down TAM or forecast solely from a broad adjacent software market. Build a bottom-up obtainable market from named buyer segments, likely deployment counts, validated spend, sales capacity, and realistic sales cycles.

## 9. Immediate decisions

1. Validate Luminous Platform as the first commercial wedge, with NixOS-native teams as the initial segment.
2. In parallel, run small customer-discovery tracks for one Mycelix application and one Symtropy developer workflow.
3. Keep Symthaea as a workload-specific technical differentiation programme until independent benchmark wins are reproduced.
4. Treat Sol Atlas as an infrastructure data / scenario pilot candidate, not a live grid-operations system.
5. Keep Xenia in pre-alpha security qualification.
6. Fund Spark Engine and other deep research through separate research partnerships and non-dilutive work packages.
7. Publish evidence profiles and benchmark results with exact revisions, denominators, uncertainty, and limitations.

## 10. External reference points

- [ITBench (ICML 2025)](https://proceedings.mlr.press/v267/jha25a.html) for multi-domain IT automation evaluation.
- [EnterpriseOps-Gym (ICML 2026)](https://proceedings.mlr.press/v306/malay26a.html) for stateful enterprise agent workflows.
- [OpenID4VP / OpenID4VCI HAIP conformance](https://openid.net/openid4vp-and-openid4vci-conformance-tests-are-complete-and-open-for-self-certification/) for identity interoperability expectations.
- [W3C VC Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/) and [W3C Data Integrity](https://www.w3.org/TR/vc-data-integrity/) for credential semantics and proof requirements.
- [NIST IR 8547](https://csrc.nist.gov/pubs/ir/8547/final) for post-quantum migration planning.
- [OGC AI-ready Geospatial Data](https://docs.ogc.org/techpaper/26-050/26-050.html) for interoperable geospatial data building blocks.

These references are comparison points, not evidence that Luminous Dynamics conforms to them or outperforms them.
