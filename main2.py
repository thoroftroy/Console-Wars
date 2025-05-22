import random
import time
from colorama import Fore, Back, Style
import os
import sys
import platform
import json
from datetime import datetime
import threading

# Define libraries and classes
class playerVariables:
    name = "placeHolderName"
    maxHealth = 25
    health = 25
    damage = 3.5
    defense = 0
    dodge = 5
    escape = 20
    drop = 7
    
    difficulty = 0 # Difficulty goes from 5 - 15, 15 = Easy, 10 = Normal, and 5 = Hard. This just deteramins starting xp (direclty the same number as difficulty but also recorded for the stats screen)
    
    actionList = ["Attack","Retreat","Level","Inventory","Minigames/Other","Stats","Exit"]
    buyList = ["Health","Damage","Defense","Dodge","Retreat","Drop"]
    gameList = ["Tamagachi","Gambling","Fishing","Wishing Well","Reborn"]
    
    xp = 0
    coins = 0
    inventory = []
    
    healthBoost = 0
    damageBoost = 0
    defenseBoost = 0
    dodgeBoost = 0
    escapeBoost = 0

class monsterVariables:
    names =     ["Slime","Goblin","Skeleton","Zombie","Vampire","Orc","Giant","Ent","Warg","Banshee","Ghoul","Bandit","Troll","Shade","Basilisk","Minotaur","Witch","Drake","Warlock","Knight","Behemoth","Chimera","Specter","Ogre","Harpy","Revenant","Lich","Manticore","Wyvern","Wyrm","Juggernaut","Hydra","Phantom","Colossus","Ifrit","Kraken","Dreadnought","Leviathan","Titan","Demon Lord"]
    maxHealth = [10,      15,      22,        33,      50,       75,   113,    170,  256,   284,      576,    864,     1297,   1946,   2919,      4378,      6568,   9852,   14778,    22168,   33252,     49878,    74818,    112227,168341, 252511,    378767,568151,     852226,  1278340,1917510,    2876265,4314398,  6471598,   9707397,14561096,21841644,     32762466,   49143699,73715548,]
    maxDamage = [4,        7,      10,        15,      23,       34,    51,     77,  115,   173,      259,    389,      584,    876,   1314,      1971,      2956,   4434,    6651,     9976,   14964,     22445,    33668,     50502, 75754, 113630,    170445,255668,     383502,  575253,  862880,    1294320,1941479,  2912219,   4368329, 6552493,9828740,      14743110,   22114665,33171997,]
    minDamage = [2,        2,       3,         5,       8,       11,    17,     26,   38,    58,       86,    130,      195,    292,    438,       657,       985,   1478,    2217,     3325,    4988,      7482,    11223,     16834, 25251,  37877,     56815, 85223,     127834,  191751,  287627,     431440, 647160,   970740,   1456110, 2184164,3276247,       4914370,    7371555,11057332,]
    Defense =   [0,        1,       1,         1,       2,        3,     4,      6,   10,    14,       22,     32,       49,     73,    109,       164,       246,    369,     554,      831,    1247,      1870,     2806,      4209,  6313,   9469,     14204, 21306,      31959,   47938,   71907,     107860, 161790,   242685,    364027,  546041,819062,        1228592,    1842889,2764333,]

    monsterId = 0
    
    currentMonsterHealth = 0
    
# Endless mode
endlessMode = False
endlessKills = 0
demon_lord_data = {
    "demonLordsDefeated": 0,
    
    "health": monsterVariables.maxHealth[-1],
    "minDamage": monsterVariables.minDamage[-1],
    "maxDamage": monsterVariables.maxDamage[-1],
    "defense": monsterVariables.Defense[-1]
}

# Minigame libraries
tamagatchi_data = {
    "tamagatchiFeeds": 0,
    
    "active": False,
    "last_update": None,
    "hunger": 0,
    "bond": 0,
    "boosts": {"health": 0, "damage": 0, "defense": 0}
}

fishing_data = {
    "active": False,
    "fishCaught": 0,
    "itemsFished": 0,
}

