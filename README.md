# Word Play Greek Mod

This repository contains a custom Greek dictionary and letter bag for the game [Word Play](https://store.steampowered.com/app/3586660/Word_Play/) by Game Maker's Toolkit.

## Contents

- `customdictionary.txt`: A list of 452,157 unique Greek words in uppercase, cleaned of accents.
- `customletterbag.txt`: Custom letter distribution and scoring based on Greek Scrabble values.

## Installation

To play Word Play in Greek:

1.  Locate your save folder:
    - **Windows**: `%LOCALAPPDATA%Low\Game Maker's Toolkit\Word Play`
2.  Download `customdictionary.txt` and `customletterbag.txt` from this repository.
3.  Place both files into the save folder.
4.  Launch the game. You should see "Custom Dictionary" in the bottom-left corner of the main menu.

## Adding Your Own Dictionaries

This mod is designed to be extensible! If you have additional Greek word lists, you can easily include them:

1.  Place your word list as a `.txt` file in the `dicts/` folder.
2.  Run the processing script: `python process_words.py`.
3.  The script will automatically scan all `.txt` files in `dicts/`, clean them, and merge them into a single `customdictionary.txt`.
4.  Copy the new `customdictionary.txt` to your game folder.

## Mod Details

- **Dictionary**: Processed to handle Greek character normalization (e.g., converting 'ς' to 'Σ', removing all accents/tonos).
- **Letter Bag**:
    - Includes 104 tiles (including 2 blanks, not yet supported by the game but accounted for in distribution).
    - Point values and counts follow official Greek Scrabble rules.

## Credits

- Game by [Game Maker's Toolkit](https://www.gamemakerstoolkit.com/).
- Greek word lists sourced from [iam1980/greeklish-wordlist](https://github.com/iam1980/greeklish-wordlist) and [huertatipografica/greekguide](https://github.com/huertatipografica/greekguide).
