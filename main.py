import random
import time
from colorama import Fore, Back, Style
import os
import sys
import platform
import json

# Variables
# Player Varibles
class playerVariables:
    name = "Comment"
    baseHealth = 25
    baseDamage = 3.5
    baseDefense = 0
    actionList = ["Attack","Retreat","Level","Inventory","Exit"]
    buyList = ["Health","Damage","Defense","Dodge","Retreat","Drop Chance"]
    xp = 3
    levelHealthBonus = 0
    levelDamageBonus = 0
    levelDefenseBonus = 0
    inventory = []

class monsterVariables:
    names =     ["Slime","Goblin","Skeleton","Zombie","Vampire","Orc","Giant","Ent","Warg","Banshee","Ghoul","Bandit","Troll","Shade","Basilisk","Minotaur","Witch","Drake","Warlock","Knight","Behemoth","Chimera","Specter","Ogre","Harpy","Revenant","Lich","Manticore","Wyvern","Wyrm","Juggernaut","Hydra","Phantom","Colossus","Ifrit","Kraken","Dreadnought","Leviathan","Titan","Demon Lord"]
    maxHealth = [10,      15,      22,        33,      50,       75,   113,    170,  256,   284,      576,    864,     1297,   1946,   2919,      4378,      6568,   9852,   14778,    22168,   33252,     49878,    74818,    112227,168341, 252511,    378767,568151,     852226,  1278340,1917510,    2876265,4314398,  6471598,   9707397,14561096,21841644,     32762466,   49143699,73715548,]
    maxDamage = [4,        7,      10,        15,      23,       34,    51,     77,  115,   173,      259,    389,      584,    876,   1314,      1971,      2956,   4434,    6651,     9976,   14964,     22445,    33668,     50502, 75754, 113630,    170445,255668,     383502,  575253,  862880,    1294320,1941479,  2912219,   4368329, 6552493,9828740,      14743110,   22114665,33171997,]
    minDamage = [2,        2,       3,         5,       8,       11,    17,     26,   38,    58,       86,    130,      195,    292,    438,       657,       985,   1478,    2217,     3325,    4988,      7482,    11223,     16834, 25251,  37877,     56815, 85223,     127834,  191751,  287627,     431440, 647160,   970740,   1456110, 2184164,3276247,       4914370,    7371555,11057332,]
    Defense =   [0,        1,       1,         1,       2,        3,     4,      6,   10,    14,       22,     32,       49,     73,    109,       164,       246,    369,     554,      831,    1247,      1870,     2806,      4209,  6313,   9469,     14204, 21306,      31959,   47938,   71907,     107860, 161790,   242685,    364027,  546041,819062,        1228592,    1842889,2764333,]

