# Podział odpowiedzialności

Własność źródeł: jedno repozytorium `lib-vlm`. Wszystkie wpisy poniżej są planowane; katalogi zawierają wyłącznie dokumentację.

| Moduł | Wejście | Wyjście | Odpowiedzialność | Status |
| --- | --- | --- | --- | --- |
| `core/` | Ujednolicone żądanie | Typy, odpowiedź, błąd | Schematy, walidacja, capabilities | PLANNED |
| `text/` | Treść tekstowa | Tekst/JSON | Chat, completion, structured output | PLANNED |
| `vision/` | Obrazy/klatki | Części wizualne | Dane wejściowe VLM, timestampy | PLANNED |
| `audio/` | Audio + metadane | Części audio | Multimodalna inferencja audio | PLANNED |
| `providers/` | Żądanie + endpoint | Znormalizowana odpowiedź | Translacja API backendu | PLANNED |

`lib-vlm` nie steruje agentami, kolejkami ani modelami w pamięci GPU. Research Autopilot odpowiada za harmonogram, leasing, routing zadań i monitoring wykonawców; `lib-exp` za protokół eksperymentu; `lib-eye` za pomiary okulograficzne; `lib-unity` i `lib-unreal` za integracje silników. Odbiorcy nie są jeszcze zweryfikowani.

Nie tworzyć kolejnej abstrakcji dla samego faktu istnienia kilku backendów. Adapter może implementować tylko podzbiór zdolności; brak zdolności to jawny błąd, nie ukryty fallback.
