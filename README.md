# Console-Wars

**Console-Wars** is a text-based terminal RPG written in Python. Battle increasingly powerful enemies, manage your inventory, evolve your character, and face off against the **Demon Lord** in endless mode. This is a solo-dev project packed with **scaling stats**, **permadeath**, and **progression systems** that reward tactical decisions.

---

## Gameplay Features

- Fight through 40+ increasingly powerful monster types
- Scale through endless floors with dynamically scaling enemies
- Gain XP and spend it on **Health**, **Damage**, **Defense**, **Dodge**, **Escape Chance**, and **Item Drop Rate**
- Collect 75+ unique **items** with passive boosts and rarity weights
- Rare duplicate items are **auto-sold for coins**
- Coins can be used to **gamble**, **convert into XP**, or **purchase upgrades**
- Adopt a Tamagatchi companion that grows stronger over time and grants **bonus stats**
- Play **minigames** like **Fishing**, **Tamagatchi**, and **Gambling** for side rewards
- Full **save/load system** with automatic file creation and dead save file viewer
- **Permadeath system** — when you die, you can only view stats and inventory

---

## Save System

- All data is saved in `.json` files under the `/saves` folder
- Dead saves are separated from active ones in the file viewer
- Dead characters cannot be played again but can be **fully viewed**

---

## File Structure
```
project_root/
│
├── saves/ # Save files
├── Console-Wars.py # The full game script
└── README.md # This file
```
## Requirements

- Python 3.6+
- `colorama` module (for colored terminal output [This is NOT optional])

Install with:
```bash
pip install colorama
```

## Launching The Game

YOU MUST RUN THE GAME FROM THE TERMINAL FOR IT TO WORK

This game should work on Linux, Windows, or macOS. Choose the command that works with your system and the way you installed Python. You can check which one will work by typing:
```
python --version
python3 --version
py --version
```
```
python Console-Wars.py
```
```
python3 Console-Wars.py
```
```
py Console-Wars.py
```
---
## How to Play
On each screen, simply type the action you want to perform. A list of valid actions will always be provided.

For example, typing attack will attack a monster. You can also use abbreviations like atk. Similarly, retreat can be shortened to ret. Most actions support multiple abbreviations. Typing leave or exit will exit the current screen.

Pressing Enter without typing anything will trigger the default or primary action—usually something like confirming a choice or attacking. This lets you quickly repeat common actions without retyping them every time.

1. Combat
   
    -Face various monsters as you climb through levels, battling them with your stats and inventory items.
    -Use your health, damage, defense, and dodge to survive and defeat enemies.
    -Items found during battles can be sold or used for their stat boosts.

3. Minigames
   
    -Tamagatchi: Adopt a pet and feed it to increase stats.
    -Fishing: Catch fish or rare items for XP and bonuses.
    -Gambling: Place bets with your coins for the chance of big rewards.
    -Gatcha: Collect chracters for passive xp gain.
    -Wishing Well: Spend coins to gain blessings or curses. The well offers a random boost or drawback to your character's stats.
   
7. Reborn
    When you reach a certain level, you can choose to reset your progress for better rewards.

## Note for Cheaters
Cheating in this game is extremely easy—just open the save file in any text editor and change the values. It's stored in JSON format, so it’s readable and editable by anyone.

So why bother with things like idle timeouts or anti-spam detection in fishing? The answer is simple: I want to prevent *accidental* cheating. The game is designed so that playing it fairly is the default and requires no extra effort.

If you choose to cheat, that's entirely up to you. It's a single-player game, and I won’t waste development time trying to stop something I ultimately can’t control. Just play the game however you enjoy it.

## Known Issue(s)
None atm (this doens't mean the program is perfect or has no bugs, it just means that I haven't tested well enough yet)
