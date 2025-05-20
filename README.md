# Console-Wars

**Console-Wars** is a retro-style **text-based combat RPG** built in Python. Battle your way through endless monsters, collect powerful loot, and upgrade your stats to survive ever-harder encounters. This project is a **solo development prototype**, currently in early development.

---

## Gameplay Overview

- Fight against a growing roster of **progressively stronger monsters**.
- Gain XP with each victory and **spend it to upgrade** your stats: health, damage, defense, dodge chance, retreat chance, and item drop rate.
- Collect **artifacts** (loot drops) that give **permanent stat boosts**.
- Each artifact has **custom stats**, drop weights, and flavor text.
- Player and monster stats scale dynamically.
- Save and load persistent progress across sessions.

---

## Current Features

- **Fully interactive combat loop** with attack, retreat, inventory, and leveling options
- **Weighted item drop system** with over 75+ unique items, including rare and legendary-tier gear
- **Save/load system** using `.json` files
- **Randomized monster generation** based on floor level and weighted difficulty scaling
- **Stat-based combat** including dodge, defense reduction, and scaling damage
- **Console-based UI** with colored text via `colorama` for immersive feedback

---

## File Structure
```
project_root/
│
├── saves/ # Contains savegame JSON files
├── main.py # Core game logic (this file)
└── README.md # You're reading it
---
```

## Requirements

- Python 3.3+
- `colorama` module

Install dependencies with:
```bash
pip install colorama
```

## Running The Game
```
python main.py
```


