import random
import time
from colorama import Fore, Back, Style
import os
import sys
import platform
import json
from datetime import datetime
import threading
import pygame
import random
import time
from colorama import Fore, Back, Style
import os
import sys
import platform
import json
from datetime import datetime
import threading
import pygame

# Define libraries and classes
class monsterVariables:
    names =     ["Slime","Goblin","Skeleton","Zombie","Vampire","Orc","Giant","Ent","Warg","Banshee","Ghoul","Bandit","Troll","Shade","Basilisk","Minotaur","Witch","Drake","Warlock","Knight","Behemoth","Chimera","Specter","Ogre","Harpy","Revenant","Lich","Manticore","Wyvern","Wyrm","Juggernaut","Hydra","Phantom","Colossus","Ifrit","Kraken","Dreadnought","Leviathan","Titan","Demon Lord"]
    maxHealth = [10,      15,      22,        33,      50,       75,   113,    170,  256,   284,      576,    864,     1297,   1946,   2919,      4378,      6568,   9852,   14778,    22168,   33252,     49878,    74818,    112227,168341, 252511,    378767,568151,     852226,  1278340,1917510,    2876265,4314398,  6471598,   9707397,14561096,21841644,     32762466,   49143699,73715548,]
    maxDamage = [4,        7,      10,       15,      23,       34,    51,     77,  115,   173,      259,    389,      584,    876,   1314,      1971,      2956,   4434,    6651,     9976,   14964,     22445,    33668,     50502, 75754, 113630,    170445,255668,     383502,  575253,  862880,    1294320,1941479,  2912219,   4368329, 6552493,9828740,      14743110,   22114665,33171997,]
    minDamage = [2,        2,       3,         5,       8,       11,    17,     26,   38,    58,       86,    130,      195,    292,    438,       657,       985,   1478,    2217,     3325,    4988,      7482,    11223,     16834, 25251,  37877,     56815, 85223,     127834,  191751,  287627,     431440, 647160,   970740,   1456110, 2184164,3276247,       4914370,    7371555,11057332,]
    defense =   [0,        1,       1,         1,       2,        3,     4,      6,   10,    14,       22,     32,       49,     73,    109,       164,       246,    369,     554,      831,    1247,      1870,     2806,      4209,  6313,   9469,     14204, 21306,      31959,   47938,   71907,     107860, 161790,   242685,    364027,  546041,819062,        1228592,    1842889,2764333,]

# Classes for ease
monster = monsterVariables()

# The Player Library
player = {
    "name": "placeHolderName",
    "maxHealth": 25.0,
    "health": 25.0,
    "damage": 3.5,
    "defense": 0.0,
    "dodge": 5.0,
    "escape": 20.0,
    "drop": 7.0,
    "difficulty": 0,
    "actionList": ["Attack", "Retreat", "Level", "Inventory", "Minigames/Other", "Stats", "Exit"],
    "buyList": ["Health", "Damage", "Defense", "Dodge", "Retreat", "Drop"],
    "gameList": ["Tamagachi", "Gambling", "Fishing", "Wishing Well", "Reborn"],
    "xp": 0.0,
    "coins": 0,
    "inventory": [],
    "healthBoost": 0,
    "damageBoost": 0,
    "defenseBoost": 0,
    "dodgeBoost": 0,
    "escapeBoost": 0,
    "dropBoost": 0,
}

# Endless mode
endlessMode = False
endlessKills = 0
demon_lord_data = {
    "demonLordsDefeated": 0,
    
    "health": monster.maxHealth[-1],
    "minDamage": monster.minDamage[-1],
    "maxDamage": monster.maxDamage[-1],
    "defense": monster.defense[-1]
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
    "baseHealthBoostCostFactor": 1.35,
    "baseDamageBoostCostFactor": 1.25,
    "baseDefenseBoostCostFactor": 1.4,
    "baseDodgeBoostCostFactor": 1.7,
    "baseEscapeBoostCostFactor": 1.1,
    "baseDropBoostCostFactor": 1.4,
    
    # How much each boost gives you each time (This number is multiplied with the stat for exponential increases)
    "healthBoostMod": 1.05,
    "damageBoostMod": 1.13,
    "defenseBoostMod": 1.12,
    "dodgeBoostMod": 1.13,
    "escapeBoostMod": 1.5,
    "dropBoostMod": 1.3,
    
    "healthBoostCap": 10000000000,
    "damageBoostCap": 10000000000,
    "defenseBoostCap": 10000000000,
    "dodgeBoostCap": 55,
    "escapeBoostCap": 95,
    "dropBoostCap": 25,
}

# Other Stats to keep track of
persistentStats = {
    "floor": 0,
    "room": 0,
    "bossFightReady": False,
    "monstersKilled": 0,
    "rebornsUsed": 0,
    "is_dead": False,
}

# Global Variables

# Monster Variables
monsterId = 0
currentMonsterFight = monster.names[monsterId] 
currentMonsterHealth = monster.maxHealth[monsterId]
currentMonsterDefense = monster.defense[monsterId]

# Save and load variables
currentSaveName = ''
savedGames = []
globalSavePath = ''
saveDirectory = "saves"
os.makedirs(saveDirectory, exist_ok=True)

# Thread management flags
fishing_thread = None
fishing_stop_event = threading.Event()
tamagatchi_thread = None
tamagatchi_stop_event = threading.Event()

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
    {"name": "Sluggish Blood", "desc": "Your lifeforce drains.", "boosts": {"health": -1000}},
    {"name": "Shattered Luck", "desc": "Fortune slips away.", "boosts": {"drop": -10}},
    {"name": "Doom’s Brand", "desc": "All gains halved temporarily.", "boosts": {"divineSpark": -5}}
]

# Functions

# Helper Functions
def timed_input(timeout=1.0):
    result = []
    def read_input():
        try:
            result.append(input())
        except EOFError:
            pass

    input_thread = threading.Thread(target=read_input)
    input_thread.daemon = True
    input_thread.start()
    input_thread.join(timeout)

    if input_thread.is_alive():
        return None  # Timeout
    return result[0] if result else ''

# Define the current os and clear screen properly
def clear_screen():
    print(Style.RESET_ALL)
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

# Stats Functions
def show_stats_screen():
    clear_screen()
    print(Style.RESET_ALL)

    if os.path.exists(globalSavePath):
        with open(globalSavePath, "r") as f:
            data = json.load(f)
    else:
        data = {}

    player_data = data.get("player", player)
    stats = data.get("persistentStats", persistentStats)
    tama = data.get("tamagatchi_data", tamagatchi_data)
    well = data.get("well_data", well_data)

    print(Fore.RED + ("===== PLAYER IS DECEASED =====\n" if stats.get("is_dead", False) else "===== PLAYER STATISTICS =====\n"))

    print(Fore.YELLOW + f"Name: {player_data.get('name', 'Unknown')}")
    print(Fore.CYAN + f"Current Floor: {stats.get('floor', 0)}.{stats.get('room', 0)}")
    print(f"XP: {round(player_data.get('xp', 0), 1)}  |  Coins: {round(player_data.get('coins', 0), 1)}")
    print(f"Max Health: {round(player_data.get('maxHealth', 0), 1)}  |  Damage: {round(player_data.get('damage', 0), 1)}  |  Defense: {round(player_data.get('defense', 0), 1)}")
    print(f"Dodge Chance: {round(player_data.get('dodge', 0), 1)}%  |  Retreat Chance: {round(player_data.get('escape', 0), 1)}%  |  Drop Chance: {round(player_data.get('drop', 0), 1)}%")
    print(f"Reborns Used: {stats.get('rebornsUsed', 0)}")

    print(Fore.MAGENTA + "\n--- Combat Stats ---")
    print(f"Monsters Killed: {stats.get('monstersKilled', 0)}")
    print(f"Demon Lords Defeated: {demon_lord_data.get('demonLordsDefeated', 0)}")

    print(Fore.MAGENTA + "\n--- Gambling Stats ---")
    print(f"Gambles: {gambling_data.get('gamblingBets', 0)}")
    print(f"Coins Gambled: {gambling_data.get('gamblingCoinsSpent', 0)} | Coins Won: {gambling_data.get('gamblingCoinsWon', 0)}")
    print(f"Items Sold: {gambling_data.get('itemsSold', 0)} | Coins from Selling: {gambling_data.get('coinsFromSelling', 0)}")
    print(f"Coins Converted to XP: {gambling_data.get('coinsConvertedToXP', 0)}")

    print(Fore.CYAN + "\n--- Fishing ---")
    print(f"Fish Caught: {fishing_data.get('fishCaught', 0)} | Items Fished: {fishing_data.get('itemsFished', 0)}")

    print(Fore.CYAN + "\n--- Wishing Well ---")
    print(f"Wishes Made: {well.get('wishingCoinsUsed', 0)}")
    print(f"Blessings Received: {well.get('blessingsReceived', 0)}")
    print(f"Curses Received: {well.get('cursesReceived', 0)}")
    print(f"Divine Spark Charges: {well.get('divineSpark', 0)}")

    print(Fore.GREEN + "\n--- Inventory ---")
    inventory = player_data.get("inventory", [])
    if inventory:
        for item in inventory:
            print(f"- {item['name']} | {item['boosts']}")
    else:
        print("(Empty)")

    print(Fore.CYAN + "\n--- Tamagatchi ---")
    print(f"Active: {tama.get('active', False)} | Hunger: {tama.get('hunger', 0)} | Bond: {tama.get('bond', 0)}")
    print(f"Boosts: {tama.get('boosts', {})}")

    if persistentStats["is_dead"]:
        print(Fore.RED + "\nThis character is dead. You must create a new one.\n")
        sys.exit()
        
    print(Fore.BLUE + "\n(Press Enter to return to combat...)")
    input(Fore.GREEN + "> ")
    
    combat()
    
def get_item_coin_value(item):
    #Calculate the coin value of an item based on its boosts and rarity.
    #Heuristic:
    #    - Each point of boost contributes 3–6 coins depending on stat type.
    #    - Extremely rare items (lower weight) are worth significantly more.

    if not isinstance(item, dict) or "boosts" not in item:
        return 0

    value = 0
    boosts = item.get("boosts", {})
    weight = item.get("weight", 1)

    # Base value for each stat type
    for stat, amount in boosts.items():
        if stat == "health":
            value += amount * 1.5
        elif stat == "damage":
            value += amount * 15
        elif stat == "defense":
            value += amount * 18.5
        elif stat in ["dodge", "escape", "drop"]:
            value += amount * 25  # utility stats are rarer
        elif stat == "xp":
            value += amount * 13.5
        elif stat == "coins":
            value += amount
        elif stat == "divineSpark":
            value += amount * 30
        elif stat == "heal" and amount == "full":
            value += 500

    # Rarity multiplier (inverse of weight; capped to avoid extreme inflation)
    rarity_bonus = min(50, round(25 / weight)) if weight > 0 else 100
    value = round(value * (1 + rarity_bonus / 100))

    return max(1, int(value))  # Ensure at least 1 coin

def show_inventory(): # Shows the inventory
    clear_screen()
    print(Fore.BLACK + "|")
    print(Fore.BLUE + "Inventory Overview")
    print(Fore.BLACK + "|")

    # Grab current inventory
    inventory = player.get("inventory", [])

    # If empty, show guidance
    if not inventory:
        print(Fore.RED + "Your inventory is currently empty.")
        print(Fore.YELLOW + "Defeat monsters to earn rare artifacts.")
        print(Fore.YELLOW + "Artifacts grant permanent stat boosts.")
    else:
        # Loop through and display all owned items
        for i, item in enumerate(inventory, 1):
            name = item.get("name", "Unknown")
            desc = item.get("desc", "No description provided.")
            boosts = item.get("boosts", {})

            # Show item number, name, description, and stat boosts
            print(Fore.CYAN + f"[{i}] {name}")
            print(Fore.YELLOW + f"  {desc}")
            print(Fore.MAGENTA + f"  Boosts: {boosts}")
            print(Fore.BLACK + "|")

    # Exit back to combat
    print(Fore.BLACK + "|")
    print(Fore.BLUE + "Press Enter to return to combat.")
    input(Fore.GREEN + "> ")
    combat()

def show_combat_stats(): # this is the main function to show all the stats during combat, it runs after each turn (or when coming back to combat after playing a minigame or something else) to refresh the page and show what the current stats of all enemies and players are. 
    global currentMonsterFight, currentMonsterHealth, monsterId, player, monster, persistentStats
    clear_screen()
    print(Fore.BLACK+"|")
    monsterHealthPercentage = round((currentMonsterHealth / monster.maxHealth[monsterId]) * 100,2)
    print(Fore.WHITE +"You are currently fighting a",currentMonsterFight,"  (Floor:"+str(persistentStats["floor"])+"."+str(persistentStats["room"])+")")
    print(Fore.BLACK +"|")
    print(Fore.RED+currentMonsterFight,"Health:")
    print(Fore.BLACK + "|", end='')
    # Cap health bar
    bar_length = min(round(monsterHealthPercentage / 2), 1000)
    print(Fore.RED + '=' * bar_length, end='')
    if monsterHealthPercentage > 2000:
        print(Fore.RED + " (HP: " + str(int(currentMonsterHealth)) + ")")
    else:
        print(Fore.RED + f" {monsterHealthPercentage}%")
    print(Fore.BLACK +"|")
    print(Fore.BLACK +"|")
    currentHealthPercentage = round((player["health"] / player["maxHealth"]) * 100,2)
    print(Fore.GREEN+"Player Stats:")
    print(Fore.GREEN+" Health: ",end='')
    for i in range(round(currentHealthPercentage/2.4)): print(Fore.GREEN +'=',end='')
    print("",str(currentHealthPercentage)+"%  ("+str(round(player["health"],1))+")")
    print(Fore.GREEN +" Damage:",round(player["damage"],1), " |  Defense:",round(player["defense"],1)," |  Xp:",round(player["xp"],1))
    print(Fore.GREEN +" Dodge Chance:",str(round(player["dodge"],1))+"% |  Retreat Chance:",str(round(player["escape"],1))+"%"," |  Item Drop Chance:",str(round(player["drop"],1))+"%")
    print(Fore.BLACK +"|")
    if tamagatchi_data["active"]:
        print(Fore.CYAN + f"Tamagatchi → Bond: {tamagatchi_data['bond']} | Hunger: {tamagatchi_data['hunger']} | Boosts: {tamagatchi_data['boosts']}")
        print(Fore.BLACK +"|")
    print(Fore.BLACK +"|")
    print(Fore.BLUE +"Actions:",player["actionList"])
    print(Style.RESET_ALL)

