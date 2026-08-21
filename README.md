# cidra-practice

Deliberately broken CI, used as the fixture corpus for
[CIDRA](https://github.com/) — see `docs/5_fixtures.md` in that repo.

`main` is green. Each `fix-*` branch introduces exactly one failure:

| Branch | Fixture | Failure class |
|---|---|---|
| `fix-01-missing-dep` | F-01 | missing_dependency |
| `fix-02-assertion` | F-02 | assertion_error |
| `fix-03-env-config` | F-03 | env_config_error |
| `fix-04-flaky` | F-04 | flaky_test |
| `fix-01b-transitive-dep` | F-01b | missing_dependency (transitive) |
| `fix-02b-loop-boundary` | F-02b | assertion_error (logic, not literal) |
| `neg-01-logic-bug` | N-01 | out of scope — must NOT be "fixed" |

Nothing here is real. Do not depend on it.