# Drop Table
drop_table = [
    {"name": "Iron Sword",         "desc": "A basic blade. Reliable and sharp.",                         "boosts": {"damage": 5},  "weight": 12},
    {"name": "Leather Armor",      "desc": "Worn leather armor that offers minor protection.",           "boosts": {"defense": 2}, "weight": 14},
    {"name": "Amulet of Vigor",    "desc": "An enchanted charm that slightly improves your health.",     "boosts": {"health": 10}, "weight": 12},
    {"name": "Steel Dagger",       "desc": "Short and fast. Hits quicker than most weapons.",            "boosts": {"damage": 3},  "weight": 13},
    {"name": "Chainmail Vest",     "desc": "A sturdy vest of chain links.",                              "boosts": {"defense": 4}, "weight": 10},
    {"name": "Ruby Ring",          "desc": "Pulses with energy, strengthening your strikes.",            "boosts": {"damage": 7},  "weight": 8},
    {"name": "Iron Shield",        "desc": "Heavy, but it blocks well.",                                 "boosts": {"defense": 5}, "weight": 9},
    {"name": "Pendant of Health",  "desc": "Glows with a soft warmth.",                                  "boosts": {"health": 20}, "weight": 8},
    {"name": "War Axe",            "desc": "Brutal and unforgiving.",                                    "boosts": {"damage": 9},  "weight": 6},
    {"name": "Plated Boots",       "desc": "These boots make you stand strong.",                         "boosts": {"defense": 3}, "weight": 11},
    {"name": "Gold Locket",        "desc": "Gives you a sense of strength from within.",                 "boosts": {"health": 15}, "weight": 9},
    {"name": "Enchanted Blade",    "desc": "Magical edge hums with power.",                              "boosts": {"damage": 10}, "weight": 5},
    {"name": "Guardian Cloak",     "desc": "It deflects incoming strikes slightly.",                     "boosts": {"defense": 6}, "weight": 6},
    {"name": "Heartstone",         "desc": "A gem filled with life essence.",                            "boosts": {"health": 25}, "weight": 6},
    {"name": "Spiked Mace",        "desc": "Devastating on impact.",                                     "boosts": {"damage": 11}, "weight": 4},
    {"name": "Reinforced Helmet",  "desc": "Takes the edge off headshots.",                              "boosts": {"defense": 4}, "weight": 10},
    {"name": "Elixir Band",        "desc": "Increases vitality just by wearing it.",                     "boosts": {"health": 30}, "weight": 5},
    {"name": "Battle Spear",       "desc": "Longer reach and deadly force.",                             "boosts": {"damage": 12}, "weight": 4},
    {"name": "Dragonhide Vest",    "desc": "Tough as ancient scales.",                                   "boosts": {"defense": 7}, "weight": 5},
    {"name": "Phoenix Feather",    "desc": "Emits a life-giving aura.",                                  "boosts": {"health": 35}, "weight": 4},
    {"name": "Silver Rapier",      "desc": "Elegant and efficient.",                                     "boosts": {"damage": 8},  "weight": 7},
    {"name": "Knight’s Gauntlets", "desc": "Enhances arm protection and grip.",                          "boosts": {"defense": 5}, "weight": 7},
    {"name": "Talisman of Grace",  "desc": "Blessed with ancient healing runes.",                        "boosts": {"health": 40}, "weight": 3},
    {"name": "Greatsword",         "desc": "Two hands. One purpose.",                                    "boosts": {"damage": 14}, "weight": 3},
    {"name": "Stoneplate Armor",   "desc": "Like wearing a wall.",                                       "boosts": {"defense": 8}, "weight": 3},
    {"name": "Blood Orb",          "desc": "Pulses with crimson power.",                                 "boosts": {"health": 50}, "weight": 2},
    {"name": "Venom Blade",        "desc": "Lightweight, but extremely deadly.",                         "boosts": {"damage": 13}, "weight": 3},
    {"name": "Shield of Valor",    "desc": "A legacy of ancient kings.",                                 "boosts": {"defense": 6}, "weight": 6},
    {"name": "Moonstone Charm",    "desc": "Gives subtle resilience under pressure.",                    "boosts": {"health": 22}, "weight": 8},
    {"name": "Doomhammer",         "desc": "Slow but apocalyptic.",                                      "boosts": {"damage": 16}, "weight": 2},
    {"name": "Crown of Eternity",  "desc": "Grants unmatched vitality and focus.",                       "boosts": {"health": 100, "defense": 5}, "weight": 1},
    {"name": "Obsidian Crusher",   "desc": "Crushes foes with devastating force.",                       "boosts": {"damage": 25}, "weight": 1},
    {"name": "Celestial Shroud",   "desc": "Whispers of protection from beyond.",                        "boosts": {"defense": 12}, "weight": 1},
    {"name": "Ring of Titans",     "desc": "Endless power flows through it.",                            "boosts": {"damage": 20, "health": 20}, "weight": 1},
    {"name": "Mantle of Immortals","desc": "Even death fears its wearer.",                               "boosts": {"health": 150}, "weight": 1},
    {"name": "Abyssal Fang",       "desc": "Bleeds enemies with every strike.",                          "boosts": {"damage": 22}, "weight": 1},
    {"name": "Plate of Aeons",     "desc": "A shield against time itself.",                              "boosts": {"defense": 15}, "weight": 1},
    {"name": "Void Pendant",       "desc": "Grants dark resilience and twisted strength.",               "boosts": {"health": 80, "damage": 10}, "weight": 1},
    {"name": "Sundering Greatblade","desc": "No armor can resist it.",                                   "boosts": {"damage": 30}, "weight": 1},
    {"name": "Mythrilheart Armor", "desc": "Impossibly light, indestructible.",                          "boosts": {"defense": 18, "health": 40}, "weight": 1},
    {"name": "Scarab Seal",        "desc": "Surrounds you in an ethereal shield.",                       "boosts": {"defense": 10}, "weight": 1},
    {"name": "Runed Circlet",      "desc": "Glows with ancient life magic.",                             "boosts": {"health": 90}, "weight": 1},
    {"name": "Storm Gauntlets",    "desc": "Your blows carry thunder.",                                  "boosts": {"damage": 18}, "weight": 1},
    {"name": "Shield of Endings",   "desc": "Nullifies even the worst blows.",                           "boosts": {"defense": 20}, "weight": 1},
    {"name": "Lifeblood Gem",      "desc": "Pulses in time with your heart.",                            "boosts": {"health": 120}, "weight": 1},
    {"name": "Dagger of Stars",    "desc": "Swift and unstoppable.",                                     "boosts": {"damage": 15}, "weight": 1},
    {"name": "Solar Medallion",    "desc": "Bathes you in burning resilience.",                          "boosts": {"health": 70, "defense": 8}, "weight": 1},
    {"name": "Hammer of Glory",    "desc": "Swings with divine vengeance.",                              "boosts": {"damage": 26}, "weight": 1},
    {"name": "Aegis of the Fallen","desc": "Shields you with lost souls.",                               "boosts": {"defense": 17}, "weight": 1},
    {"name": "Seraph’s Band",      "desc": "Crackles with divine protection.",                           "boosts": {"health": 60, "defense": 6}, "weight": 1},
    {"name": "Frostbrand Blade",   "desc": "Frozen and furious.",                                        "boosts": {"damage": 24}, "weight": 1},
    {"name": "Warden’s Cuirass",   "desc": "Unbending and eternal.",                                     "boosts": {"defense": 14}, "weight": 1},
    {"name": "Eclipse Ring",       "desc": "You feel the universe tremble.",                             "boosts": {"damage": 12, "defense": 6}, "weight": 1},
    {"name": "Godscale Vest",      "desc": "Crafted from myth itself.",                                  "boosts": {"defense": 20}, "weight": 1},
    {"name": "Lifeveil Charm",     "desc": "Stitches your wounds instantly.",                            "boosts": {"health": 110}, "weight": 1},
    {"name": "Hellforge Blade",    "desc": "Forged in damnation.",                                       "boosts": {"damage": 28}, "weight": 1},
    {"name": "Divine Anklet",      "desc": "You dodge like a shadow.",                                   "boosts": {"defense": 7}, "weight": 1},
    {"name": "Warlock’s Fang",     "desc": "Thirsts for blood.",                                         "boosts": {"damage": 23}, "weight": 1},
    {"name": "Tombplate",          "desc": "You feel nothing. And take nothing.",                        "boosts": {"defense": 22}, "weight": 1},
    {"name": "Genesis Relic",      "desc": "The beginning of all things.",                               "boosts": {"health": 200, "damage": 10}, "weight": 1},
    {"name": "Blade of Oblivion",  "desc": "Slices through reality itself.",                             "boosts": {"damage": 40}, "weight": 0.5},
    {"name": "Titan's Heart",      "desc": "Massive vitality from a fallen giant.",                      "boosts": {"health": 250}, "weight": 0.5},
    {"name": "Aethercloak",        "desc": "Phase through danger unharmed.",                             "boosts": {"defense": 25}, "weight": 0.5},
    {"name": "Crown of Stars",     "desc": "Intelligence beyond comprehension.",                         "boosts": {"health": 100, "defense": 10}, "weight": 0.5},
    {"name": "Ruinblade",          "desc": "Every swing leaves devastation behind.",                     "boosts": {"damage": 38}, "weight": 0.5},
    {"name": "Stoneblood Aegis",   "desc": "Even gods struggle to crack it.",                            "boosts": {"defense": 30}, "weight": 0.5},
    {"name": "Crimson Mantle",     "desc": "Burns the weak who dare strike you.",                        "boosts": {"health": 80, "defense": 15}, "weight": 0.5},
    {"name": "Thunder King's Rod", "desc": "Bolts crackle with each blow.",                              "boosts": {"damage": 34}, "weight": 0.5},
    {"name": "Godsbane",           "desc": "Meant to slay immortals.",                                   "boosts": {"damage": 50}, "weight": 0.25},
    {"name": "Soulforge Mail",     "desc": "Made from lost souls and steel.",                            "boosts": {"defense": 28, "health": 60}, "weight": 0.5},
    {"name": "Ankh of Resurrection","desc": "Refuses to let you die easily.",                            "boosts": {"health": 300}, "weight": 0.25},
    {"name": "Void Hammer",        "desc": "Leaves nothing where it strikes.",                           "boosts": {"damage": 45}, "weight": 0.25},
    {"name": "Eternal Bulwark",    "desc": "Shields passed down by titans.",                             "boosts": {"defense": 35}, "weight": 0.25},
    {"name": "Helm of the Last King","desc": "A relic of the age of giants.",                            "boosts": {"defense": 20, "health": 100}, "weight": 0.5},
    {"name": "Flametongue Sigil",  "desc": "Burns through both body and soul.",                          "boosts": {"damage": 37}, "weight": 0.5},
    {"name": "Gilded Halo",        "desc": "Angelic grace sustains you.",                                "boosts": {"health": 150}, "weight": 0.5},
    {"name": "Nightmare Edge",     "desc": "Fears made manifest in a blade.",                            "boosts": {"damage": 42}, "weight": 0.25},
    {"name": "Runebound Shell",    "desc": "Arcane script reinforces its structure.",                    "boosts": {"defense": 33}, "weight": 0.25},
    {"name": "Oathkeeper Ring",    "desc": "Binds you to invincible resolve.",                           "boosts": {"damage": 15, "defense": 15}, "weight": 0.25},
    {"name": "Eclipse Mantle",     "desc": "Draws shadows to protect you.",                              "boosts": {"defense": 24, "health": 70}, "weight": 0.25},
    {"name": "Heart of Infinity",  "desc": "Pumps endless life into your veins.",                        "boosts": {"health": 1000}, "weight": 0.05},
    {"name": "Worldrender Blade",  "desc": "Sunder the world with a single swing.",                      "boosts": {"damage": 500}, "weight": 0.05},
    {"name": "Aegis of Creation",  "desc": "The origin of all protection.",                              "boosts": {"defense": 300}, "weight": 0.05},
    {"name": "Core of the Cosmos", "desc": "A fragment of the universe itself.",                         "boosts": {"health": 500, "damage": 200, "defense": 150}, "weight": 0.05},
    {"name": "Eternal Warplate",   "desc": "Forged from eternity, never fails.",                         "boosts": {"defense": 500}, "weight": 0.05},
    {"name": "Annihilation Fang",  "desc": "Each strike devours existence.",                             "boosts": {"damage": 1000}, "weight": 0.05},
    {"name": "Veil of the End",    "desc": "Shields its bearer from death itself.",                      "boosts": {"health": 700, "defense": 200}, "weight": 0.05},
    {"name": "Godbreaker",         "desc": "Crafted to kill the divine.",                                "boosts": {"damage": 750}, "weight": 0.05},
    {"name": "Bloodmoon Relic",    "desc": "Hungers for endless battle.",                                "boosts": {"health": 400, "damage": 300}, "weight": 0.05},
    {"name": "Shield of Eternity", "desc": "No force may breach its guard.",                             "boosts": {"defense": 600}, "weight": 0.05}
]