# Minigame/Other Functions
def reborn():
    global player, shop_data, well_data, persistentStats

    clear_screen()

    if persistentStats["floor"] < 100:
        print(Fore.RED + "You must reach floor 100 to use Reborn.")
        time.sleep(2)
        combat()
        return

    print(Fore.YELLOW + "--- Reborn ---")
    print(Fore.CYAN + "Reset to Floor 0 while keeping all stat boosts and inventory.")
    print(Fore.CYAN + "Shop prices reset, Tamagatchi improves, and well cost resets.")
    print(Fore.CYAN + "Cost: 1000 XP  →  Reward: 100,000 coins")
    print(Fore.YELLOW + "\nReborn? (yes/no)")

    choice = input(Fore.GREEN + "> ").strip().lower()
    if choice in ["yes", "y"]:
        if player["xp"] < 1000:
            print(Fore.RED + "You don't have enough XP.")
            time.sleep(2)
            combat()
            return

        player["xp"] -= 1000
        player["coins"] += 100000
        well_data["wishing_well_cost"] = 1000
        persistentStats["floor"] = 0
        persistentStats["room"] = 0
        persistentStats["rebornsUsed"] += 1

        # Reset shop costs to base values
        shop_data["baseHealthBoostCost"] = 2
        shop_data["baseDamageBoostCost"] = 3
        shop_data["baseDefenseBoostCost"] = 4
        shop_data["baseDodgeBoostCost"] = 5
        shop_data["baseEscapeBoostCost"] = 2
        shop_data["baseDropBoostCost"] = 10

        print(Fore.GREEN + "You have been reborn. The climb begins anew...")
        time.sleep(3)

        reset_monster()
        combat()
    else:
        print(Fore.YELLOW + "Rebirth canceled.")
        time.sleep(1.5)
        combat()

# Section for managing the wishing well
def wishing_well():
    global player, well_data

    clear_screen()
    if persistentStats["monstersKilled"] < 1000:
        print(Fore.RED + "You must defeat 1000 monsters to unlock the Wishing Well.")
        time.sleep(2)
        combat()
        return

    cost = well_data["wishing_well_cost"]
    print(Fore.CYAN + "--- The Wishing Well ---")
    print(Fore.YELLOW + f"Cost to Wish: {cost} coins")
    print(f"You have: {player['coins']} coins")
    print(Fore.MAGENTA + "Make a wish? (yes / no)")

    choice = input(Fore.GREEN + "> ").strip().lower()
    if choice not in ["yes", "y"]:
        combat()
        return

    if player["coins"] < cost:
        print(Fore.RED + "Not enough coins!")
        time.sleep(2)
        combat()
        return

    player["coins"] -= cost
    well_data["wishing_well_cost"] = int(cost * 1.25)
    well_data["wishingCoinsUsed"] += 1

    roll = random.randint(1, 100)
    result_type = "blessing" if roll <= 60 else "curse" if roll <= 95 else "spark"

    if result_type == "spark":
        print(Fore.CYAN + "A Divine Spark ignites within you. +1 charge!")
        well_data["divineSpark"] += 1
        time.sleep(2)
        combat()
        return

    elif result_type == "blessing":
        blessing = random.choice(blessings)
        if blessing["name"] in well_data["obtainedBlessings"]:
            print(Fore.YELLOW + f"You already received {blessing['name']}. Refund: {cost // 2} coins.")
            player["coins"] += cost // 2
        else:
            apply_boost(blessing["boosts"])
            well_data["obtainedBlessings"].append(blessing["name"])
            well_data["blessingsReceived"] += 1
            print(Fore.GREEN + f"Blessing: {blessing['name']} → {blessing['desc']}")

    else:  # curse
        curse = random.choice(curses)
        if curse["name"] in well_data["obtainedCurses"]:
            print(Fore.YELLOW + f"You already endured {curse['name']}. Refund: {cost // 2} coins.")
            player["coins"] += cost // 2
        else:
            apply_boost(curse["boosts"])
            well_data["obtainedCurses"].append(curse["name"])
            well_data["cursesReceived"] += 1
            print(Fore.RED + f"Curse: {curse['name']} → {curse['desc']}")

    apply_boosts()
    time.sleep(3)
    combat()

def apply_boost(boost_dict): # This is for the well specifically, not to be confused with the apply boost(s) function down below
    for key, value in boost_dict.items():
        if key == "heal" and value == "full":
            player["health"] = player["maxHealth"]
        elif key == "divineSpark":
            well_data["divineSpark"] += value
        elif key == "xp":
            player["xp"] += value
        elif key == "coins":
            player["coins"] += value
        elif key in player:
            player[key] += value

# Section for managing the fishing minigame
def fishing():
    global fishing_active, fishing_thread, fishing_stop_event
    fishing_active = True
    clear_screen()
    print(Style.RESET_ALL)
    print(Fore.CYAN + "You sit quietly by the water and begin fishing...")
    print(Fore.YELLOW + "When a fish bites, press Enter 2-3 times quickly to catch it!")
    print(Fore.YELLOW + "Type 'leave' to stop fishing at any time.\n")

    idle_enter_count = 0
    fish_ready = False
    cooldown_until = 0
    fishing_penalty = False
    penalty_end_time = 0

    def fishing_loop():
        nonlocal fish_ready, cooldown_until, fishing_penalty, penalty_end_time
        while fishing_active and not fishing_stop_event.is_set():
            if fishing_penalty or time.time() < cooldown_until:
                time.sleep(0.2)
                continue
            print(Fore.BLUE + "Waiting for a bite...")
            time.sleep(random.uniform(4, 9))
            if not fishing_active or fishing_stop_event.is_set():
                break
            fish_ready = True
            print(Fore.YELLOW + "\nA fish is on the line! Press Enter quickly!")
            
            response = timed_input(timeout=1.0)
            fish_ready = False

            if response is None:
                print(Fore.RED + "Too slow! The fish got away.")
                cooldown_until = time.time() + 3
                continue

            fish_ready = False

            #if reaction_time > 1.0:
            #    print(Fore.RED + "Too slow! The fish got away.")
            #    cooldown_until = time.time() + 3
            #    continue
            if fishing_penalty:
                print(Fore.RED + "Rod tangled from spam. No reward.")
                continue

            if random.random() < 0.8:
                scale = 1 + (persistentStats["floor"] * 2)
                mult = 10 * int(persistentStats["floor"] * 10) if persistentStats["floor"] >= 50 else 1
                xp_gain = round(random.uniform(0.5, 5.0) * scale * mult, 1)
                player["xp"] += xp_gain
                print(Fore.GREEN + f"You caught a fish and earned {xp_gain} XP!")
                fishing_data["fishCaught"] += 1
            else:
                item = random.choices(drop_table, weights=[i["weight"] for i in drop_table], k=1)[0]
                owned_names = [i["name"] for i in player["inventory"]]
                if item["name"] in owned_names:
                    value = get_item_coin_value(item)
                    player["coins"] += value
                    print(Fore.MAGENTA + f"Duplicate item: {item['name']} → sold for {value} coins.")
                    gambling_data["itemsSold"] += 1
                    gambling_data["coinsFromSelling"] += value
                else:
                    player["inventory"].append(item)
                    print(Fore.MAGENTA + f"Fished a rare item: {item['name']}!")
                    print(Fore.YELLOW + item["desc"])
                fishing_data["itemsFished"] += 1
                apply_boosts()
            cooldown_until = time.time() + 1

    if fishing_thread and fishing_thread.is_alive():
        print(Fore.YELLOW + "Fishing is already active.")
    else:
        fishing_stop_event.clear()
        fishing_thread = threading.Thread(target=fishing_loop, daemon=True)
        fishing_thread.start()

    while fishing_active:
        now = time.time()
        if fishing_penalty:
            remaining = int(penalty_end_time - now)
            if remaining <= 0:
                fishing_penalty = False
                print(Fore.GREEN + "Line untangled. You may fish again.")
            else:
                print(Fore.RED + f"Line tangled! Wait {remaining}s.")
            time.sleep(1)
            continue

        cmd = input()
        if cmd.strip().lower() in ["leave", "exit"]:
            fishing_active = False
            fishing_stop_event.set()
            print(Fore.GREEN + "You pack up and return to combat...")
            time.sleep(1)
            break
        if cmd.strip() == "" and not fish_ready:
            idle_enter_count += 1
            if idle_enter_count > 2:
                print(Fore.RED + "Stop yanking! Line tangled.")
                fishing_penalty = True
                penalty_end_time = time.time() + 10
                idle_enter_count = 0
        else:
            idle_enter_count = 0
    combat()

# Section for managing the gambling minigame
def gamble_stat_change(amount): # Returns how much the stats change when doing a high risk gamble
    roll = random.randint(1, 100)
    if roll <= 10:
        return -amount
    elif roll <= 30:
        return -int(amount * 0.5)
    elif roll <= 50:
        return int(amount * 0.2)
    elif roll <= 75:
        return int(amount * 0.5)
    elif roll <= 90:
        return amount
    else:
        return amount * 2

def gambling(): # Manages the gambling screen
    global player
    clear_screen()
    print(Style.RESET_ALL)
    print(Fore.YELLOW + "Welcome to the Gambling Den")
    print(Fore.CYAN + f"You have {player['coins']} coins.")
    print(Fore.BLACK,"|")

    if player["coins"] == 0 and not player["inventory"]:
        print(Fore.RED + "\nYou have no coins or items to interact with.")
        print(Fore.YELLOW + "Defeat monsters to gain items. Sell them for coins to gamble!")
        time.sleep(3)
        combat()
        return

    print(Fore.GREEN + "\nOptions:")
    print(Fore.GREEN + " [sell]    → Sell inventory items for coins")
    print(Fore.GREEN + " [gamble]  → Bet a custom amount of coins")
    print(Fore.GREEN + " [convert] → Convert 10 coins into 1 XP")
    if persistentStats["floor"] >= 50:
        print(Fore.GREEN + " [highrisk] → Gamble health, damage, or defense stats")
    else:
        print(Fore.RED + " [highrisk] → Unlocks at Floor 50+")
    print(Fore.GREEN + " [leave]   → Exit back to combat")
    print(Fore.BLACK,"|")

    choice = input(Fore.CYAN + "\nYour choice: ").strip().lower()

    if choice in ["sell"]:
        if not player["inventory"]:
            print(Fore.RED + "You have no items to sell.")
        else:
            for i, item in enumerate(player["inventory"]):
                value = get_item_coin_value(item)
                print(Fore.CYAN + f"[{i}] {item['name']} → {value} coins")
                print(Fore.MAGENTA + f"     {item['desc']}")

            sel = input(Fore.GREEN + "\nChoose item number to sell or 'all': ").strip().lower()
            if sel == "all":
                total = sum(get_item_coin_value(i) for i in player["inventory"])
                player["coins"] += total
                gambling_data["itemsSold"] += len(player["inventory"])
                gambling_data["coinsFromSelling"] += total
                player["inventory"].clear()
                print(Fore.GREEN + f"Sold all items for {total} coins.")
            elif sel.isdigit():
                i = int(sel)
                if 0 <= i < len(player["inventory"]):
                    item = player["inventory"].pop(i)
                    value = get_item_coin_value(item)
                    player["coins"] += value
                    gambling_data["itemsSold"] += 1
                    gambling_data["coinsFromSelling"] += value
                    print(Fore.GREEN + f"Sold {item['name']} for {value} coins.")
                else:
                    print(Fore.RED + "Invalid item index.")
            else:
                print(Fore.RED + "Invalid input.")
        apply_boosts()

    elif choice in ["gamble", "gam"]:
        try:
            amt = int(input(Fore.YELLOW + "Enter coin amount to bet: ").strip())
            if amt <= 0 or amt > player["coins"]:
                print(Fore.RED + "Invalid bet amount.")
            else:
                mults = [0, 0.1, 0.2, 0.5, 1.0, 1.2, 1.5, 2.0, 3.0]
                weights = [10, 20, 10, 5, 6, 10, 50, 5, 2]
                scale = 1 + (persistentStats["floor"] * 0.5)
                mult = random.choices(mults, weights)[0] * scale
                result = int(amt * mult)
                player["coins"] -= amt
                player["coins"] += result + 1
                gambling_data["gamblingBets"] += 1
                gambling_data["gamblingCoinsSpent"] += amt
                gambling_data["gamblingCoinsWon"] += result
                if result == 0:
                    print(Fore.RED + "You lost everything!")
                elif result < amt:
                    print(Fore.YELLOW + f"You lost some. You got {result} coins back.")
                else:
                    print(Fore.GREEN + f"You won! You now have {result} more coins.")
                    player["coins"] += amt
        except:
            print(Fore.RED + "Invalid number.")

    elif choice in ["convert"]:
        try:
            amt = int(input(Fore.YELLOW + "Coins to convert to XP (10 coins = 1 XP): ").strip())
            if amt < 10 or amt > player["coins"]:
                print(Fore.RED + "Invalid amount.")
            else:
                xp = round(amt / 10, 2)
                player["coins"] -= amt
                player["xp"] += xp
                gambling_data["coinsConvertedToXP"] += amt
                print(Fore.GREEN + f"Gained {xp} XP.")
        except:
            print(Fore.RED + "Invalid input.")

    elif choice in ["highrisk", "high", "risk"]:
        if persistentStats["floor"] < 50:
            print(Fore.RED + "High Risk unlocked at Floor 50")
        else:
            stat = input(Fore.YELLOW + "Which stat? [health/damage/defense]: ").strip().lower()
            if stat in ["health", "damage", "defense"]:
                try:
                    amt = int(input(Fore.CYAN + f"Points of {stat} to gamble: ").strip())
                    key = f"{stat}Boost"
                    if amt <= 0 or amt > player[key]:
                        print(Fore.RED + "Invalid amount.")
                    else:
                        change = gamble_stat_change(amt)
                        player[key] = max(0, player[key] + change)
                        print(Fore.MAGENTA + f"{stat.capitalize()} changed by {change}.")
                        apply_boosts()
                except:
                    print(Fore.RED + "Invalid number.")
            else:
                print(Fore.RED + "Invalid stat.")

    elif choice in ["leave", "exit"]:
        combat()
        return

    else:
        print(Fore.RED + "Invalid input.")

    time.sleep(2)
    gambling()

