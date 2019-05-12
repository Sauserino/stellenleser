#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def saetze(woerter=["schmunzelte"]):
    
    """Liest aus einer Datei alle Sätze vor, die Schlüsselwörter enthalten. 
    
    Der Funktion wird eine Liste mit Strings als Argument mitgegeben. Default
    ist das Wort 'schmunzelte'. Grundlage ist das File 'text.txt' im 
    selben Ordner wie die Funktion."""
    
    file1 = open("text.txt","r") 
    stelle = False
    
    text = file1.read()
    saetze = text.split(". ")
    
    for satz in saetze: 
        for wort in woerter:
            if wort in satz:
                stelle = True
                os.system("say "+ satz)
                
    if stelle == False:
          os.system("say "+ "Was für ein langweiliges Buch. Es handelt nicht \
          mal von " + woerter[0])

saetze()
