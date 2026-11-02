# Luminous Evidence Result Profile (LEP) — Draft 0.1

**Status:** Experimental proposal, 2 November 2026  
**Scope:** A small cross-project profile for recording reproducible computational, simulation, infrastructure, and decision-evaluation results.  
**Not a standard:** This draft is not a certification, safety case, cryptographic protocol, or assurance that a result is correct.

## 1. Design goal

Luminous Dynamics projects span software builds, cognitive-computation experiments, physics simulations, geospatial scenarios, distributed workflows, and controlled infrastructure operations. Those domains need different predicates, but reviewers repeatedly need the same basic questions answered:

- What exact subject and inputs did this result concern?
- Which code, model, configuration, dataset, and environment were used?
- What was actually executed?
- Which checks ran, and which failed or were skipped?
- What is the result's scope, uncertainty, and limitation?
- Can another party reproduce or independently verify it?

LEP defines a **thin result predicate profile**, not a replacement attestation stack. It is intended to sit inside an existing authenticated envelope, preferably an [in-toto Attestation Framework](https://github.com/in-toto/attestation) statement. Software build provenance should use [SLSA provenance](https://slsa.dev/spec/v1.0/provenance) where applicable. Provenance relationships can be mapped to [W3C PROV-O](https://www.w3.org/TR/prov-o/). The profile does not define new signature algorithms, key discovery, identity, or trust roots.

## 2. Non-goals

LEP does not:

- certify a product, operator, model, dataset, institution, or deployment;
- prove that a model is conscious, aligned, safe, clinically valid, or legally compliant;
- make a simulator physically valid merely because it emits a signed result;
- replace SLSA build provenance, SBOM formats, W3C Verifiable Credentials, or domain standards;
- require sensitive source data to be copied into an evidence package;
- turn a confidence score or model-generated explanation into authorization.

## 3. Predicate placement and envelope

The profile defines the payload for a versioned in-toto predicate. The statement subject MUST identify the artifact or immutable run descriptor to which the result applies. The authenticated envelope MUST be produced by an existing supported signing mechanism. Implementations SHOULD prefer established DSSE/in-toto tooling rather than invent a custom signature wrapper.

The predicate type for this draft is:

```text
https://github.com/Luminous-Dynamics/.github/blob/main/standards/evidence/v0.1/README.md
```

The schema is [evidence-result.schema.json](evidence-result.schema.json). Example payloads are in [examples/](examples/).

A bare JSON payload without a verifiable envelope is useful for local development, but MUST NOT be described as a signed attestation.

## 4. Required semantics

### 4.1 Subject and inputs

Every result identifies its subject and all material inputs. Each artifact reference SHOULD include a cryptographic digest, media type, human-readable name, and immutable retrieval or revision reference. For a private or sensitive artifact, the package MAY reference a controlled locator and digest without embedding the artifact itself.

A digest proves byte identity relative to the stated algorithm; it does not prove source authenticity, data quality, or truth.

### 4.2 Execution identity

A run records start and completion times, executor identity, toolchain or software revisions, relevant environment details, and any random seeds. If a field is unknown, it is omitted or explicitly marked unknown; it MUST NOT be inferred after the run.

Reproducibility claims MUST specify the level being claimed:

- **Bitwise:** identical output bytes under the stated environment and version.
- **Numerical:** output within a declared tolerance and comparison metric.
- **Procedural:** the same documented method and inputs can be re-executed, with bounded nondeterminism.
- **Independent replication:** a separate implementation or team reproduces the result under a separately documented environment.

These levels are not interchangeable.

### 4.3 Checks and negative controls

Each check identifies its method, verifier, result, and whether it is required by the declared evaluation policy. The result vocabulary is:

- `PASS`: the specific check passed under its stated method and scope.
- `FAIL`: the check found a violation or the observed result failed its criterion.
- `INCONCLUSIVE`: evidence was insufficient to decide.
- `NOT_RUN`: the check was not executed.
- `SKIPPED`: the check was intentionally not applicable, with a reason.

A producer MUST NOT convert `NOT_RUN`, `SKIPPED`, missing evidence, verifier errors, or unknown states into `PASS`. The overall conclusion MUST be `INCONCLUSIVE` or `FAIL` whenever a required check is not satisfied. A policy that consumes LEP results MUST define its required checks; a schema-valid predicate alone is not an authorization decision.

Security, safety, and reliability evaluations SHOULD include negative controls, adversarial cases, and at least one explicit check that a known-invalid input is rejected. An all-positive test suite is insufficient evidence of fail-closed behavior.

### 4.4 Uncertainty and limitations

A result SHOULD state relevant uncertainty, statistical method, sample size, interval, units, and known sources of bias. If uncertainty cannot be quantified, the limitation MUST be stated. Point estimates MUST NOT be presented as certainty.

The limitations list is required. Empty limitations means the producer explicitly asserts no known limitations within the stated scope; it does not assert that none exist in reality. Consumers SHOULD treat an unexpectedly empty limitations list as a review trigger for high-impact results.

### 4.5 Conclusion

Overall status is one of `PASS`, `FAIL`, or `INCONCLUSIVE`. The conclusion summarizes only the evaluated claim and scope. It MUST NOT generalize a passing benchmark into universal correctness, production readiness, security, or regulatory approval.

## 5. Monotonic and fail-closed consumption

Policies that consume LEP MUST be monotonic with respect to missing evidence: removing an attestation, required field, or required check MUST NOT turn a DENY into an ALLOW.

Unknown predicate versions, unsupported digest algorithms, missing required subjects, invalid signatures, stale policy epochs, missing required checks, and unverifiable references MUST NOT result in an affirmative authorization decision.

Unknown extension fields MAY be ignored for forward compatibility, but MUST NOT alter the meaning of required fields. Producers SHOULD place project-specific additions under an `extensions` object with collision-resistant names.

## 6. Privacy and data minimization

Evidence is not a mandate to publish source data. Use content digests, access-controlled locators, redacted summaries, or zero-knowledge claims where appropriate. Do not include secrets, personal data, medical records, credentials, private keys, or confidential infrastructure details in public predicates.

A verifier must distinguish "the commitment matches" from "the underlying data is complete, valid, and representative." Those are separate checks.

## 7. Domain profiles

LEP's common envelope is intentionally small. Domain-specific profiles should be separate, versioned predicates or extension schemas:

- **Build / software supply chain:** SLSA provenance, SBOM, source revision, builder identity and reproducibility.
- **Cognitive computation:** dataset splits, model and tokenizer hashes, prompts/configuration where applicable, compute budget, latency, energy, accuracy, calibration, and leakage controls.
- **Physics / simulation:** initial conditions, solver revision, timestep/integrator, conservation and constraint errors, reference solutions, tolerances, and numerical stability.
- **Distributed coordination:** agent count, topology, conductor versions, DHT/consistency conditions, revocation and restart tests, adversarial peers, and privacy boundaries.
- **Geospatial / digital twin:** source identifiers, licenses, observation time, CRS, transformations, spatial/temporal resolution, quality flags, lineage, and uncertainty.
- **Infrastructure operations:** exact flake lock/revision, target identity, plan digest, authorization receipt, snapshot, action log, post-state digest, and recovery evidence.

## 8. Compatibility and standards mapping

| LEP concern | Existing standard or ecosystem | Relationship |
|---|---|---|
| Authenticated statement and predicate | [in-toto Attestation Framework](https://github.com/in-toto/attestation) | LEP is a predicate profile; it does not redefine the envelope |
| Software build origin | [SLSA provenance](https://slsa.dev/spec/v1.0/provenance) | Reuse for build-specific provenance |
| Provenance relationships | [W3C PROV-O](https://www.w3.org/TR/prov-o/) | Map entity/activity/agent relationships where useful |
| Credentials and claims | [W3C VC Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/) | Use when the subject is a credential or presentation |
| Geospatial observations | [OGC SensorThings API](https://www.ogc.org/standard/sensorthings/) | Use for sensor/observation interfaces; LEP records run lineage and checks |
| Spatial interoperability | [OGC 26-050](https://docs.ogc.org/techpaper/26-050/26-050.html) | Align data profile, catalog, vocabulary, and lineage concepts |

This profile should remain interoperable with standard identifiers, digest types, and envelopes. It should not claim standards conformance without running the corresponding conformance suites.

## 9. Adoption sequence

1. Validate the JSON Schema and examples.
2. Implement one producer and one independent verifier in a low-risk repository.
3. Add valid, invalid, missing-field, altered-digest, unknown-version, and skipped-required-check fixtures.
4. Demonstrate that policy evaluation fails closed.
5. Compare the profile against in-toto/SLSA and domain-specific standards; remove duplicated fields where a standard already defines them.
6. Seek external review before calling the format stable or recommending it to third parties.

## 10. Open questions

- Should uncertainty fields be standardized in the common profile or always delegated to domain predicates?
- Which canonicalization and digest rules should the payload use for stable signing?
- How should references to private evidence be resolved and authorized across organizations?
- Which in-toto bundle and envelope versions should the first interoperable implementation support?
- Which parts, if any, should be proposed upstream to an existing standards community instead of maintained here?

## References

- [in-toto Attestation Framework](https://github.com/in-toto/attestation)
- [SLSA provenance](https://slsa.dev/spec/v1.0/provenance)
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)
- [W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/)
- [OGC SensorThings API](https://www.ogc.org/standard/sensorthings/)
- [OGC Document 26-050: AI-ready geospatial data](https://docs.ogc.org/techpaper/26-050/26-050.html)