# Tamagachi stuff
def start_tamagatchi_thread():
    global tamagatchi_thread
    if tamagatchi_thread and tamagatchi_thread.is_alive():
        return
    tamagatchi_stop_event.clear()
    def loop():
        while tamagatchi_data["active"] and not tamagatchi_stop_event.is_set():
            if tamagatchi_data["last_update"] is not None:
                update_tamagatchi()
            time.sleep(random.uniform(30, 200)) # How long it takes for the tamagatchi to update
    tamagatchi_thread = threading.Thread(target=loop, daemon=True)
    tamagatchi_thread.start()

def update_tamagatchi():
    hunger = tamagatchi_data["hunger"]
    bond = tamagatchi_data["bond"]
    kills = persistentStats.get("monstersKilled", 0)

    # Hunger increases
    if hunger < 100:
        tamagatchi_data["hunger"] += 1

    # Bond slowly increases if well-fed (under 20 hunger)
    if hunger < 20 and random.random() < 0.5: # 50% chance to gain a bond each update if the hunger is low enough
        tamagatchi_data["bond"] += 1

    # Recalculate boosts
    if bond > 0:
        scale = 1
        if persistentStats.get("rebornsUsed", 0) >= 6:
            scale = 3
        elif persistentStats.get("rebornsUsed", 0) >= 1:
            scale = 2

        tamagatchi_data["boosts"]["health"] = int(bond * scale * (1 + (kills/10) * 1))
        tamagatchi_data["boosts"]["damage"] = int(bond * scale * (1 + (kills/10) * 0.3))
        tamagatchi_data["boosts"]["defense"] = int(bond * scale * (1 + (kills/10) * 0.1))
    
    apply_boosts()

def tamagatchi():
    global player, persistentStats
    max_bond = 20 * (persistentStats["rebornsUsed"] + 1)
    clear_screen()
    print(Style.RESET_ALL)

    if not tamagatchi_data["active"]:
        if player["xp"] < 100:
            print(Fore.RED + "You need 100 XP to adopt a Tamagatchi.")
            time.sleep(3)
            combat()
            return
        player["xp"] -= 100
        tamagatchi_data.update({
            "active": True,
            "last_update": datetime.now().isoformat(),
            "hunger": 3,
            "bond": 5
        })
        start_tamagatchi_thread()
        print(Fore.YELLOW + "You adopted a glowing creature!")
        print(Fore.RED + "Feed it to earn permanent boosts.")
        time.sleep(2)

    while True:
        clear_screen()
        hunger = tamagatchi_data["hunger"]
        bond = tamagatchi_data["bond"]
        boosts = tamagatchi_data["boosts"]
        print(Fore.CYAN + "\n--- Tamagatchi Status ---")
        print(Fore.MAGENTA + f"Hunger: {hunger} / 100")
        print(Fore.MAGENTA + f"Bond: {bond} / {max_bond}")
        print(Fore.GREEN + f"Boosts: {boosts}")
        print(Fore.YELLOW + f"XP: {round(player['xp'], 1)}")
        print(Fore.BLACK+"|")
        print(Fore.YELLOW+"Tamagatchi will be much happier if hunger is kept under 20")
        print(Fore.BLACK+"|")

        if hunger <= 5:
            print(Fore.YELLOW + "It's not hungry enough to feed.")
        else:
            cost = round(hunger * 1.3 * (tamagatchi_data["tamagatchiFeeds"] + 1), 1)
            print(Fore.YELLOW + f"Feeding cost: {round(cost, 1)} XP")

        print(Fore.CYAN + "\nType 'feed' to feed, or 'exit' to return to combat.")
        choice = input().strip().lower()

        if choice in ["exit", "leave"]:
            combat()
            return
        elif choice == "feed":
            if hunger <= 5:
                print(Fore.YELLOW + "It's not hungry enough to feed.")
            elif player["xp"] >= cost: # type: ignore
                tamagatchi_data["hunger"] = max(hunger - 4, 0)
                tamagatchi_data["bond"] = min(bond + 1, max_bond)
                player["xp"] -= cost # type: ignore
                tamagatchi_data["tamagatchiFeeds"] += 1
                print(Fore.GREEN + "You feed your companion! It looks happier.")
            else:
                print(Fore.RED + "Not enough XP.")
        else:
            print(Fore.RED + "Invalid command.")
        apply_boosts()
        time.sleep(1.5)

# The screen for selecting minigames
def minigame_selection():
    clear_screen()
    print(Fore.BLACK + "|")
    print(Fore.YELLOW + "Welcome to the Minigame/Other section!")
    print(Fore.BLUE + "  Complete minigames to earn boosts, XP, and more!")
    print(Fore.BLACK + "|")
    print(Fore.YELLOW + "Tamagatchi     → Feed a friend for passive stat boosts.")
    print(Fore.YELLOW + "Gambling       → Risk coins/items to multiply rewards.")
    print(Fore.YELLOW + "Fishing        → Relax and earn items or XP.")
    print(Fore.YELLOW + "Wishing Well   → Spend coins for powerful blessings—or curses.")
    print(Fore.YELLOW + "Reborn         → Reset with your stats intact after high progress.")
    print(Fore.BLACK + "|")
    print(Fore.BLUE + "Options:", player["gameList"])
    print(Fore.BLACK + "|")
    print(Style.RESET_ALL)

    choice = input(Fore.GREEN + "> ").strip().lower()

    if choice in ["tamagatchi", "tama"]:
        tamagatchi()
    elif choice in ["gambling", "gamble", "gamb"]:
        gambling()
    elif choice in ["fishing", "fish"]:
        fishing()
    elif choice in ["wishing well", "wish", "wishingwell", "wsh"]:
        wishing_well()
    elif choice in ["reborn", "re", "born"]:
        reborn()
    elif choice == "exit":
        combat()
    else:
        print(Fore.RED + "Invalid input. Try again.")
        time.sleep(1)
        minigame_selection()

# Saving and Loading Functions
def save_to_file(): # Saves the file
    global globalSavePath, player, persistentStats, tamagatchi_data, well_data
    player["name"] = os.path.splitext(currentSaveName)[0]

    data = {
        "player": player,
        "persistentStats": persistentStats,
        "tamagatchi_data": tamagatchi_data,
        "well_data": well_data,
        "shop_data": shop_data,
        "fishing_data": fishing_data,
        "gambling_data": gambling_data,
        "endlessMode": endlessMode,
        "endlessKills": endlessKills,
        "monsterId": monsterId,
        "currentMonsterHealth": currentMonsterHealth
    }

    with open(globalSavePath, "w") as f:
        json.dump(data, f, indent=4)
    
def list_saved_files(): # lists saved files
    files = os.listdir(saveDirectory)
    json_files = [f for f in files if f.endswith('.json')]
    active = []
    dead = []

    for file in json_files:
        try:
            with open(os.path.join(saveDirectory, file), 'r') as f:
                data = json.load(f)
                if data.get("persistentStats", {}).get("is_dead", False):
                    dead.append(file)
                else:
                    active.append(file)
        except Exception:
            continue

    print(Fore.CYAN + "Active Save Files:")
    for f in active:
        print("  " + f)
    print(Fore.RED + "\nDead Save Files:")
    for f in dead:
        print("  " + f)
    print(Style.RESET_ALL)

def load_from_file(filename): # Load data from files
    global globalSavePath, player, persistentStats, tamagatchi_data, well_data
    global endlessMode, endlessKills, monsterId, currentMonsterFight, currentMonsterHealth, currentMonsterDefense

    path = os.path.join(saveDirectory, filename)
    globalSavePath = path

    try:
        with open(path, "r") as f:
            data = json.load(f)
        
        player.update(data.get("player", {}))
        persistentStats.update(data.get("persistentStats", {}))
        tamagatchi_data.update(data.get("tamagatchi_data", {}))
        shop_data.update(data.get("shop_data", {}))
        well_data.update(data.get("well_data", {}))
        fishing_data.update(data.get("fishing_data", {}))
        gambling_data.update(data.get("gambling_data", {}))
        endlessMode = data.get("endlessMode", False)
        endlessKills = data.get("endlessKills", 0)
        monsterId = data.get("monsterId", 0)
        currentMonsterFight = monster.names[monsterId]
        currentMonsterHealth = data.get("currentMonsterHealth", monster.maxHealth[monsterId])
        currentMonsterDefense = monster.defense[monsterId]

        # Stats the tamagatchi thread
        if tamagatchi_data.get("active"):
            start_tamagatchi_thread()

        print(Fore.GREEN + f"Loaded from {filename}")
        return True
    except Exception as e:
        print(Fore.RED + f"Failed to load save: {e}")
        return False

# Other Main Functions
def try_drop_item():
    #Attempts to drop an item after combat or fishing, based on player's drop chance.
    #If an item is already in inventory, it is auto-sold for coins instead.
    #Applies item boosts immediately if obtained.
    
    drop_chance = player["drop"]
    if random.uniform(0, 100) <= drop_chance:
        # Get weights and choose one item
        weights = [item.get("weight", 1) for item in drop_table]
        dropped_item = random.choices(drop_table, weights=weights, k=1)[0]

        owned_names = [i["name"] for i in player["inventory"]]
        if dropped_item["name"] in owned_names:
            # Duplicate item → convert to coins
            value = get_item_coin_value(dropped_item)
            player["coins"] += value
            print(Fore.MAGENTA + f"You found {dropped_item['name']} again.")
            print(Fore.YELLOW + f"It was converted into {value} coins.")
        else:
            # New item → add to inventory
            player["inventory"].append(dropped_item)
            print(Fore.MAGENTA + f"You found: {dropped_item['name']}!")
            print(Fore.YELLOW + dropped_item["desc"])

        apply_boosts()
        time.sleep(0.5)


def apply_boosts():
    #Recalculate and apply all stat boosts from level-ups, items, tamagatchi, and blessings.
    #This function resets stats to base values and then adds all applicable bonuses.

    # Base stats 
    base_health = 25.0
    base_damage = 3.5
    base_defense = 0.0
    base_dodge = 5.0
    base_escape = 20.0
    base_drop = 7.0

    # Reset stats to base + permanent boosts
    player["maxHealth"] = base_health + player["healthBoost"]
    player["damage"] = base_damage + player["damageBoost"]
    player["defense"] = base_defense + player["defenseBoost"]
    player["dodge"] = base_dodge + player["dodgeBoost"]
    player["escape"] = base_escape + player["escapeBoost"]
    player["drop"] = base_drop + player["dropBoost"] 

    # Add item boosts
    for item in player["inventory"]:
        boosts = item.get("boosts", {})
        player["maxHealth"] += boosts.get("health", 0)
        player["damage"] += boosts.get("damage", 0)
        player["defense"] += boosts.get("defense", 0)
        player["dodge"] += boosts.get("dodge", 0)
        player["escape"] += boosts.get("escape", 0)
        player["drop"] += boosts.get("drop", 0)

    # Clamp capped values
    player["drop"] = min(player["drop"], shop_data["dropBoostCap"])
    player["dodge"] = min(player["dodge"], shop_data["dodgeBoostCap"])
    player["escape"] = min(player["escape"], shop_data["escapeBoostCap"])

    # Apply tamagatchi boosts
    if tamagatchi_data.get("active"):
        boosts = tamagatchi_data["boosts"]
        player["maxHealth"] += boosts.get("health", 0)
        player["damage"] += boosts.get("damage", 0)
        player["defense"] += boosts.get("defense", 0)

    # Make sure current health isn't above max
    if player["health"] > player["maxHealth"]:
        player["health"] = player["maxHealth"]


