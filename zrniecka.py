#!/usr/bin/env python3


def pocet_zrniecok_na_policku(exp):
    pocet = 2**exp
    return pocet


VJZ = 0.029  # vaha jedneho zrniecka ryze (v gramoch)
"""
https://en.wikipedia.org/wiki/Fortescue_Metals_Group
"""
TNMV = 29000 / 2500  # ton_na_meter_vlaku
KMNM = 384400  # km na mesiac

total = 0
for policko in range(1, 65):
    total = total + pocet_zrniecok_na_policku(policko - 1)
    print(
        f"Policko {policko} -> zrniecok na policku {pocet_zrniecok_na_policku(policko - 1)}, spolu pocet zrniecok {total}"
    )

tony = total * VJZ / 1000 / 1000
dlzka_vlaku_km = tony / TNMV / 1000
dlzok_na_mesiac = dlzka_vlaku_km / KMNM

print(f"Vaha vsetkych zrniecok (ton): {tony:.2f}")
print(f"Dlzka vlaku v km: {dlzka_vlaku_km:.2f}")
print(f"Dlzok na mesiac (cele cislo): {dlzok_na_mesiac:.0f}")
