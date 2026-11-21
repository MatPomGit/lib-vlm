# ADR-0001: jeden właściciel kontraktu

Data: 2026-11-21  
Status: proposed

## Kontekst

Klienci lokalnych modeli tekstowych i multimodalnych potrzebują spójnego modelu żądania, odpowiedzi i błędu; duplikacja kontraktów utrudnia reprodukowalność.

## Propozycja

Repozytorium `lib-vlm` posiada kanoniczny kontrakt oraz planowany kod `core` i `providers`. `contracts/api.json` rejestruje **faktycznie dostępne** symbole (na razie brak), a [docs/contracts.md](../contracts.md) opisuje kontrakt docelowy. Systemy badawcze przypinają wersję lub SHA, bez kopiowania biblioteki.

## Konsekwencje

Wspólne API dla LLM/VLM; breaking change wymaga dokumentacji i testów zgodności. Planowane konstrukcje pozostają `NOT_IMPLEMENTED` do czasu dowodu.