def reset_monster():
    # Resets monster based on current floor + room count, or spawns boss
    global monsterId, player, monster, currentMonsterFight, currentMonsterHealth, currentMonsterDefense, persistentStats

    if persistentStats["bossFightReady"]:
        boss_index = min(monsterId + 1, len(monster.names) - 1)
        monsterId = boss_index
        persistentStats["bossFightReady"] = False

    if endlessMode:
            # Endless mode: demon lord keeps getting stronger
            demon_lord_data["demonLordsDefeated"] += 1
            multiplier = 2 ** demon_lord_data["demonLordsDefeated"]

            demon_lord_data["health"] = monster.maxHealth[-1] * multiplier
            demon_lord_data["minDamage"] = monster.minDamage[-1] * multiplier
            demon_lord_data["maxDamage"] = monster.maxDamage[-1] * multiplier
            demon_lord_data["defense"] = monster.defense[-1] * multiplier

            currentMonsterFight = f"Demon Lord x{demon_lord_data['demonLordsDefeated']}"
            currentMonsterHealth = demon_lord_data["health"]
            currentMonsterDefense = demon_lord_data["defense"]
            return
    else:
        weights = manage_floors()
        tier_indices = [i for i, w in enumerate(weights) if w > 0]

        if persistentStats["bossFightReady"] and persistentStats["room"] == 10:
            print(Fore.RED+"A boss monster approaches... defeat this enemy to move on to the next floor")
            time.sleep(1.5)
            # Boss is the monster immediately to the right of the strongest in the tier
            boss_index = tier_indices[-1] + 1
            if boss_index >= len(monster.names):
                boss_index = tier_indices[-1]  # fallback to last if out of range
            monsterId = boss_index
        else:
            # Random monster from current floor weights
            monsterId = random.choices(range(len(monster.names)), weights=weights, k=1)[0]

        currentMonsterFight = monster.names[monsterId]
        currentMonsterHealth = monster.maxHealth[monsterId]
        currentMonsterDefense = monster.defense[monsterId]

def manage_floors():
    # Calculates spawn weights for current floor based on 3 rotating monsters
    global persistentStats, monster

    total_monsters = len(monster.names)
    tier_size = 3

    # Determine monster tier group for this floor
    floor = persistentStats["floor"]
    tier_start = min(floor % (total_monsters - tier_size + 1), total_monsters - tier_size)
    tier_end = tier_start + tier_size

    # Determine if boss is available
    if persistentStats["room"] >= 10:
        persistentStats["bossFightReady"] = True

    # Weights: [common, uncommon, rare]
    base_weights = [1.0, 0.75, 0.5]
    weights = [base_weights[i - tier_start] if tier_start <= i < tier_end else 0 for i in range(total_monsters)]
    return weights

# The level up screen
def level_up():
    while True:
        clear_screen()
        print(Fore.BLACK + "|")
        print(Fore.GREEN + f"Upgrade Costs (Current XP: {round(player['xp'], 1)})")
        print(Fore.GREEN +
            f" Health: {shop_data['baseHealthBoostCost']} |" +
            f" Damage: {shop_data['baseDamageBoostCost']} |" +
            f" Defense: {shop_data['baseDefenseBoostCost']}\n" +
            f" Dodge: {shop_data['baseDodgeBoostCost']} |" +
            f" Escape: {shop_data['baseEscapeBoostCost']} |" +
            f" Drop: {shop_data['baseDropBoostCost']}")
        print(Fore.BLACK + "|\n" + Fore.BLUE + "Options:", player["buyList"])
        print(Fore.BLUE + "(Type 'exit' to return to combat)")

        choice = input(Fore.GREEN + "> ").strip().lower()

        upgrade_map = {
            "health": ("healthBoost", "baseHealthBoostCost", "baseHealthBoostCostFactor", "healthBoostMod", "healthBoostCap"),
            "damage": ("damageBoost", "baseDamageBoostCost", "baseDamageBoostCostFactor", "damageBoostMod", "damageBoostCap"),
            "defense": ("defenseBoost", "baseDefenseBoostCost", "baseDefenseBoostCostFactor", "defenseBoostMod", "defenseBoostCap"),
            "dodge": ("dodgeBoost", "baseDodgeBoostCost", "baseDodgeBoostCostFactor", "dodgeBoostMod", "dodgeBoostCap"),
            "escape": ("escapeBoost", "baseEscapeBoostCost", "baseEscapeBoostCostFactor", "escapeBoostMod", "escapeBoostCap"),
            "drop": ("dropBoost", "baseDropBoostCost", "baseDropBoostCostFactor", "dropBoostMod", "dropBoostCap"),
        }

        aliases = {
            "hp": "health", "hlth": "health",
            "dmg": "damage",
            "def": "defense",
            "dod": "dodge", "dodge chance": "dodge", "dodgechance": "dodge",
            "ret": "escape", "esc": "escape", "retreat": "escape",
            "drp": "drop", "drop chance": "drop", "dropchance": "drop"
        }

        choice = aliases.get(choice, choice)

        if choice in upgrade_map:
            boost_key, cost_key, factor_key, mod_key, cap_key = upgrade_map[choice]
            current_cost = shop_data[cost_key]
            boost_mod = shop_data[mod_key]
            cap = shop_data[cap_key]

            if player["xp"] < current_cost:
                print(Fore.RED + "Not enough XP!")
            elif player[boost_key] >= cap:
                print(Fore.RED + f"{boost_key.capitalize()} boost is capped at {cap}.")
            else:  # applies stat boosts
                player["xp"] -= current_cost

                if choice == "health":
                    base_health = 25.0

                    if player[boost_key] <= 0:
                        player[boost_key] = 1.0  # Starting point

                    current_boost = player[boost_key]
                    proposed_boost = current_boost * boost_mod

                    # Calculate new maxHealth
                    current_max = player["maxHealth"]
                    proposed_max = base_health + proposed_boost
                    increase = proposed_max - current_max
                    max_increase = current_max * 0.05

                    # Enforce cap
                    if increase > max_increase:
                        proposed_max = current_max + max_increase
                        proposed_boost = proposed_max - base_health

                    player[boost_key] = min(proposed_boost, cap)

                    apply_boosts()
                    heal_amount = player["maxHealth"] * 0.5
                    player["health"] = min(player["health"] + heal_amount, player["maxHealth"])

                else:
                    player[boost_key] += boost_mod
                    player[boost_key] = min(player[boost_key], cap)  # Clamp all boosts

                # Apply scaling multipliers only to linear boosts
                if choice not in ["dodge", "escape", "drop"]:
                    shop_data[mod_key] *= shop_data[factor_key]

                # Always scale price
                shop_data[cost_key] = round(shop_data[cost_key] * shop_data[factor_key], 1)

                apply_boosts()
                print(Fore.YELLOW + f"{boost_key.capitalize()} boosted! New value: {round(player[boost_key], 2)}")

        elif choice == "exit":
            return
        else:
            print(Fore.RED + "Invalid input.")
        time.sleep(1)

def monster_death_check():
    global currentMonsterHealth, monsterId, player, persistentStats, endlessMode, endlessKills
    if currentMonsterHealth <= 0:
    # Activate Endless Mode when Demon Lord dies
        if currentMonsterFight == "Demon Lord" and not endlessMode:
            endlessMode = True
            endlessKills = 0
            print(Fore.RED + "\n--- ENDLESS MODE UNLOCKED ---")
            print(Fore.MAGENTA + "Demon Lords will now respawn stronger each time.")
            time.sleep(5)
            
        if tamagatchi_data.get("active") and tamagatchi_data["hunger"] < 20:
            if random.random() < 0.2:
                tamagatchi_data["bond"] += 1
        print(Fore.GREEN + "You defeated the monster!")
            
        persistentStats["monstersKilled"] += 1
        player["health"] += round(monster.maxHealth[monsterId]/10)

        if persistentStats.get("bossFightReady", False):
            persistentStats["floor"] += 1
            persistentStats["room"] = 0
            persistentStats["bossFightReady"] = False
            print(Fore.GREEN + f"You conquered the boss! Now entering floor {persistentStats['floor']}.")
            time.sleep(0.5)
        else:
            persistentStats["room"] += 1

        # This is what happens when you kill a monster
        xp_gain = round(monster.maxHealth[monsterId] / 12, 1)
        if well_data["divineSpark"] > 0:
            xp_gain *= 2
            well_data["divineSpark"] -= 1
            print(Fore.YELLOW + f"The Divine Spark doubles your XP to {xp_gain}!")

        player["xp"] += xp_gain
        try_drop_item()

        if currentMonsterFight == "Demon Lord":
            endlessKills += 1
            print(Fore.MAGENTA + f"Demon Lord defeated! Total defeated: {endlessKills}")
        elif endlessMode:
            endlessKills += 1

        time.sleep(0.5)
        reset_monster()
        apply_boosts()
    else:
        monster_turn()

def monster_turn():
    global currentMonsterHealth, monsterId, player, persistentStats, endlessMode, endlessKills
    if random.randint(0, 100) < player["dodge"]:
        print(Fore.YELLOW + "You dodged the attack!")
    else:
        print(Fore.YELLOW + f"{currentMonsterFight} attacks!")
        if endlessMode:
            scale = 4 ** endlessKills
            dmg = round(random.uniform(demon_lord_data["minDamage"], demon_lord_data["maxDamage"]) * scale - player["defense"], 2)
        else:
            dmg = round(random.uniform(monster.minDamage[monsterId], monster.maxDamage[monsterId]) - player["defense"], 2)

        dmg = max(1, dmg)
        player["health"] -= dmg
        print(Fore.RED + f"{currentMonsterFight} deals {dmg} damage!")
        time.sleep(0.8)

# Main Functions
def combat():
    global currentMonsterHealth, monsterId, player, persistentStats, endlessMode, endlessKills

    while True:
        show_combat_stats()
        save_to_file()

        # Handle boss prompt if room is at 10 and not already in a boss fight
        if persistentStats["room"] >= 10 and not persistentStats["bossFightReady"]:
            print(Fore.YELLOW + "A powerful presence blocks your path... Boss fight?")
            choice = input(Fore.GREEN + "Do you wish to challenge it? (yes/no) > ").strip().lower()
            if choice in ["yes", "y"]:
                persistentStats["bossFightReady"] = True
            else:
                print(Fore.RED + "You chose to wait. The boss still blocks your progress.")
                persistentStats["room"] = 9
                time.sleep(1.5)
                continue

        choice = input(Fore.BLUE + "What will you do? ").strip().lower()
        print()

        if choice in ["attack", "atk", ""]:
            print(Fore.YELLOW + "You attack!")
            damage = max(1, round(player["damage"] * random.uniform(0.75, 1.25) - currentMonsterDefense, 2))
            currentMonsterHealth -= damage
            print(Fore.RED + f"You dealt {damage} to {currentMonsterFight}.")
            time.sleep(0.2)
            monster_death_check()

        elif choice in ["retreat", "ret"]:
            if persistentStats.get("bossFightReady", False):
                print(Fore.RED + "You cannot retreat from a boss fight!")
                time.sleep(1)
                monster_death_check()
                continue
            print(Fore.YELLOW + "Attempting to retreat...")
            if random.randint(0, 100) < player["escape"]:
                print(Fore.GREEN + "You successfully escaped!")
                reset_monster()
                continue
            else:
                print(Fore.RED + "Retreat failed!")
                monster_turn()

        elif choice in ["level", "lvl"]:
            level_up()

        elif choice in ["inventory", "inv"]:
            show_inventory()

        elif choice in ["minigames", "mini", "games", "min", "other"]:
            minigame_selection()

        elif choice in ["stats", "st"]:
            show_stats_screen()

        elif choice == "exit":
            sys.exit()

        else:
            print(Fore.RED + "Invalid input.")
            time.sleep(0.8)
            continue 

        time.sleep(0.5)

        if player["health"] <= 0:
            print(Fore.RED + "You have died.")
            if endlessMode:
                print(Fore.YELLOW + f"You defeated {endlessKills} Demon Lords!")
            persistentStats["is_dead"] = True
            save_to_file()
            show_stats_screen()  

# Stat up code
def startup():
    global currentSaveName, savedGames, globalSavePath, endlessMode, endlessKills

    clear_screen()
    print(Fore.BLUE + "What is your name? [Type existing name to load or new name to create a save]")
    list_saved_files()

    name_input = input(Fore.GREEN + "\n> ").strip().lower()
    if not name_input.endswith(".json"):
        name_input += ".json"

    currentSaveName = name_input
    globalSavePath = os.path.join(saveDirectory, currentSaveName)

    savedGames = [f for f in os.listdir(saveDirectory) if f.endswith(".json")]

    if currentSaveName in savedGames:
        success = load_from_file(currentSaveName)
        if not success:
            print(Fore.RED + "Failed to load save. Exiting.")
            sys.exit()
        if persistentStats.get("is_dead", False):
            show_stats_screen()
            print(Fore.RED + "\nThis character is dead. You must create a new one.\n")
            sys.exit()
    else:
        print(Fore.YELLOW + f"Creating new save file: {currentSaveName}")

    if currentSaveName not in savedGames:
        print(Fore.YELLOW + "Choose difficulty: Easy / Normal / Hard")
        print(Fore.CYAN + "(Easy gives bonus XP; Hard gives less)")
        choice = input(Fore.GREEN + "> ").strip().lower()

        if choice == "easy":
            player["difficulty"] = 15
        elif choice == "normal":
            player["difficulty"] = 10 
        elif choice == "hard":
            player["difficulty"] = 5
        else:
            player["difficulty"] = 10   # Default to normal

        player["xp"] += player["difficulty"]

    combat()

