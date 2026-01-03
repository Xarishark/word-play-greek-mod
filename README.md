# 🇬🇷 Word Play - Greek Mod

Elevate your **Word Play** experience with this comprehensive Greek language expansion! This mod brings the rich vocabulary and unique balance of the Greek alphabet to Game Maker's Toolkit's word-puzzler.

![GitHub last commit](https://img.shields.io/github/last-commit/Xarishark/word-play-greek-mod?style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/Xarishark/word-play-greek-mod?style=flat-square)

---

## 🚀 Quick Start

To play **Word Play** in Greek, follow these simple steps:

1.  **Locate Save Folder**: Navigate to your game's save location:
    - 📂 `C:\Users\%USERNAME%\AppData\LocalLow\Game Maker's Toolkit\Word Play`
2.  **Install Files**: Download and place [customdictionary.txt](https://raw.githubusercontent.com/Xarishark/word-play-greek-mod/main/customdictionary.txt) and [customletterbag.txt](https://raw.githubusercontent.com/Xarishark/word-play-greek-mod/main/customletterbag.txt) into the folder.
3.  **Launch & Play**: Open the game. Look for the ✨ **"Custom Dictionary"** tag in the bottom-left corner of the main menu.

---

## 📊 Greek Letter Bag (Scrabble Balanced)

The letter distribution and point values are meticulously balanced based on official Greek Scrabble rules to ensure a fair and strategic game.

| Letter | Points | Count | Name |
| :---: | :---: | :---: | :--- |
| **Α** | 1 | 12 | Alpha |
| **Ο** | 1 | 9 | Omicron |
| **Ε** | 1 | 8 | Epsilon |
| **Ι** | 1 | 8 | Iota |
| **Τ** | 1 | 8 | Tau |
| **Η** | 1 | 7 | Eta |
| **Σ** | 1 | 7 | Sigma |
| **Ν** | 1 | 6 | Nu |
| **Ρ** | 2 | 5 | Rho |
| **Κ** | 2 | 4 | Kappa |
| **Π** | 2 | 4 | Pi |
| **Υ** | 2 | 4 | Upsilon |
| **Λ** | 3 | 3 | Lambda |
| **Μ** | 3 | 3 | Mu |
| **Ω** | 3 | 3 | Omega |
| **Γ** | 4 | 2 | Gamma |
| **Δ** | 4 | 2 | Delta |
| **Β** | 8 | 1 | Beta |
| **Φ** | 8 | 1 | Phi |
| **Χ** | 8 | 1 | Chi |
| **Ζ** | 10 | 1 | Zeta |
| **Θ** | 10 | 1 | Theta |
| **Ξ** | 10 | 1 | Xi |
| **Ψ** | 10 | 1 | Psi |
| ✨ | 0 | 2 | Blank (Wildcard) |

---

## 🛠️ Extensibility & Customization

This mod is designed to grow! If you want to add your own dictionaries or specialized word lists:

1.  **Add your words**: Drop any `.txt` file into the `dicts/` folder.
2.  **Process**: Run the script: `python process_words.py`.
3.  **Merge**: The script automatically cleans (removes accents, converts casing, normalizes Sigmas) and merges all lists into a single `customdictionary.txt`.

---

## 📜 Credits & Sources

- **Game**: [Word Play](https://store.steampowered.com/app/3586660/Word_Play/) by Game Maker's Toolkit.
- **Word Lists**: 
  - [iam1980/greeklish-wordlist](https://github.com/iam1980/greeklish-wordlist)
  - [huertatipografica/greekguide](https://github.com/huertatipografica/greekguide)

Developed with ❤️ for the Word Play community.
