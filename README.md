# Console-Wars

**Console-Wars** is a text-based terminal RPG written in Python. Battle increasingly powerful enemies, manage your inventory, evolve your character, and face off against the **Demon Lord** in endless mode. This is a solo-dev project packed with **scaling stats**, **permadeath**, and **progression systems** that reward tactical decisions.

---

## Gameplay Features

- Battle through 40+ unique and scaling monster types across endless floors
- Fight stronger monsters and bosses as you progress through the infinite tower
- Earn XP and spend it to permanently upgrade **Health**, **Damage**, **Defense**, **Dodge Chance**, **Retreat Chance**, and **Item Drop Rate**
- Play minigames like:
  - **Fishing**: Timed reaction-based item/XP minigame with anti-spam logic
  - **Gambling**: Risk coins for greater rewards, sell items, or convert coins to XP
  - **Gatcha**: Unlock passive XP-earning characters who fight in the background
  - **Wishing Well**: Spend coins for powerful blessings or dangerous curses
  - **Reborn**: Reset progress after Floor 25 for massive rewards and improved scaling
- Dynamic scaling system for **XP gain**, **coin value**, and **combat difficulty**
- Fully integrated **save/load system** with automatic saving and a detailed dead-player stats screen
- **Permadeath**: If you die, your run ends — you can view your stats but must start a new game

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

- Python 3.3 or higher
- The `colorama` module (for colored terminal output — **this is NOT optional**)

Install `colorama` with:

```bash
pip install colorama
```
---

## Installing Python

### Windows

1. Download the latest version of Python from the official site: https://www.python.org/downloads/windows/
2. Run the installer.
3. **Important:** Make sure to check the box that says **"Add Python to PATH"** during installation.
4. After installation, open Command Prompt and type `python --version` to verify it works.

### macOS
I don't generally use a mac so it hasn't been tested as much (I don't own one) so if this doesn't work then follow the tutorial on this website: https://docs.python.org/3/using/mac.html

1. Install Homebrew if you don’t already have it:  
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Python:  
   ```bash
   brew install python
   ```
3. Confirm installation:  
   ```bash
   python3 --version
   ```

### Linux
Generally doing anything here is unnessisary as python is installed by default, just check what version you have and ensure it works.

If you do need to install it change the dnf to apt or pacman or whatever your package installer is. 

1. Update package list and install Python:
   ```bash
   sudo dnf update
   sudo dnf install python3 python3-pip
   ```
2. Confirm installation:
   ```bash
   python3 --version
   ```

### Installing Pip
On Linux or Mac
```
python -m ensurepip --upgrade
```
And on windows
```
py -m ensurepip --upgrade
```
Go to https://pip.pypa.io/en/stable/installation/ for more information

After installing Pip, use `pip` or `pip3` to install the required module:

```bash
pip install colorama
# or
pip3 install colorama
```

## Launching The Game

YOU MUST RUN THE GAME FROM THE TERMINAL FOR IT TO WORK

This game should work on Linux, Windows, or macOS. Choose the command that works with your system and the way you installed Python.
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

The goal of the game is to kill as many demon lords as possible, they will be unlocked once you make it far enough into the game. 

Combat

- Face various monsters as you climb through levels, battling them with your stats and inventory items.
- Use your health, damage, defense, and dodge to survive and defeat enemies.
- Items found during battles can be sold or used for their stat boosts.

Minigames
   
- Tamagatchi: Adopt a pet and feed it to increase stats.
- Fishing: Catch fish or rare items for XP and bonuses.
- Gambling: Place bets with your coins for the chance of big rewards.
- Gatcha: Collect chracters for passive xp gain.
- Wishing Well: Spend coins to gain blessings or curses. The well offers a random boost or drawback to your character's stats.

Reborn
- When you reach a certain level, you can choose to reset your progress for better rewards.

## Note on Releases vs. Source Code

The **Releases** tab contains major versions that are considered relatively stable. However, these releases may be slightly outdated compared to the latest version in the repository.

The main `.py` file in the repository is a **rolling release** used for active testing and development. It will always contain the most up-to-date features, but may be less stable or partially unfinished.

If you want the newest features, clone or download the source directly. If you prefer a more stable experience, use the latest tagged release.

## Note for Cheaters
Cheating in this game is extremely easy—just open the save file in any text editor and change the values. It's stored in JSON format, so it’s readable and editable by anyone.

So why bother with things like idle timeouts or anti-spam detection in fishing? The answer is simple: I want to prevent *accidental* cheating. The game is designed so that playing it fairly is the default and requires no extra effort.

If you choose to cheat, that's entirely up to you. It's a single-player game, and I won’t waste development time trying to stop something I ultimately can’t control. Just play the game however you enjoy it.

## Known Issue(s)
On some devices the fishing minigame will simply not work, when hitting enter quickly to catch a fish nothing will happen

## Disclaimer
This program was my first python program in a while, it was originaly just supposed to be a practice program to relearn python but it kept getting more complicated beacuse it ended up being really fun. I would like to make other games at some point as well but this won't ever really be big, it was never even supposed to get a full release. 