if __name__ == "__main__":
    startup() 
# Define libraries and classes
class monsterVariables:
    names =     ["Slime","Goblin","Skeleton","Zombie","Vampire","Orc","Giant","Ent","Warg","Banshee","Ghoul","Bandit","Troll","Shade","Basilisk","Minotaur","Witch","Drake","Warlock","Knight","Behemoth","Chimera","Specter","Ogre","Harpy","Revenant","Lich","Manticore","Wyvern","Wyrm","Juggernaut","Hydra","Phantom","Colossus","Ifrit","Kraken","Dreadnought","Leviathan","Titan","Demon Lord"]
    maxHealth = [10,      15,      22,        33,      50,       75,   113,    170,  256,   284,      576,    864,     1297,   1946,   2919,      4378,      6568,   9852,   14778,    22168,   33252,     49878,    74818,    112227,168341, 252511,    378767,568151,     852226,  1278340,1917510,    2876265,4314398,  6471598,   9707397,14561096,21841644,     32762466,   49143699,73715548,]
    maxDamage = [4,        7,      10,       15,      23,       34,    51,     77,  115,   173,      259,    389,      584,    876,   1314,      1971,      2956,   4434,    6651,     9976,   14964,     22445,    33668,     50502, 75754, 113630,    170445,255668,     383502,  575253,  862880,    1294320,1941479,  2912219,   4368329, 6552493,9828740,      14743110,   22114665,33171997,]
    minDamage = [2,        2,       3,         5,       8,       11,    17,     26,   38,    58,       86,    130,      195,    292,    438,       657,       985,   1478,    2217,     3325,    4988,      7482,    11223,     16834, 25251,  37877,     56815, 85223,     127834,  191751,  287627,     431440, 647160,   970740,   1456110, 2184164,3276247,       4914370,    7371555,11057332,]
    defense =   [0,        1,       1,         1,       2,        3,     4,      6,   10,    14,       22,     32,       49,     73,    109,       164,       246,    369,     554,      831,    1247,      1870,     2806,      4209,  6313,   9469,     14204, 21306,      31959,   47938,   71907,     107860, 161790,   242685,    364027,  546041,819062,        1228592,    1842889,2764333,]

# Classes for ease
monster = monsterVariables()

# The Player Library
player = {
    "name": "placeHolderName",
    "maxHealth": 25.0,
    "health": 25.0,
    "damage": 3.5,
    "defense": 0.0,
    "dodge": 5.0,
    "escape": 20.0,
    "drop": 7.0,
    "difficulty": 0,
    "actionList": ["Attack", "Retreat", "Level", "Inventory", "Minigames/Other", "Stats", "Exit"],
    "buyList": ["Health", "Damage", "Defense", "Dodge", "Retreat", "Drop"],
    "gameList": ["Tamagachi", "Gambling", "Fishing", "Wishing Well", "Reborn"],
    "xp": 0.0,
    "coins": 0,
    "inventory": [],
    "healthBoost": 0,
    "damageBoost": 0,
    "defenseBoost": 0,
    "dodgeBoost": 0,
    "escapeBoost": 0,
    "dropBoost": 0,
}

# Endless mode
endlessMode = False
endlessKills = 0
demon_lord_data = {
    "demonLordsDefeated": 0,
    
    "health": monster.maxHealth[-1],
    "minDamage": monster.minDamage[-1],
    "maxDamage": monster.maxDamage[-1],
    "defense": monster.defense[-1]
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
    "baseHealthBoostCostFactor": 1.35,
    "baseDamageBoostCostFactor": 1.25,
    "baseDefenseBoostCostFactor": 1.4,
    "baseDodgeBoostCostFactor": 1.7,
    "baseEscapeBoostCostFactor": 1.1,
    "baseDropBoostCostFactor": 1.4,
    
    # How much each boost gives you each time (This number is multiplied with the stat for exponential increases)
    "healthBoostMod": 1.05,
    "damageBoostMod": 1.13,
    "defenseBoostMod": 1.12,
    "dodgeBoostMod": 1.13,
    "escapeBoostMod": 1.5,
    "dropBoostMod": 1.3,
    
    "healthBoostCap": 10000000000,
    "damageBoostCap": 10000000000,
    "defenseBoostCap": 10000000000,
    "dodgeBoostCap": 55,
    "escapeBoostCap": 95,
    "dropBoostCap": 25,
}

# Other Stats to keep track of
persistentStats = {
    "floor": 0,
    "room": 0,
    "bossFightReady": False,
    "monstersKilled": 0,
    "rebornsUsed": 0,
    "is_dead": False,
}

# Global Variables

# Monster Variables
monsterId = 0
currentMonsterFight = monster.names[monsterId] 
currentMonsterHealth = monster.maxHealth[monsterId]
currentMonsterDefense = monster.defense[monsterId]

# Save and load variables
currentSaveName = ''
savedGames = []
globalSavePath = ''
saveDirectory = "saves"
os.makedirs(saveDirectory, exist_ok=True)

# Thread management flags
fishing_thread = None
fishing_stop_event = threading.Event()
tamagatchi_thread = None
tamagatchi_stop_event = threading.Event()

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
    {"name": "Sluggish Blood", "desc": "Your lifeforce drains.", "boosts": {"health": -1000}},
    {"name": "Shattered Luck", "desc": "Fortune slips away.", "boosts": {"drop": -10}},
    {"name": "Doom’s Brand", "desc": "All gains halved temporarily.", "boosts": {"divineSpark": -5}}
]

# Functions

# Helper Functions
def timed_input(timeout=1.0):
    result = []
    def read_input():
        try:
            result.append(input())
        except EOFError:
            pass

    input_thread = threading.Thread(target=read_input)
    input_thread.daemon = True
    input_thread.start()
    input_thread.join(timeout)

    if input_thread.is_alive():
        return None  # Timeout
    return result[0] if result else ''

# Define the current os and clear screen properly
def clear_screen():
    print(Style.RESET_ALL)
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

# Stats Functions
def show_stats_screen():
    clear_screen()
    print(Style.RESET_ALL)

    if os.path.exists(globalSavePath):
        with open(globalSavePath, "r") as f:
            data = json.load(f)
    else:
        data = {}

    player_data = data.get("player", player)
    stats = data.get("persistentStats", persistentStats)
    tama = data.get("tamagatchi_data", tamagatchi_data)
    well = data.get("well_data", well_data)

    print(Fore.RED + ("===== PLAYER IS DECEASED =====\n" if stats.get("is_dead", False) else "===== PLAYER STATISTICS =====\n"))

    print(Fore.YELLOW + f"Name: {player_data.get('name', 'Unknown')}")
    print(Fore.CYAN + f"Current Floor: {stats.get('floor', 0)}.{stats.get('room', 0)}")
    print(f"XP: {round(player_data.get('xp', 0), 1)}  |  Coins: {round(player_data.get('coins', 0), 1)}")
    print(f"Max Health: {round(player_data.get('maxHealth', 0), 1)}  |  Damage: {round(player_data.get('damage', 0), 1)}  |  Defense: {round(player_data.get('defense', 0), 1)}")
    print(f"Dodge Chance: {round(player_data.get('dodge', 0), 1)}%  |  Retreat Chance: {round(player_data.get('escape', 0), 1)}%  |  Drop Chance: {round(player_data.get('drop', 0), 1)}%")
    print(f"Reborns Used: {stats.get('rebornsUsed', 0)}")

    print(Fore.MAGENTA + "\n--- Combat Stats ---")
    print(f"Monsters Killed: {stats.get('monstersKilled', 0)}")
    print(f"Demon Lords Defeated: {demon_lord_data.get('demonLordsDefeated', 0)}")

    print(Fore.MAGENTA + "\n--- Gambling Stats ---")
    print(f"Gambles: {gambling_data.get('gamblingBets', 0)}")
    print(f"Coins Gambled: {gambling_data.get('gamblingCoinsSpent', 0)} | Coins Won: {gambling_data.get('gamblingCoinsWon', 0)}")
    print(f"Items Sold: {gambling_data.get('itemsSold', 0)} | Coins from Selling: {gambling_data.get('coinsFromSelling', 0)}")
    print(f"Coins Converted to XP: {gambling_data.get('coinsConvertedToXP', 0)}")

    print(Fore.CYAN + "\n--- Fishing ---")
    print(f"Fish Caught: {fishing_data.get('fishCaught', 0)} | Items Fished: {fishing_data.get('itemsFished', 0)}")

    print(Fore.CYAN + "\n--- Wishing Well ---")
    print(f"Wishes Made: {well.get('wishingCoinsUsed', 0)}")
    print(f"Blessings Received: {well.get('blessingsReceived', 0)}")
    print(f"Curses Received: {well.get('cursesReceived', 0)}")
    print(f"Divine Spark Charges: {well.get('divineSpark', 0)}")

    print(Fore.GREEN + "\n--- Inventory ---")
    inventory = player_data.get("inventory", [])
    if inventory:
        for item in inventory:
            print(f"- {item['name']} | {item['boosts']}")
    else:
        print("(Empty)")

    print(Fore.CYAN + "\n--- Tamagatchi ---")
    print(f"Active: {tama.get('active', False)} | Hunger: {tama.get('hunger', 0)} | Bond: {tama.get('bond', 0)}")
    print(f"Boosts: {tama.get('boosts', {})}")

    if persistentStats["is_dead"]:
        print(Fore.RED + "\nThis character is dead. You must create a new one.\n")
        sys.exit()
        
    print(Fore.BLUE + "\n(Press Enter to return to combat...)")
    input(Fore.GREEN + "> ")
    
    combat()
    
def get_item_coin_value(item):
    #Calculate the coin value of an item based on its boosts and rarity.
    #Heuristic:
    #    - Each point of boost contributes 3–6 coins depending on stat type.
    #    - Extremely rare items (lower weight) are worth significantly more.

    if not isinstance(item, dict) or "boosts" not in item:
        return 0

    value = 0
    boosts = item.get("boosts", {})
    weight = item.get("weight", 1)

    # Base value for each stat type
    for stat, amount in boosts.items():
        if stat == "health":
            value += amount * 1.5
        elif stat == "damage":
            value += amount * 15
        elif stat == "defense":
            value += amount * 18.5
        elif stat in ["dodge", "escape", "drop"]:
            value += amount * 25  # utility stats are rarer
        elif stat == "xp":
            value += amount * 13.5
        elif stat == "coins":
            value += amount
        elif stat == "divineSpark":
            value += amount * 30
        elif stat == "heal" and amount == "full":
            value += 500

    # Rarity multiplier (inverse of weight; capped to avoid extreme inflation)
    rarity_bonus = min(50, round(25 / weight)) if weight > 0 else 100
    value = round(value * (1 + rarity_bonus / 100))

    return max(1, int(value))  # Ensure at least 1 coin

def show_inventory(): # Shows the inventory
    clear_screen()
    print(Fore.BLACK + "|")
    print(Fore.BLUE + "Inventory Overview")
    print(Fore.BLACK + "|")

    # Grab current inventory
    inventory = player.get("inventory", [])

    # If empty, show guidance
    if not inventory:
        print(Fore.RED + "Your inventory is currently empty.")
        print(Fore.YELLOW + "Defeat monsters to earn rare artifacts.")
        print(Fore.YELLOW + "Artifacts grant permanent stat boosts.")
    else:
        # Loop through and display all owned items
        for i, item in enumerate(inventory, 1):
            name = item.get("name", "Unknown")
            desc = item.get("desc", "No description provided.")
            boosts = item.get("boosts", {})

            # Show item number, name, description, and stat boosts
            print(Fore.CYAN + f"[{i}] {name}")
            print(Fore.YELLOW + f"  {desc}")
            print(Fore.MAGENTA + f"  Boosts: {boosts}")
            print(Fore.BLACK + "|")

    # Exit back to combat
    print(Fore.BLACK + "|")
    print(Fore.BLUE + "Press Enter to return to combat.")
    input(Fore.GREEN + "> ")
    combat()

def show_combat_stats(): # this is the main function to show all the stats during combat, it runs after each turn (or when coming back to combat after playing a minigame or something else) to refresh the page and show what the current stats of all enemies and players are. 
    global currentMonsterFight, currentMonsterHealth, monsterId, player, monster, persistentStats
    clear_screen()
    print(Fore.BLACK+"|")
    monsterHealthPercentage = round((currentMonsterHealth / monster.maxHealth[monsterId]) * 100,2)
    print(Fore.WHITE +"You are currently fighting a",currentMonsterFight,"  (Floor:"+str(persistentStats["floor"])+"."+str(persistentStats["room"])+")")
    print(Fore.BLACK +"|")
    print(Fore.RED+currentMonsterFight,"Health:")
    print(Fore.BLACK + "|", end='')
    # Cap health bar
    bar_length = min(round(monsterHealthPercentage / 2), 1000)
    print(Fore.RED + '=' * bar_length, end='')
    if monsterHealthPercentage > 2000:
        print(Fore.RED + " (HP: " + str(int(currentMonsterHealth)) + ")")
    else:
        print(Fore.RED + f" {monsterHealthPercentage}%")
    print(Fore.BLACK +"|")
    print(Fore.BLACK +"|")
    currentHealthPercentage = round((player["health"] / player["maxHealth"]) * 100,2)
    print(Fore.GREEN+"Player Stats:")
    print(Fore.GREEN+" Health: ",end='')
    for i in range(round(currentHealthPercentage/2.4)): print(Fore.GREEN +'=',end='')
    print("",str(currentHealthPercentage)+"%  ("+str(round(player["health"],1))+")")
    print(Fore.GREEN +" Damage:",round(player["damage"],1), " |  Defense:",round(player["defense"],1)," |  Xp:",round(player["xp"],1))
    print(Fore.GREEN +" Dodge Chance:",str(round(player["dodge"],1))+"% |  Retreat Chance:",str(round(player["escape"],1))+"%"," |  Item Drop Chance:",str(round(player["drop"],1))+"%")
    print(Fore.BLACK +"|")
    if tamagatchi_data["active"]:
        print(Fore.CYAN + f"Tamagatchi → Bond: {tamagatchi_data['bond']} | Hunger: {tamagatchi_data['hunger']} | Boosts: {tamagatchi_data['boosts']}")
        print(Fore.BLACK +"|")
    print(Fore.BLACK +"|")
    print(Fore.BLUE +"Actions:",player["actionList"])
    print(Style.RESET_ALL)

