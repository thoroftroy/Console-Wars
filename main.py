import random
import time
from colorama import Fore, Back, Style
import os
import sys
import platform
import json
from datetime import datetime
import threading

# Variables
# Player Varibles
class playerVariables:
    name = "placeHolderName"
    baseHealth = 25
    baseDamage = 3.5
    baseDefense = 0
    actionList = ["Attack","Retreat","Level","Inventory","Minigames/Other","Stats","Exit"]
    buyList = ["Health","Damage","Defense","Dodge","Retreat","Drop"]
    gameList = ["Tamagachi","Gambling","Fishing","Wishing Well","Reborn"]
    xp = 5
    coins = 0
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

# Endless mode
endlessMode = False
endlessKills = 0
demonLordBaseStats = {
    "health": monsterVariables.maxHealth[-1],
    "minDamage": monsterVariables.minDamage[-1],
    "maxDamage": monsterVariables.maxDamage[-1],
    "defense": monsterVariables.Defense[-1]
}

# Drop Table
drop_table = [
    {"name": "Iron Sword",         "desc": "A basic blade. Reliable and sharp.",                         "boosts": {"damage": 5},  "weight": 12},
    {"name": "Leather Armor",      "desc": "Worn leather armor that offers minor protection.",           "boosts": {"defense": 2}, "weight": 14},
    {"name": "Amulet of Vigor",    "desc": "An enchanted charm that slightly improves your health.",     "boosts": {"health": 10}, "weight": 12},
    {"name": "Steel Dagger",       "desc": "Short and fast. Hits quicker than most weapons.",            "boosts": {"damage": 3},  "weight": 13},
    {"name": "Chainmail Vest",     "desc": "A sturdy vest of chain links.",                              "boosts": {"defense": 4}, "weight": 10},
    {"name": "Lucky Ring",         "desc": "Makes you more likley to dodge!",                            "boosts": {"dodge": 5}, "weight": 10},
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

# Wishing well
blessings = [
    {"name": "Blessing of Vitality", "desc": "Greatly increases your max health.", "effect": lambda p: setattr(p, 'levelHealthBonus', p.levelHealthBonus + 50)},
    {"name": "Blessing of Power", "desc": "Greatly increases your damage.", "effect": lambda p: setattr(p, 'levelDamageBonus', p.levelDamageBonus + 20)},
    {"name": "Blessing of Fortitude", "desc": "Greatly increases your defense.", "effect": lambda p: setattr(p, 'levelDefenseBonus', p.levelDefenseBonus + 20)},
    {"name": "Powerful Blessing of Vitality", "desc": "Greatly increases your max health.", "effect": lambda p: setattr(p, 'levelHealthBonus', p.levelHealthBonus + 500)},
    {"name": "PowerfulBlessing of Power", "desc": "Greatly increases your damage.", "effect": lambda p: setattr(p, 'levelDamageBonus', p.levelDamageBonus + 200)},
    {"name": "Powerful Blessing of Fortitude", "desc": "Greatly increases your defense.", "effect": lambda p: setattr(p, 'levelDefenseBonus', p.levelDefenseBonus + 200)},
    {"name": "Divine Spark", "desc": "Doubles XP gained from next 5 fights.", "effect": lambda p: persistentStats.update({"divineSpark": persistentStats.get("divineSpark", 0) + 5})},
    {"name": "Gift of Giants", "desc": "Boosts your health by 200.", "effect": lambda p: setattr(p, 'levelHealthBonus', p.levelHealthBonus + 200)},
    {"name": "Fury Unleashed", "desc": "Gain +100 damage instantly.", "effect": lambda p: setattr(p, 'levelDamageBonus', p.levelDamageBonus + 100)},
    {"name": "Iron Will", "desc": "Gain +80 defense.", "effect": lambda p: setattr(p, 'levelDefenseBonus', p.levelDefenseBonus + 80)},
    {"name": "Echo of Titans", "desc": "Grants +300 health.", "effect": lambda p: setattr(p, 'levelHealthBonus', p.levelHealthBonus + 300)},
    {"name": "Blazing Strength", "desc": "You feel unstoppable. +250 damage.", "effect": lambda p: setattr(p, 'levelDamageBonus', p.levelDamageBonus + 250)},
    {"name": "Wall of Ages", "desc": "Ancient defense awakens. +200 defense.", "effect": lambda p: setattr(p, 'levelDefenseBonus', p.levelDefenseBonus + 200)},
    {"name": "Vital Infusion", "desc": "Permanently enhances your life force by 1000.", "effect": lambda p: setattr(p, 'levelHealthBonus', p.levelHealthBonus + 1000)},
    {"name": "Warrior’s Flame", "desc": "You burn with battle energy. +400 damage.", "effect": lambda p: setattr(p, 'levelDamageBonus', p.levelDamageBonus + 400)},
    {"name": "Unbreakable Shell", "desc": "Gain +350 defense.", "effect": lambda p: setattr(p, 'levelDefenseBonus', p.levelDefenseBonus + 350)},
    {"name": "Starlight Boon", "desc": "XP gained is doubled for 10 fights.", "effect": lambda p: persistentStats.update({"divineSpark": persistentStats.get("divineSpark", 0) + 10})},
    {"name": "Overflowing Vitality", "desc": "Gain +2000 health.", "effect": lambda p: setattr(p, 'levelHealthBonus', p.levelHealthBonus + 2000)},
    {"name": "Executioner’s Edge", "desc": "You thirst for combat. +600 damage.", "effect": lambda p: setattr(p, 'levelDamageBonus', p.levelDamageBonus + 600)},
    {"name": "Impenetrable Core", "desc": "Gain +500 defense.", "effect": lambda p: setattr(p, 'levelDefenseBonus', p.levelDefenseBonus + 500)},
    {"name": "Fortune’s Favor", "desc": "Boosts drop chance by 5%.", "effect": lambda p: globals().__setitem__('dropChanceBoostMod', min(0.5, dropChanceBoostMod + 0.05))},
    {"name": "Dodge Mastery", "desc": "Gain +10% dodge chance.", "effect": lambda p: globals().__setitem__('dodgeBoostMod', min(100, dodgeBoostMod + 10))},
    {"name": "Escape Artist", "desc": "Retreat chance +15%.", "effect": lambda p: globals().__setitem__('escapeBoostMod', min(100, escapeBoostMod + 15))},
    {"name": "XP Infusion", "desc": "Gain 1000 XP instantly.", "effect": lambda p: setattr(p, 'xp', p.xp + 1000)},
    {"name": "Coin Cascade", "desc": "Gain 5000 coins.", "effect": lambda p: setattr(p, 'coins', p.coins + 5000)},
    {"name": "Jackpot", "desc": "Gain 50,000 coins.", "effect": lambda p: setattr(p, 'coins', p.coins + 50000)},
    {"name": "Hyper Health", "desc": "Gain +5000 health.", "effect": lambda p: setattr(p, 'levelHealthBonus', p.levelHealthBonus + 5000)},
    {"name": "Overclocked Power", "desc": "+1000 damage instantly.", "effect": lambda p: setattr(p, 'levelDamageBonus', p.levelDamageBonus + 1000)},
    {"name": "Ancient Plate", "desc": "Gain +1000 defense.", "effect": lambda p: setattr(p, 'levelDefenseBonus', p.levelDefenseBonus + 1000)},
    {"name": "Sacred Surge", "desc": "Gain +1500 health and +300 defense.", "effect": lambda p: [setattr(p, 'levelHealthBonus', p.levelHealthBonus + 1500), setattr(p, 'levelDefenseBonus', p.levelDefenseBonus + 300)]},
    {"name": "Storm Rage", "desc": "Gain +1200 damage and +10% dodge.", "effect": lambda p: [setattr(p, 'levelDamageBonus', p.levelDamageBonus + 1200), globals().__setitem__('dodgeBoostMod', min(100, dodgeBoostMod + 10))]},
    {"name": "Radiant Core", "desc": "Full heal to max HP.", "effect": lambda p: globals().__setitem__('currentHealth', maxHealth)},
    {"name": "Essence of Time", "desc": "XP gain is doubled forever.", "effect": lambda p: persistentStats.update({"divineSpark": 99999})},
    {"name": "Bloodlust", "desc": "Gain +1500 damage, but lose 1000 health.", "effect": lambda p: [setattr(p, 'levelDamageBonus', p.levelDamageBonus + 1500), setattr(p, 'levelHealthBonus', max(0, p.levelHealthBonus - 1000))]},
    {"name": "Armor of Fate", "desc": "Gain +1500 defense and 1000 health.", "effect": lambda p: [setattr(p, 'levelDefenseBonus', p.levelDefenseBonus + 1500), setattr(p, 'levelHealthBonus', p.levelHealthBonus + 1000)]},
    {"name": "Wish of Kings", "desc": "Gain 500 XP and 5000 coins.", "effect": lambda p: [setattr(p, 'xp', p.xp + 500), setattr(p, 'coins', p.coins + 5000)]},
    {"name": "Ultimate Form", "desc": "+2000 in most stats.", "effect": lambda p: [setattr(p, 'levelHealthBonus', p.levelHealthBonus + 2000), setattr(p, 'levelDamageBonus', p.levelDamageBonus + 2000), setattr(p, 'levelDefenseBonus', p.levelDefenseBonus + 200)]},
]

curses = [
    {"name": "Curse of Weakness", "desc": "Reduces your damage.", "effect": lambda p: setattr(p, 'levelDamageBonus', max(0, p.levelDamageBonus - 10))},
    {"name": "Curse of Fragility", "desc": "Reduces your health.", "effect": lambda p: setattr(p, 'levelHealthBonus', max(0, p.levelHealthBonus - 30))},
    {"name": "Curse of Vulnerability", "desc": "Reduces your defense.", "effect": lambda p: setattr(p, 'levelDefenseBonus', max(0, p.levelDefenseBonus - 10))},
    {"name": "Hex of Misfortune", "desc": "Drop chance reduced.", "effect": lambda p: globals().__setitem__('dropChanceBoostMod', max(0.01, dropChanceBoostMod - 0.05))},
    {"name": "Curse of Confusion", "desc": "Lose 25% of your XP.", "effect": lambda p: setattr(p, 'xp', max(0, p.xp * 0.75))},
    {"name": "Curse of Loss", "desc": "Lose 50% of your coins.", "effect": lambda p: setattr(p, 'coins', int(p.coins * 0.5))},
    {"name": "Crippling Wound", "desc": "Lose 200 health permanently.", "effect": lambda p: setattr(p, 'levelHealthBonus', max(0, p.levelHealthBonus - 200))},
    {"name": "Crack in Armor", "desc": "Lose 100 defense permanently.", "effect": lambda p: setattr(p, 'levelDefenseBonus', max(0, p.levelDefenseBonus - 100))},
    {"name": "Broken Blade", "desc": "Lose 150 damage permanently.", "effect": lambda p: setattr(p, 'levelDamageBonus', max(0, p.levelDamageBonus - 150))},
    {"name": "Hex of Exhaustion", "desc": "Next 3 XP gains are halved.", "effect": lambda p: persistentStats.update({"divineSpark": -3})},
    {"name": "Weakening Fog", "desc": "Lose 10% health and defense.", "effect": lambda p: [setattr(p, 'levelHealthBonus', max(0, int(p.levelHealthBonus * 0.9))), setattr(p, 'levelDefenseBonus', max(0, int(p.levelDefenseBonus * 0.9)))]},
    {"name": "Sluggish Blood", "desc": "Lose 1000 health instantly.", "effect": lambda p: globals().__setitem__('currentHealth', max(0, currentHealth - 1000))},
    {"name": "Shattered Luck", "desc": "Drop chance reduced by 10%.", "effect": lambda p: globals().__setitem__('dropChanceBoostMod', max(0.01, dropChanceBoostMod - 0.10))},
    {"name": "Doom’s Brand", "desc": "All gains halved for 5 fights.", "effect": lambda p: persistentStats.update({"divineSpark": -5})},
]


# Tamagatchi stuff (why)
tamagatchi_data = {
    "active": False,
    "last_update": None,
    "hunger": 0,
    "bond": 0,
    "boosts": {"health": 0, "damage": 0, "defense": 0}
}

# Stats to keep track of
persistentStats = {
    "monstersKilled": 0,
    "demonLordsDefeated": 0,
    "fishCaught": 0,
    "itemsFished": 0,
    "gamblingBets": 0,
    "gamblingCoinsSpent": 0,
    "gamblingCoinsWon": 0,
    "itemsSold": 0,
    "coinsFromSelling": 0,
    "coinsConvertedToXP": 0,
    "tamagatchiFeeds": 0,
    "wishingCoinsUsed": 0,
    "blessingsReceived": 0,
    "cursesReceived": 0,
    "divineSpark": 0,
    "obtainedBlessings": [],
    "obtainedCurses": [],
    "rebornsUsed": 0,
}


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
baseDodgeBoostMod = 5

currentSaveName = ''
savedGames = []
globalSavePath = ''
saveDirectory = "saves"
os.makedirs(saveDirectory, exist_ok=True)
player = playerVariables()
fishing_active = False
is_dead = False
wishing_well_cost = 1000 

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

# This should flush the input preventing glitches from input buffering
def get_clean_input(prompt=""):
    try:
        time.sleep(0.05)
        print(prompt, end='', flush=True)
        return input()
    except EOFError:
        return ""

#                                       Functions
def show_stats_screen():
    global is_dead
    
    clearScreen()
    print(Style.RESET_ALL)

    # Load from file to see if player is dead
    if os.path.exists(globalSavePath):
        with open(globalSavePath, "r") as f:
            data = json.load(f)
    else:
        data = {}

    #is_dead = data.get("dead", False)
    player_data = data.get("player", {
        "name": player.name,
        "xp": player.xp,
        "coins": player.coins,
        "baseDamage": player.baseDamage,
        "baseDefense": player.baseDefense,
        "levelDamageBonus": player.levelDamageBonus,
        "levelDefenseBonus": player.levelDefenseBonus,
        "inventory": player.inventory
    })
    stats = data.get("persistentStats", persistentStats)
    tama = data.get("tamagatchi", tamagatchi_data)

    if data.get("currentHealth", currentHealth) <= 0:
        print(Fore.RED + "===== PLAYER IS DECEASED =====\n")
    else:
        print(Fore.RED + "===== PLAYER STATISTICS =====\n")

    print(Fore.YELLOW + f"Name: {player_data.get('name', 'Unknown')}")
    print(Fore.CYAN + f"{'Final' if is_dead else 'Current'} Floor: {data.get('currentFloor', currentFloor) * 100:.0f}")
    print(f"XP: {round(player_data.get('xp', player.xp), 1)}  |  Coins: {round(player_data.get('coins', player.coins), 1)}")
    print(f"Health: {round(data.get('maxHealth', maxHealth), 1)}  |  Damage: {round(player_data.get('baseDamage', 0) + player_data.get('levelDamageBonus', 0), 1)}  |  Defense: {round(player_data.get('baseDefense', 0) + player_data.get('levelDefenseBonus', 0), 1)}")
    print(f"Dodge: {round(data.get('dodgeBoostMod', dodgeBoostMod), 1)}%  |  Drop Chance: {round(data.get('dropChanceBoostMod', dropChanceBoostMod) * 100, 1)}%")

    print(f"Reborns Used: {stats.get('rebornsUsed', 0)}")

    print(Fore.MAGENTA + "\n--- Persistent Stats ---")
    print(f"Monsters Killed: {stats.get('monstersKilled', 0)}")
    print(f"Demon Lords Defeated: {stats.get('demonLordsDefeated', 0)}")
    print(f"Fish Caught: {stats.get('fishCaught', 0)}")
    print(f"Items Fished: {stats.get('itemsFished', 0)}")
    print(f"Gambles: {stats.get('gamblingBets', 0)}")
    print(f"Coins Gambled: {stats.get('gamblingCoinsSpent', 0)} | Coins Won: {stats.get('gamblingCoinsWon', 0)}")
    print(f"Items Sold: {stats.get('itemsSold', 0)}  |  Coins from Selling: {stats.get('coinsFromSelling', 0)}")
    print(f"Coins → XP: {stats.get('coinsConvertedToXP', 0)}")
    print(f"Tamagatchi Feeds: {stats.get('tamagatchiFeeds', 0)}")
    
    print(Fore.CYAN + "\n--- Wishing Well ---")
    print(f"Wishes Made: {stats.get('wishingCoinsUsed', 0)}")
    print(f"Blessings Received: {stats.get('blessingsReceived', 0)}")
    print(f"Curses Received: {stats.get('cursesReceived', 0)}")
    print(f"Divine Spark Charges: {stats.get('divineSpark', 0)}")

    print(Fore.GREEN + "\n--- Inventory ---")
    inventory = player_data.get("inventory", [])
    if inventory:
        for item in inventory:
            print(f"- {item['name']} | {item['boosts']}")
    else:
        print("(Empty)")

    print(Fore.CYAN + "\n--- Tamagatchi ---")
    print(f"Active: {tama.get('active', False)}")
    print(f"Hunger: {tama.get('hunger', 0)}")
    print(f"Bond: {tama.get('bond', 0)}")
    print(f"Boosts: {tama.get('boosts', {})}")

    if data.get("currentHealth", currentHealth) <= 0:
        print(Fore.RED + "\nThis player is dead. Exiting...")
        get_clean_input()
        sys.exit()
    else:
        print(Fore.BLUE + "\n(Press Enter to return to combat...)")
        get_clean_input()
        combat()

# The section for being reborn
def reborn():
    global player, currentFloor
    global healthboostCost, damageBoostCost, DefenseBoostCost
    global dodgeBoostCost, escapeBoostCost, dropChanceBoostCost
    clearScreen()

    #if persistentStats["monstersKilled"] < 150:
    #    print(Fore.RED + "You must defeat 150 monsters to unlock Reborn.")
    #    time.sleep(2)
    #    combat()
    #    return

    if currentFloor < 1.70:
        print(Fore.RED + "You must reach floor 170 to use Reborn.")
        time.sleep(2)
        combat()
        return

    print(Fore.YELLOW + "--- Reborn ---")
    print(Fore.CYAN + "This resets you to Floor 0 with all boosts kept.")
    print(Fore.CYAN+"This will reset the price of items in the shop, but not how much they boost your character.")
    print(Fore.CYAN + "You gain 100,000 coins. It costs 1,000 XP to use.")
    print(Fore.CYAN + "You can only do this after reaching Floor 170")
    print(Fore.YELLOW + "\nDo you want to Reborn? (yes/no)")

    choice = get_clean_input().strip().lower()
    if choice in ["yes", "y"]:
        if player.xp < 1000:
            print(Fore.RED + "You don't have enough XP!")
            time.sleep(2)
            combat()
            return
        player.xp -= 1000
        player.coins += 100000
        currentFloor = 0
        persistentStats["rebornsUsed"] += 1
        print(Fore.GREEN + "You are reborn. The climb begins anew!")
        time.sleep(5)
        # Reset shop costs to base values
        healthboostCost = 2
        damageBoostCost = 3
        DefenseBoostCost = 4
        dodgeBoostCost = 5
        escapeBoostCost = 2
        dropChanceBoostCost = 10

        resetMonster()
        combat()
    else:
        print(Fore.YELLOW + "Rebirth canceled.")
        time.sleep(1.5)
        combat()

# Help me god oh please help me
def wishing_well():
    global player, wishing_well_cost

    clearScreen()
    if persistentStats["monstersKilled"] < 100:
        print(Fore.RED + "You must defeat 100 monsters to unlock the Wishing Well.")
        time.sleep(2)
        combat()
        return

    while True:
        clearScreen()
        print(Fore.CYAN + "--- The Wishing Well ---")
        print(Fore.YELLOW + f"Current Wish Cost: {wishing_well_cost} coins        |    Current Coins:",player.coins)
        print(Fore.GREEN + f"Blessings so far: {persistentStats['blessingsReceived']}")
        print(Fore.RED + f"Curses so far: {persistentStats['cursesReceived']}")
        print(Fore.BLUE + f"Wishes made: {persistentStats['wishingCoinsUsed']}")

        print(Fore.MAGENTA + "\nBoosts granted by blessings so far:")
        print(f" +{round(player.levelHealthBonus,1)} Health  |  +{round(player.levelDamageBonus,1)} Damage  |  +{round(player.levelDefenseBonus,1)} Defense")
        print(f"Divine Spark Charges: {persistentStats.get('divineSpark', 0)}")
        print(Fore.YELLOW + "\nType 'y' to wish, or 'exit' to leave.")

        choice = get_clean_input().strip().lower()
        if choice in ["exit", "leave"]:
            combat()
            return
        if choice != "y":
            if len(persistentStats["obtainedBlessings"]) == len(blessings) and len(persistentStats["obtainedCurses"]) == len(curses):
                print(Fore.LIGHTBLACK_EX + "You have received every blessing and curse. You gain some xp instead!")
                pityXp = (wishing_well_cost * 1.2)
                player.xp += pityXp
                print(Fore.GREEN+("You gained",round(pityXp,1)))
                time.sleep(2)
                combat()
                return
            else:
                continue

        if player.coins < wishing_well_cost:
            print(Fore.RED + "Not enough coins.")
            time.sleep(2)
            continue

        player.coins -= wishing_well_cost
        persistentStats["wishingCoinsUsed"] += 1
        wishing_well_cost = int(wishing_well_cost * 1.2)

        roll = random.randint(1, 100)
        if roll <= 55:
            # Blessing
            blessing = random.choice(blessings)
            if blessing["name"] in persistentStats["obtainedBlessings"]:
                print(Fore.YELLOW + f"You already received {blessing['name']}! You get half your coins back.")
                player.coins += wishing_well_cost // 2
            else:
                blessing["effect"](player)
                persistentStats["obtainedBlessings"].append(blessing["name"])
                persistentStats["blessingsReceived"] += 1
                print(Fore.GREEN + f"Blessing: {blessing['name']} → {blessing['desc']}")
        elif roll <= 95:
            # Curse
            curse = random.choice(curses)
            if curse["name"] in persistentStats["obtainedCurses"]:
                print(Fore.YELLOW + f"You already endured {curse['name']}. Refunding half your coins.")
                player.coins += wishing_well_cost // 2
            else:
                curse["effect"](player)
                persistentStats["obtainedCurses"].append(curse["name"])
                persistentStats["cursesReceived"] += 1
                print(Fore.RED + f"Curse: {curse['name']} → {curse['desc']}")
        else:
            # 5% Chance: Divine Spark or Nothing
            if random.random() < 0.5:
                persistentStats["divineSpark"] += 1
                print(Fore.CYAN + "A Divine Spark ignites within you. +1 charge!")
            else:
                print(Fore.LIGHTBLACK_EX + "The well remains silent. Nothing happens.")

        apply_inventory_boosts()
        time.sleep(3)

# LETS GO GAMBLING!!!!!
def get_item_coin_value(item):
    boosts = item.get("boosts", {})
    value = 0
    if boosts:
        for stat, val in boosts.items():
            if stat == "health":
                value += val * 1
            elif stat == "damage":
                value += val * 2
            elif stat == "defense":
                value += val * 1.5
            elif stat == "dodge":
                value += val * 3
    return max(1, int(value))  # always at least 1 coin

def gamble_stat_change(amount):
    roll = random.randint(1, 100)
    if roll <= 10:
        # Lose it all
        return -amount
    elif roll <= 30:
        # Lose half
        return -int(amount * 0.5)
    elif roll <= 50:
        # Small Change
        return int(amount * 0.2)
    elif roll <= 75:
        # Gain 50%
        return int(amount * 0.5)
    elif roll <= 90:
        # Double
        return amount
    else:
        # Triple
        return amount * 2

def gambling():
    global player
    clearScreen()
    print(Style.RESET_ALL)
    print(Fore.YELLOW + "Welcome to the Gambling Den")
    print(Fore.CYAN + f"You have {player.coins} coins.")
    print(Fore.CYAN + f"You have {len(player.inventory)} items in your inventory.")
    print(Fore.BLACK,"|")
    print(Fore.MAGENTA + "\n--- Gamble-Affected Stats (Without Boosts) ---")
    print(Fore.YELLOW + f"Health Bonus: {round(player.levelHealthBonus, 1)}  |  Damage Bonus: {round(player.levelDamageBonus, 1)}  |  Defense Bonus: {round(player.levelDefenseBonus, 1)}")
    print(Fore.LIGHTBLACK_EX + "(These are the actual values affected by gambling.)")
    print(Fore.LIGHTBLACK_EX + "Your *true* stats in combat may be much higher due to items, blessings, and tamagatchi bonuses.")
    print(Fore.BLACK,"|")
    
    if player.coins == 0 and not player.inventory:
        print(Fore.RED + "\nYou have no coins or items to interact with.")
        print(Fore.YELLOW + "Defeat monsters to gain items. Sell them for coins to gamble!")
        print(Fore.RED + "Returning in 5 seconds...")
        time.sleep(5)
        combat()
        return

    print(Fore.GREEN + "\nOptions:")
    print(Fore.GREEN + " [sell]    → Sell inventory items for coins")
    print(Fore.GREEN + " [gamble]  → Bet a custom amount of coins")
    print(Fore.GREEN + " [convert] → Convert 5 coins into 1 XP")
    if currentFloor >= 2.0:
        print(Fore.GREEN + " [highrisk] → Gamble your health, damage, or defense stats")
    else:
        print(Fore.RED + " [highrisk] → (Unlocks at level 200)")
    print(Fore.GREEN + " [leave]   → Exit back to combat")
    print(Fore.BLACK,"|")
    choice = input(Fore.CYAN + "\nYour choice: ").lower().strip()

    if choice == "sell" or choice == "sll":
        if not player.inventory:
            print(Fore.RED + "You have no items to sell.")
        else:
            print(Fore.YELLOW + "Your inventory:")
            for i, item in enumerate(player.inventory):
                value = get_item_coin_value(item)
                print(Fore.CYAN + f"[{i}] {item['name']} → {value} coins")
                print(Fore.MAGENTA + f"     {item['desc']}")

            print(Fore.GREEN + "\nChoose an item number to sell it, or type 'all' to sell everything.")
            sell_choice = input(Fore.CYAN + "Sell choice: ").strip().lower()

            if sell_choice == "all":
                total_value = sum(get_item_coin_value(item) for item in player.inventory)
                player.coins += total_value
                print(Fore.GREEN + f"Sold {len(player.inventory)} items for {total_value} coins.")
                player.inventory.clear()
            elif sell_choice.isdigit():
                idx = int(sell_choice)
                if 0 <= idx < len(player.inventory):
                    item = player.inventory.pop(idx)
                    value = get_item_coin_value(item)
                    player.coins += value
                    print(Fore.GREEN + f"Sold {item['name']} for {value} coins.")
                    persistentStats["coinsFromSelling"] += value
                else:
                    print(Fore.RED + "Invalid item number.")
            else:
                print(Fore.RED + "Invalid input.")
            persistentStats["itemsSold"] += len(player.inventory)
            apply_inventory_boosts()
    elif choice == "gamble" or choice == "gam":
        try:
            amount = int(input(Fore.YELLOW + "Enter the number of coins to bet: ").strip())
            if amount <= 0 or amount > player.coins:
                print(Fore.RED + "Invalid amount.")
            else:
                floor_scale = 1 + (currentFloor * 5)
                multipliers = [0, 0.25, 0.5, 0.75, 1.0, 1.5, 2, 3, 5, 10]
                weights = [15, 20, 18, 15, 10, 8, 6, 5, 2, 1]

                # Boost rewards slightly at higher floors
                scaled_multipliers = [m * floor_scale for m in multipliers]

                result = random.choices(scaled_multipliers, weights=weights, k=1)[0]
                change = int(amount * result)
                player.coins -= amount
                persistentStats["gamblingBets"] += 1
                persistentStats["gamblingCoinsSpent"] += amount
                persistentStats["gamblingCoinsWon"] += max(0, change)
                player.coins += change
                
                if result == 0:
                    print(Fore.RED + f"You lost everything you bet!")
                elif result < 1:
                    print(Fore.YELLOW + f"You lost some coins. You only got {change} back.")
                elif result == 1 * floor_scale:
                    print(Fore.GREEN + "You broke even.")
                else:
                    print(Fore.GREEN + f"You won! Your coins grew to {change} from your bet.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
    elif choice == "convert" or choice == "con":
        if player.coins < 10:
            print(Fore.RED + "You need at least 10 coins to convert to XP.")
        else:
            print(Fore.YELLOW + f"You currently have {player.coins} coins.")
            try:
                amount = int(input(Fore.CYAN + "How many coins would you like to convert (5 coins = 1 xp)? ").strip())
                if amount < 10 or amount > player.coins:
                    print(Fore.RED + "Invalid amount. Must be at least 10 and no more than your current coins.")
                else:
                    xp_gain = round(amount / 5, 2)
                    player.coins -= amount
                    player.xp += xp_gain
                    persistentStats["coinsConvertedToXP"] += amount
                    print(Fore.GREEN + f"Converted {amount} coins into {xp_gain} XP.")
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")
    elif choice == "highrisk" or choice == "risk" or choice == "high" or choice == "high risk":
        if currentFloor < 2.0:
            print(Fore.RED + "You must be level 200+ to use High Risk Gamble.")
        else:
            print(Fore.YELLOW + "Choose a stat to gamble: [health / damage / defense]")
            stat_choice = input().strip().lower()
            abbreviations = {
                "hp": "health",
                "dmg": "damage",
                "def": "defense"
            }
            stat_choice = abbreviations.get(stat_choice, stat_choice)

            if stat_choice not in ["health", "damage", "defense"]:
                print(Fore.RED + "Invalid stat.")
            else:
                try:
                    amount = int(input(Fore.CYAN + f"How many points of {stat_choice} to gamble? ").strip())
                    if amount <= 0 or amount > getattr(player, f"level{stat_choice.capitalize()}Bonus"):
                        print(Fore.RED + "Invalid amount.")
                    else:
                        change = gamble_stat_change(amount)
                        new_total = getattr(player, f"level{stat_choice.capitalize()}Bonus") + change
                        setattr(player, f"level{stat_choice.capitalize()}Bonus", max(0, new_total))
                        print(Fore.MAGENTA + f"{stat_choice.capitalize()} changed by {change}. New total: {max(0, new_total)}")
                except ValueError:
                    print(Fore.RED + "Invalid number.")
    elif choice == "leave" or choice == "exit":
        saveToFile()
        combat()
        return
    else:
        print(Fore.RED + "Invalid choice.")

    time.sleep(2.2)
    gambling()

# Tamagachi stuff
def start_tamagatchi_thread():
    def loop():
        while tamagatchi_data["active"]:
            if tamagatchi_data["last_update"] is not None:
                update_tamagatchi()
            time.sleep(60)  # every minute
    thread = threading.Thread(target=loop, daemon=True)
    thread.start()

def tamagatchi():
    global player
    clearScreen()
    print(Style.RESET_ALL)

    if not tamagatchi_data["active"]:
        if player.xp < 100:
            print(Fore.RED + "You need 100 XP to adopt a Tamagatchi.")
            print(Fore.YELLOW + "Come back when you're ready.")
            time.sleep(3)
            combat()
            return
        player.xp -= 100
        tamagatchi_data["active"] = True
        tamagatchi_data["last_update"] = datetime.now().isoformat()
        tamagatchi_data["hunger"] = 3
        tamagatchi_data["bond"] = 5
        start_tamagatchi_thread()
        print(Fore.YELLOW + "You have adopted a strange glowing creature!")
        print(Fore.RED + "Feed and care for it to earn permanent stat boosts.")
        time.sleep(2)

    while True:
        clearScreen()
        update_tamagatchi()
        print(Fore.CYAN + "\n--- Tamagatchi Status ---")
        print(Fore.MAGENTA + f"Hunger: {tamagatchi_data['hunger']} / 100")
        print(Fore.MAGENTA + f"Bond: {tamagatchi_data['bond']} / 50")
        print(Fore.GREEN + f"Boosts: {tamagatchi_data['boosts']}")
        print(Fore.YELLOW + f"XP: {round(player.xp,1)}")

        if tamagatchi_data["hunger"] <= 5:
            print(Fore.YELLOW + "Your Tamagatchi isn't hungry enough to be fed.")
        else:
            cost = tamagatchi_data["hunger"] * 1.4 * (persistentStats["tamagatchiFeeds"] + 1)
            print(Fore.YELLOW + f"Feeding cost: {round(cost,1)} XP")
        
        print(Fore.CYAN + "\nType 'feed' to feed, or 'exit' to return to combat.")
        choice = get_clean_input().strip().lower()

        if choice in ["exit", "leave"]:
            combat()
            return

        if choice == "feed":
            if tamagatchi_data["hunger"] <= 5:
                print(Fore.YELLOW + "It's not hungry enough to feed.")
            else:
                if player.xp >= cost:
                    tamagatchi_data["hunger"] = max(tamagatchi_data["hunger"] - 4, 0)
                    tamagatchi_data["bond"] = min(tamagatchi_data["bond"] + 1, 20)
                    player.xp -= cost
                    persistentStats["tamagatchiFeeds"] += 1
                    print(Fore.GREEN + "You feed your companion! It looks happier.")
                else:
                    print(Fore.RED + "Not enough XP to feed.")
            time.sleep(1.5)
        else:
            print(Fore.RED + "Invalid command.")
            time.sleep(1.2)

        apply_inventory_boosts()

def update_tamagatchi():
    if not tamagatchi_data["active"] or tamagatchi_data["last_update"] is None:
        return

    last_time = datetime.fromisoformat(tamagatchi_data["last_update"])
    now = datetime.now()
    elapsed = (now - last_time).total_seconds()

    # Hunger increases every once in a while
    hunger_increase = int(elapsed // random.randint(60, 640))
    if hunger_increase > 0:
        tamagatchi_data["hunger"] += hunger_increase
        tamagatchi_data["last_update"] = now.isoformat()

    if tamagatchi_data["hunger"] > 100:
        tamagatchi_data["bond"] = max(0, tamagatchi_data["bond"] - 1)
        tamagatchi_data["hunger"] = 100
    elif tamagatchi_data["hunger"] < 5:
        tamagatchi_data["bond"] += 1

    tamagatchi_data["bond"] = min(tamagatchi_data["bond"], 50)

    # Boosts scale stronger now
    bond = tamagatchi_data["bond"]
    scale = max(1, currentFloor * 10)
    tamagatchi_data["boosts"]["health"] = int(bond * 4 * scale)
    tamagatchi_data["boosts"]["damage"] = int(bond * 2 * scale)
    tamagatchi_data["boosts"]["defense"] = int((bond * 1.1) * scale)

# Fishing stuff
def fishing():
    global fishing_active
    fishing_active = True
    clearScreen()
    print(Style.RESET_ALL)
    print(Fore.CYAN + "You sit quietly by the water and begin fishing...")
    print(Fore.YELLOW + "When a fish goes on the line hit enter quickly to catch it!")
    print(Fore.YELLOW + "Type 'leave' to stop fishing at any time.\n")

    idle_enter_count = 0
    fish_ready = False
    cooldown_until = 0
    fishingPenalty = False
    penalty_end_time = 0

    def fishing_loop():
        nonlocal fish_ready, cooldown_until, fishingPenalty, penalty_end_time
        while fishing_active:
            if fishingPenalty:
                time.sleep(0.5)
                continue
            if time.time() < cooldown_until:
                time.sleep(0.5)
                continue

            wait_time = random.uniform(4, 9)
            print(Fore.BLUE + "Waiting for a bite...")
            time.sleep(wait_time)
            if not fishing_active:
                break

            fish_ready = True
            print(Fore.YELLOW + "\nA fish is on the line! Press Enter quickly!")

            start = time.time()
            response = get_clean_input()
            reaction = time.time() - start

            fish_ready = False

            if reaction > 1.0:
                print(Fore.RED + "Too slow! The fish got away.")
                cooldown_until = time.time() + 3
                continue

            elif fishingPenalty == True:
                print(Fore.RED + "You reacted in time, but you were penalized for spamming. No rewards given.")
            elif fishing_active:
                roll = random.random()
                if roll < 0.8:
                    if currentFloor >= 50:
                        mult = 10 * int(currentFloor * 1000)
                    else:
                        mult = 1
                    scale = 1 + (currentFloor * 10)
                    base_xp = random.uniform(0.5, 5.0)
                    xp_gain = round((base_xp * scale) * mult, 1)
                    player.xp += xp_gain
                    print(Fore.GREEN + f"You caught a fish and gained {xp_gain} XP!")
                    persistentStats["fishCaught"] += 1
                else:
                    weights = [item.get("weight", 1) for item in drop_table]
                    item = random.choices(drop_table, weights=weights, k=1)[0]
                    item_names = [i["name"] for i in player.inventory]
                    if item["name"] in item_names:
                        value = get_item_coin_value(item)
                        player.coins += value
                        print(Fore.MAGENTA + f"You fished up {item['name']} again, but you already own it.")
                        print(Fore.YELLOW + f"It was automatically sold for {value} coins.")
                        persistentStats["itemsSold"] += 1
                        persistentStats["coinsFromSelling"] += value
                    else:
                        player.inventory.append(item)
                        print(Fore.MAGENTA + f"You fished up a rare item: {item['name']}!")
                        print(Fore.YELLOW + item['desc'])
                    persistentStats["itemsFished"] += 1
                    apply_inventory_boosts()

            cooldown_until = time.time() + 3

    thread = threading.Thread(target=fishing_loop, daemon=True)
    thread.start()

    while fishing_active:
        now = time.time()
        if fishingPenalty:
            remaining = int(penalty_end_time - now)
            if remaining <= 0:
                fishingPenalty = False
                print(Fore.GREEN + "Penalty over. You may fish again.")
            else:
                print(Fore.RED + f"Penalty active! Wait {remaining}s.")
            time.sleep(1)
            continue

        cmd = get_clean_input()

        if cmd.strip().lower() in ["leave", "exit"]:
            fishing_active = False
            print(Fore.GREEN + "You reel in your line and return to the fight...")
            time.sleep(1)
            combat()
            return

        if cmd.strip() == "" and not fish_ready:
            idle_enter_count += 1
            if idle_enter_count > 2:
                print(Fore.RED + "You're yanking the reel too much! Your line is tangled.")
                fishingPenalty = True
                penalty_end_time = time.time() + 10
                idle_enter_count = 0
        else:
            idle_enter_count = 0

def minigameSelection():
    global currentHealth,currentDamage,currentDefense,monsterId,currentMonsterFight,currentMonsterHealth,currentMonsterDefense,healthboostCost
    global damageBoostCost,DefenseBoostCost, healthBoostMod, damageBoostMod, defenseBoostMod, dodgeBoostMod, escapeBoostMod, dodgeBoostCost, dodgeBoostCostFactor
    global escapeBoostCost, escapeboostCostFactor, maxHealth, currentFloor, dropChanceBoostMod, dropChanceBoostCost, dropChanceBoostCostFactor, endlessMode, endlessKills
    clearScreen()
    print(Style.RESET_ALL)
    print(Fore.BLACK+"|")
    print(Fore.YELLOW+"Welcome to the Minigame/Other section!")
    print(Fore.BLUE+"  You can complete minigames for boosts to stats or xp!")
    print(Fore.BLACK+"|")
    print(Fore.YELLOW+"Tamagatchi: A friend you feed xp from time to time for stat boosts.")
    print(Fore.YELLOW+"Gambling: Gamble your items and coins into more xp and eventually, massive stat bonuses.")
    print(Fore.YELLOW+"Fishing: Sit down, relax, and fish for xp and items.")
    print(Fore.YELLOW+"Wishing Well: Spend lots of coins (from gambling) to unlock massive stat bonuses, but bewhere, for you may get cursed...")
    print(Fore.YELLOW+"Reborn: Start the game over again with all your stats once you reach a high enough level.")
    print(Fore.BLACK+"|")
    print(Fore.BLUE,player.gameList)
    print(Fore.BLACK+"|")
    print(Fore.BLACK+"|")
    print(Fore.BLACK+"|")
    print(Style.RESET_ALL)
    choice = get_clean_input().lower()
    if choice == "tamagatchi" or choice == "tama":
        tamagatchi()
    elif choice == "gambling" or choice == "gamble" or choice == "gamb":
        gambling()
    elif choice == "fishing" or choice == "fish":
        fishing()
    elif choice == "exit":
        combat()
    elif choice == "wishing well" or choice == "wish" or choice == "wishingwell" or choice == "wsh":
        wishing_well()
    elif choice == "reborn" or choice == "born" or choice == "re":
        reborn()
    else:
        print(Fore.RED+"Invalid input, try again")
        minigameSelection()

def saveToFile():
    global currentMonsterFight, currentMonsterHealth, globalSavePath, monsterId, endlessMode, endlessKills, wishing_well_cost
    save_path = os.path.join(saveDirectory, currentSaveName)
    globalSavePath = save_path

    player.name = os.path.splitext(currentSaveName)[0]
    
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
            "inventory": player.inventory,
            "coins": player.coins,
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
        "firstLaunch": firstLaunch,
        "tamagatchi": tamagatchi_data,
        "persistentStats": persistentStats,
        "wishing_well_cost": wishing_well_cost,
    }

    with open(save_path, "w") as f:
        json.dump(data, f, indent=4)

def listSavedFiles():
    files = os.listdir(saveDirectory)
    json_files = [f for f in files if f.endswith('.json')]
    active_files = []
    dead_files = []

    for file in json_files:
        try:
            with open(os.path.join(saveDirectory, file), 'r') as f:
                data = json.load(f)
                if data.get("dead", False):
                    dead_files.append(file)
                else:
                    active_files.append(file)
        except Exception:
            continue

    print(Fore.BLACK+"|")
    print(Fore.CYAN + "Active Save Files:")
    for f in active_files:
        print("  " + f)
    print(Fore.BLACK+"|")
    print(Fore.RED + "\nDead Save Files:")
    for f in dead_files:
        print("  " + f)
    print(Fore.BLACK+"|")
    print(Fore.WHITE)

def loadFromFile(filename):
    global currentHealth, maxHealth, currentFloor
    global dodgeBoostMod, escapeBoostMod, dropChanceBoostMod
    global healthboostCost, damageBoostCost, DefenseBoostCost
    global dodgeBoostCost, escapeBoostCost, dropChanceBoostCost
    global currentMonsterFight, currentMonsterHealth, monsterId, firstLaunch, endlessMode, endlessKills
    global tamagatchi_data, is_dead, wishing_well_cost

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
        tamagatchi_data = data.get("tamagatchi", tamagatchi_data)
        player.coins = data["player"].get("coins", 0)
        
        wishing_well_cost = data.get("wishing_well_cost", wishing_well_cost)
        
        if "persistentStats" in data:
            persistentStats.update(data["persistentStats"])
            
        is_dead = data.get("dead", False)

        apply_inventory_boosts()
        return data
    except FileNotFoundError:
        print(Fore.RED + "File not found.")
        return None

def try_drop_item():
    global drop_table, dropChanceBoostMod

    if drop_table and random.random() < dropChanceBoostMod:
        weights = [item.get("weight", 1) for item in drop_table]
        item = random.choices(drop_table, weights=weights, k=1)[0]

        # Check for duplicates
        item_names = [i["name"] for i in player.inventory]
        if item["name"] in item_names:
            value = get_item_coin_value(item)
            player.coins += value
            print(Fore.MAGENTA + f"You found: {item['name']} again, but you already own it.")
            print(Fore.YELLOW + f"It was automatically converted into {value} coins.")
        else:
            player.inventory.append(item)
            print(Fore.MAGENTA + f"You found: {item['name']}!")
            print(Fore.YELLOW + item['desc'])

        apply_inventory_boosts()
        time.sleep(0.5)

def apply_inventory_boosts():
    global currentHealth, maxHealth, currentDamage, currentDefense
    global dodgeBoostMod, baseDodgeBoostMod

    # Reset stats to base + level bonuses
    maxHealth = player.baseHealth + player.levelHealthBonus
    currentDamage = player.baseDamage + player.levelDamageBonus
    currentDefense = player.baseDefense + player.levelDefenseBonus

    # Reset dodge to base blessing value
    dodgeBoostMod = baseDodgeBoostMod

    # Apply item bonuses
    for item in player.inventory:
        boosts = item.get("boosts", {})
        maxHealth += boosts.get("health", 0)
        currentDamage += boosts.get("damage", 0)
        currentDefense += boosts.get("defense", 0)
        dodgeBoostMod += boosts.get("dodge", 0)

    # Clamp dodge from items
    if dodgeBoostMod > baseDodgeBoostMod + 20:
        dodgeBoostMod = baseDodgeBoostMod + 20

    # Apply tamagatchi boosts
    update_tamagatchi()
    if tamagatchi_data["active"]:
        maxHealth += tamagatchi_data["boosts"]["health"]
        currentDamage += tamagatchi_data["boosts"]["damage"]
        currentDefense += tamagatchi_data["boosts"]["defense"]

    # Clamp health
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
    global escapeBoostCost, escapeboostCostFactor, maxHealth, currentFloor, dropChanceBoostMod, dropChanceBoostCost, dropChanceBoostCostFactor, endlessMode, endlessKills
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
    choice = get_clean_input().lower()
    combat()

def resetMonster():
    global currentHealth,currentDamage,currentDefense,monsterId,currentMonsterFight,currentMonsterHealth,currentMonsterDefense,healthboostCost
    global damageBoostCost,DefenseBoostCost, healthBoostMod, damageBoostMod, defenseBoostMod, dodgeBoostMod, escapeBoostMod, dodgeBoostCost, dodgeBoostCostFactor
    global escapeBoostCost, escapeboostCostFactor, maxHealth, currentFloor, dropChanceBoostMod, dropChanceBoostCost, dropChanceBoostCostFactor, endlessMode, endlessKills
    global monsterId, currentMonsterFight, currentMonsterHealth, currentMonsterDefense
    if endlessMode:
        monsterId = len(monsterVariables.names) - 1  # Demon Lord index
        currentMonsterFight = "Demon Lord"
        scale = 2 ** endlessKills
        currentMonsterHealth = demonLordBaseStats["health"] * scale
        currentMonsterDefense = demonLordBaseStats["defense"] * scale
    else:
        weights = get_dynamic_weights(currentFloor, len(monsterVariables.names))
        monsterId = random.choices(range(len(monsterVariables.names)), weights=weights, k=1)[0]
        currentMonsterFight = monsterVariables.names[monsterId]
        currentMonsterHealth = monsterVariables.maxHealth[monsterId]
        currentMonsterDefense = monsterVariables.Defense[monsterId]

def showCombatStats():
    global currentHealth,currentDamage,currentDefense,monsterId,currentMonsterFight,currentMonsterHealth,currentMonsterDefense,healthboostCost
    global damageBoostCost,DefenseBoostCost, healthBoostMod, damageBoostMod, defenseBoostMod, dodgeBoostMod, escapeBoostMod, dodgeBoostCost, dodgeBoostCostFactor
    global escapeBoostCost, escapeboostCostFactor, maxHealth, currentFloor, dropChanceBoostMod, dropChanceBoostCost, dropChanceBoostCostFactor, endlessMode, endlessKills
    clearScreen()
    print(Style.RESET_ALL)
    monsterHealthPercentage = round((currentMonsterHealth / monsterVariables.maxHealth[monsterId]) * 100,2)
    print(Fore.WHITE +"You are currently fighting a",currentMonsterFight," ( Difficulty:",round(currentFloor*100),")")
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
    currentHealthPercentage = round((currentHealth / maxHealth) * 100,2)
    print(Fore.GREEN+"Player Stats:")
    print(Fore.GREEN+" Health: ",end='')
    for i in range(round(currentHealthPercentage/2.4)): print(Fore.GREEN +'=',end='')
    print("",currentHealthPercentage,"%  (",round(currentHealth,1),")")
    print(Fore.GREEN +" Damage:",round(currentDamage,1), " |  Defense:",round(currentDefense,1)," |  Xp:",round(player.xp,1))
    print(Fore.GREEN +" Dodge Chance:",dodgeBoostMod,"% |  Retreat Chance:",escapeBoostMod,"%"," |  Item Drop Chance:",round(dropChanceBoostMod*100),"%")
    print(Fore.BLACK +"|")
    if tamagatchi_data["active"]:
        print(Fore.CYAN + f"Tamagatchi → Bond: {tamagatchi_data['bond']} | Hunger: {tamagatchi_data['hunger']} | Boosts: {tamagatchi_data['boosts']}")
        print(Fore.BLACK +"|")
    print(Fore.BLACK +"|")
    print(Fore.BLUE +"Actions:",player.actionList)
    print(Style.RESET_ALL)
    
def levelup():
    global currentHealth,currentDamage,currentDefense,monsterId,currentMonsterFight,currentMonsterHealth,currentMonsterDefense,healthboostCost
    global damageBoostCost,DefenseBoostCost, healthBoostMod, damageBoostMod, defenseBoostMod, dodgeBoostMod, escapeBoostMod, dodgeBoostCost, dodgeBoostCostFactor
    global escapeBoostCost, escapeboostCostFactor, maxHealth, currentFloor, dropChanceBoostMod, dropChanceBoostCost, dropChanceBoostCostFactor, endlessMode, endlessKills
    clearScreen()
    print(Style.RESET_ALL)
    print(Fore.BLACK+"|")
    print(Fore.GREEN+"Ugrade Costs (Current Xp:",round(player.xp,1),")")
    print(Fore.GREEN+" Health Boost:",healthboostCost," |  Damage Boost:",damageBoostCost," |  Defense Boost:",DefenseBoostCost,"\n Dodge Boost:",dodgeBoostCost,"  | Retreat Boost:",escapeBoostCost, " |  Item Drop Boost:",dropChanceBoostCost)
    print(Fore.BLACK+"|")
    print(Fore.BLACK+"|")
    print(Fore.BLUE+"Things you can buy:",player.buyList)
    print(Fore.BLUE+"(Type 'exit' to go back to combat)")
    choice = get_clean_input().lower()
    if choice == "health" or choice == "hlth" or choice == "hp":
        if player.xp >= healthboostCost:
            player.levelHealthBonus += healthBoostMod
            currentHealth = round(healthBoostMod + currentHealth,2)
            if currentHealth >= maxHealth:
                currentHealth = maxHealth
            healthBoostMod = round(healthBoostMod * healthboostCostFactor,1)
            player.xp -= healthboostCost
            currentHealth += round(maxHealth / 4,1)
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
    global escapeBoostCost, escapeboostCostFactor, maxHealth, currentFloor, dropChanceBoostMod, dropChanceBoostCost, dropChanceBoostCostFactor, endlessMode, endlessKills
    dodged = False
    escaped = False
    showCombatStats()
    saveToFile() # Saves the file every turn
    # Player's actions
    choice = get_clean_input().lower()
    if choice == "attack" or choice == "atk" or choice == "":
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
    elif choice == "minigames" or choice == "mini" or choice == "games" or choice == "minigames" or choice == "min" or choice == "other":
        minigameSelection()
    elif choice == "stats" or choice == "st":
        show_stats_screen()
        input(Fore.CYAN + "\n(Press Enter to return to combat...)")
        combat()
        return
    elif choice == "exit":
        sys.exit()
    else:
        print(Fore.RED +"Invalid input")
        time.sleep(0.8)
        combat()
    time.sleep(0.5)
# Section that plays when you beat a monster
    if currentMonsterHealth <= 0:
        if endlessMode:
            endlessKills += 1
            print(Fore.MAGENTA + f"Demon Lord defeated! Total defeated: {endlessKills}")
            persistentStats["demonLordsDefeated"] += 1
            xpGain = round(currentMonsterHealth / 12, 1)
            if xpGain <= 100000000:
                xpGain = 100000000
            player.xp += xpGain
            resetMonster()
            apply_inventory_boosts()
            time.sleep(0.5)
            combat()
        elif currentMonsterFight == "Demon Lord":
            print(Fore.GREEN + "You have defeated the Demon Lord!")
            time.sleep(1)
            print(Fore.RED + "But something stirs... You hear his laughter echoing endlessly...")
            time.sleep(1)
            endlessKills = 1
            endlessMode = True
            resetMonster()
            combat()
        else:
            # regular monster win
            print(Fore.GREEN + "You win!")
            persistentStats["monstersKilled"] += 1
            currentHealth = round(currentHealth + healthBoostMod, 2)
            currentFloor = round(currentFloor + 0.01, 2)
            if currentHealth > maxHealth:
                currentHealth = maxHealth
            try_drop_item()
            
            # Calculate XP with Divine Spark bonus
            xpGain = round(monsterVariables.maxHealth[monsterId] / 12, 1)
            if persistentStats.get("divineSpark", 0) > 0:
                xpGain *= 2
                persistentStats["divineSpark"] -= 1
                print(Fore.YELLOW + f"The Divine Spark doubles your XP to {xpGain}!")
            
            player.xp += xpGain
            
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
            if endlessMode:
                base_min = demonLordBaseStats["minDamage"]
                base_max = demonLordBaseStats["maxDamage"]
                scale = 4 ** endlessKills
                damage = round(random.uniform(base_min, base_max) * scale - currentDefense, 2)
                currentHealth -= damage
            else:
                damage = round(random.uniform(monsterVariables.minDamage[monsterId], monsterVariables.maxDamage[monsterId]) - currentDefense, 2)
                if damage <= 1:
                    damage = 1
                currentHealth = round(currentHealth - damage,2)
                print(Fore.RED+currentMonsterFight,"deals",damage,"damage!")
    # What happens when you die
    if currentHealth <= 0:
        print("You died!")
        if endlessMode:
            print(Fore.YELLOW + f"You defeated {endlessKills} Demon Lords in endless mode!")

        # Save final state as dead
        saveToFile()
        with open(globalSavePath, "r") as f:
            data = json.load(f)
        data["dead"] = True
        with open(globalSavePath, "w") as f:
            json.dump(data, f, indent=4)

        show_stats_screen()
        sys.exit()

    else:
        time.sleep(0.8)
        combat()
    
def main():
    global currentSaveName, savedGames, loadedData, firstLaunch, is_dead
    print(Style.RESET_ALL)
    clearScreen()
    print(Fore.BLUE+"What is your name? [type the name you used previously to load the file]")
    listSavedFiles()
    name_input = get_clean_input().strip().lower()
    
    # Ensure the save file ends with `.json`
    if not name_input.endswith('.json'):
        name_input += '.json'
    
    currentSaveName = name_input
    
    savedGames = os.listdir(saveDirectory)
    savedGames = [f for f in savedGames if f.endswith('.json')]
    
    if currentSaveName in savedGames:
        loadedData = loadFromFile(currentSaveName)
        if is_dead: 
            show_stats_screen()
            print(Fore.RED + "\nThis character is dead. You must create a new one.\n")
            sys.exit()
    else:
        print(Fore.GREEN+f"New save will be created as '{currentSaveName}'.")

    if firstLaunch == True:
        print(Fore.YELLOW+"Chooce difficulty: (Easy or Hard)")
        print(Fore.CYAN+"          (Easy justs boosts your starting xp)")
        choice = get_clean_input().lower()
        if choice == "easy":
            print(Fore.GREEN+"Granting extra xp!")
            player.xp += 15
        else:
            pass
    else:
        pass
    firstLaunch = False
    combat()

if __name__ == "__main__":
    main()
