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
├── main.py # The full game script
└── README.md # This file
```
## Requirements

- Python 3.6+
- `colorama` module (for colored terminal output)

Install with:
```bash
pip install colorama
```

## Launching The Game
```
python main.py
```