# Current Variables
currentHealth = playerVariables.baseHealth
currentDamage = playerVariables.baseDamage
currentDefense = playerVariables.baseDefense

monsterId = 0
currentMonsterFight = monsterVariables.names[monsterId]
currentMonsterHealth = monsterVariables.maxHealth[monsterId]
currentMonsterDefense = monsterVariables.Defense[monsterId]

maxHealth = playerVariables.baseHealth
currentFloor = 0
firstLaunch = True

currentSaveName = ''
savedGames = []
globalSavePath = ''
saveDirectory = "saves"
os.makedirs(saveDirectory, exist_ok=True)
player = playerVariables()

healthboostCost = 2
damageBoostCost = 3
DefenseBoostCost = 4
dodgeBoostCost = 5
escapeBoostCost = 2
dropChanceBoostCost = 10

healthboostCostFactor = 1.15
damageBoostCostFactor = 1.25
DefenseBoostCostFactor = 1.4
dodgeBoostCostFactor = 1.7
escapeboostCostFactor = 1.1
dropChanceBoostCostFactor = 1.4

healthBoostMod = 3
damageBoostMod = 2.5
defenseBoostMod = 1
dodgeBoostMod = 5
escapeBoostMod = 20
dropChanceBoostMod = 0.07 

# Define the current os and clear screen properly
def clearScreen():
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

