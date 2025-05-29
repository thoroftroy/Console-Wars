# Console-Wars

**Console-Wars** is a brutal, text-based terminal RPG written in Python. Battle increasingly powerful enemies, manage your inventory, evolve your character, and face off against the **Demon Lord** in endless mode. This is a solo-dev project packed with **scaling stats**, **permadeath**, and **progression systems** that reward tactical decisions.

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

## Minigames

- **Fishing** – Time-based reaction game to catch fish or rare items
- **Gambling** – Risk coins for big multipliers
- **Tamagatchi** – Feed and care for your companion to unlock permanent stat boosts

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
**Note**

You will notice that there are 3 python files in the repository. Main is the original, Main2 is a slightly older version of the main game and Console-Wars is the actual game. The other two files are only there for archival purposes, you do not need to install them. 

## How to Play
1. Combat
   
    Face various monsters as you climb through levels, battling them with your stats and inventory items.
    Use your health, damage, defense, and dodge to survive and defeat enemies.
    Items found during battles can be sold, used for stat boosts, or used to heal.

3. Minigames
   
    Tamagatchi: Adopt a pet and feed it to increase stats.
    Fishing: Catch fish or rare items for XP and bonuses.
    Gambling: Place bets with your coins for the chance of big rewards.
   
5. Wishing Well
   
    Spend coins to gain blessings or curses. The well offers a random boost or drawback to your character's stats.
   
7. Reborn
   
    When you reach a certain level, you can choose to reset your progress for better rewards.
## Known Issue(s)
For the life of me I can't figure out how but the tamagatchi's bond can go above its maximum number

If you play the old version(s) (main.py):

*WARNING* this issue is gamebreaking: If you play for too long it reaches a maximum recursion rate and currupts you entire save. I am currently working on a fix. For now, every 200 or so levels just exit and reopen the game and that will temporarily fix it.

The game is so broken with lots of hacky garbage code so I am working on a second version of the game, main2.py is this newer version, it will slowly get updates as I recode the entire thing but with hindsite helping the orginization.

It is reccomended that you always play the Console-Wars version or the major release in the releases tab. This version is running in the new code-base and has many less bugs.