# Minigame/Other Functions
def reborn():
    global player, shop_data, well_data, persistentStats

    clear_screen()

    if persistentStats["floor"] < 100:
        print(Fore.RED + "You must reach floor 100 to use Reborn.")
        time.sleep(2)
        combat()
        return

    print(Fore.YELLOW + "--- Reborn ---")
    print(Fore.CYAN + "Reset to Floor 0 while keeping all stat boosts and inventory.")
    print(Fore.CYAN + "Shop prices reset, Tamagatchi improves, and well cost resets.")
    print(Fore.CYAN + "Cost: 1000 XP  →  Reward: 100,000 coins")
    print(Fore.YELLOW + "\nReborn? (yes/no)")

    choice = input(Fore.GREEN + "> ").strip().lower()
    if choice in ["yes", "y"]:
        if player["xp"] < 1000:
            print(Fore.RED + "You don't have enough XP.")
            time.sleep(2)
            combat()
            return

        player["xp"] -= 1000
        player["coins"] += 100000
        well_data["wishing_well_cost"] = 1000
        persistentStats["floor"] = 0
        persistentStats["room"] = 0
        persistentStats["rebornsUsed"] += 1

        # Reset shop costs to base values
        shop_data["baseHealthBoostCost"] = 2
        shop_data["baseDamageBoostCost"] = 3
        shop_data["baseDefenseBoostCost"] = 4
        shop_data["baseDodgeBoostCost"] = 5
        shop_data["baseEscapeBoostCost"] = 2
        shop_data["baseDropBoostCost"] = 10

        print(Fore.GREEN + "You have been reborn. The climb begins anew...")
        time.sleep(3)

        reset_monster()
        combat()
    else:
        print(Fore.YELLOW + "Rebirth canceled.")
        time.sleep(1.5)
        combat()

# Section for managing the wishing well
def wishing_well():
    global player, well_data

    clear_screen()
    if persistentStats["monstersKilled"] < 1000:
        print(Fore.RED + "You must defeat 1000 monsters to unlock the Wishing Well.")
        time.sleep(2)
        combat()
        return

    cost = well_data["wishing_well_cost"]
    print(Fore.CYAN + "--- The Wishing Well ---")
    print(Fore.YELLOW + f"Cost to Wish: {cost} coins")
    print(f"You have: {player['coins']} coins")
    print(Fore.MAGENTA + "Make a wish? (yes / no)")

    choice = input(Fore.GREEN + "> ").strip().lower()
    if choice not in ["yes", "y"]:
        combat()
        return

    if player["coins"] < cost:
        print(Fore.RED + "Not enough coins!")
        time.sleep(2)
        combat()
        return

    player["coins"] -= cost
    well_data["wishing_well_cost"] = int(cost * 1.25)
    well_data["wishingCoinsUsed"] += 1

    roll = random.randint(1, 100)
    result_type = "blessing" if roll <= 60 else "curse" if roll <= 95 else "spark"

    if result_type == "spark":
        print(Fore.CYAN + "A Divine Spark ignites within you. +1 charge!")
        well_data["divineSpark"] += 1
        time.sleep(2)
        combat()
        return

    elif result_type == "blessing":
        blessing = random.choice(blessings)
        if blessing["name"] in well_data["obtainedBlessings"]:
            print(Fore.YELLOW + f"You already received {blessing['name']}. Refund: {cost // 2} coins.")
            player["coins"] += cost // 2
        else:
            apply_boost(blessing["boosts"])
            well_data["obtainedBlessings"].append(blessing["name"])
            well_data["blessingsReceived"] += 1
            print(Fore.GREEN + f"Blessing: {blessing['name']} → {blessing['desc']}")

    else:  # curse
        curse = random.choice(curses)
        if curse["name"] in well_data["obtainedCurses"]:
            print(Fore.YELLOW + f"You already endured {curse['name']}. Refund: {cost // 2} coins.")
            player["coins"] += cost // 2
        else:
            apply_boost(curse["boosts"])
            well_data["obtainedCurses"].append(curse["name"])
            well_data["cursesReceived"] += 1
            print(Fore.RED + f"Curse: {curse['name']} → {curse['desc']}")

    apply_boosts()
    time.sleep(3)
    combat()

def apply_boost(boost_dict): # This is for the well specifically, not to be confused with the apply boost(s) function down below
    for key, value in boost_dict.items():
        if key == "heal" and value == "full":
            player["health"] = player["maxHealth"]
        elif key == "divineSpark":
            well_data["divineSpark"] += value
        elif key == "xp":
            player["xp"] += value
        elif key == "coins":
            player["coins"] += value
        elif key in player:
            player[key] += value

# Section for managing the fishing minigame
def fishing():
    global fishing_active, fishing_thread, fishing_stop_event
    fishing_active = True
    clear_screen()
    print(Style.RESET_ALL)
    print(Fore.CYAN + "You sit quietly by the water and begin fishing...")
    print(Fore.YELLOW + "When a fish bites, press Enter 2-3 times quickly to catch it!")
    print(Fore.YELLOW + "Type 'leave' to stop fishing at any time.\n")

    idle_enter_count = 0
    fish_ready = False
    cooldown_until = 0
    fishing_penalty = False
    penalty_end_time = 0

    def fishing_loop():
        nonlocal fish_ready, cooldown_until, fishing_penalty, penalty_end_time
        while fishing_active and not fishing_stop_event.is_set():
            if fishing_penalty or time.time() < cooldown_until:
                time.sleep(0.2)
                continue
            print(Fore.BLUE + "Waiting for a bite...")
            time.sleep(random.uniform(4, 9))
            if not fishing_active or fishing_stop_event.is_set():
                break
            fish_ready = True
            print(Fore.YELLOW + "\nA fish is on the line! Press Enter quickly!")
            
            response = timed_input(timeout=1.0)
            fish_ready = False

            if response is None:
                print(Fore.RED + "Too slow! The fish got away.")
                cooldown_until = time.time() + 3
                continue

            fish_ready = False

            #if reaction_time > 1.0:
            #    print(Fore.RED + "Too slow! The fish got away.")
            #    cooldown_until = time.time() + 3
            #    continue
            if fishing_penalty:
                print(Fore.RED + "Rod tangled from spam. No reward.")
                continue

            if random.random() < 0.8:
                scale = 1 + (persistentStats["floor"] * 2)
                mult = 10 * int(persistentStats["floor"] * 10) if persistentStats["floor"] >= 50 else 1
                xp_gain = round(random.uniform(0.5, 5.0) * scale * mult, 1)
                player["xp"] += xp_gain
                print(Fore.GREEN + f"You caught a fish and earned {xp_gain} XP!")
                fishing_data["fishCaught"] += 1
            else:
                item = random.choices(drop_table, weights=[i["weight"] for i in drop_table], k=1)[0]
                owned_names = [i["name"] for i in player["inventory"]]
                if item["name"] in owned_names:
                    value = get_item_coin_value(item)
                    player["coins"] += value
                    print(Fore.MAGENTA + f"Duplicate item: {item['name']} → sold for {value} coins.")
                    gambling_data["itemsSold"] += 1
                    gambling_data["coinsFromSelling"] += value
                else:
                    player["inventory"].append(item)
                    print(Fore.MAGENTA + f"Fished a rare item: {item['name']}!")
                    print(Fore.YELLOW + item["desc"])
                fishing_data["itemsFished"] += 1
                apply_boosts()
            cooldown_until = time.time() + 1

    if fishing_thread and fishing_thread.is_alive():
        print(Fore.YELLOW + "Fishing is already active.")
    else:
        fishing_stop_event.clear()
        fishing_thread = threading.Thread(target=fishing_loop, daemon=True)
        fishing_thread.start()

    while fishing_active:
        now = time.time()
        if fishing_penalty:
            remaining = int(penalty_end_time - now)
            if remaining <= 0:
                fishing_penalty = False
                print(Fore.GREEN + "Line untangled. You may fish again.")
            else:
                print(Fore.RED + f"Line tangled! Wait {remaining}s.")
            time.sleep(1)
            continue

        cmd = input()
        if cmd.strip().lower() in ["leave", "exit"]:
            fishing_active = False
            fishing_stop_event.set()
            print(Fore.GREEN + "You pack up and return to combat...")
            time.sleep(1)
            break
        if cmd.strip() == "" and not fish_ready:
            idle_enter_count += 1
            if idle_enter_count > 2:
                print(Fore.RED + "Stop yanking! Line tangled.")
                fishing_penalty = True
                penalty_end_time = time.time() + 10
                idle_enter_count = 0
        else:
            idle_enter_count = 0
    combat()

# Section for managing the gambling minigame
def gamble_stat_change(amount): # Returns how much the stats change when doing a high risk gamble
    roll = random.randint(1, 100)
    if roll <= 10:
        return -amount
    elif roll <= 30:
        return -int(amount * 0.5)
    elif roll <= 50:
        return int(amount * 0.2)
    elif roll <= 75:
        return int(amount * 0.5)
    elif roll <= 90:
        return amount
    else:
        return amount * 2

def gambling(): # Manages the gambling screen
    global player
    clear_screen()
    print(Style.RESET_ALL)
    print(Fore.YELLOW + "Welcome to the Gambling Den")
    print(Fore.CYAN + f"You have {player['coins']} coins.")
    print(Fore.BLACK,"|")

    if player["coins"] == 0 and not player["inventory"]:
        print(Fore.RED + "\nYou have no coins or items to interact with.")
        print(Fore.YELLOW + "Defeat monsters to gain items. Sell them for coins to gamble!")
        time.sleep(3)
        combat()
        return

    print(Fore.GREEN + "\nOptions:")
    print(Fore.GREEN + " [sell]    → Sell inventory items for coins")
    print(Fore.GREEN + " [gamble]  → Bet a custom amount of coins")
    print(Fore.GREEN + " [convert] → Convert 10 coins into 1 XP")
    if persistentStats["floor"] >= 50:
        print(Fore.GREEN + " [highrisk] → Gamble health, damage, or defense stats")
    else:
        print(Fore.RED + " [highrisk] → Unlocks at Floor 50+")
    print(Fore.GREEN + " [leave]   → Exit back to combat")
    print(Fore.BLACK,"|")

    choice = input(Fore.CYAN + "\nYour choice: ").strip().lower()

    if choice in ["sell"]:
        if not player["inventory"]:
            print(Fore.RED + "You have no items to sell.")
        else:
            for i, item in enumerate(player["inventory"]):
                value = get_item_coin_value(item)
                print(Fore.CYAN + f"[{i}] {item['name']} → {value} coins")
                print(Fore.MAGENTA + f"     {item['desc']}")

            sel = input(Fore.GREEN + "\nChoose item number to sell or 'all': ").strip().lower()
            if sel == "all":
                total = sum(get_item_coin_value(i) for i in player["inventory"])
                player["coins"] += total
                gambling_data["itemsSold"] += len(player["inventory"])
                gambling_data["coinsFromSelling"] += total
                player["inventory"].clear()
                print(Fore.GREEN + f"Sold all items for {total} coins.")
            elif sel.isdigit():
                i = int(sel)
                if 0 <= i < len(player["inventory"]):
                    item = player["inventory"].pop(i)
                    value = get_item_coin_value(item)
                    player["coins"] += value
                    gambling_data["itemsSold"] += 1
                    gambling_data["coinsFromSelling"] += value
                    print(Fore.GREEN + f"Sold {item['name']} for {value} coins.")
                else:
                    print(Fore.RED + "Invalid item index.")
            else:
                print(Fore.RED + "Invalid input.")
        apply_boosts()

    elif choice in ["gamble", "gam"]:
        try:
            amt = int(input(Fore.YELLOW + "Enter coin amount to bet: ").strip())
            if amt <= 0 or amt > player["coins"]:
                print(Fore.RED + "Invalid bet amount.")
            else:
                mults = [0, 0.1, 0.2, 0.5, 1.0, 1.2, 1.5, 2.0, 3.0]
                weights = [10, 20, 10, 5, 6, 10, 50, 5, 2]
                scale = 1 + (persistentStats["floor"] * 0.5)
                mult = random.choices(mults, weights)[0] * scale
                result = int(amt * mult)
                player["coins"] -= amt
                player["coins"] += result + 1
                gambling_data["gamblingBets"] += 1
                gambling_data["gamblingCoinsSpent"] += amt
                gambling_data["gamblingCoinsWon"] += result
                if result == 0:
                    print(Fore.RED + "You lost everything!")
                elif result < amt:
                    print(Fore.YELLOW + f"You lost some. You got {result} coins back.")
                else:
                    print(Fore.GREEN + f"You won! You now have {result} more coins.")
                    player["coins"] += amt
        except:
            print(Fore.RED + "Invalid number.")

    elif choice in ["convert"]:
        try:
            amt = int(input(Fore.YELLOW + "Coins to convert to XP (10 coins = 1 XP): ").strip())
            if amt < 10 or amt > player["coins"]:
                print(Fore.RED + "Invalid amount.")
            else:
                xp = round(amt / 10, 2)
                player["coins"] -= amt
                player["xp"] += xp
                gambling_data["coinsConvertedToXP"] += amt
                print(Fore.GREEN + f"Gained {xp} XP.")
        except:
            print(Fore.RED + "Invalid input.")

    elif choice in ["highrisk", "high", "risk"]:
        if persistentStats["floor"] < 50:
            print(Fore.RED + "High Risk unlocked at Floor 50")
        else:
            stat = input(Fore.YELLOW + "Which stat? [health/damage/defense]: ").strip().lower()
            if stat in ["health", "damage", "defense"]:
                try:
                    amt = int(input(Fore.CYAN + f"Points of {stat} to gamble: ").strip())
                    key = f"{stat}Boost"
                    if amt <= 0 or amt > player[key]:
                        print(Fore.RED + "Invalid amount.")
                    else:
                        change = gamble_stat_change(amt)
                        player[key] = max(0, player[key] + change)
                        print(Fore.MAGENTA + f"{stat.capitalize()} changed by {change}.")
                        apply_boosts()
                except:
                    print(Fore.RED + "Invalid number.")
            else:
                print(Fore.RED + "Invalid stat.")

    elif choice in ["leave", "exit"]:
        combat()
        return

    else:
        print(Fore.RED + "Invalid input.")

    time.sleep(2)
    gambling()