gambling_data = {
    "gamblingBets": 0,
    "gamblingCoinsSpent": 0,
    "gamblingCoinsWon": 0,
    "itemsSold": 0,
    "coinsFromSelling": 0,
    "coinsConvertedToXP": 0,
}

well_data = {
    "wishing_well_cost": 1000,
    "wishingCoinsUsed": 0,
    "blessingsReceived": 0,
    "cursesReceived": 0,
    "divineSpark": 0,
    "obtainedBlessings": [],
    "obtainedCurses": [],
}

# Keep track of stats from the shop
shop_data = {
    # The base cost of each item in the shop
    "baseHealthBoostCost": 2,
    "baseDamageBoostCost": 3,
    "baseDefenseBoostCost": 4,
    "baseDodgeBoostCost": 5,
    "baseEscapeBoostCost": 2,
    "baseDropBoostCost": 10,
    
    # How much the cost goes up each time
    "baseHealthBoostCostFactor": 1.15,
    "baseDamageBoostCostFactor": 1.25,
    "baseDefenseBoostCostFactor": 1.4,
    "baseDodgeBoostCostFactor": 1.7,
    "baseEscapeBoostCostFactor": 1.1,
    "baseDropBoostCostFactor": 1.4,
    
    # How much each boost gives you each time (This number is multiplied with the stat for exponential increases)
    "healthBoostMod": 1.2,
    "damageBoostMod": 1.2,
    "defenseBoostMod": 1.2,
    "dodgeBoostMod": 1.2,
    "escapeBoostMod": 1.2,
    "dropBoostMod": 1.2,
    
    "healthBoostCap": 10000000000,
    "damageBoostCap": 10000000000,
    "defenseBoostCap": 10000000000,
    "dodgeBoostCap": 55,
    "escapeBoostCap": 95,
    "dropBoostCap": 25,
}

# Other Stats to keep track of
persistentStats = {
    "currentFloor": 0,
    "currentRoom": 0,
    "monstersKilled": 0,
    "rebornsUsed": 0,
    "is_dead": False,
}

# Current Variables
# Classes for ease
player = playerVariables()
monster = monsterVariables()
# Important stuff
firstLaunch = True

# Monster Variables
currentMonsterFight = monster[monster.monsterId] # type: ignore
currentMonsterHealth = monster[monster.monsterId] # type: ignore

# Save and load variables
currentSaveName = ''
savedGames = []
globalSavePath = ''
saveDirectory = "saves"
os.makedirs(saveDirectory, exist_ok=True)

