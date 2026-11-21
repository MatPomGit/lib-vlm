# Konsumenci i granice integracji

Poniższe systemy są **potencjalnymi odbiorcami**, a nie potwierdzonymi zależnościami:

| System | Cel przyszłej integracji | Status |
| --- | --- | --- |
| Research Autopilot | Zunifikowane wywołania lokalnych LLM/VLM | PROPOSED |
| `lib-exp` | Generowanie tekstowych i multimodalnych bodźców | PROPOSED |
| `lib-unity` / `lib-unreal` | Inferencja w procesach authoringu scen | PROPOSED |
| Projekty `arc-ai`, `arc-neuro`, `arc-xr` | Powtarzalne eksperymenty modelowe | PROPOSED |

Nie ma obecnie potwierdzonego odbiorcy przypiętego do wydania `lib-vlm`. Pierwszy konsument wymaga wersjonowanego kontraktu, testów integracyjnych i odnotowanego SHA. `lib-llm` nie powinno być zależnością ani alternatywnym właścicielem implementacji.
