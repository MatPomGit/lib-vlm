# ADR-0004: wspólna biblioteka LLM i VLM

Data: 2026-11-21  
Status: accepted (decyzja o granicy repozytorium, bez wydania kodu)

## Kontekst

Tekstowe i multimodalne modele korzystają często z tych samych lokalnych backendów, formatu wiadomości, modelu błędów, konfiguracji i identyfikacji wersji. Oddzielne biblioteki `lib-llm` i `lib-vlm` prowadziłyby do równoległych abstrakcji i walidacji.

## Decyzja

Zachować **`lib-vlm` jako jedyny docelowy właściciel** kodu integracyjnego LLM/VLM. W nim umieścić `core`, `text`, `vision`, `audio` i `providers`. Wykorzystywać istniejące API dostawców zamiast przepisywać silniki inferencji. `lib-llm` nie jest zależnością; jego archiwizacja lub usunięcie następuje osobno.

## Odrzucone warianty

- Dwa niezależne pakiety: duplikacja modeli żądań i adapterów.
- Osobna aplikacja z schedulerem: duplikacja Research Autopilot.
- Włączenie akwizycji kamer i mikrofonów: rozmycie granicy wobec bibliotek sensorycznych.

## Konsekwencje

Jedno API redukuje koszty utrzymania, ale wymaga jawnych capabilities, by nie obiecywać obsługi wizji/audio przez każdy backend. Implementacja, licencja, testy modelowe, E2E i release pozostają niezrealizowane.

Dowody: [architektura](../architecture/components.md), [kontrakt](../contracts.md), [plan testów](../testing.md).
