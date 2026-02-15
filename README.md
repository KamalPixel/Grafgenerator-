# Lab 1 – Grafgenerator for fysikkrapport 🚗📉

Hei! I stedet for å plotte grafer manuelt i Excel, laget jeg et lite Python-script som automatiserer hele greia.  
Startet som ren latskap, endte opp som et ganske nyttig verktøy.

## Bakgrunn

Dette scriptet ble til for **lab 1 i fysikk og kjemi** (2. semester, dataingeniør).  
Tema: kinematikk, fritt fall og sirkelbevegelse.  

Målet var reproduserbare, pene grafer som er enkle å oppdatere når måledataene endrer seg, og ærlig talt: mye gøyere å kode enn å dra linjer for hånd i Excel.

## Hva genereres?

| Fil                        | Innhold                                                                 |
|----------------------------|-------------------------------------------------------------------------|
| `oppgave1_grafer.png`      | To subplots – bilens bevegelse:<br>• Hastighet over tid<br>• Akselerasjon over tid (stegfunksjon) |
| `oppgave2_sammenligning.png` | Stolpediagram – forsøksdata vs teori for 1 m og 2 m fritt fall:<br>• Falltid<br>• Akselerasjon<br>• Slutthastighet |

Alle grafer har:
- tydelige annotasjoner  
- fargekodet fasemarkering  
- korrekte aksetitler og enheter  

## Kjør selv

```bash
# Installer avhengigheter
pip install -r requirements.txt

# Generer grafene
python generate_graphs.py