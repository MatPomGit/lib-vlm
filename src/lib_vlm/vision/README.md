# vision

**Zakres:** pojedyncze obrazy i uporządkowane serie klatek wideo kierowane do modelu VLM. Obraz powinien mieć jawny format MIME, rozmiar, pochodzenie i kontrolę maksymalnego rozmiaru danych. Klatki wideo zachowują timestamp w sekundach lub jawnej jednostce i kolejność.

Normalizacja obrazu, próbkowanie klatek i ekstrakcja z kamery nie należą do tego modułu: realizują je odrębne biblioteki obrazu lub aplikacje. Adapter VLM przekazuje zatwierdzone fragmenty danych; nie publikuje materiału badawczego ani danych osób badanych w logach.

Capability discovery rozróżnia wejścia obrazu, wieloobrazowe i natywne wideo. **Status: PLANNED, bez kodu.**
