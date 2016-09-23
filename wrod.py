#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
import sys
import shutil
import math


print ("-" * 80)
print ("Üdvözlöm.".center(80)) # Középre igazítva
print ("Ez a program kiszámolja egy hengeres vasrúd súlyát.".center(80)) # Középre igazítva
print ("A Programból való kilépéshez nyomja meg a CTRL-C billentyű kombinációt".center(80)) # Középre igazítva
print ("-" * 80)
s = 7.85 # A lágyacél sűrűsége. (The density of the mild steel.)
y = 4 # Ez a szám akármennyi lehet. (This number can be any number.)
while True:
    while True:
        try:
            hossz = int(input('A rúd hossza (mm): '))# A rúd hosszának megkérdezése
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
            d = int(input('A rúd ármérője (mm): '))#A rúd átmérőjének megkérdezése
            if d < 0:
               d = 0
            else:
                pass
            w = y/d
            break
        except ValueError:
            print ("Ez nem egy szám, vagy nem egész érték van megadva!")#A belovasott érték valóban egész szám?
        except ZeroDivisionError:
            print ("A megadott érték nulla vagy negatív!")#A beolvasott érték nem lehet nulla
        except KeyboardInterrupt:#control-c -re kilép a programból
            sys.exit(0)
    r = d /2#Sugár
    t = (r * r) * math.pi
    suly = ((t * hossz * s) / 10**6)#A rúd súlyának kiszámolása
    if suly < 1:
        suly = suly * 10**3
        print ("-" * 80)
        print ("A rúd mérete:", hossz, "mm *", d, "mm")
        print ("A rúd súlya:", "%.2f" % suly, "gramm.")#Ha kisebb mint 1kg akkor grammban írja ki a súlyt
        print ("-" * 80)
        print ("A Programból való kilépéshez nyomja meg a CTRL-C billentyű kombinációt".center(80))  # Középre igazítva
        print ("-" * 80)
    else:
        print ("-" * 80)
        print("A rúd mérete:", hossz, "mm *", d, "mm")
        print("A rúd súlya:", "%.2f" % suly, "kg.")  # Ha kisebb mint 1kg akkor grammban írja ki a súlyt
        print ("-" * 80)
        print ("A Programból való kilépéshez nyomja meg a CTRL-C billentyű kombinációt".center(80))  # Középre igazítva
        print ("-" * 80)