# Tamagachi stuff
def start_tamagatchi_thread():
    global tamagatchi_thread
    if tamagatchi_thread and tamagatchi_thread.is_alive():
        return
    tamagatchi_stop_event.clear()
    def loop():
        while tamagatchi_data["active"] and not tamagatchi_stop_event.is_set():
            if tamagatchi_data["last_update"] is not None:
                update_tamagatchi()
            time.sleep(random.uniform(30, 200)) # How long it takes for the tamagatchi to update
    tamagatchi_thread = threading.Thread(target=loop, daemon=True)
    tamagatchi_thread.start()

def update_tamagatchi():
    hunger = tamagatchi_data["hunger"]
    bond = tamagatchi_data["bond"]
    kills = persistentStats.get("monstersKilled", 0)

    # Hunger increases
    if hunger < 100:
        tamagatchi_data["hunger"] += 1

    # Bond slowly increases if well-fed (under 20 hunger)
    if hunger < 20 and random.random() < 0.5: # 50% chance to gain a bond each update if the hunger is low enough
        tamagatchi_data["bond"] += 1

    # Recalculate boosts
    if bond > 0:
        scale = 1
        if persistentStats.get("rebornsUsed", 0) >= 6:
            scale = 3
        elif persistentStats.get("rebornsUsed", 0) >= 1:
            scale = 2

        tamagatchi_data["boosts"]["health"] = int(bond * scale * (1 + (kills/10) * 1))
        tamagatchi_data["boosts"]["damage"] = int(bond * scale * (1 + (kills/10) * 0.3))
        tamagatchi_data["boosts"]["defense"] = int(bond * scale * (1 + (kills/10) * 0.1))
    
    apply_boosts()

def tamagatchi():
    global player, persistentStats
    max_bond = 20 * (persistentStats["rebornsUsed"] + 1)
    clear_screen()
    print(Style.RESET_ALL)

    if not tamagatchi_data["active"]:
        if player["xp"] < 100:
            print(Fore.RED + "You need 100 XP to adopt a Tamagatchi.")
            time.sleep(3)
            combat()
            return
        player["xp"] -= 100
        tamagatchi_data.update({
            "active": True,
            "last_update": datetime.now().isoformat(),
            "hunger": 3,
            "bond": 5
        })
        start_tamagatchi_thread()
        print(Fore.YELLOW + "You adopted a glowing creature!")
        print(Fore.RED + "Feed it to earn permanent boosts.")
        time.sleep(2)

    while True:
        clear_screen()
        hunger = tamagatchi_data["hunger"]
        bond = tamagatchi_data["bond"]
        boosts = tamagatchi_data["boosts"]
        print(Fore.CYAN + "\n--- Tamagatchi Status ---")
        print(Fore.MAGENTA + f"Hunger: {hunger} / 100")
        print(Fore.MAGENTA + f"Bond: {bond} / {max_bond}")
        print(Fore.GREEN + f"Boosts: {boosts}")
        print(Fore.YELLOW + f"XP: {round(player['xp'], 1)}")
        print(Fore.BLACK+"|")
        print(Fore.YELLOW+"Tamagatchi will be much happier if hunger is kept under 20")
        print(Fore.BLACK+"|")

        if hunger <= 5:
            print(Fore.YELLOW + "It's not hungry enough to feed.")
        else:
            cost = round(hunger * 1.3 * (tamagatchi_data["tamagatchiFeeds"] + 1), 1)
            print(Fore.YELLOW + f"Feeding cost: {round(cost, 1)} XP")

        print(Fore.CYAN + "\nType 'feed' to feed, or 'exit' to return to combat.")
        choice = input().strip().lower()

        if choice in ["exit", "leave"]:
            combat()
            return
        elif choice == "feed":
            if hunger <= 5:
                print(Fore.YELLOW + "It's not hungry enough to feed.")
            elif player["xp"] >= cost: # type: ignore
                tamagatchi_data["hunger"] = max(hunger - 4, 0)
                tamagatchi_data["bond"] = min(bond + 1, max_bond)
                player["xp"] -= cost # type: ignore
                tamagatchi_data["tamagatchiFeeds"] += 1
                print(Fore.GREEN + "You feed your companion! It looks happier.")
            else:
                print(Fore.RED + "Not enough XP.")
        else:
            print(Fore.RED + "Invalid command.")
        apply_boosts()
        time.sleep(1.5)

# The screen for selecting minigames
def minigame_selection():
    clear_screen()
    print(Fore.BLACK + "|")
    print(Fore.YELLOW + "Welcome to the Minigame/Other section!")
    print(Fore.BLUE + "  Complete minigames to earn boosts, XP, and more!")
    print(Fore.BLACK + "|")
    print(Fore.YELLOW + "Tamagatchi     → Feed a friend for passive stat boosts.")
    print(Fore.YELLOW + "Gambling       → Risk coins/items to multiply rewards.")
    print(Fore.YELLOW + "Fishing        → Relax and earn items or XP.")
    print(Fore.YELLOW + "Wishing Well   → Spend coins for powerful blessings—or curses.")
    print(Fore.YELLOW + "Reborn         → Reset with your stats intact after high progress.")
    print(Fore.BLACK + "|")
    print(Fore.BLUE + "Options:", player["gameList"])
    print(Fore.BLACK + "|")
    print(Style.RESET_ALL)

    choice = input(Fore.GREEN + "> ").strip().lower()

    if choice in ["tamagatchi", "tama"]:
        tamagatchi()
    elif choice in ["gambling", "gamble", "gamb"]:
        gambling()
    elif choice in ["fishing", "fish"]:
        fishing()
    elif choice in ["wishing well", "wish", "wishingwell", "wsh"]:
        wishing_well()
    elif choice in ["reborn", "re", "born"]:
        reborn()
    elif choice == "exit":
        combat()
    else:
        print(Fore.RED + "Invalid input. Try again.")
        time.sleep(1)
        minigame_selection()

# Saving and Loading Functions
def save_to_file(): # Saves the file
    global globalSavePath, player, persistentStats, tamagatchi_data, well_data
    player["name"] = os.path.splitext(currentSaveName)[0]

    data = {
        "player": player,
        "persistentStats": persistentStats,
        "tamagatchi_data": tamagatchi_data,
        "well_data": well_data,
        "shop_data": shop_data,
        "fishing_data": fishing_data,
        "gambling_data": gambling_data,
        "endlessMode": endlessMode,
        "endlessKills": endlessKills,
        "monsterId": monsterId,
        "currentMonsterHealth": currentMonsterHealth
    }

    with open(globalSavePath, "w") as f:
        json.dump(data, f, indent=4)
    
def list_saved_files(): # lists saved files
    files = os.listdir(saveDirectory)
    json_files = [f for f in files if f.endswith('.json')]
    active = []
    dead = []

    for file in json_files:
        try:
            with open(os.path.join(saveDirectory, file), 'r') as f:
                data = json.load(f)
                if data.get("persistentStats", {}).get("is_dead", False):
                    dead.append(file)
                else:
                    active.append(file)
        except Exception:
            continue

    print(Fore.CYAN + "Active Save Files:")
    for f in active:
        print("  " + f)
    print(Fore.RED + "\nDead Save Files:")
    for f in dead:
        print("  " + f)
    print(Style.RESET_ALL)

def load_from_file(filename): # Load data from files
    global globalSavePath, player, persistentStats, tamagatchi_data, well_data
    global endlessMode, endlessKills, monsterId, currentMonsterFight, currentMonsterHealth, currentMonsterDefense

    path = os.path.join(saveDirectory, filename)
    globalSavePath = path

    try:
        with open(path, "r") as f:
            data = json.load(f)
        
        player.update(data.get("player", {}))
        persistentStats.update(data.get("persistentStats", {}))
        tamagatchi_data.update(data.get("tamagatchi_data", {}))
        shop_data.update(data.get("shop_data", {}))
        well_data.update(data.get("well_data", {}))
        fishing_data.update(data.get("fishing_data", {}))
        gambling_data.update(data.get("gambling_data", {}))
        endlessMode = data.get("endlessMode", False)
        endlessKills = data.get("endlessKills", 0)
        monsterId = data.get("monsterId", 0)
        currentMonsterFight = monster.names[monsterId]
        currentMonsterHealth = data.get("currentMonsterHealth", monster.maxHealth[monsterId])
        currentMonsterDefense = monster.defense[monsterId]

        # Stats the tamagatchi thread
        if tamagatchi_data.get("active"):
            start_tamagatchi_thread()

        print(Fore.GREEN + f"Loaded from {filename}")
        return True
    except Exception as e:
        print(Fore.RED + f"Failed to load save: {e}")
        return False

# Other Main Functions
def try_drop_item():
    #Attempts to drop an item after combat or fishing, based on player's drop chance.
    #If an item is already in inventory, it is auto-sold for coins instead.
    #Applies item boosts immediately if obtained.
    
    drop_chance = player["drop"]
    if random.uniform(0, 100) <= drop_chance:
        # Get weights and choose one item
        weights = [item.get("weight", 1) for item in drop_table]
        dropped_item = random.choices(drop_table, weights=weights, k=1)[0]

        owned_names = [i["name"] for i in player["inventory"]]
        if dropped_item["name"] in owned_names:
            # Duplicate item → convert to coins
            value = get_item_coin_value(dropped_item)
            player["coins"] += value
            print(Fore.MAGENTA + f"You found {dropped_item['name']} again.")
            print(Fore.YELLOW + f"It was converted into {value} coins.")
        else:
            # New item → add to inventory
            player["inventory"].append(dropped_item)
            print(Fore.MAGENTA + f"You found: {dropped_item['name']}!")
            print(Fore.YELLOW + dropped_item["desc"])

        apply_boosts()
        time.sleep(0.5)


def apply_boosts():
    #Recalculate and apply all stat boosts from level-ups, items, tamagatchi, and blessings.
    #This function resets stats to base values and then adds all applicable bonuses.

    # Base stats 
    base_health = 25.0
    base_damage = 3.5
    base_defense = 0.0
    base_dodge = 5.0
    base_escape = 20.0
    base_drop = 7.0

    # Reset stats to base + permanent boosts
    player["maxHealth"] = base_health + player["healthBoost"]
    player["damage"] = base_damage + player["damageBoost"]
    player["defense"] = base_defense + player["defenseBoost"]
    player["dodge"] = base_dodge + player["dodgeBoost"]
    player["escape"] = base_escape + player["escapeBoost"]
    player["drop"] = base_drop + player["dropBoost"] 

    # Add item boosts
    for item in player["inventory"]:
        boosts = item.get("boosts", {})
        player["maxHealth"] += boosts.get("health", 0)
        player["damage"] += boosts.get("damage", 0)
        player["defense"] += boosts.get("defense", 0)
        player["dodge"] += boosts.get("dodge", 0)
        player["escape"] += boosts.get("escape", 0)
        player["drop"] += boosts.get("drop", 0)

    # Clamp capped values
    player["drop"] = min(player["drop"], shop_data["dropBoostCap"])
    player["dodge"] = min(player["dodge"], shop_data["dodgeBoostCap"])
    player["escape"] = min(player["escape"], shop_data["escapeBoostCap"])

    # Apply tamagatchi boosts
    if tamagatchi_data.get("active"):
        boosts = tamagatchi_data["boosts"]
        player["maxHealth"] += boosts.get("health", 0)
        player["damage"] += boosts.get("damage", 0)
        player["defense"] += boosts.get("defense", 0)

    # Make sure current health isn't above max
    if player["health"] > player["maxHealth"]:
        player["health"] = player["maxHealth"]


