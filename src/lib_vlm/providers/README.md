# providers

**Zakres:** adaptery do istniejących silników inferencji, a nie własna implementacja LLM/VLM. Kandydaci: lokalne API Ollama, kompatybilne endpointy OpenAI, llama.cpp server; dodatkowi dostawcy tylko gdy uzasadnia ich rzeczywisty konsument.

Każdy adapter implementuje wspólny kontrakt z `core`, mapuje odpowiedzi i wyjątki na typy biblioteki oraz **deklaruje rzeczywistą** obsługę tekstu, obrazu, audio, streaming, structured output, narzędzia i limity kontekstu. Nie powinien udawać funkcji nieobsługiwanej przez backend.

Wymagane: jawnie wybrany endpoint, timeouts, kontrola egress, bezpieczna obsługa tokenów, brak logowania promptów i danych osobowych. Domyślnie preferowany backend lokalny, ale sama sieć loopback nie gwarantuje bezpieczeństwa.

**Status: PLANNED, bez kodu i integracji.**
