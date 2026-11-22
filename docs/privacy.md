# Prywatność i dane multimodalne

**Status: PROPOSED / NOT_IMPLEMENTED.** Biblioteka nie wykonuje
inferencji ani transportu. Tekst, obrazy, klatki wideo, audio i prompty
mogą zawierać dane osobowe lub wrażliwe. Nie umieszcza się danych osób
badanych, nagrań, promptów ani sekretów w publicznych repozytoriach,
PR, Issues, Pages i logach CI.

## Jawny brak zabezpieczeń w manifeście

Aktualny `config/component.json` **nie zawiera** pól
`data_classification` ani `network_egress`. Są to
**niezaimplementowane mechanizmy kontroli**, a nie wartości domyślnie
bezpieczne. Przed wdrożeniem pierwszego `providers` należy uzupełnić
kontrakt manifestu i jego walidację; brak klasyfikacji lub reguły
egress oznacza **DENY / NOT_CONFIGURED**, nie pozwolenie na inferencję
lub przesyłanie danych.

## Minimalny kontrakt przed uruchomieniem transportu

| Granica | Warunek konieczny | Stan |
| --- | --- | --- |
| Konsument → `core` | Cel, zgoda/podstawa przetwarzania, pochodzenie, `data_classification` i dozwolone modalności | NOT_IMPLEMENTED |
| `core` → `providers` | Limity wejścia i rozmiaru mediów, walidacja MIME, uprawnień do plików i zdolności modelu | NOT_IMPLEMENTED |
| `providers` → backend | Jawna allowlista adresów i portów `network_egress`, tożsamość odbiorcy, autoryzacja, zakaz ukrytych przekierowań | NOT_IMPLEMENTED |
| Backend → wynik/log | Retencja, termin usuwania, minimalizacja pól, redakcja promptów i danych uczestników, kontrola dostępu | NOT_IMPLEMENTED |

Nazwa `localhost` nie jest dowodem izolacji ani autoryzacji backendu.
Bez jawnej konfiguracji endpointu, zasad retencji, decyzji o eksporcie
i zakresu zbieranych danych adapter **nie powinien być uruchamiany**
z danymi rzeczywistymi. Sekrety pozostają poza repo, poza promptami
i poza raportami testów. Identyfikatory urządzeń, znaczniki czasu,
wersje modeli i metadane pochodzenia podlegają polityce eksperymentu;
mogą same ujawniać wrażliwe informacje.

## Przyszłe testy negatywne

Przed E2E wymagane są odtwarzalne przypadki odmowy: brak klasyfikacji
danych, nieznany odbiorca lub endpoint, nieautoryzowany egress, plik
poza dozwolonym katalogiem, niedozwolona modalność, nadmierny rozmiar
mediów, nieokreślona retencja oraz próba ujawnienia payloadu lub tokenu
w logach. Testy używają syntetycznych danych, jawnych SHA i wersji
backendu. **Obecne testy inferencji, zabezpieczeń runtime i E2E:
NOT_RUN**. Zielony Scaffold CI nie potwierdza działania tych kontroli.

Powiązania: [model zagrożeń](security/threat-model.md),
[przepływ danych](architecture/data-flow.md),
[plan walidacji](testing.md).