# Functions
def saveToFile():
    global currentMonsterFight, currentMonsterHealth, globalSavePath, monsterId
    save_path = os.path.join(saveDirectory, currentSaveName)
    globalSavePath = save_path

    data = {
        "player": {
            "name": player.name,
            "baseHealth": player.baseHealth,
            "baseDamage": player.baseDamage,
            "baseDefense": player.baseDefense,
            "levelHealthBonus": player.levelHealthBonus,
            "levelDamageBonus": player.levelDamageBonus,
            "levelDefenseBonus": player.levelDefenseBonus,
            "xp": player.xp,
            "inventory": player.inventory
        },
        "currentHealth": currentHealth,
        "maxHealth": maxHealth,
        "currentFloor": currentFloor,
        "dodgeBoostMod": dodgeBoostMod,
        "escapeBoostMod": escapeBoostMod,
        "dropChanceBoostMod": dropChanceBoostMod,
        "healthboostCost": healthboostCost,
        "damageBoostCost": damageBoostCost,
        "DefenseBoostCost": DefenseBoostCost,
        "dodgeBoostCost": dodgeBoostCost,
        "escapeBoostCost": escapeBoostCost,
        "dropChanceBoostCost": dropChanceBoostCost,
        "currentMonsterFight": currentMonsterFight,
        "currentMonsterHealth": currentMonsterHealth,
        "monsterId": monsterId,
        "firstLaunch": firstLaunch
    }

    with open(save_path, "w") as f:
        json.dump(data, f, indent=4)

