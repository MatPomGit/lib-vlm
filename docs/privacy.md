# Prywatność i dane multimodalne

Biblioteka ma przyjmować tekst, obrazy, klatki wideo i audio, które mogą zawierać dane osobowe. **Nie przechowuje się** materiałów uczestników, nagrań, promptów ani danych eksperymentalnych w publicznym repozytorium, PR, Pages i logach CI.

Przed implementacją transportu należy określić dozwolone endpointy, kontrolę przesyłania danych poza host, retencję, zgodę i cel przetwarzania oraz minimalną telemetrię. Nie wolno utożsamiać `localhost` z pełną izolacją: kontrolę dostępu i uprawnień zapewnia również konfiguracja backendu.

Identyfikatory sprzętu i źródeł pomiarowych należą do kontrolowanego rejestru urządzeń; metadane pochodzenia, timestampy i wersje modeli mogą być zapisywane wyłącznie zgodnie z polityką danych eksperymentu. Każdy adapter musi definiować, co opuszcza proces i które pola mogą znaleźć się w logach. Domyślnie odrzuca się pełne payloady w logowaniu.
