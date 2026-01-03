# Word Play Greek Mod

This repository contains a custom Greek dictionary and letter bag for the game [Word Play](https://store.steampowered.com/app/3586660/Word_Play/) by Game Maker's Toolkit.

## Contents

- `customdictionary.txt`: A list of 314,000+ Greek words in uppercase, cleaned of accents.
- `customletterbag.txt`: Custom letter distribution and scoring based on Greek Scrabble values.

## Installation

To play Word Play in Greek:

1.  Locate your save folder:
    - **Windows**: `%LOCALAPPDATA%Low\Game Maker's Toolkit\Word Play`
2.  Download `customdictionary.txt` and `customletterbag.txt` from this repository.
3.  Place both files into the save folder.
4.  Launch the game. You should see "Custom Dictionary" in the bottom-left corner of the main menu.

## Mod Details

- **Dictionary**: Processed to handle Greek character normalization (e.g., converting 'ς' to 'Σ', removing all accents/tonos).
- **Letter Bag**:
    - Includes 104 tiles (including 2 blanks, not yet supported by the game but accounted for in distribution).
    - Point values and counts follow official Greek Scrabble rules.

## Credits

- Game by [Game Maker's Toolkit](https://www.gamemakerstoolkit.com/).
- Greek word list sourced from [iam1980/greeklish-wordlist](https://github.com/iam1980/greeklish-wordlist).
