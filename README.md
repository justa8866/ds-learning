# ds-learning

Repozytorium do nauki i realizacji pierwszych projektów z zakresu uczenia maszynowego.
Materiały i ćwiczenia obejmują analizę danych oraz pracę z Git.

## Cel projektu

Poznawanie procesu analizy danych: od przygotowania i eksploracji danych, przez ich wizualizację, aż po wyciąganie wniosków.

## Etapy pracy

- Przygotowanie i sprawdzenie jakości danych.
- Eksploracja danych i wizualizacja zależności.
- Podsumowanie wyników i wniosków.

## Dane i modele

Pliki CSV oraz lokalne katalogi `data/` i `models/` są ignorowane przez Git. Nie trafiają do historii repozytorium.

## Synchronizacja

Zmiany z lokalnego repozytorium i GitHub są łączone za pomocą poleceń `push` i `pull`.

## Porównywanie zmian

- `git diff` pokazuje niezacommitowane zmiany w plikach.
- `git diff HEAD~1 HEAD` porównuje ostatni commit z jego poprzednikiem.
- `git diff <commit-hash1> <commit-hash2>` porównuje dwa wybrane commity.