# Drop Table
drop_table = [
    {"name": "Iron Sword",         "desc": "A basic blade. Reliable and sharp.",                         "boosts": {"damage": 5},  "weight": 12},
    {"name": "Leather Armor",      "desc": "Worn leather armor that offers minor protection.",           "boosts": {"defense": 2}, "weight": 14},
    {"name": "Amulet of Vigor",    "desc": "An enchanted charm that slightly improves your health.",     "boosts": {"health": 10}, "weight": 12},
    {"name": "Steel Dagger",       "desc": "Short and fast. Hits quicker than most weapons.",            "boosts": {"damage": 3},  "weight": 13},
    {"name": "Chainmail Vest",     "desc": "A sturdy vest of chain links.",                              "boosts": {"defense": 4}, "weight": 10},
    {"name": "Lucky Ring",         "desc": "Makes you more likely to dodge!",                            "boosts": {"dodge": 5}, "weight": 10},
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

# Wishing well buffs and nerfs
blessings = [
    {"name": "Blessing of Vitality", "desc": "Greatly increases your max health.", "boosts": {"health": 50}},
    {"name": "Blessing of Power", "desc": "Greatly increases your damage.", "boosts": {"damage": 20}},
    {"name": "Blessing of Fortitude", "desc": "Greatly increases your defense.", "boosts": {"defense": 20}},
    {"name": "Powerful Blessing of Vitality", "desc": "Massively boosts your max health.", "boosts": {"health": 500}},
    {"name": "Powerful Blessing of Power", "desc": "Massively boosts your damage.", "boosts": {"damage": 200}},
    {"name": "Powerful Blessing of Fortitude", "desc": "Massively boosts your defense.", "boosts": {"defense": 200}},
    {"name": "Divine Spark", "desc": "Doubles XP gain from next 5 fights.", "boosts": {"divineSpark": 5}},
    {"name": "Gift of Giants", "desc": "Grants incredible health.", "boosts": {"health": 200}},
    {"name": "Fury Unleashed", "desc": "Unleashes devastating power.", "boosts": {"damage": 100}},
    {"name": "Iron Will", "desc": "Bolsters your defenses.", "boosts": {"defense": 80}},
    {"name": "Echo of Titans", "desc": "A resounding health surge.", "boosts": {"health": 300}},
    {"name": "Blazing Strength", "desc": "Overwhelming might fills you.", "boosts": {"damage": 250}},
    {"name": "Wall of Ages", "desc": "Your armor thickens with time.", "boosts": {"defense": 200}},
    {"name": "Vital Infusion", "desc": "Legendary health enhancement.", "boosts": {"health": 1000}},
    {"name": "Warrior’s Flame", "desc": "Burns with immense power.", "boosts": {"damage": 400}},
    {"name": "Unbreakable Shell", "desc": "Impenetrable defenses.", "boosts": {"defense": 350}},
    {"name": "Starlight Boon", "desc": "Double XP for 10 fights.", "boosts": {"divineSpark": 10}},
    {"name": "Overflowing Vitality", "desc": "Surging health boost.", "boosts": {"health": 2000}},
    {"name": "Executioner’s Edge", "desc": "Lethal combat precision.", "boosts": {"damage": 600}},
    {"name": "Impenetrable Core", "desc": "Fortress-like endurance.", "boosts": {"defense": 500}},
    {"name": "Fortune’s Favor", "desc": "Boosts drop rate.", "boosts": {"drop": 5}},
    {"name": "Dodge Mastery", "desc": "Increased dodge capability.", "boosts": {"dodge": 10}},
    {"name": "Escape Artist", "desc": "Enhanced retreat chance.", "boosts": {"escape": 15}},
    {"name": "XP Infusion", "desc": "Gain a large XP boost.", "boosts": {"xp": 1000}},
    {"name": "Coin Cascade", "desc": "Gain a surge of wealth.", "boosts": {"coins": 5000}},
    {"name": "Jackpot", "desc": "An immense wealth blessing.", "boosts": {"coins": 50000}},
    {"name": "Hyper Health", "desc": "Extreme vitality granted.", "boosts": {"health": 5000}},
    {"name": "Overclocked Power", "desc": "Inhuman strength surge.", "boosts": {"damage": 1000}},
    {"name": "Ancient Plate", "desc": "Timeless defense boost.", "boosts": {"defense": 1000}},
    {"name": "Sacred Surge", "desc": "Holy boost to health and defense.", "boosts": {"health": 1500, "defense": 300}},
    {"name": "Storm Rage", "desc": "Storm-born speed and power.", "boosts": {"damage": 1200, "dodge": 10}},
    {"name": "Radiant Core", "desc": "Heals you to full.", "boosts": {"heal": "full"}},
    {"name": "Essence of Time", "desc": "XP gain doubled forever.", "boosts": {"divineSpark": 99999}},
    {"name": "Bloodlust", "desc": "Massive damage at health cost.", "boosts": {"damage": 1500, "health": -500}},
    {"name": "Armor of Fate", "desc": "Boosts defense and health.", "boosts": {"defense": 1500, "health": 1000}},
    {"name": "Wish of Kings", "desc": "XP and coin surge.", "boosts": {"xp": 500, "coins": 5000}},
    {"name": "Ultimate Form", "desc": "Ascend to greatness.", "boosts": {"health": 20000, "damage": 20000, "defense": 2000}}
]
curses = [
    {"name": "Curse of Weakness", "desc": "Your strength fades.", "boosts": {"damage": -10}},
    {"name": "Curse of Fragility", "desc": "You feel frail.", "boosts": {"health": -30}},
    {"name": "Curse of Vulnerability", "desc": "Your armor fails you.", "boosts": {"defense": -10}},
    {"name": "Hex of Misfortune", "desc": "You lose your edge in luck.", "boosts": {"drop": -5}},
    {"name": "Curse of Confusion", "desc": "Your mind blurs, XP drops.", "boosts": {"xp": -250}},
    {"name": "Curse of Loss", "desc": "Half your coins vanish.", "boosts": {"coins": -50}},
    {"name": "Crippling Wound", "desc": "You bleed long after the blow.", "boosts": {"health": -200}},
    {"name": "Crack in Armor", "desc": "Your defenses fall apart.", "boosts": {"defense": -100}},
    {"name": "Broken Blade", "desc": "Your weapon weakens.", "boosts": {"damage": -150}},
    {"name": "Hex of Exhaustion", "desc": "You feel weary. XP halved.", "boosts": {"divineSpark": -3}},
    {"name": "Weakening Fog", "desc": "Your body fades.", "boosts": {"health": -10, "defense": -10}},
    {"name": "Sluggish Blood", "desc": "Your lifeforce drains.", "boosts": {"healh": -1000}},
    {"name": "Shattered Luck", "desc": "Fortune slips away.", "boosts": {"drop": -10}},
    {"name": "Doom’s Brand", "desc": "All gains halved temporarily.", "boosts": {"divineSpark": -5}}
]

# Functions

# Helper Functions
# Define the current os and clear screen properly
def clear_screen():
    print(Style.RESET_ALL)
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

# Stats Functions
def show_stats_screen(): # Shows a bunch of player stats for the dead file and living ones if you want
    pass

def get_item_coin_value(): # Gets the coin value of an item
    pass

def show_inventory(): # Shows the players inventory
    pass

def show_combat_stats(): # this is the main function to show all the stats during combat, it runs after each turn (or when coming back to combat after playing a minigame or something else) to refresh the page and show what the current stats of all enemies and players are. 
    pass

# Minigame/Other Functions
def reborn(): # A simple rebirth, resets the floor to default but keep boosts to get even stronger
    pass

# Section for managing the wishing well
def wishing_well(): 
    pass

# Section for managing the fishing minigame
def fishing():
    pass

# Section for managing the gambling minigame
def gamble_stat_change(): # Returns how much the stats change when doing a high risk gamble
    pass
def gamble_change(): # Returns how much coinage you get while doing a normal gamble
    pass
def convert_coins_xp(): # Converts coins to xp
    pass
def gambling(): # Manges the gambling screen
    pass

# Section for managing tamagatchi stuff
def update_tamagatchi(): # Mangages the tamagatchi bonuses, hunger and bond
    pass
def start_tamagatchi_thread(): # Starts the thread for the tamagatchi loop
    pass
def tamagatchi(): # The tamagatchi minigame management code (feeding and such)
    pass

# The screen for selecting minigames
def minigame_selection():
    pass

# Saving and Loading Functions
def save_to_file():
    pass
def list_saved_files():
    pass
def load_from_file():
    pass

# Other Main Functions
def try_drop_item(): # This runs when attacking or fishing to try to drop an item and to know weather to sell it or not
    pass

def apply_boosts(): # Applies external boosts from items, wishes, lvl ups/shops and gambling
    pass

def reset_monster(): # Used with manage_floor to reset the monster to the next one after it is killed
    pass

def manage_foors(): # Assigns monsters to each floor, ecah floor has 10 rooms which can spawn 3 monsters from the list, shifting once to the right every floor. The 10 rooms can be tried as many times as you want until you kill the boss, an optional super strong monster at the end of each floor. (This will just be the monster after the 3rd or strongest enemy in the floor). After killing the boss (only accessable after clearing 10 rooms) you can type next to go to the next floor at any time or stay on the floor and grind. This funciton also manages the weights of the mosnters so the first in the 3 that cna spawn is the most common with the third being the least common
    pass

def level_up(): # Manages the level up screen or shop where you can buy boosts
    pass


# Main Functions
def combat():
    
    while True:
        pass
    
def startup(): # funciton that runs on start up, allows loading a file or creating a new one, choosing difficulty, then starts combat.
    pass
