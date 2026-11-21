# Dystrybucja

Preferowany format docelowy: pakiet Python `lib-vlm` z katalogu `src/lib_vlm/`. W repozytorium obecnie **nie ma modułów Python, `pyproject.toml` ani opublikowanego pakietu**. Nie jest możliwa instalacja produkcyjna.

Każde wydanie musi posiadać zgodną licencję, określone zależności i lockfile lub reprodukowalny zestaw ograniczeń, test jednostkowy/kontraktowy, build sdist i wheel, clean-install, sprawdzony SHA i zgodę na release. SDK, modele i wagi mają osobne licencje; sam kod biblioteki nie daje prawa do ich dystrybucji.

Repozytorium nie publikuje GitHub Pages przy merge. Dokumentacja publiczna korzysta wyłącznie z `pages/`, odseparowanego od `docs/`.
