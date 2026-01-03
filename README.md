# 🇬🇷 Word Play - Greek Mod

Elevate your **Word Play** experience with this comprehensive Greek language expansion! This mod brings the rich vocabulary and unique balance of the Greek alphabet to Game Maker's Toolkit's word-puzzler.

![GitHub last commit](https://img.shields.io/github/last-commit/Xarishark/word-play-greek-mod?style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/Xarishark/word-play-greek-mod?style=flat-square)

---

## 🚀 Quick Start

To play **Word Play** in Greek, follow these simple steps:

1.  **Locate Save Folder**: Navigate to your game's save location based on your OS:
    - 🪟 **Windows**: `C:\Users\%USERNAME%\AppData\LocalLow\Game Maker's Toolkit\Word Play`
    - 🍎 **macOS**: `~/Library/Application Support/Game Maker's Toolkit/Word Play`
    - 🐧 **Linux (Proton)**: `~/.steam/steam/steamapps/compatdata/3586660/pfx/drive_c/users/steamuser/AppData/LocalLow/Game Maker's Toolkit/Word Play`
2.  **Install Files**: Download and place [customdictionary.txt](https://raw.githubusercontent.com/Xarishark/word-play-greek-mod/main/customdictionary.txt) and [customletterbag.txt](https://raw.githubusercontent.com/Xarishark/word-play-greek-mod/main/customletterbag.txt) into the folder.
3.  **Launch & Play**: Open the game. Look for the ✨ **"Custom Dictionary"** tag in the bottom-left corner of the main menu.

---

## 📊 Greek Letter Bag (Scrabble Balanced)

The letter distribution and point values are meticulously balanced based on official Greek Scrabble rules to ensure a fair and strategic game.

| Letter | Points | Count | Name |
| :---: | :---: | :---: | :--- |
| **Α** | 1 | 12 | Άλφα |
| **Ο** | 1 | 9 | Όμικρον |
| **Ε** | 1 | 8 | Έψιλον |
| **Ι** | 1 | 8 | Ιώτα |
| **Τ** | 1 | 8 | Ταυ |
| **Η** | 1 | 7 | Ήτα |
| **Σ** | 1 | 7 | Σίγμα |
| **Ν** | 1 | 6 | Νι |
| **Ρ** | 2 | 5 | Ρο |
| **Κ** | 2 | 4 | Κάππα |
| **Π** | 2 | 4 | Πι |
| **Υ** | 2 | 4 | Ύψιλον |
| **Λ** | 3 | 3 | Λάμδα |
| **Μ** | 3 | 3 | Μι |
| **Ω** | 3 | 3 | Ωμέγα |
| **Γ** | 4 | 2 | Γάμμα |
| **Δ** | 4 | 2 | Δέλτα |
| **Β** | 8 | 1 | Βήτα |
| **Φ** | 8 | 1 | Φι |
| **Χ** | 8 | 1 | Χι |
| **Ζ** | 10 | 1 | Ζήτα |
| **Θ** | 10 | 1 | Θήτα |
| **Ξ** | 10 | 1 | Ξι |
| **Ψ** | 10 | 1 | Ψι |
| ✨ | 0 | 2 | Μπαλαντέρ (Wildcard) |

---

### 🛠️ Extensibility & Customization

This mod is designed to grow! If you want to add your own dictionaries or specialized word lists:

1.  **Add your words**: Drop any `.txt` file into the `dicts/` folder.
2.  **Process**: Run the word processor to merge your new words.

> [!IMPORTANT]
> **Python 3 is required** to run the processing script on all platforms. Ensure it is installed and added to your PATH.

#### 🪟 Windows
Double-click `process_words.bat` to run the processor automatically.

#### 🍎 macOS
Open your terminal in the project folder and run:
```bash
sh process_words.sh
```

#### 🐧 Linux
Open your terminal in the project folder and run:
```bash
sh process_words.sh
```

#### 🐍 Advanced (Direct Python)
If you prefer running the script directly:
```bash
python process_words.py
```

3.  **Merge**: The script automatically cleans (removes accents, converts casing, normalizes Sigmas) and merges all lists into a single `customdictionary.txt`.

---

## 📜 Credits & Sources

- **Game**: [Word Play](https://store.steampowered.com/app/3586660/Word_Play/) by Game Maker's Toolkit.
- **Word Lists**: 
  - [iam1980/greeklish-wordlist](https://github.com/iam1980/greeklish-wordlist)
  - [huertatipografica/greekguide](https://github.com/huertatipografica/greekguide)

Developed with ❤️ for the Word Play community.