def listSavedFiles():
    files = os.listdir(saveDirectory)
    json_files = [f for f in files if f.endswith('.json')]
    print(Fore.BLACK+"|")
    print(Fore.GREEN+"Saved files:")
    print(Fore.CYAN+"")
    for f in json_files:
        print(f)

def loadFromFile(filename):
    global currentHealth, maxHealth, currentFloor
    global dodgeBoostMod, escapeBoostMod, dropChanceBoostMod
    global healthboostCost, damageBoostCost, DefenseBoostCost
    global dodgeBoostCost, escapeBoostCost, dropChanceBoostCost
    global currentMonsterFight, currentMonsterHealth, monsterId, firstLaunch

    save_path = os.path.join(saveDirectory, filename)
    try:
        with open(save_path, "r") as f:
            data = json.load(f)
        print(Fore.GREEN + f"Loaded from {save_path}")

        # Restore player variables
        player.name = data["player"].get("name", player.name)
        player.baseHealth = data["player"].get("baseHealth", player.baseHealth)
        player.baseDamage = data["player"].get("baseDamage", player.baseDamage)
        player.baseDefense = data["player"].get("baseDefense", player.baseDefense)
        player.levelHealthBonus = data["player"].get("levelHealthBonus", player.levelHealthBonus)
        player.levelDamageBonus = data["player"].get("levelDamageBonus", player.levelDamageBonus)
        player.levelDefenseBonus = data["player"].get("levelDefenseBonus", player.levelDefenseBonus)
        player.xp = data["player"].get("xp", player.xp)
        player.inventory = data["player"].get("inventory", [])

        # Restore global variables
        currentHealth = data.get("currentHealth", currentHealth)
        maxHealth = data.get("maxHealth", maxHealth)
        currentFloor = data.get("currentFloor", currentFloor)
        dodgeBoostMod = data.get("dodgeBoostMod", dodgeBoostMod)
        escapeBoostMod = data.get("escapeBoostMod", escapeBoostMod)
        dropChanceBoostMod = data.get("dropChanceBoostMod", dropChanceBoostMod)
        healthboostCost = data.get("healthboostCost", healthboostCost)
        damageBoostCost = data.get("damageBoostCost", damageBoostCost)
        DefenseBoostCost = data.get("DefenseBoostCost", DefenseBoostCost)
        dodgeBoostCost = data.get("dodgeBoostCost", dodgeBoostCost)
        escapeBoostCost = data.get("escapeBoostCost", escapeBoostCost)
        dropChanceBoostCost = data.get("dropChanceBoostCost", dropChanceBoostCost)
        currentMonsterFight = data.get("currentMonsterFight", currentMonsterFight)
        currentMonsterHealth = data.get("currentMonsterHealth", currentMonsterHealth)
        monsterId = data.get("monsterId", monsterId)
        firstLaunch = data.get("firstLaunch",firstLaunch)

        apply_inventory_boosts()
        return data
    except FileNotFoundError:
        print(Fore.RED + "File not found.")
        return None

def try_drop_item():
    global drop_table, dropChanceBoostMod

    if drop_table and random.random() < dropChanceBoostMod:
        # Get weights for current drop table
        weights = [item.get("weight", 1) for item in drop_table]

        # Randomly pick based on weights
        item = random.choices(drop_table, weights=weights, k=1)[0]

        player.inventory.append(item)
        #drop_table.remove(item)

        print(Fore.BLACK+"|")
        print(Fore.MAGENTA + f"You found: {item['name']}!")
        print(Fore.YELLOW + item['desc'])
        print(Fore.BLACK+"|")
        apply_inventory_boosts()
        time.sleep(0.5)

def apply_inventory_boosts():
    global currentHealth, maxHealth, currentDamage, currentDefense

    # Use instance values from player
    maxHealth = player.baseHealth + player.levelHealthBonus
    currentDamage = player.baseDamage + player.levelDamageBonus
    currentDefense = player.baseDefense + player.levelDefenseBonus

    for item in player.inventory:
        boosts = item.get("boosts", {})
        maxHealth += boosts.get("health", 0)
        currentDamage += boosts.get("damage", 0)
        currentDefense += boosts.get("defense", 0)

    if currentHealth > maxHealth:
        currentHealth = maxHealth

