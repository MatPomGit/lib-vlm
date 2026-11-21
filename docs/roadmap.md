# Plan wdrożenia lib-vlm

Realizacja etapami, bez budowy drugiego systemu agentowego.

| Etap | Cel | Kryterium ukończenia | Status |
| --- | --- | --- | --- |
| V0 | Jedna architektura LLM/VLM i dokumentacja | Repo, moduły, zakres, kontrakt, ryzyka | IN_PROGRESS |
| V1 | Minimalny `core` | Typy żądań/odpowiedzi, błędy, testy kontraktowe | NOT_STARTED |
| V2 | Jeden lokalny provider | Odkrycie modelu, inferencja tekstu, test offline i live | NOT_STARTED |
| V3 | `vision` i `audio` | Jawne capabilities, testy obrazu, wideo i audio | NOT_STARTED |
| V4 | Integracja z konsumentami | Jeden E2E z Research Autopilot, test clean-install | NOT_STARTED |

Biblioteka nie implementuje kolejki zadań, agentów ani automatycznego routingu modeli. Własność mechanizmów sterowania pozostaje w Research Autopilot. Wydanie, Pages i dostęp do danych wrażliwych mają osobne bramki.

Zależności między etapami: V1 → V2 → V3 → V4. Przegląd PR i wyniki CI nie oznaczają wdrożenia modelu. Status docelowo aktualizowany na podstawie testów i SHA.
