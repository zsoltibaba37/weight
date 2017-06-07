#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import os
import shutil

print ("-" * 80)
print ("Üdvözlöm.".center(80)) # Középre igazítva
print ("Ez a program kiszámolja egy lemeztábla súlyát.".center(80)) # Középre igazítva
print ("A Programból való kilépéshez nyomja meg a CTRL-C billentyű kombinációt".center(80)) # Középre igazítva
print ("-" * 80)
s = 7.85 # A lágyacél sűrűsége. (The density of the mild steel.)
y = 4 # Ez a szám akármennyi lehet. (This number can be any number.)
while True:
    while True:
        try:
            hossz = int(input('A lemez hossza (mm): '))# A lemeztábla hosszának megkérdezése
            if hossz < 0:
               hossz = 0
            else:
                pass
            z = y/hossz
            break
        except ValueError:
            print ("Ez nem egy szám, vagy nem egész érték van megadva!")#A belovasott érték valóban egész szám?
        except ZeroDivisionError:
            print ("A megadott érték nulla vagy negatív!")#A beolvasott érték nem lehet nulla
        except KeyboardInterrupt:#control-c -re kilép a programból
            sys.exit(0)
    while True:
        try:
            szelesseg = int(input('A lemez szélessége (mm): '))#A lemeztábla szélességének megkérdezése
            if szelesseg < 0:
               szelesseg = 0
            else:
                pass
            w = y/szelesseg
            break
        except ValueError:
            print ("Ez nem egy szám, vagy nem egész érték van megadva!")#A belovasott érték valóban egész szám?
        except ZeroDivisionError:
            print ("A megadott érték nulla vagy negatív!")#A beolvasott érték nem lehet nulla
        except KeyboardInterrupt:#control-c -re kilép a programból
            sys.exit(0)
    while True:
        try:
            vastagsag = float(input('A lemez vastagsága (mm): '))#A lemeztábla vastagságának megkérdezése
            if vastagsag < 0:
               vastagsag = 0
            else:
                pass
            q = y/vastagsag
            break
        except ValueError:
            print ("Ez nem egy szám, vagy a formátum nem jó. Pl.: 1.5")#A belovasott érték valóban lebegőpontos szám?
        except ZeroDivisionError:
            print ("A megadott érték nulla vagy negatív!")#A beolvasott érték nem lehet nulla
        except KeyboardInterrupt:#control-c -re kilép a programból
            sys.exit(0)
    suly = ((hossz*szelesseg*vastagsag*s)/10**6)#A lemeztábla súlyának kiszámolása
    if suly < 1:
        suly = suly * 10**3
        print ("-" * 80)
        print ("A tábla mérete:", hossz, "mm *", szelesseg, "mm *", vastagsag,"mm")
        print ("A lemez súlya:", "%.2f" % suly, "gramm.")#Ha kisebb mint 1kg akkor grammban írja ki a súlyt
        print ("-" * 80)
        print ("A Programból való kilépéshez nyomja meg a CTRL-C billentyű kombinációt".center(80))  # Középre igazítva
        print ("-" * 80)
    else:
        print ("-" * 80)
        print ("A tábla mérete:", hossz, "mm *", szelesseg, "mm *", vastagsag, "mm")
        print ("A lemez súlya:", "%.2f" % suly, "kg.")#Ha nagyobb mint 1kg akkor kilóban írja ki a súlyt
        print ("-" * 80)
        print ("A Programból való kilépéshez nyomja meg a CTRL-C billentyű kombinációt".center(80))  # Középre igazítva
        print ("-" * 80)

