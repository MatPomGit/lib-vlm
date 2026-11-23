# audio

**Zakres:** wiadomości audio dla modeli multimodalnych, np. interpretacja nagrania lub odpowiedź mówiona, wyłącznie kiedy backend deklaruje taką funkcjonalność. Każdy fragment ma format, liczbę kanałów, częstotliwość próbkowania, czas trwania i jawne źródło znacznika czasu.

Ten moduł nie zastępuje osobnej biblioteki przetwarzania sygnałów, VAD, akwizycji mikrofonu ani syntezy głosu Piper. Konwersje i dekodowanie powinny być explicit i walidowane; domyślnie nie przechowuje się surowego audio w logach ani trwałych plikach.

**Status: PLANNED, bez kodu.**
