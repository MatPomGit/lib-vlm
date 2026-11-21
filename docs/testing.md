# Plan walidacji i kryteria akceptacji

**Obecny dowód:** tylko testy strukturalne szablonu; inferencja i API lib-vlm nie istnieją.

## Etap CORE

Testy kontraktu i serializacji obejmą: poprawne wieloczęściowe żądanie, odmowę nieobsługiwanej modalności, limity rozmiaru, stabilny `request_id`, timeout, anulowanie i jednoznaczne błędy. Niezgodna wersja schematu nie może zostać przyjęta milcząco.

## Etap PROVIDERS

Mockowane odpowiedzi tekstowe, błędy HTTP, pusty wynik, brak modelu, zmiana capabilities, obsługa strumieniowania i brak wycieku sekretów. Faktyczny test z lokalnym serwerem powinien podać wersję API, model/digest i SHA. Nie wykonywać testów niezaufanych PR na stałych runnerach.

## Etap MULTIMODAL

Obraz: format MIME, rozdzielczość, limit bajtów i integracja z VLM; wideo: wiele klatek, timestampy i zachowana kolejność; audio: format, częstotliwość próbkowania i jawne jednostki. Wynik syntetyczny nie zastępuje testu na realnym modelu.

## Dowody i wydanie

Każdy raport zawiera środowisko, SHA, komendy, identyfikator modelu, metrykę i stan `PASS/FAIL/NOT_RUN/UNAVAILABLE`. Osobno wymagane są build, clean-install, audyt licencji, testy konsumenta i zatwierdzenie wydania. Nie publikować nagrań, obrazów uczestników ani promptów w artefaktach CI.

Polecenia walidacji obecnego szkieletu:

```bash
python scripts/validate_repository.py --phase scaffold
python scripts/validate_documentation.py
python scripts/validate_pages.py
python -m unittest discover -s tests -v
```
