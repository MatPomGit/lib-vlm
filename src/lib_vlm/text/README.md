# text

**Zakres:** chat/completions, wiadomości systemowe i użytkownika, odpowiedzi strukturalne, parametry generowania, ewentualnie embeddingi tekstowe przez odrębnie zadeklarowaną zdolność backendu.

Wejście i wyjście używają wspólnych `ContentPart` i `ModelResponse` z `core`. Wsparcie JSON Schema, tool calling i streaming nie może być zakładane globalnie: każde wymaga osobnej deklaracji i testu dla konkretnego modelu/backendu. Biblioteka nie przechowuje historii rozmów trwale.

**Status: PLANNED, bez kodu.** Kontrakt: [docs/contracts.md](../../../docs/contracts.md).
