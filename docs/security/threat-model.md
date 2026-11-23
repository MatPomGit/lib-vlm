# Model zagrożeń biblioteki lib-vlm

**Status: PROPOSED / NOT_IMPLEMENTED.** Jest to analiza zagrożeń
planowanej architektury multimodalnej, a nie audyt uruchomionego kodu.
Inferencja, przesyłanie mediów, testy modelowe i sprzętowe: **NOT_RUN**.

| Aktywo / granica zaufania | Scenariusz i skutek | Planowana kontrola oraz kryterium testu |
| --- | --- | --- |
| Prompty, historia konwersacji, instrukcje | Ujawnienie poufnego tekstu lub prompt injection w materiałach źródłowych | Redakcja logów, rozdzielenie instrukcji od danych, test niezaufanej treści |
| Obrazy, wideo, audio uczestników | Przesłanie danych osobowych do nieautoryzowanego backendu | `data_classification`, świadomy odbiorca, zgoda/podstawa, odmowa niejawnego transferu |
| Dane wejściowe `core` | Payload z niedozwoloną modalnością, formatem lub rozmiarem | Limity MIME/bajtów/klatek/czasu i negatywne testy odrzucenia |
| `providers` i endpoint sieciowy | Nieautoryzowany `network_egress`, DNS/redirect i zdalny wyciek | Jawna allowlista celu, portu, adresu IP, brak ukrytych przekierowań, test odmowy |
| Poświadczenia, tokeny, metadane | Eksfiltracja przez logi, wyjątki, pliki lub telemetrykę | Sekrety w kontrolowanym magazynie, maskowanie, testy braku wycieków |
| Odpowiedź modelu / użycie u konsumenta | Halucynacje i złośliwe sugestie interpretowane jako instrukcje | Odpowiedź jako dane niezaufane, brak samoczynnych tool calls, odrębna kontrola działań |
| Retencja i pochodzenie | Ponowne użycie lub niejawne utrwalenie danych, ujawnienie przez hash i identyfikatory | Jawna retencja, usuwanie, minimalizacja i uprawnienia, test braku payloadu w artefaktach |
| Model, dostawca i wydanie | Nieautoryzowane pobranie modelu lub błędna identyfikacja wersji | Rejestr dostawcy/digest, licencja, audyt zależności, clean-install i zgoda na release |

## Właściciel kontroli i warunki uruchomienia

Właściciel kontraktu biblioteki odpowiada za walidację
`data_classification`, `network_egress`, rozmiarów danych oraz
identyfikatorów modelu. Konsument odpowiada za podstawę przetwarzania,
uprawnienia użytkownika, politykę retencji i odbiorców. Operator
backendu odpowiada za uwierzytelnienie, izolację hosta i zgodność
z deklarowanym endpointem. Odpowiedzialności **nie są obecnie
zaimplementowanymi zabezpieczeniami**.

Przed pierwszym aktywnym providerem wymagane są: rozszerzenie
`config/component.json` i walidatora, negatywne testy deny-by-default,
testy egress/retencji, przegląd uprawnień i zatwierdzenie odbiorcy.
Brak dowolnego obowiązkowego elementu ma kończyć się
`DENY / NOT_CONFIGURED`. Prawdziwe dane nie mogą trafiać do CI.

## Ryzyko rezydualne

Brak modeli i runtime uniemożliwia pomiar skuteczności zabezpieczeń.
`config/component.json` nie zawiera aktualnie `data_classification`
ani `network_egress`. `LICENSE` jest `UNDECIDED`;
`SECURITY.md` ma `CONTACT_NOT_CONFIGURED`.
To jawne bramki przed implementacją i wydaniem, a nie dowody PASS.

[Polityka prywatności](../privacy.md) ·
[Przepływy](../architecture/data-flow.md) ·
[Testy](../testing.md)
