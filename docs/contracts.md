# Planowany kontrakt inferencji

**Status: PROPOSED, NOT_IMPLEMENTED.** `contracts/api.json` zachowuje `public_entrypoints: []`, ponieważ nie istnieją publiczne symbole programu. Opis stanowi specyfikację docelową, a nie działające SDK.

## Typy

| Typ | Kluczowe pola | Semantyka |
| --- | --- | --- |
| `ContentPart` | `kind`, `data`, `mime_type`, `timestamp_s?` | Jedna część tekstu, obrazu, audio lub klatki |
| `Message` | `role`, `parts[]` | Uporządkowane fragmenty treści |
| `ModelRequest` | `request_id`, `model`, `messages[]`, `parameters` | Jedno żądanie inferencji |
| `ModelCapabilities` | `input_modalities`, `output_modalities`, `features` | Odkryte, zweryfikowane możliwości modelu |
| `ModelResponse` | `request_id`, `parts[]`, `finish_reason`, `usage?` | Znormalizowany wynik z opcjonalnymi metrykami |
| `InferenceError` | `code`, `retryable`, `provider_details?` | Stabilna klasa błędu i jawna możliwość retry |

Proponowane `kind`: `text`, `image`, `video_frame`, `audio`. `timestamp_s` dotyczy czasu klatki względem początku próbki, nie czasu systemowego; identyfikator modelu nie zastępuje wersji/digestu. `usage` może być nieobecne, nie należy wymyślać tokenów ani wydajności.

## Zachowanie

1. Zdolności są sprawdzane dla konkretnego backendu i modelu; unsupported modality → `UNSUPPORTED_MODALITY`.
2. `request_id` jest przekazywany bez transformacji, co pozwala na powiązanie z zadaniem nadrzędnym.
3. Błędy transportu i limity czasu pozostają odróżnialne od odmowy modelu, pustej odpowiedzi i błędu formatu.
4. Timeout oraz streaming muszą być jawne. Nie następuje automatyczna zmiana modelu ani dostawcy po błędzie.
5. Interfejs nie wykonuje agentowych tool calls, pobierania modeli ani nie zapisuje trwałej historii rozmów.

Wersja schematu, semantyka wyjątków i format serializacji zostaną utrwalone wraz z pierwszą implementacją. Zmiana niekompatybilna po uruchomieniu konsumentów wymaga MAJOR i opisu migracji.
