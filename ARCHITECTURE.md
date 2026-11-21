# Architektura lib-vlm

`lib-vlm` to **jedna biblioteka klienta inferencji** dla modeli LLM i VLM. Nadzoruje format żądania/odpowiedzi oraz adaptery transportowe. Nie pobiera modeli, nie zarządza zadaniami, nie prowadzi schedulerów i nie przejmuje odpowiedzialności Research Autopilot za kolejkę i routing wykonawców.

Planowany kierunek zależności:

```text
Research Autopilot / aplikacja / eksperyment
                |
           lib-vlm.core
                |
       +--------+--------+
       |        |        |
      text    vision   audio
       +--------+--------+
                |
        lib-vlm.providers
                |
     lokalny backend inferencji
```

Katalogi `src/lib_vlm/{core,text,vision,audio,providers}/` zawierają na razie **dokumentację projektową**, nie moduły Python. Szczegóły odpowiedzialności opisano w [komponentach](docs/architecture/components.md). Kontrakt docelowy w [docs/contracts.md](docs/contracts.md) ma status **PROPOSED**; [contracts/api.json](contracts/api.json) rejestruje faktycznie udostępnione symbole (obecnie puste).

Warstwa multimodalna może używać jednego żądania zawierającego treści różnych typów, ale nie może deklarować obsługi modalności niezgłoszonej przez model. Pliki i dane badawcze pozostają poza repozytorium. Transport sieciowy i uprawnienia zapisano w [przepływach danych](docs/architecture/data-flow.md), [prywatności](docs/privacy.md) oraz [ADR-0004](docs/adr/0004-unified-llm-vlm.md).

**Stan:** struktura zaprojektowana, implementacja nie istnieje, testy na modelach NOT_RUN, wydanie NOT_RELEASED.
