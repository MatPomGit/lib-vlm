# core

**Odpowiedzialność:** jeden kontrakt inferencji dla modeli tekstowych i multimodalnych.

Docelowe struktury: `ModelRequest`, `ContentPart`, `ModelResponse`, `ModelCapabilities`, `InferenceError`. `ContentPart` rozróżnia tekst, obraz i audio; klatki wideo zachowują timestamp oraz kolejność. `ModelRequest` przenosi jawny identyfikator modelu, wiadomości/treści, parametry generowania i identyfikator żądania. `ModelResponse` przenosi wynik, informację o zakończeniu, metadane backendu i ewentualne statystyki, jeśli rzeczywiście są dostępne.

Warstwa podstawowa odpowiada za walidację, serializację, zgodność typów i stabilny model błędów; nie prowadzi schedulerów, model-routera ani telemetrii Research Autopilot. Kontrole przepływu informacji i retry powinny być jawne, ograniczone i idempotentne tam, gdzie to możliwe.

Kontrakt: [docs/contracts.md](../../../../docs/contracts.md). **Status: PLANNED, bez kodu.**
