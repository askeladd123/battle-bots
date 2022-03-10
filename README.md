# BattleBots

BattleBots er lite spill der du skal styre en tank ved å programmere instruksjoner i python. Du kan flytte på deg, skyte andre tanks, og plukke opp skudd. Du kan legge til så mange tanks du vil, og på den måten kan dere spille algoritmene mot hverandre, så mange dere vil. Du kan også styre opp til to tanks med piltastene og "wasd".

Spillet er inspirert av oppgavene i et fag jeg hadde, *ikt111*, og følger ca. samme API.

## Build

Altså, er bare source code og bildefiler. Så hvis du klarer å bytte working directory og å sette opp build config, og det ikke funker, så tar jeg 0 ansvar. Men husk å:
1. klone github repo
2. velg `example.py` som target *(IDE-spesefikt)*
3. velg *working directory* der mappen *res* ligger 

## Setup

Åpne `example.py`. Her ser du hvordan jeg bruker API-en. Slik fungerer den: 

Før du starter spillet, kan du registrere en spiller. Det gjør du ved å skrive `super_ai`-funksjonen. Den ser slik ut:

```python
import BattleBots

@BattleBots.register_ai
def super_ai(input):
  ...


BattleBots.start()
```

Inni funksjonen skriver du instruksjonene til din tank. 
1. All tilgjengelig informasjon ligger i objektet *input*.
2. Alle mulige instruksjoner returneres som tekst.

#### Input

|**innhold**       |**type**           |**forklaring**
|------------------|-------------------|-----------
|`position`        |`(int, int)`       |din tank sine x og y-koordinater
|`enemy_positions` |`[(int, int), ...]`|har x og y-koordinater til alle andre tanks
|`enemies`         |`int`              |antall andre tanks
|`ammo`            |`int`              |antall ammo i din tank *(max 3)*
|`bullets`         |`int`              |antall ammo tilstede i labyrinten
|`bullet_positions`|`[(int, int), ...]`|har x og y-koordinatene til patronene i labyrinten
|`gamestate`       |`[[int, ...], ...]`|inneholder id-er for rutene i labyrinten, **forklart under**
|`is_legal()`      |`boolean`          |sier om en gitt rute er ledig, **forklart under**

#### is_legal
Gir `true` hvis en gitt rute er ledig. 
Du spesifiserer hvilken rute ved å gi funksjonen tekst: `"up"`, `"down"`, `"right"`, `"left"`.
Det betyr at du bare kan sjekke naborutene i labyrinten.

#### gamestate
En **n x m** matrise der **n** er ruter i bredden, og **m** er ruter i høyden. 
|id|rute  |
|-|-------|
|0|tom    |
|1|mur    |
|2|spiller|
|3|ammo?? |

Matrisen består av `int`s, der hver rute har en id. 
Du kan bruke dette til å hente mer informasjon om labyrinten.

## Return
Koden min forventer at `super_ai` returnerer instruksjoner som tekst:
- `"up"`, `"down"`, `"right"`, `"left"`.
- `"shoot up"`, `"shoot down"`, `"shoot right"`, `"shoot left"`.

**PASS PÅ:** Hvis din tank står ved en vegg når den skyter, kan den risikere å sprenge seg selv. Det er fordi skuddene har *splash damage*. 

## Start

Etter du har skrevet koden for alle tanks, må du *starte spillet*.

```python
BattleBots.start()
```
```python
BattleBots.start(1)
```
```python
BattleBots.start(2)
```

Parameteret er valgfritt, men bestemmer hvor mange som kan bruke *keyboardet*. 
- **spiller 1:** piltaster og "space"
- **spiller 2:** "wasd" og "h"

###### snakkas - Ask Sødal
