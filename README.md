# Pribeh o sachu

Ked som chodil na navstevy k mojmu dedovi a uz som zacal navstevovat zakladnu skolu, dodo, asko sme ho volali, mi z casu na cas pripomenul tento pribeh o tom ako tento jeden sedliak vymyslel sach.

Po predstaveni sachovej hry vladcovi krajiny sa vladca optytal aku odmenu si vynalezca praje za tuto hru. Vynalezca mu vravi - na prve policko dajte jedno zrnko ryze, na druhe dve, na tretie styri a takto pokracujte az do posledneho policka. To bude moja odmena. Vladcovi to neprislo vela.

Kolko to je v skutocnosti zrniecok a kolko kilo ryze vynalezca dostal?

Mame 8x8 = 64 policok. Postupnost je jednoducha dvojkova sustava s faktorialom - zacneme 2^0, co je 1 na prvom policku, pokracujeme az do 2^63 a potom vseto spocitame.

| Policko | Pocet zrniecok na policku | Celkovy pocet zrniecok |
| ------- | ------------------------- | ---------------------- |
| A1 (1)  | 2^0 = 1                   | 1                      |
| A2 (2)  | 2^1 = 2                   | 2^0 + 2^1 = 3          |
| A3 (3)  | 2^2 = 4                   | 1 + 2 + 4 = 7          |
| ...     |                           |                        |
| H8 (64) | 2^63                      | 2^0 + 2^1 + … + 2^63   |

## Vypocet

Vypocet poctu zrniecok je v Python scripte zrniecka.py - staci spustit program (python3)

## NB

Tento pribeh sa vola aj https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem ako som zistil v 2022. Original zaznam o pribehu ktory mi rozpraval dodo nechavam bez zmeny.