def reset_monster():
    # Resets monster based on current floor + room count, or spawns boss
    global monsterId, player, monster, currentMonsterFight, currentMonsterHealth, currentMonsterDefense, persistentStats

    if persistentStats["bossFightReady"]:
        boss_index = min(monsterId + 1, len(monster.names) - 1)
        monsterId = boss_index
        persistentStats["bossFightReady"] = False

    if endlessMode:
            # Endless mode: demon lord keeps getting stronger
            demon_lord_data["demonLordsDefeated"] += 1
            multiplier = 2 ** demon_lord_data["demonLordsDefeated"]

            demon_lord_data["health"] = monster.maxHealth[-1] * multiplier
            demon_lord_data["minDamage"] = monster.minDamage[-1] * multiplier
            demon_lord_data["maxDamage"] = monster.maxDamage[-1] * multiplier
            demon_lord_data["defense"] = monster.defense[-1] * multiplier

            currentMonsterFight = f"Demon Lord x{demon_lord_data['demonLordsDefeated']}"
            currentMonsterHealth = demon_lord_data["health"]
            currentMonsterDefense = demon_lord_data["defense"]
            return
    else:
        weights = manage_floors()
        tier_indices = [i for i, w in enumerate(weights) if w > 0]

        if persistentStats["bossFightReady"] and persistentStats["room"] == 10:
            print(Fore.RED+"A boss monster approaches... defeat this enemy to move on to the next floor")
            time.sleep(1.5)
            # Boss is the monster immediately to the right of the strongest in the tier
            boss_index = tier_indices[-1] + 1
            if boss_index >= len(monster.names):
                boss_index = tier_indices[-1]  # fallback to last if out of range
            monsterId = boss_index
        else:
            # Random monster from current floor weights
            monsterId = random.choices(range(len(monster.names)), weights=weights, k=1)[0]

        currentMonsterFight = monster.names[monsterId]
        currentMonsterHealth = monster.maxHealth[monsterId]
        currentMonsterDefense = monster.defense[monsterId]

def manage_floors():
    # Calculates spawn weights for current floor based on 3 rotating monsters
    global persistentStats, monster

    total_monsters = len(monster.names)
    tier_size = 3

    # Determine monster tier group for this floor
    floor = persistentStats["floor"]
    tier_start = min(floor % (total_monsters - tier_size + 1), total_monsters - tier_size)
    tier_end = tier_start + tier_size

    # Determine if boss is available
    if persistentStats["room"] >= 10:
        persistentStats["bossFightReady"] = True

    # Weights: [common, uncommon, rare]
    base_weights = [1.0, 0.75, 0.5]
    weights = [base_weights[i - tier_start] if tier_start <= i < tier_end else 0 for i in range(total_monsters)]
    return weights

# The level up screen
def level_up():
    while True:
        clear_screen()
        print(Fore.BLACK + "|")
        print(Fore.GREEN + f"Upgrade Costs (Current XP: {round(player['xp'], 1)})")
        print(Fore.GREEN +
            f" Health: {shop_data['baseHealthBoostCost']} |" +
            f" Damage: {shop_data['baseDamageBoostCost']} |" +
            f" Defense: {shop_data['baseDefenseBoostCost']}\n" +
            f" Dodge: {shop_data['baseDodgeBoostCost']} |" +
            f" Escape: {shop_data['baseEscapeBoostCost']} |" +
            f" Drop: {shop_data['baseDropBoostCost']}")
        print(Fore.BLACK + "|\n" + Fore.BLUE + "Options:", player["buyList"])
        print(Fore.BLUE + "(Type 'exit' to return to combat)")

        choice = input(Fore.GREEN + "> ").strip().lower()

        upgrade_map = {
            "health": ("healthBoost", "baseHealthBoostCost", "baseHealthBoostCostFactor", "healthBoostMod", "healthBoostCap"),
            "damage": ("damageBoost", "baseDamageBoostCost", "baseDamageBoostCostFactor", "damageBoostMod", "damageBoostCap"),
            "defense": ("defenseBoost", "baseDefenseBoostCost", "baseDefenseBoostCostFactor", "defenseBoostMod", "defenseBoostCap"),
            "dodge": ("dodgeBoost", "baseDodgeBoostCost", "baseDodgeBoostCostFactor", "dodgeBoostMod", "dodgeBoostCap"),
            "escape": ("escapeBoost", "baseEscapeBoostCost", "baseEscapeBoostCostFactor", "escapeBoostMod", "escapeBoostCap"),
            "drop": ("dropBoost", "baseDropBoostCost", "baseDropBoostCostFactor", "dropBoostMod", "dropBoostCap"),
        }

        aliases = {
            "hp": "health", "hlth": "health",
            "dmg": "damage",
            "def": "defense",
            "dod": "dodge", "dodge chance": "dodge", "dodgechance": "dodge",
            "ret": "escape", "esc": "escape", "retreat": "escape",
            "drp": "drop", "drop chance": "drop", "dropchance": "drop"
        }

        choice = aliases.get(choice, choice)

        if choice in upgrade_map:
            boost_key, cost_key, factor_key, mod_key, cap_key = upgrade_map[choice]
            current_cost = shop_data[cost_key]
            boost_mod = shop_data[mod_key]
            cap = shop_data[cap_key]

            if player["xp"] < current_cost:
                print(Fore.RED + "Not enough XP!")
            elif player[boost_key] >= cap:
                print(Fore.RED + f"{boost_key.capitalize()} boost is capped at {cap}.")
            else:  # applies stat boosts
                player["xp"] -= current_cost

                if choice == "health":
                    base_health = 25.0

                    if player[boost_key] <= 0:
                        player[boost_key] = 1.0  # Starting point

                    current_boost = player[boost_key]
                    proposed_boost = current_boost * boost_mod

                    # Calculate new maxHealth
                    current_max = player["maxHealth"]
                    proposed_max = base_health + proposed_boost
                    increase = proposed_max - current_max
                    max_increase = current_max * 0.5

                    # Enforce cap
                    if increase > max_increase:
                        proposed_max = current_max + max_increase
                        proposed_boost = proposed_max - base_health

                    player[boost_key] = min(proposed_boost, cap)

                    apply_boosts()
                    heal_amount = player["maxHealth"] * 0.5
                    player["health"] = min(player["health"] + heal_amount, player["maxHealth"])

                else:
                    player[boost_key] += boost_mod
                    player[boost_key] = min(player[boost_key], cap)  # Clamp all boosts

                # Apply scaling multipliers only to linear boosts
                if choice not in ["dodge", "escape", "drop"]:
                    shop_data[mod_key] *= shop_data[factor_key]

                # Always scale price
                shop_data[cost_key] = round(shop_data[cost_key] * shop_data[factor_key], 1)

                apply_boosts()
                print(Fore.YELLOW + f"{boost_key.capitalize()} boosted! New value: {round(player[boost_key], 2)}")

        elif choice == "exit":
            return
        else:
            print(Fore.RED + "Invalid input.")
        time.sleep(1)

def monster_death_check():
    global currentMonsterHealth, monsterId, player, persistentStats, endlessMode, endlessKills
    if currentMonsterHealth <= 0:
    # Activate Endless Mode when Demon Lord dies
        if currentMonsterFight == "Demon Lord" and not endlessMode:
            endlessMode = True
            endlessKills = 0
            print(Fore.RED + "\n--- ENDLESS MODE UNLOCKED ---")
            print(Fore.MAGENTA + "Demon Lords will now respawn stronger each time.")
            time.sleep(5)
            
        if tamagatchi_data.get("active") and tamagatchi_data["hunger"] < 20:
            if random.random() < 0.2:
                tamagatchi_data["bond"] += 1
        print(Fore.GREEN + "You defeated the monster!")
            
        persistentStats["monstersKilled"] += 1
        player["health"] += round(monster.maxHealth[monsterId]/10)

        if persistentStats.get("bossFightReady", False):
            persistentStats["floor"] += 1
            persistentStats["room"] = 0
            persistentStats["bossFightReady"] = False
            print(Fore.GREEN + f"You conquered the boss! Now entering floor {persistentStats['floor']}.")
            time.sleep(0.5)
        else:
            persistentStats["room"] += 1

        # This is what happens when you kill a monster
        xp_gain = round(monster.maxHealth[monsterId] / 12, 1)
        if well_data["divineSpark"] > 0:
            xp_gain *= 2
            well_data["divineSpark"] -= 1
            print(Fore.YELLOW + f"The Divine Spark doubles your XP to {xp_gain}!")

        player["xp"] += xp_gain
        try_drop_item()

        if currentMonsterFight == "Demon Lord":
            endlessKills += 1
            print(Fore.MAGENTA + f"Demon Lord defeated! Total defeated: {endlessKills}")
        elif endlessMode:
            endlessKills += 1

        time.sleep(0.5)
        reset_monster()
        apply_boosts()
    else:
        monster_turn()

def monster_turn():
    global currentMonsterHealth, monsterId, player, persistentStats, endlessMode, endlessKills
    if random.randint(0, 100) < player["dodge"]:
        print(Fore.YELLOW + "You dodged the attack!")
    else:
        print(Fore.YELLOW + f"{currentMonsterFight} attacks!")
        if endlessMode:
            scale = 4 ** endlessKills
            dmg = round(random.uniform(demon_lord_data["minDamage"], demon_lord_data["maxDamage"]) * scale - player["defense"], 2)
        else:
            dmg = round(random.uniform(monster.minDamage[monsterId], monster.maxDamage[monsterId]) - player["defense"], 2)

        dmg = max(1, dmg)
        player["health"] -= dmg
        print(Fore.RED + f"{currentMonsterFight} deals {dmg} damage!")
        time.sleep(0.8)

# Main Functions
def combat():
    global currentMonsterHealth, monsterId, player, persistentStats, endlessMode, endlessKills

    while True:
        show_combat_stats()
        save_to_file()

        # Handle boss prompt if room is at 10 and not already in a boss fight
        if persistentStats["room"] >= 10 and not persistentStats["bossFightReady"]:
            print(Fore.YELLOW + "A powerful presence blocks your path... Boss fight?")
            choice = input(Fore.GREEN + "Do you wish to challenge it? (yes/no) > ").strip().lower()
            if choice in ["yes", "y"]:
                persistentStats["bossFightReady"] = True
            else:
                print(Fore.RED + "You chose to wait. The boss still blocks your progress.")
                persistentStats["room"] = 9
                time.sleep(1.5)
                continue

        choice = input(Fore.BLUE + "What will you do? ").strip().lower()
        print()

        if choice in ["attack", "atk", ""]:
            print(Fore.YELLOW + "You attack!")
            damage = max(1, round(player["damage"] * random.uniform(0.75, 1.25) - currentMonsterDefense, 2))
            currentMonsterHealth -= damage
            print(Fore.RED + f"You dealt {damage} to {currentMonsterFight}.")
            time.sleep(0.2)
            monster_death_check()

        elif choice in ["retreat", "ret"]:
            if persistentStats.get("bossFightReady", False):
                print(Fore.RED + "You cannot retreat from a boss fight!")
                time.sleep(1)
                monster_death_check()
                continue
            print(Fore.YELLOW + "Attempting to retreat...")
            if random.randint(0, 100) < player["escape"]:
                print(Fore.GREEN + "You successfully escaped!")
                reset_monster()
                continue
            else:
                print(Fore.RED + "Retreat failed!")
                monster_turn()

        elif choice in ["level", "lvl"]:
            level_up()

        elif choice in ["inventory", "inv"]:
            show_inventory()

        elif choice in ["minigames", "mini", "games", "min", "other"]:
            minigame_selection()

        elif choice in ["stats", "st"]:
            show_stats_screen()

        elif choice == "exit":
            sys.exit()

        else:
            print(Fore.RED + "Invalid input.")
            time.sleep(0.8)
            continue 

        time.sleep(0.5)

        if player["health"] <= 0:
            print(Fore.RED + "You have died.")
            if endlessMode:
                print(Fore.YELLOW + f"You defeated {endlessKills} Demon Lords!")
            persistentStats["is_dead"] = True
            save_to_file()
            show_stats_screen()  

# Stat up code
def startup():
    global currentSaveName, savedGames, globalSavePath, endlessMode, endlessKills

    clear_screen()
    print(Fore.BLUE + "What is your name? [Type existing name to load or new name to create a save]")
    list_saved_files()

    name_input = input(Fore.GREEN + "\n> ").strip().lower()
    if not name_input.endswith(".json"):
        name_input += ".json"

    currentSaveName = name_input
    globalSavePath = os.path.join(saveDirectory, currentSaveName)

    savedGames = [f for f in os.listdir(saveDirectory) if f.endswith(".json")]

    if currentSaveName in savedGames:
        success = load_from_file(currentSaveName)
        if not success:
            print(Fore.RED + "Failed to load save. Exiting.")
            sys.exit()
        if persistentStats.get("is_dead", False):
            show_stats_screen()
            print(Fore.RED + "\nThis character is dead. You must create a new one.\n")
            sys.exit()
    else:
        print(Fore.YELLOW + f"Creating new save file: {currentSaveName}")

    if currentSaveName not in savedGames:
        print(Fore.YELLOW + "Choose difficulty: Easy / Normal / Hard")
        print(Fore.CYAN + "(Easy gives bonus XP; Hard gives less)")
        choice = input(Fore.GREEN + "> ").strip().lower()

        if choice == "easy":
            player["difficulty"] = 15
        elif choice == "normal":
            player["difficulty"] = 10 
        elif choice == "hard":
            player["difficulty"] = 5
        else:
            player["difficulty"] = 10   # Default to normal

        player["xp"] += player["difficulty"]

    combat()

if __name__ == "__main__":
    startup() 
