# Przepływy danych i granice zaufania

Projektowany przebieg: **konsument → żądanie `core` → walidacja zdolności i modalności → adapter `providers` → wskazany backend → normalizacja odpowiedzi → konsument**.

## Dane wejściowe

Żądanie zawiera identyfikator modelu, listę uporządkowanych wiadomości/fragmentów i parametry generowania. Fragment może reprezentować tekst, obraz, klatkę wideo z timestampem lub audio z jednostkami pomiarowymi. Rozmiary, typy MIME, limity liczby klatek i czasu audio muszą zostać zweryfikowane przed wysłaniem. Kod źródłowy nie przechowuje danych eksperymentalnych ani surowych mediów.

## Granice zaufania

Wybrany endpoint to osobna granica zaufania nawet przy `localhost`. Żadne żądanie nie może samoczynnie wybrać zewnętrznego hosta, przesłać pliku bez zgody wywołującego, rozwiązywać ścieżek poza autoryzowanym katalogiem ani ujawniać promptów w logach. Sekrety są przekazywane przez środowisko/menedżer poświadczeń konsumenta i nie są serializowane w raporcie.

## Odtwarzalność

Raport wykonania powinien zawierać: identyfikator żądania, backend i faktyczną wersję modelu (w tym digest, jeżeli dostępny), parametry, źródło czasu, status i zmierzone czasy wykonania. Hash wejścia wyłącznie wtedy, gdy polityka danych pozwala na taką metadaną; nie zapisywać obrazów, audio ani danych osób badanych w publicznym CI.

**Stan implementacji i audytu ruchu sieciowego: NOT_RUN.**
