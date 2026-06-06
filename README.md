# Sklep internetowy "Multishop" - Backend

Projekt akademicki realizujący architekturę wielowarstwową dla systemu e-commerce.

## O projekcie
Repozytorium zawiera implementację **Warstwy Logiki Biznesowej (Business Logic Layer)** dla modułu obsługi zamówień i zarządzania koszykiem. Projekt został zaprojektowany zgodnie z zasadami programowania obiektowego.

## Architektura i zawartość
Zaimplementowane elementy systemu (w pliku `main.py`):
* **Modele domenowe:** `Product`, `ShoppingCart`
* **Serwisy (Reguły biznesowe):** `OrderService` (weryfikacja dostępności, przeliczanie wartości, aktualizacja stanów magazynowych).
* **Testy jednostkowe:** Moduł `unittest` weryfikujący poprawność działania logiki w izolacji.

## Uruchomienie testów
Aby zweryfikować poprawne działanie logiki biznesowej, należy uruchomić wbudowane testy jednostkowe.

Wymagania: środowisko uruchomieniowe `Python 3.x`. Brak zewnętrznych zależności.

Komenda do uruchomienia:
```bash
python main.py
