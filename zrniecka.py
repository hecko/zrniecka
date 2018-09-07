#!/usr/bin/env python3


def pocet_zrniecok_na_policku(exp):
    pocet = 2 ** exp
    return pocet


vaha_jedneho_zrniecka = 0.029
"""
https://en.wikipedia.org/wiki/Fortescue_Metals_Group
"""
ton_na_meter_vlaku = 29000 / 2500
km_na_mesiac = 384400

total = 0
for policko in range(1, 65):
    total = total + pocet_zrniecok_na_policku(policko - 1)
    print(
        "Policko {} pocet zrniecok na policku {} spolu pocet zrniecok {}".format(
            policko, pocet_zrniecok_na_policku(policko - 1), total
        )
    )

tony = total * vaha_jedneho_zrniecka / 1000 / 1000
dlzka_vlaku_km = tony / ton_na_meter_vlaku / 1000
dlzok_na_mesiac = dlzka_vlaku_km / km_na_mesiac

print("Vaha vsetkych zrniecok (ton): {:.2f}".format(tony))
print("Dlzka vlaku v km: {:.2f}".format(dlzka_vlaku_km))
print("Dlzok na mesiac (cele cislo): {:.0f}".format(dlzok_na_mesiac))