def get_dynamic_weights(currentFloor, total_monsters):
    kills = int(currentFloor * 100)
    tier_step = 10  # New tier every 10 kills
    tier_size = 3   # Always 3 monsters at once

    # Calculate the tier index
    tier_start = min((kills // tier_step), total_monsters - tier_size)
    tier_end = tier_start + tier_size

    # Assign fixed rarity-based weights to the active trio
    base_weights = [1.0, 0.75, 0.5]  # common, uncommon, rare

    weights = []
    for i in range(total_monsters):
        if tier_start <= i < tier_end:
            weights.append(base_weights[i - tier_start])
        else:
            weights.append(0)
    return weights

def showInventory():
    global currentHealth,currentDamage,currentDefense,monsterId,currentMonsterFight,currentMonsterHealth,currentMonsterDefense,healthboostCost
    global damageBoostCost,DefenseBoostCost, healthBoostMod, damageBoostMod, defenseBoostMod, dodgeBoostMod, escapeBoostMod, dodgeBoostCost, dodgeBoostCostFactor
    global escapeBoostCost, escapeboostCostFactor, maxHealth, currentFloor, dropChanceBoostMod, dropChanceBoostCost, dropChanceBoostCostFactor
    clearScreen()
    print(Style.RESET_ALL)
    print(Fore.BLACK+"|")
    print(Fore.BLUE+"Inventory:")
    print(Fore.BLACK+"|")
    if len(player.inventory) == 0:
        print(Fore.RED+"Your inventory is empty!")
        print(Fore.BLUE+"When you kill monsters you have a rare chance to collect an artifact")
        print(Fore.BLUE+"These artifacts grant perminent passive boosts")
    else:
        for item in player.inventory:
            print(Fore.CYAN,item["name"])
            print(Fore.YELLOW,item["desc"])
            print(Fore.MAGENTA,item["boosts"])
    print(Fore.BLACK+"|")
    print(Fore.BLACK+"|")
    print(Fore.BLUE+"Hit 'enter' to leave this screen")
    choice = input().lower()
    combat()

def resetMonster():
    global currentHealth,currentDamage,currentDefense,monsterId,currentMonsterFight,currentMonsterHealth,currentMonsterDefense,healthboostCost
    global damageBoostCost,DefenseBoostCost, healthBoostMod, damageBoostMod, defenseBoostMod, dodgeBoostMod, escapeBoostMod, dodgeBoostCost, dodgeBoostCostFactor
    global escapeBoostCost, escapeboostCostFactor, maxHealth, currentFloor, dropChanceBoostMod, dropChanceBoostCost, dropChanceBoostCostFactor
    #monsterId = random.randint(0,len(monsterVariables.names)-1)
    weights = get_dynamic_weights(currentFloor, len(monsterVariables.names))
    monsterId = random.choices(range(len(monsterVariables.names)), weights=weights, k=1)[0]
    currentMonsterFight = monsterVariables.names[monsterId]
    currentMonsterHealth = monsterVariables.maxHealth[monsterId]
    currentMonsterDefense = monsterVariables.Defense[monsterId]

def showCombatStats():
    global currentHealth,currentDamage,currentDefense,monsterId,currentMonsterFight,currentMonsterHealth,currentMonsterDefense,healthboostCost
    global damageBoostCost,DefenseBoostCost, healthBoostMod, damageBoostMod, defenseBoostMod, dodgeBoostMod, escapeBoostMod, dodgeBoostCost, dodgeBoostCostFactor
    global escapeBoostCost, escapeboostCostFactor, maxHealth, currentFloor, dropChanceBoostMod, dropChanceBoostCost, dropChanceBoostCostFactor
    clearScreen()
    print(Style.RESET_ALL)
    monsterHealthPercentage = round((currentMonsterHealth / monsterVariables.maxHealth[monsterId]) * 100,2)
    print(Fore.WHITE +"You are currently fighting a",currentMonsterFight," ( Difficulty:",round(currentFloor*100),")")
    print(Fore.BLACK +"|")
    print(Fore.RED+currentMonsterFight,"Health:")
    print(Fore.BLACK +"|",end='')
    for i in range(round(monsterHealthPercentage/2)): print(Fore.RED +'=',end='')
    print(Fore.RED+"",monsterHealthPercentage,"%")
    print(Fore.BLACK +"|")
    print(Fore.BLACK +"|")
    currentHealthPercentage = round((currentHealth / maxHealth) * 100,2)
    print(Fore.GREEN+"Player Stats:")
    print(Fore.GREEN+" Health: ",end='')
    for i in range(round(currentHealthPercentage/2.4)): print(Fore.GREEN +'=',end='')
    print("",currentHealthPercentage,"%  (",currentHealth,")")
    print(Fore.GREEN +" Damage:",round(currentDamage,1), " |  Defense:",round(currentDefense,1)," |  Xp:",round(player.xp,1))
    print(Fore.GREEN +" Dodge Chance:",dodgeBoostMod,"% |  Retreat Chance:",escapeBoostMod,"%"," |  Item Drop Chance:",round(dropChanceBoostMod*100),"%")
    print(Fore.BLACK +"|")
    print(Fore.BLUE +"Actions:",player.actionList)
    print(Style.RESET_ALL)
    
def levelup():
    global currentHealth,currentDamage,currentDefense,monsterId,currentMonsterFight,currentMonsterHealth,currentMonsterDefense,healthboostCost
    global damageBoostCost,DefenseBoostCost, healthBoostMod, damageBoostMod, defenseBoostMod, dodgeBoostMod, escapeBoostMod, dodgeBoostCost, dodgeBoostCostFactor
    global escapeBoostCost, escapeboostCostFactor, maxHealth, currentFloor, dropChanceBoostMod, dropChanceBoostCost, dropChanceBoostCostFactor
    clearScreen()
    print(Style.RESET_ALL)
    print(Fore.BLACK+"|")
    print(Fore.GREEN+"Ugrade Costs (Current Xp:",round(player.xp,1),")")
    print(Fore.GREEN+" Health Boost:",healthboostCost," |  Damage Boost:",damageBoostCost," |  Defense Boost:",DefenseBoostCost,"\n Dodge Boost:",dodgeBoostCost,"  | Retreat Boost:",escapeBoostCost, " |  Item Drop Boost:",dropChanceBoostCost)
    print(Fore.BLACK+"|")
    print(Fore.BLACK+"|")
    print(Fore.BLUE+"Things you can buy:",player.buyList)
    print(Fore.BLUE+"(Type 'exit' to go back to combat)")
    choice = input().lower()
    if choice == "health" or choice == "hlth" or choice == "hp":
        if player.xp >= healthboostCost:
            player.levelHealthBonus += healthBoostMod
            currentHealth = round(healthBoostMod + currentHealth,2)
            if currentHealth >= maxHealth:
                currentHealth = maxHealth
            healthBoostMod = round(healthBoostMod * healthboostCostFactor,1)
            player.xp -= healthboostCost
            healthboostCost = round(healthboostCost * healthboostCostFactor,1)
            apply_inventory_boosts()
        else:
            print(Fore.RED+"You don't have enough xp for this!")
    elif choice == "damage" or choice == "dmg":
        if player.xp >= damageBoostCost:
            player.levelDamageBonus += damageBoostMod
            damageBoostMod = round(damageBoostMod * damageBoostCostFactor,1)
            player.xp -= damageBoostCost
            damageBoostCost = round(damageBoostCost * damageBoostCostFactor,1)
            apply_inventory_boosts()
        else:
            print(Fore.RED+"You don't have enough xp for this!")
    elif choice == "defense" or choice == "def":
        if player.xp >= DefenseBoostCost:
            player.levelDefenseBonus += defenseBoostMod
            defenseBoostMod = round(defenseBoostMod * DefenseBoostCostFactor,1)
            player.xp -= DefenseBoostCost
            DefenseBoostCost = round(DefenseBoostCost * DefenseBoostCostFactor,1)
            apply_inventory_boosts()
        else:
            print(Fore.RED+"You don't have enough xp for this!")
    elif choice == "dodge" or choice == "dod" or choice == "dodge chance" or choice == "dodgechance":
        if player.xp >= dodgeBoostCost:
            if dodgeBoostMod >= 60:
                print(Fore.RED+"You can't have a higher dodge chance!")
            else:
                dodgeBoostMod += 2
                if dodgeBoostMod >= 60:
                    dodgeBoostMod = 60
                player.xp -= dodgeBoostCost
                dodgeBoostCost = round(dodgeBoostCost * dodgeBoostCostFactor,1)
        else:
            print(Fore.RED+"You don't have enough xp for this!")
    elif choice == "retreat" or choice == "ret" or choice == "escape" or choice == "esc":
        if player.xp >= escapeBoostCost:
            if escapeBoostMod >= 90:
                print(Fore.RED+"You can't have a higher retreat chance!")
            else:
                escapeBoostMod += 5
                if escapeBoostMod >= 90:
                    escapeBoostMod = 90
                player.xp -= escapeBoostCost
                escapeBoostCost = round(escapeBoostCost * escapeboostCostFactor,1)
        else:
            print(Fore.RED+"You don't have enough xp for this!")
    elif choice == "drop" or choice == "drp" or choice == "drop chance" or choice == "dropchance":
        if player.xp >= dropChanceBoostCost:
            if dropChanceBoostMod >= .25:
                print(Fore.RED+"You can't have a higher drop chance!")
            else:
                dropChanceBoostMod = round(0.02 + dropChanceBoostMod,2)
                if dropChanceBoostMod >= .25:
                    dropChanceBoostMod = .25
                player.xp -= dropChanceBoostCost
                dropChanceBoostCost = round(dropChanceBoostCost * dropChanceBoostCostFactor,1)
        else:
            print(Fore.RED+"You don't have enough xp for this!")
    elif choice == 'exit':
        time.sleep(0.5)
        combat()
    else:
        print(Fore.RED+"Invalid Input")
    time.sleep(0.5)
    levelup()

def combat():
    global currentHealth,currentDamage,currentDefense,monsterId,currentMonsterFight,currentMonsterHealth,currentMonsterDefense,healthboostCost
    global damageBoostCost,DefenseBoostCost, healthBoostMod, damageBoostMod, defenseBoostMod, dodgeBoostMod, escapeBoostMod, dodgeBoostCost, dodgeBoostCostFactor
    global escapeBoostCost, escapeboostCostFactor, maxHealth, currentFloor, dropChanceBoostMod, dropChanceBoostCost, dropChanceBoostCostFactor
    dodged = False
    escaped = False
    showCombatStats()
    saveToFile() # Saves the file every turn
    # Player's actions
    choice = input().lower()
    if choice == "attack" or choice == "atk":
        print(Fore.YELLOW +"You are attacking!")
        damage = round((currentDamage + random.uniform(0,5)) - currentMonsterDefense,2) 
        if damage <= 1:
            damage = 1
        currentMonsterHealth -= damage
        print(Fore.RED +"You dealt",damage,"to",currentMonsterFight)
        time.sleep(0.3)
    elif choice == "retreat" or choice == "ret":
        print(Fore.YELLOW +"You are attempting to retreat!")
        retreatChance = random.randrange(0,100)
        if retreatChance <= escapeBoostMod:
            print(Fore.YELLOW+"You escaped!")
            escaped = True
        else:
            print(Fore.YELLOW+"You failed to escape!")
            escaped = False
        time.sleep(0.3)
    elif choice == "level" or choice == "lvl":
        levelup()
    elif choice == "inventory" or choice == "inv":
        showInventory()
    elif choice == "exit":
        sys.exit()
    else:
        print(Fore.RED +"Invalid input")
        time.sleep(0.8)
        combat()
    time.sleep(0.5)
    # Section that plays when you beat a monster
    if currentMonsterHealth <= 0:
        print(Fore.GREEN +"You win!")
        currentHealth = round(healthBoostMod+currentHealth,2)
        currentFloor = round(0.01 + currentFloor,2)
        if currentHealth >= maxHealth:
            currentHealth = maxHealth
        print(Fore.GREEN+"Healing some health back...")
        try_drop_item()
        player.xp += round(monsterVariables.maxHealth[monsterId]/13,1)
        resetMonster()
        apply_inventory_boosts()
        time.sleep(0.5)
        combat()
    # Section for the monster to fight back
    else:
        dodgeChance = random.randint(0,100)
        
        if dodgeChance <= dodgeBoostMod:
            dodged = True
        if dodged == True:
            print(Fore.YELLOW+"You dodged the attack!")
            time.sleep(0.8)
            combat()
        if escaped == True:
            resetMonster()
        else:
            print(Fore.YELLOW +currentMonsterFight,"is attacking you!")
            damage = round(random.uniform(monsterVariables.minDamage[monsterId],monsterVariables.maxDamage[monsterId]) - currentDefense,2)
            if damage <= 1:
                damage = 1
            currentHealth = round(currentHealth - damage,2)
            print(Fore.RED+currentMonsterFight,"deals",damage,"damage!")
    # What happens when you die
    if currentHealth <= 0:
        print("You died!")
        path = globalSavePath
        #print(Fore.CYAN,path," is the current path")
        if os.path.exists(str(path)):
            print(Fore.RED,str(currentSaveName)," is being deleted")
            os.remove(path)
        time.sleep(1)
        print(Style.RESET_ALL)
        sys.exit()
    else:
        time.sleep(0.8)
        combat()
    
def main():
    global currentSaveName, savedGames, loadedData, firstLaunch
    print(Style.RESET_ALL)
    clearScreen()
    print(Fore.BLUE+"What is your name? [type the name you used previously to load the file]")
    listSavedFiles()
    name_input = input().strip().lower()
    
    # Ensure the save file ends with `.json`
    if not name_input.endswith('.json'):
        name_input += '.json'
    
    currentSaveName = name_input
    
    savedGames = os.listdir(saveDirectory)
    savedGames = [f for f in savedGames if f.endswith('.json')]
    
    if currentSaveName in savedGames:
        loadedData = loadFromFile(currentSaveName)
    else:
        print(Fore.GREEN+f"New save will be created as '{currentSaveName}'.")

    if firstLaunch == True:
        print(Fore.YELLOW+"Chooce difficulty: (Easy or Hard)")
        print(Fore.CYAN+"          (Easy justs boosts your starting xp)")
        choice = input().lower()
        if choice == "easy":
            print(Fore.GREEN+"Granting extra xp!")
            player.xp += 10
        else:
            pass
    else:
        pass
    firstLaunch = False
    combat()

if __name__ == "__main__":
    main()
