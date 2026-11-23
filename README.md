# lib-vlm

**Wspólna biblioteka dostępu do modeli językowych i multimodalnych.** Projekt obejmuje LLM oraz VLM w jednym repozytorium i jednej rodzinie kontraktów. Status: **architektura opracowana, implementacja i wydanie NOT_IMPLEMENTED**.

Biblioteka ma ujednolicać żądania tekstowe, obrazy, wybrane reprezentacje wideo i audio, odpowiedzi, metadane modelu oraz błędy backendów. Głównym zastosowaniem jest integracja lokalnej inferencji z narzędziami badawczymi i automatyzacją. Nie jest to odrębny system agentowy ani silnik inferencji.

## Zakres

| Moduł | Zakres | Status |
| --- | --- | --- |
| [core](src/lib_vlm/core/README.md) | ModelRequest, ModelResponse, części treści, zdolności modelu | PLANNED |
| [text](src/lib_vlm/text/README.md) | Konwersacje, tekst, odpowiedzi strukturalne | PLANNED |
| [vision](src/lib_vlm/vision/README.md) | Obrazy, klatki wideo i metadane czasowe | PLANNED |
| [audio](src/lib_vlm/audio/README.md) | Wejście i wyjście audio modeli multimodalnych | PLANNED |
| [providers](src/lib_vlm/providers/README.md) | Adaptery lokalnych API inferencji | PLANNED |

## Dokumentacja

[Architektura](ARCHITECTURE.md) · [Kontrakt API](docs/contracts.md) · [Przepływ danych](docs/architecture/data-flow.md) · [Plan walidacji](docs/testing.md) · [Roadmap](docs/roadmap.md) · [Bezpieczeństwo](SECURITY.md).

Jedynym właścicielem kodu multimodalnych adapterów będzie `lib-vlm`; osobne `lib-llm` nie jest zależnością ani wymogiem. Planowane integracje to Research Autopilot, aplikacje eksperymentalne oraz biblioteki Unity/Unreal. **Nie ma jeszcze potwierdzonych konsumentów ani testów inferencji.**

## Status techniczny

W repozytorium działa jedynie szkielet walidacji. Brak instalowalnego pakietu, modeli i runtime. `LICENSE` wymaga wyboru licencji przed dystrybucją. Dokumentacja w `docs/` jest inżynierska; `pages/` pozostaje oddzielnym źródłem ewentualnej witryny, bez automatycznej publikacji.
