# Architektura lib-vlm

[ARCHITECTURE.md](../../ARCHITECTURE.md) przedstawia topologię biblioteki. Dokumenty techniczne:

- [Komponenty](components.md): odpowiedzialności planowanych modułów `core/text/vision/audio/providers`.
- [Przepływy danych](data-flow.md): format wejść i wyjść, granice zaufania i przetwarzanie multimodalne.
- [Dystrybucja](distribution.md): plan pakowania i rozdzielenie stanów test/publikacja.
- [Kontrakty](../contracts.md): planowane typy, błędy i semantyka API.
- [ADR-0004](../adr/0004-unified-llm-vlm.md): decyzja o jednym repo dla LLM/VLM.

**Status: PROPOSED / NOT_IMPLEMENTED.** Zmiana kontraktu po uruchomieniu konsumentów wymaga testów i kontroli SemVer.
