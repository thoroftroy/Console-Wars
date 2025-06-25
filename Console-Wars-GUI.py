import random
import time
from colorama import Fore, Style
import os
import sys
import platform
import json
from datetime import datetime
import threading
import shutil
from packaging.version import Version
import pygame
import pygame_gui

# Define libraries and classes

# Monster Stuff
class monsterVariables:
    names = ["Rat", "Maggot", "Bat", "Spider", "Ant Swarm", "Beetle", "Moss Imp", "Cave Mite", "Slime", "Goblin",
             "Skeleton", "Zombie", "Wasp Fiend", "Carrion Crow", "Feral Dog", "Bog Rat", "Dustling", "Gremlin", "Gnoll",
             "Lizardman", "Bone Whelp", "Murkstain", "Shade", "Bandit", "Orc", "Warg", "Ghoul", "Drowned One",
             "Banshee", "Dire Wolf", "Witch", "Harpy", "Troll", "Mire Hag", "Ent", "Ogre", "Swamp Horror", "Cave Troll",
             "Wight", "Stone Golem", "Barrow Fiend", "Gnoll Shaman", "Hill Giant", "Brute", "Minotaur",
             "Forest Guardian", "Ice Wraith", "Fire Beetle", "Mud Serpent", "Ravager", "Grave Knight", "Bone Construct",
             "Warlock", "Cursed Beast", "Blood Bat", "Venomfang", "Chimera Cub", "Cave Basilisk", "Corrupted Treant",
             "Stormling", "Vile Sorcerer", "Razorbeak", "Flesh Eater", "Wyrmling", "Lava Golem", "Specter",
             "Flayed Stalker", "Thorn Fiend", "Ash Walker", "Drake", "Frost Giant", "Hell Hound", "Screechling",
             "Bogmire Shambler", "Maggot Queen", "Ironbound", "Shard Serpent", "Darkfang", "Pyre Warden",
             "Ice Revenant", "Blood Mage", "Sunken Horror", "Blackscale", "Manticore", "Vampire", "Runebound Knight",
             "Skull Crawler", "Hexslinger", "Sand Wyrm", "Plague Bearer", "Fungal Horror", "Brimstone Fiend", "Wyrm",
             "Shadow Reaver", "Crystal Guardian", "Hellfire Drake", "Soulstealer", "Twilight Howler", "Arcane Shade",
             "Bone Hydra", "Tempest Djinn", "Doomcaller", "Obsidian Giant", "Iron Tyrant", "Void Spawn", "Behemoth",
             "Abyss Crawler", "Crimson Moth", "Storm Revenant", "Warped Templar", "Nether Hound", "Blackthorn Beast",
             "Sunbreaker", "Rift Warden", "Lich", "Scourge Knight", "Chaos Imp", "Runescarred", "Flame Serpent",
             "Ancient Treant", "Doom Serpent", "Wailing Horror", "Night Gaunt", "Blight Witch", "Crystal Serpent",
             "Ashbound Giant", "Stone Colossus", "Flayer Lord", "Infernal Hound", "Chasm Horror", "Dark Herald",
             "Sky Terror", "Aether Drake", "Vortex Golem", "Witherfang", "Bloodroot Horror", "Ash Tyrant",
             "Gloom Crawler", "Void Knight", "Eclipse Wraith", "Thunder Wyrm", "Lurking Terror", "Frost Revenant",
             "Brine Lord", "Elder Hydra", "Oblivion Fiend", "Arcane Horror", "Nethermancer", "Cursed Juggernaut",
             "Shatter Golem", "Stormcaller", "Venom Hydra", "Phantom King", "Dire Revenant", "Soul Warden",
             "Hollow Knight", "Elder Wyrm", "Abyss Knight", "Crag Behemoth", "Pyre Lord", "Nether Shade",
             "Corruption Spawn", "Ash Wyrm", "Flesh Colossus", "Titanborn", "Wretched Seer", "Blood Wyrm",
             "Skull Titan", "Skybreaker", "Maw Serpent", "Bone Titan", "Flame Reaper", "Frost Tyrant",
             "Iron Juggernaut", "Storm Sovereign", "Oblivion Beast", "Warping Horror", "Celestial Reaver",
             "Flesh Tyrant", "Void Reaver", "Shadow Sovereign", "Titan of Cinders", "Storm Wyrm", "Blackfire Colossus",
             "Abyss Tyrant", "Soul Flayer", "Dread Revenant", "Flesh Reaver", "Elder Horror", "Titan Wraith",
             "Lord of Ruin", "Doom Sovereign", "Nether Titan", "Ember Wyrm", "Shattered Titan", "Cinder Reaver",
             "Ruinborn Horror", "Blood Sovereign", "Demon Lord"]
    maxHealth = [11, 12, 13, 14, 16, 18, 20, 23, 26, 29, 33, 37, 42, 48, 55, 63, 72, 82, 94, 108, 124, 142, 163, 187,
                 215, 247, 284, 326, 374, 430, 494, 568, 653, 750, 862, 991, 1139, 1309, 1505, 1730, 1989, 2287, 2630,
                 3024, 3477, 3998, 4597, 5286, 6078, 6989, 8037, 9242, 10628, 12222, 14055, 16163, 18587, 21375, 24581,
                 28268, 32508, 37384, 42991, 49439, 56854, 65382, 75189, 86467, 99437, 114352, 131504, 151229, 173913,
                 199999, 229998, 264497, 304171, 349796, 402265, 462604, 531994, 611793, 703561, 809095, 930459,
                 1070027, 1230531, 1415110, 1627376, 1871482, 2152204, 2475034, 2846289, 3273232, 3764216, 4328848,
                 4978175, 5724901, 6583636, 7571181, 8706858, 10012886, 11514818, 13242040, 15228345, 17512596,
                 20139485, 23160407, 26634468, 30629638, 35224083, 40507695, 46583849, 53571426, 61607139, 70848209,
                 81475440, 93696756, 107751269, 123913959, 142501052, 163876209, 188457640, 216726285, 249235227,
                 286620511, 329613587, 379055625, 435913968, 501301063, 576496222, 662970655, 762416253, 876778690,
                 1008295493, 1159539816, 1333470788, 1533491406, 1763515116, 2028042383, 2332248740, 2682086051,
                 3084398958, 3547058801, 4079117621, 4690985264, 5394633053, 6203828010, 7134402211, 8204562542,
                 9435246923, 10850533961, 12478114055, 14349831163, 16502305837, 18977651712, 21824299468, 25097944388,
                 28862636046, 33192031452, 38170836169, 43896461594, 50480930833, 58053070457, 66761031025, 76775185678,
                 88291463529, 101535183058, 116765460516, 134280279593, 154422321531, 177585669760, 204223520223,
                 234857048256, 270085605494, 310598446318, 357188213265, 410766445254, 472381412042, 543238623848,
                 624724417425, 718433080038, 826198042043, 950127748349, 1092646910601, 1256543947191, 1445025539269,
                 1661779370159, 1911046275682, 2197703217034, 2527358699589, 2906462504527, 3342431880206,
                 3843796662236, 4420366161571, 5083421085806, 5845934248676, 6722824385977, 7731248043873]
    maxDamage = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 23, 26, 29, 33, 37, 42, 48, 55, 63, 72, 82, 94, 108,
                 124, 142, 163, 187, 215, 247, 284, 326, 374, 430, 494, 568, 653, 750, 862, 991, 1139, 1309, 1505, 1730,
                 1989, 2287, 2630, 3024, 3477, 3998, 4597, 5286, 6078, 6989, 8037, 9242, 10628, 12222, 14055, 16163,
                 18587, 21375, 24581, 28268, 32508, 37384, 42991, 49439, 56854, 65382, 75189, 86467, 99437, 114352,
                 131504, 151229, 173913, 199999, 229998, 264497, 304171, 349796, 402265, 462604, 531994, 611793, 703561,
                 809095, 930459, 1070027, 1230531, 1415110, 1627376, 1871482, 2152204, 2475034, 2846289, 3273232,
                 3764216, 4328848, 4978175, 5724901, 6583636, 7571181, 8706858, 10012886, 11514818, 13242040, 15228345,
                 17512596, 20139485, 23160407, 26634468, 30629638, 35224083, 40507695, 46583849, 53571426, 61607139,
                 70848209, 81475440, 93696756, 107751269, 123913959, 142501052, 163876209, 188457640, 216726285,
                 249235227, 286620511, 329613587, 379055625, 435913968, 501301063, 576496222, 662970655, 762416253,
                 876778690, 1008295493, 1159539816, 1333470788, 1533491406, 1763515116, 2028042383, 2332248740,
                 2682086051, 3084398958, 3547058801, 4079117621, 4690985264, 5394633053, 6203828010, 7134402211,
                 8204562542, 9435246923, 10850533961, 12478114055, 14349831163, 16502305837, 18977651712, 21824299468,
                 25097944388, 28862636046, 33192031452, 38170836169, 43896461594, 50480930833, 58053070457, 66761031025,
                 76775185678, 88291463529, 101535183058, 116765460516, 134280279593, 154422321531, 177585669760,
                 204223520223, 234857048256, 270085605494, 310598446318, 357188213265, 410766445254, 472381412042,
                 543238623848, 624724417425, 718433080038, 826198042043, 950127748349, 1092646910601, 1256543947191,
                 1445025539269, 1661779370159, 1911046275682, 2197703217034, 2527358699589, 2906462504527,
                 3342431880206]
    minDamage = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 23, 26, 29, 33, 37, 42, 48, 55, 63, 72, 82, 94,
                 108, 124, 142, 163, 187, 215, 247, 284, 326, 374, 430, 494, 568, 653, 750, 862, 991, 1139, 1309, 1505,
                 1730, 1989, 2287, 2630, 3024, 3477, 3998, 4597, 5286, 6078, 6989, 8037, 9242, 10628, 12222, 14055,
                 16163, 18587, 21375, 24581, 28268, 32508, 37384, 42991, 49439, 56854, 65382, 75189, 86467, 99437,
                 114352, 131504, 151229, 173913, 199999, 229998, 264497, 304171, 349796, 402265, 462604, 531994, 611793,
                 703561, 809095, 930459, 1070027, 1230531, 1415110, 1627376, 1871482, 2152204, 2475034, 2846289,
                 3273232, 3764216, 4328848, 4978175, 5724901, 6583636, 7571181, 8706858, 10012886, 11514818, 13242040,
                 15228345, 17512596, 20139485, 23160407, 26634468, 30629638, 35224083, 40507695, 46583849, 53571426,
                 61607139, 70848209, 81475440, 93696756, 107751269, 123913959, 142501052, 163876209, 188457640,
                 216726285, 249235227, 286620511, 329613587, 379055625, 435913968, 501301063, 576496222, 662970655,
                 762416253, 876778690, 1008295493, 1159539816, 1333470788, 1533491406, 1763515116, 2028042383,
                 2332248740, 2682086051, 3084398958, 3547058801, 4079117621, 4690985264, 5394633053, 6203828010,
                 7134402211, 8204562542, 9435246923, 10850533961, 12478114055, 14349831163, 16502305837, 18977651712,
                 21824299468, 25097944388, 28862636046, 33192031452, 38170836169, 43896461594, 50480930833, 58053070457,
                 66761031025, 76775185678, 88291463529, 101535183058, 116765460516, 134280279593, 154422321531,
                 177585669760, 204223520223, 234857048256, 270085605494, 310598446318, 357188213265, 410766445254,
                 472381412042, 543238623848, 624724417425, 718433080038, 826198042043, 950127748349, 1092646910601,
                 1256543947191, 1445025539269, 1661779370159, 1911046275682, 2197703217034, 2527358699589]
    defense = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 23, 26, 29, 33, 37, 42, 48, 55, 63, 72, 82,
               94, 108, 124, 142, 163, 187, 215, 247, 284, 326, 374, 430, 494, 568, 653, 750, 862, 991, 1139, 1309,
               1505, 1730, 1989, 2287, 2630, 3024, 3477, 3998, 4597, 5286, 6078, 6989, 8037, 9242, 10628, 12222, 14055,
               16163, 18587, 21375, 24581, 28268, 32508, 37384, 42991, 49439, 56854, 65382, 75189, 86467, 99437, 114352,
               131504, 151229, 173913, 199999, 229998, 264497, 304171, 349796, 402265, 462604, 531994, 611793, 703561,
               809095, 930459, 1070027, 1230531, 1415110, 1627376, 1871482, 2152204, 2475034, 2846289, 3273232, 3764216,
               4328848, 4978175, 5724901, 6583636, 7571181, 8706858, 10012886, 11514818, 13242040, 15228345, 17512596,
               20139485, 23160407, 26634468, 30629638, 35224083, 40507695, 46583849, 53571426, 61607139, 70848209,
               81475440, 93696756, 107751269, 123913959, 142501052, 163876209, 188457640, 216726285, 249235227,
               286620511, 329613587, 379055625, 435913968, 501301063, 576496222, 662970655, 762416253, 876778690,
               1008295493, 1159539816, 1333470788, 1533491406, 1763515116, 2028042383, 2332248740, 2682086051,
               3084398958, 3547058801, 4079117621, 4690985264, 5394633053, 6203828010, 7134402211, 8204562542,
               9435246923, 10850533961, 12478114055, 14349831163, 16502305837, 18977651712, 21824299468, 25097944388,
               28862636046, 33192031452, 38170836169, 43896461594, 50480930833, 58053070457, 66761031025, 76775185678,
               88291463529, 101535183058, 116765460516, 134280279593, 154422321531, 177585669760, 204223520223,
               234857048256, 270085605494, 310598446318, 357188213265, 410766445254, 472381412042, 543238623848,
               624724417425, 718433080038, 826198042043, 950127748349, 1092646910601, 1256543947191, 1445025539269,
               1661779370159, 1911046275682]


monster = monsterVariables()

# The Player Library
player = {
    "name": "placeHolderName",

    "maxHealth": 25.0,
    "health": 25.0,
    "damage": 3.5,
    "defense": 1.0,
    "dodge": 5.0,
    "escape": 50.0,
    "drop": 7.0,

    "difficulty": 0,

    "buyList": ["Health", "Damage", "Defense", "Dodge", "Retreat", "Drop"],
    "gameList": ["Tamagachi", "Gambling", "Fishing", "Gacha", "Wishing Well", "Reborn", "Portal Travel"],

    "xp": 0.0,
    "coins": 0,
    "inventory": [],
    "relics": [],

    "healthBoost": 0,
    "damageBoost": 0,
    "defenseBoost": 0,
    "dodgeBoost": 0,
    "escapeBoost": 0,
    "dropBoost": 0,

    "eye_purchased": False,
    "weighted_dice_purchased": False,
    "monster_bait_purchased": False,
    "dog_house_purchased": False,
    "mirror_pendant_purchased": False,
    "escape_key_purchased": False,
    "reaper's_token_purchased": False,
    "greed's_gullet_purchased": False,
    "soul_mirror_purchased": False,
    "portal_attractor_purchased": False,
    "shield_disruptor_purchased": False,

    "berserkerLevel": 0,

    "kills_sense_reborn": 100,
    "kills_sense_portal": 0,
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
tamagotchi_data = {
    "tamagotchiFeeds": 0,
    "active": False,
    "last_update": None,
    "hunger": 0,
    "bond": 0,
    "boosts": {"health": 0, "damage": 0, "defense": 0},
}

fishing_data = {
    "active": False,
    "fish_caught": 0,
    "items_fished": 0,
}

gambling_data = {
    "gamblingBets": 0,
    "gamblingCoinsSpent": 0,
    "gamblingCoinsWon": 0,
    "itemsSold": 0,
    "coinsFromSelling": 0,
    "coinsConvertedToXP": 0,
    "highRiskStatChange": 0,
}

well_data = {
    "wishing_well_cost": 50000,
    "wishing_coins_used": 0,
    "blessings_received": 0,
    "curses_received": 0,
    "divine_spark": 0,
    "obtained_blessings": [],
    "obtained_curses": [],
}

gacha_data = {
    "gacha_pulls_available": 0,
    "gachas_pulled": 0,
    "xp_earned": 0,
    "characters_owned": [],
    "last_update": time.time(),
    "active": False,
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

    # Single use upgrades
    "eyeFloor": 3,
    "weightedDiceFloor": 25,
    "monsterBaitFloor": 5,
    "dogHouseFloor": 15,
    "mirrorPendantFloor": 45,
    "escapeKeyFloor": 40,
    "reaperTokenFloor": 75,
    "greedGulletFloor": 20,
    "soulMirrorFloor": 25,
    "portalAttractorFloor": 15,
    "shieldDisruptorFloor": 100,

    "berserker1Kills": 500,
    "berserker2Kills": 750,
    "berserker3Kills": 1000,
    "berserker4Kills": 5000,

    "eyeCost": 500,
    "weightedDiceCost": 10500,
    "monsterBaitCost": 500,
    "dogHouseCost": 5000,
    "mirrorPendantCost": 10000,
    "escapeKeyCost": 25000,
    "reaperTokenCost": 150000,
    "greedGulletCost": 5550,
    "soulMirrorCost": 1800,
    "portalAttractorCost": 600,
    "shieldDisruptorCost": 1000000,

    "berserker1Cost": 10000,
    "berserker2Cost": 500000,
    "berserker3Cost": 10000000,
    "berserker4Cost": 100000000,

    # How much the cost goes up each time
    "baseHealthBoostCostFactor": 1.45,
    "baseDamageBoostCostFactor": 1.35,
    "baseDefenseBoostCostFactor": 1.5,
    "baseDodgeBoostCostFactor": 1.8,
    "baseEscapeBoostCostFactor": 1.3,
    "baseDropBoostCostFactor": 1.9,

    # How much each boost gives you each time
    "healthBoostMod": 1.05,
    "damageBoostMod": 1.13,
    "defenseBoostMod": 1.12,
    "dodgeBoostMod": 1.13,
    "escapeBoostMod": 1.5,
    "dropBoostMod": 1.3,

    # 9,223,372,036,854,775,807 is the overflow number, just ensure that number is never exeeded
    "healthBoostCap": 8000000000000000000,
    "damageBoostCap": 8000000000000000000,
    "defenseBoostCap": 8000000000000000000,
    "dodgeBoostCap": 75,
    "escapeBoostCap": 85,
    "dropBoostCap": 35,
}

# Other Stats to keep track of
persistentStats = {
    "floor": 0,
    "room": 0,
    "highest_floor": 0,
    "loop_times": 0,
    "boss_fight_ready": False,
    "monsters_killed": 0,
    "reborns_used": 0,
    "is_dead": False,
    "escapes_used": 0,
    "coins_from_escapes": 0,

    "currentVersion": "Unknown",
}

# Global Variables

# Idle management
last_user_action = time.time()
idle_lock = threading.Lock()

# Startup
startup_grace_period = True

# Monster Variables
monsterId = 0
monsterAttack = 0
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
tamagotchi_thread = None
tamagotchi_stop_event = threading.Event()
gacha_thread = None
gacha_stop_event = threading.Event()

# Drop Table
drop_table = [
    {"name": "Iron Sword", "desc": "A basic blade. Reliable and sharp.", "boosts": {"damage": 5}, "weight": 12},
    {"name": "Leather Armor", "desc": "Worn leather armor that offers minor protection.", "boosts": {"defense": 2},
     "weight": 14},
    {"name": "Amulet of Vigor", "desc": "An enchanted charm that slightly improves your health.",
     "boosts": {"health": 10}, "weight": 12},
    {"name": "Steel Dagger", "desc": "Short and fast. Hits quicker than most weapons.", "boosts": {"damage": 3},
     "weight": 13},
    {"name": "Chainmail Vest", "desc": "A sturdy vest of chain links.", "boosts": {"defense": 4}, "weight": 10},
    {"name": "Lucky Ring", "desc": "Makes you more likely to dodge!", "boosts": {"dodge": 15}, "weight": 7},
    {"name": "Ruby Ring", "desc": "Pulses with energy, strengthening your strikes.", "boosts": {"damage": 7},
     "weight": 8},
    {"name": "Iron Shield", "desc": "Heavy, but it blocks well.", "boosts": {"defense": 5}, "weight": 9},
    {"name": "Pendant of Health", "desc": "Glows with a soft warmth.", "boosts": {"health": 20}, "weight": 8},
    {"name": "War Axe", "desc": "Brutal and unforgiving.", "boosts": {"damage": 9}, "weight": 6},
    {"name": "Plated Boots", "desc": "These boots make you stand strong.", "boosts": {"defense": 3}, "weight": 11},
    {"name": "Gold Locket", "desc": "Gives you a sense of strength from within.", "boosts": {"health": 15},
     "weight": 9},
    {"name": "Enchanted Blade", "desc": "Magical edge hums with power.", "boosts": {"damage": 10}, "weight": 5},
    {"name": "Guardian Cloak", "desc": "It deflects incoming strikes slightly.", "boosts": {"defense": 6}, "weight": 6},
    {"name": "Heartstone", "desc": "A gem filled with life essence.", "boosts": {"health": 25}, "weight": 6},
    {"name": "Spiked Mace", "desc": "Devastating on impact.", "boosts": {"damage": 11}, "weight": 4},
    {"name": "Reinforced Helmet", "desc": "Takes the edge off headshots.", "boosts": {"defense": 4}, "weight": 10},
    {"name": "Elixir Band", "desc": "Increases vitality just by wearing it.", "boosts": {"health": 30}, "weight": 5},
    {"name": "Battle Spear", "desc": "Longer reach and deadly force.", "boosts": {"damage": 12}, "weight": 4},
    {"name": "Dragonhide Vest", "desc": "Tough as ancient scales.", "boosts": {"defense": 7}, "weight": 5},
    {"name": "Phoenix Feather", "desc": "Emits a life-giving aura.", "boosts": {"health": 35}, "weight": 4},
    {"name": "Silver Rapier", "desc": "Elegant and efficient.", "boosts": {"damage": 8}, "weight": 7},
    {"name": "Knight’s Gauntlets", "desc": "Enhances arm protection and grip.", "boosts": {"defense": 5}, "weight": 7},
    {"name": "Talisman of Grace", "desc": "Blessed with ancient healing runes.", "boosts": {"health": 40}, "weight": 3},
    {"name": "Greatsword", "desc": "Two hands. One purpose.", "boosts": {"damage": 14}, "weight": 3},
    {"name": "Stoneplate Armor", "desc": "Like wearing a wall.", "boosts": {"defense": 8}, "weight": 3},
    {"name": "Blood Orb", "desc": "Pulses with crimson power.", "boosts": {"health": 50}, "weight": 2},
    {"name": "Venom Blade", "desc": "Lightweight, but extremely deadly.", "boosts": {"damage": 13}, "weight": 3},
    {"name": "Shield of Valor", "desc": "A legacy of ancient kings.", "boosts": {"defense": 6}, "weight": 6},
    {"name": "Moonstone Charm", "desc": "Gives subtle resilience under pressure.", "boosts": {"health": 22},
     "weight": 8},
    {"name": "Doomhammer", "desc": "Slow but apocalyptic.", "boosts": {"damage": 16}, "weight": 2},
    {"name": "Crown of Eternity", "desc": "Grants unmatched vitality and focus.",
     "boosts": {"health": 100, "defense": 5}, "weight": 1},
    {"name": "Obsidian Crusher", "desc": "Crushes foes with devastating force.", "boosts": {"damage": 25}, "weight": 1},
    {"name": "Celestial Shroud", "desc": "Whispers of protection from beyond.", "boosts": {"defense": 12}, "weight": 1},
    {"name": "Ring of Titans", "desc": "Endless power flows through it.", "boosts": {"damage": 20, "health": 20},
     "weight": 1},
    {"name": "Mantle of Immortals", "desc": "Even death fears its wearer.", "boosts": {"health": 150}, "weight": 1},
    {"name": "Abyssal Fang", "desc": "Bleeds enemies with every strike.", "boosts": {"damage": 22}, "weight": 1},
    {"name": "Plate of Aeons", "desc": "A shield against time itself.", "boosts": {"defense": 15}, "weight": 1},
    {"name": "Void Pendant", "desc": "Grants dark resilience and twisted strength.",
     "boosts": {"health": 80, "damage": 10}, "weight": 1},
    {"name": "Sundering Greatblade", "desc": "No armor can resist it.", "boosts": {"damage": 30}, "weight": 1},
    {"name": "Mythrilheart Armor", "desc": "Impossibly light, indestructible.", "boosts": {"defense": 18, "health": 40},
     "weight": 1},
    {"name": "Scarab Seal", "desc": "Surrounds you in an ethereal shield.", "boosts": {"defense": 10}, "weight": 1},
    {"name": "Runed Circlet", "desc": "Glows with ancient life magic.", "boosts": {"health": 90}, "weight": 1},
    {"name": "Storm Gauntlets", "desc": "Your blows carry thunder.", "boosts": {"damage": 18}, "weight": 1},
    {"name": "Shield of Endings", "desc": "Nullifies even the worst blows.", "boosts": {"defense": 20}, "weight": 1},
    {"name": "Lifeblood Gem", "desc": "Pulses in time with your heart.", "boosts": {"health": 120}, "weight": 1},
    {"name": "Dagger of Stars", "desc": "Swift and unstoppable.", "boosts": {"damage": 15}, "weight": 1},
    {"name": "Solar Medallion", "desc": "Bathes you in burning resilience.", "boosts": {"health": 70, "defense": 8},
     "weight": 1},
    {"name": "Hammer of Glory", "desc": "Swings with divine vengeance.", "boosts": {"damage": 26}, "weight": 1},
    {"name": "Aegis of the Fallen", "desc": "Shields you with lost souls.", "boosts": {"defense": 17}, "weight": 1},
    {"name": "Seraph’s Band", "desc": "Crackles with divine protection.", "boosts": {"health": 60, "defense": 6},
     "weight": 1},
    {"name": "Frostbrand Blade", "desc": "Frozen and furious.", "boosts": {"damage": 24}, "weight": 1},
    {"name": "Warden’s Cuirass", "desc": "Unbending and eternal.", "boosts": {"defense": 14}, "weight": 1},
    {"name": "Eclipse Ring", "desc": "You feel the universe tremble.", "boosts": {"damage": 12, "defense": 6},
     "weight": 1},
    {"name": "Godscale Vest", "desc": "Crafted from myth itself.", "boosts": {"defense": 20}, "weight": 1},
    {"name": "Lifeveil Charm", "desc": "Stitches your wounds instantly.", "boosts": {"health": 110}, "weight": 1},
    {"name": "Hellforge Blade", "desc": "Forged in damnation.", "boosts": {"damage": 28}, "weight": 1},
    {"name": "Divine Anklet", "desc": "You dodge like a shadow.", "boosts": {"defense": 7}, "weight": 1},
    {"name": "Warlock’s Fang", "desc": "Thirsts for blood.", "boosts": {"damage": 23}, "weight": 1},
    {"name": "Tombplate", "desc": "You feel nothing. And take nothing.", "boosts": {"defense": 22}, "weight": 1},
    {"name": "Genesis Relic", "desc": "The beginning of all things.", "boosts": {"health": 200, "damage": 10},
     "weight": 1},
    {"name": "Blade of Oblivion", "desc": "Slices through reality itself.", "boosts": {"damage": 40}, "weight": 0.5},
    {"name": "Titan's Heart", "desc": "Massive vitality from a fallen giant.", "boosts": {"health": 250},
     "weight": 0.5},
    {"name": "Aethercloak", "desc": "Phase through danger unharmed.", "boosts": {"defense": 25}, "weight": 0.5},
    {"name": "Crown of Stars", "desc": "Intelligence beyond comprehension.", "boosts": {"health": 100, "defense": 10},
     "weight": 0.5},
    {"name": "Ruinblade", "desc": "Every swing leaves devastation behind.", "boosts": {"damage": 38}, "weight": 0.5},
    {"name": "Stoneblood Aegis", "desc": "Even gods struggle to crack it.", "boosts": {"defense": 30}, "weight": 0.5},
    {"name": "Crimson Mantle", "desc": "Burns the weak who dare strike you.", "boosts": {"health": 80, "defense": 15},
     "weight": 0.5},
    {"name": "Thunder King's Rod", "desc": "Bolts crackle with each blow.", "boosts": {"damage": 34}, "weight": 0.5},
    {"name": "Godsbane", "desc": "Meant to slay immortals.", "boosts": {"damage": 50}, "weight": 0.25},
    {"name": "Soulforge Mail", "desc": "Made from lost souls and steel.", "boosts": {"defense": 28, "health": 60},
     "weight": 0.5},
    {"name": "Ankh of Resurrection", "desc": "Refuses to let you die easily.", "boosts": {"health": 300},
     "weight": 0.25},
    {"name": "Void Hammer", "desc": "Leaves nothing where it strikes.", "boosts": {"damage": 45}, "weight": 0.25},
    {"name": "Eternal Bulwark", "desc": "Shields passed down by titans.", "boosts": {"defense": 35}, "weight": 0.25},
    {"name": "Helm of the Last King", "desc": "A relic of the age of giants.", "boosts": {"defense": 20, "health": 100},
     "weight": 0.5},
    {"name": "Flametongue Sigil", "desc": "Burns through both body and soul.", "boosts": {"damage": 37}, "weight": 0.5},
    {"name": "Gilded Halo", "desc": "Angelic grace sustains you.", "boosts": {"health": 150}, "weight": 0.5},
    {"name": "Nightmare Edge", "desc": "Fears made manifest in a blade.", "boosts": {"damage": 42}, "weight": 0.25},
    {"name": "Runebound Shell", "desc": "Arcane script reinforces its structure.", "boosts": {"defense": 33},
     "weight": 0.25},
    {"name": "Oathkeeper Ring", "desc": "Binds you to invincible resolve.", "boosts": {"damage": 15, "defense": 15},
     "weight": 0.25},
    {"name": "Eclipse Mantle", "desc": "Draws shadows to protect you.", "boosts": {"defense": 24, "health": 70},
     "weight": 0.25},
    {"name": "Heart of Infinity", "desc": "Pumps endless life into your veins.", "boosts": {"health": 1000},
     "weight": 0.05},
    {"name": "Worldrender Blade", "desc": "Sunder the world with a single swing.", "boosts": {"damage": 500},
     "weight": 0.05},
    {"name": "Aegis of Creation", "desc": "The origin of all protection.", "boosts": {"defense": 300}, "weight": 0.05},
    {"name": "Core of the Cosmos", "desc": "A fragment of the universe itself.",
     "boosts": {"health": 500, "damage": 200, "defense": 150}, "weight": 0.05},
    {"name": "Eternal Warplate", "desc": "Forged from eternity, never fails.", "boosts": {"defense": 500},
     "weight": 0.05},
    {"name": "Annihilation Fang", "desc": "Each strike devours existence.", "boosts": {"damage": 1000}, "weight": 0.05},
    {"name": "Veil of the End", "desc": "Shields its bearer from death itself.",
     "boosts": {"health": 700, "defense": 200}, "weight": 0.05},
    {"name": "Godbreaker", "desc": "Crafted to kill the divine.", "boosts": {"damage": 750}, "weight": 0.05},
    {"name": "Bloodmoon Relic", "desc": "Hungers for endless battle.", "boosts": {"health": 400, "damage": 300},
     "weight": 0.05},
    {"name": "Shield of Eternity", "desc": "No force may breach its guard.", "boosts": {"defense": 600},
     "weight": 0.05},
    {"name": "Infinity Gauntlet", "desc": "I am inevitable", "boosts": {"damage": 1000, "defense": 600},
     "weight": 0.05},
]

# Wishing well buffs and nerfs
blessings = [  # Massive bonuses from the wishing well
    {"name": "Blessing of Vitality", "desc": "Greatly increases your max health. (+500 health)",
     "boosts": {"health": 500}},
    {"name": "Blessing of Power", "desc": "Greatly increases your damage. (+200 damage)", "boosts": {"damage": 200}},
    {"name": "Blessing of Fortitude", "desc": "Greatly increases your defense. (+200 defense)",
     "boosts": {"defense": 200}},
    {"name": "Powerful Blessing of Vitality", "desc": "Massively boosts your max health. (+500 health)",
     "boosts": {"health": 500}},
    {"name": "Powerful Blessing of Power", "desc": "Massively boosts your damage. (+200 damage)",
     "boosts": {"damage": 200}},
    {"name": "Powerful Blessing of Fortitude", "desc": "Massively boosts your defense. (+2000 defense)",
     "boosts": {"defense": 2000}},
    {"name": "Divine Spark", "desc": "Doubles XP gain from next 5 fights. (+5 sparks)", "boosts": {"divine_spark": 5}},
    {"name": "Gift of Giants", "desc": "Grants incredible health. (+200 health)", "boosts": {"health": 200}},
    {"name": "Fury Unleashed", "desc": "Unleashes devastating power. (+100 damage)", "boosts": {"damage": 100}},
    {"name": "Iron Will", "desc": "Bolsters your defenses. (+80 defense)", "boosts": {"defense": 80}},
    {"name": "Echo of Titans", "desc": "A resounding health surge. (+300 health)", "boosts": {"health": 300}},
    {"name": "Blazing Strength", "desc": "Overwhelming might fills you. (+250 damage)", "boosts": {"damage": 250}},
    {"name": "Wall of Ages", "desc": "Your armor thickens with time. (+200 defense)", "boosts": {"defense": 200}},
    {"name": "Vital Infusion", "desc": "Legendary health enhancement. (+1000 health)", "boosts": {"health": 1000}},
    {"name": "Warrior’s Flame", "desc": "Burns with immense power. (+400 damage)", "boosts": {"damage": 400}},
    {"name": "Unbreakable Shell", "desc": "Impenetrable defenses. (+250 defense)", "boosts": {"defense": 350}},
    {"name": "Starlight Boon", "desc": "Double XP for 10 fights. (+10 spark)", "boosts": {"divine_spark": 10}},
    {"name": "Overflowing Vitality", "desc": "Surging health boost. (+20000 health)", "boosts": {"health": 20000}},
    {"name": "Executioner’s Edge", "desc": "Lethal combat precision. (+600 damage)", "boosts": {"damage": 600}},
    {"name": "Impenetrable Core", "desc": "Fortress-like endurance. (+500 defense)", "boosts": {"defense": 500}},
    {"name": "Fortune’s Favor", "desc": "Boosts drop rate. (+5 drop chance)", "boosts": {"drop": 5}},
    {"name": "Dodge Mastery", "desc": "Increased dodge capability. (+10 dodge chance)", "boosts": {"dodge": 10}},
    {"name": "Escape Artist", "desc": "Enhanced retreat chance. (+80 retreat chance)", "boosts": {"escape": 40}},
    {"name": "XP Infusion", "desc": "Gain a large XP boost. (+100000 xp)", "boosts": {"xp": 100000}},
    {"name": "Coin Cascade", "desc": "Gain a surge of wealth. (+5000 coins)", "boosts": {"coins": 5000}},
    {"name": "Jackpot", "desc": "An immense wealth blessing. (+50000 coins)", "boosts": {"coins": 50000}},
    {"name": "Hyper Health", "desc": "Extreme vitality granted. (+50000 health)", "boosts": {"health": 50000}},
    {"name": "Overclocked Power", "desc": "Inhuman strength surge. (+10000 damage)", "boosts": {"damage": 10000}},
    {"name": "Ancient Plate", "desc": "Timeless defense boost. (+10000 defense)", "boosts": {"defense": 10000}},
    {"name": "Sacred Surge", "desc": "Holy boost to health and defense. (+1500 health, +3000 defense)",
     "boosts": {"health": 1500, "defense": 3000}},
    {"name": "Storm Rage", "desc": "Storm-born speed and power. (+1200 damage, +10 dodge chance)",
     "boosts": {"damage": 1200, "dodge": 10}},
    {"name": "Radiant Core", "desc": "Heals you to full.", "boosts": {"heal": "full"}},
    {"name": "Essence of Time", "desc": "XP gain doubled forever. (+99999 spark)", "boosts": {"divine_spark": 99999}},
    {"name": "Bloodlust", "desc": "Massive damage at health cost. (+15000 damage, -1000 health)",
     "boosts": {"damage": 15000, "health": -1000}},
    {"name": "Armor of Fate", "desc": "Boosts defense and health. (+15000, +10000 health)",
     "boosts": {"defense": 15000, "health": 10000}},
    {"name": "Wish of Kings", "desc": "XP and coin surge. (+5000 xp, coins 50000)",
     "boosts": {"xp": 5000, "coins": 50000}},
    {"name": "Ultimate Form", "desc": "Ascend to greatness. (+20000 health, +20000 damage, +2000 defense)",
     "boosts": {"health": 20000, "damage": 20000, "defense": 2000}},
    {"name": "Ultimate Soul", "desc": "Above all else. (+15000 health, +2000 damage, +2000 defense)",
     "boosts": {"health": 15000, "damage": 2000, "defense": 2000}},
    {"name": "Ultimate Hammer",
     "desc": "Let the judgment of god strike. (+1000 health, +20000 damage, +2000 defense)",
     "boosts": {"health": 1000, "damage": 20000, "defense": 2000}},
    {"name": "Op Blessing", "desc": "The best one, makes you overpowered (+1000000 health, damage, and defense)",
     "boosts": {"health": 1000000, "damage": 1000000, "defense": 1000000}},
]
curses = [  # Small rare penalties from the wishing well
    {"name": "Curse of Weakness", "desc": "Your strength fades. (-100 damage)", "boosts": {"damage": -100}},
    {"name": "Curse of Fragility", "desc": "You feel frail. (-300 health)", "boosts": {"health": -300}},
    {"name": "Curse of Vulnerability", "desc": "Your armor fails you (-100 defense).", "boosts": {"defense": -100}},
    {"name": "Hex of Misfortune", "desc": "You lose your edge in luck. (-50 drop chance)", "boosts": {"drop": -50}},
    {"name": "Curse of Confusion", "desc": "Your mind blurs, XP drops. (-25000 xp)", "boosts": {"xp": -25000}},
    {"name": "Curse of Loss", "desc": "You lose some coins. (-50000 coins)", "boosts": {"coins": -50000}},
    {"name": "Crippling Wound", "desc": "You bleed long after the blow. (-2000 health)", "boosts": {"health": -2000}},
    {"name": "Crack in Armor", "desc": "Your defenses fall apart. (-1000 defense)", "boosts": {"defense": -1000}},
    {"name": "Broken Blade", "desc": "Your weapon weakens. (-1500 damage)", "boosts": {"damage": -1500}},
    {"name": "Hex of Exhaustion", "desc": "You feel weary. XP halved. (-30 sparks)", "boosts": {"divine_spark": -30}},
    {"name": "Weakening Fog", "desc": "Your body fades. (-100 health and defense)",
     "boosts": {"health": -100, "defense": -100}},
    {"name": "Sluggish Blood", "desc": "Your lifeforce drains. (-10000 health)", "boosts": {"health": -10000}},
    {"name": "Shattered Luck", "desc": "Fortune slips away. (-100 drop chance)", "boosts": {"drop": -100}},
    {"name": "Doom’s Brand", "desc": "All gains halved temporarily (-50 spark).", "boosts": {"divine_spark": -50}}
]

# Gacha Table
gacha = [  # The gacha characters will passively earn XP over time as they fight for you in other battles
    # Common = 1-4
    # Normal = 5-10
    # Rare = 11-20
    # Super Rare = 21-30
    # Ultra Rare = 31-40
    # MEGA rare = 41-100
    {"name": "Catgirl", "desc": "Why?", "rank": "Common", "boosts": {"xp_bonus": 1}},
    {"name": "Sticky Champion", "desc": "Very sticky...", "rank": "Common", "boosts": {"xp_bonus": 2}},
    {"name": "Funky Snail", "desc": "Screams when idle.", "rank": "Common", "boosts": {"xp_bonus": 3}},
    {"name": "Wandering Ghost", "desc": "Only eats moonlight.", "rank": "Common", "boosts": {"xp_bonus": 4}},
    {"name": "Snoring Ogre", "desc": "Dreams of battle.", "rank": "Common", "boosts": {"xp_bonus": 5}},
    {"name": "Puddle Mage", "desc": "Wields dampness.", "rank": "Common", "boosts": {"xp_bonus": 6}},
    {"name": "Gremlin Cook", "desc": "Secret ingredient: chaos.", "rank": "Common", "boosts": {"xp_bonus": 7}},
    {"name": "Rusty Bot", "desc": "Still operational... mostly.", "rank": "Common", "boosts": {"xp_bonus": 8}},
    {"name": "Melancholy Imp", "desc": "Sighs explosively.", "rank": "Common", "boosts": {"xp_bonus": 9}},
    {"name": "Rock Collector", "desc": "They might be magic.", "rank": "Common", "boosts": {"xp_bonus": 10}},
    {"name": "Lantern Bug", "desc": "Buzzes with energy.", "rank": "Common", "boosts": {"xp_bonus": 11}},
    {"name": "Mushroom Knight", "desc": "Spores of justice.", "rank": "Common", "boosts": {"xp_bonus": 12}},
    {"name": "Sock Thief", "desc": "Where do they go?", "rank": "Common", "boosts": {"xp_bonus": 13}},

    {"name": "Almond Man", "desc": "The king of nuts.", "rank": "Normal", "boosts": {"xp_bonus": 5}},
    {"name": "Fishing Master", "desc": "I like fsh.", "rank": "Normal", "boosts": {"xp_bonus": 6}},
    {"name": "Lesser Demon", "desc": "I'm on your side now.", "rank": "Normal", "boosts": {"xp_bonus": 7}},
    {"name": "Tiny Champion", "desc": "Only eats moonlight.", "rank": "Normal", "boosts": {"xp_bonus": 8}},
    {"name": "Cyber Snail", "desc": "Glows slightly.", "rank": "Normal", "boosts": {"xp_bonus": 9}},
    {"name": "Sticky Ghost", "desc": "Built for hugs.", "rank": "Normal", "boosts": {"xp_bonus": 10}},
    {"name": "Glass Archer", "desc": "Delicate but deadly.", "rank": "Normal", "boosts": {"xp_bonus": 11}},
    {"name": "Moon Dancer", "desc": "Twilight twirls.", "rank": "Normal", "boosts": {"xp_bonus": 12}},
    {"name": "Bored Dragon", "desc": "Yawn and burn.", "rank": "Normal", "boosts": {"xp_bonus": 13}},
    {"name": "Tidy Ogre", "desc": "Neat freak bruiser.", "rank": "Normal", "boosts": {"xp_bonus": 14}},

    {"name": "Jack Black", "desc": "I... Am Steeve.", "rank": "Rare", "boosts": {"xp_bonus": 11}},
    {"name": "Big Red Rock Eater", "desc": "What's big and red and eats rocks?", "rank": "Rare",
     "boosts": {"xp_bonus": 12}},
    {"name": "Sentient Toaster", "desc": "I make vengeance crunchy.", "rank": "Rare", "boosts": {"xp_bonus": 13}},
    {"name": "Quantum Ferret", "desc": "Exists in multiple states of chaos.", "rank": "Rare",
     "boosts": {"xp_bonus": 14}},
    {"name": "Wandering Champion", "desc": "Tastes like victory.", "rank": "Rare", "boosts": {"xp_bonus": 15}},
    {"name": "Rust Lizard", "desc": "Crunchy scales.", "rank": "Rare", "boosts": {"xp_bonus": 16}},
    {"name": "Jelly Oracle", "desc": "Wiggles with wisdom.", "rank": "Rare", "boosts": {"xp_bonus": 17}},
    {"name": "Mimic Pianist", "desc": "Strikes a deadly chord.", "rank": "Rare", "boosts": {"xp_bonus": 18}},
    {"name": "Cyber Fighter", "desc": "The power of CYBER!.", "rank": "Rare", "boosts": {"xp_bonus": 19}},
    {"name": "Sticky Witch", "desc": "Glows slightly.", "rank": "Rare", "boosts": {"xp_bonus": 20}},

    {"name": "Moody Knight", "desc": "Cries in plate armor.", "rank": "Super Rare", "boosts": {"xp_bonus": 21}},
    {"name": "Broccoli Mage", "desc": "Eat your greens or else.", "rank": "Super Rare", "boosts": {"xp_bonus": 22}},
    {"name": "Angry Librarian", "desc": "Shhh... or perish.", "rank": "Super Rare", "boosts": {"xp_bonus": 23}},
    {"name": "Cyberpunk Slug", "desc": "Slow but digitally enhanced.", "rank": "Super Rare",
     "boosts": {"xp_bonus": 24}},
    {"name": "Sticky Champion", "desc": "Prefers chaos.", "rank": "Super Rare", "boosts": {"xp_bonus": 25}},
    {"name": "Funky Snail", "desc": "Tastes like victory.", "rank": "Super Rare", "boosts": {"xp_bonus": 30}},
    {"name": "Wandering Ghost", "desc": "Comes with a manual.", "rank": "Super Rare", "boosts": {"xp_bonus": 35}},
    {"name": "Iron Fighter", "desc": "Smart as a brick.", "rank": "Super Rare", "boosts": {"xp_bonus": 45}},
    {"name": "Tiny Witch", "desc": "Glows slightly.", "rank": "Super Rare", "boosts": {"xp_bonus": 40}},
    {"name": "Cyber Tank", "desc": "Screams when idle.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 50}},

    {"name": "Moss Wizard", "desc": "Photosynthesis and fireballs.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 110}},
    {"name": "Tax Goblin", "desc": "You owe XP this quarter.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 120}},
    {"name": "Haunted Barista", "desc": "Your latte is cursed.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 130}},
    {"name": "Sticky Archer", "desc": "Hates stairs.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 140}},
    {"name": "Funky Mystic", "desc": "Tastes like victory.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 150}},
    {"name": "Wandering Beast", "desc": "Where am I?", "rank": "Ultra Rare", "boosts": {"xp_bonus": 160}},
    {"name": "Iron Agent", "desc": "Only eats moonlight.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 170}},

    {"name": "Banana Paladin", "desc": "He slips... into battle.", "rank": "MEGA Rare", "boosts": {"xp_bonus": 410}},
    {"name": "Bird Lawyer", "desc": "Caws for justice!", "rank": "MEGA Rare", "boosts": {"xp_bonus": 420}},
    {"name": "Bread Prophet", "desc": "Foretells gluten-based doom.", "rank": "MEGA Rare", "boosts": {"xp_bonus": 430}},
    {"name": "Doombot 3000", "desc": "Will explode for fun and profit.", "rank": "MEGA Rare",
     "boosts": {"xp_bonus": 44}},
    {"name": "Teacup Berserker", "desc": "Tiny, angry, porcelain.", "rank": "MEGA Rare", "boosts": {"xp_bonus": 450}},
]

# late game multipliers
relics = [
    {"name": "Relic of the Colossus", "desc": "You grow ever harder to kill.", "boosts": {"mult_health": 2.0},
     "weight": 2},
    {"name": "Relic of Annihilation", "desc": "Your blows echo with godlike wrath.", "boosts": {"mult_damage": 2.5},
     "weight": 2},
    {"name": "Relic of the Aegis", "desc": "You feel no pain.", "boosts": {"mult_defense": 2.5}, "weight": 2},
    {"name": "Relic of the Bloodforged", "desc": "Hurt more. Hurt harder.",
     "boosts": {"mult_damage": 3.0, "mult_health": 0.6}, "weight": 1},
    {"name": "Relic of Immortality", "desc": "You simply don’t die.", "boosts": {"mult_health": 3.0}, "weight": 1},
    {"name": "Relic of the End", "desc": "Every strike ends something.",
     "boosts": {"mult_damage": 2.2, "mult_defense": 0.5}, "weight": 2},
    {"name": "Relic of the Glass Titan", "desc": "Unreal strength, fragile soul.",
     "boosts": {"mult_damage": 3.5, "mult_health": 0.4}, "weight": 1},
    {"name": "Relic of the Unbroken Wall", "desc": "Nothing can pass.", "boosts": {"mult_defense": 3.0}, "weight": 2},
    {"name": "Relic of Twilight", "desc": "Balance between extremes.",
     "boosts": {"mult_health": 1.5, "mult_damage": 1.5, "mult_defense": 1.5}, "weight": 2},
    {"name": "Relic of Mutation", "desc": "Power mutates the flesh.",
     "boosts": {"mult_health": 0.75, "mult_damage": 2.2, "mult_defense": 1.2}, "weight": 2},
    {"name": "Relic of Destiny", "desc": "Your path cannot be denied.",
     "boosts": {"mult_health": 1.3, "mult_damage": 1.3, "mult_defense": 1.3}, "weight": 1},
    {"name": "Relic of the Pale Flame", "desc": "You burn with gentle fury.",
     "boosts": {"mult_damage": 1.8, "mult_defense": 1.1}, "weight": 2},
    {"name": "Relic of Dust", "desc": "Everything falls apart... except you.", "boosts": {"mult_defense": 3.0},
     "weight": 3},
    {"name": "Relic of Suffering", "desc": "Pain is strength.", "boosts": {"mult_damage": 1.5, "mult_health": 0.5},
     "weight": 3},
    {"name": "Relic of the Broken Seal", "desc": "Power... at a cost.",
     "boosts": {"mult_damage": 4.0, "mult_defense": 0.2}, "weight": 0.5},
    {"name": "Relic of Silence", "desc": "You strike before sound.", "boosts": {"mult_damage": 1.6}, "weight": 2},
    {"name": "Relic of the Abysscore", "desc": "The void strengthens you.",
     "boosts": {"mult_health": 1.6, "mult_defense": 1.6}, "weight": 2},
    {"name": "Relic of the Godshell", "desc": "You are a fortress.", "boosts": {"mult_defense": 5.0}, "weight": 0.5},
]

# Initialize pygame
pygame.init()

# Screen
window_size = (1000, 700)
window_surface = pygame.display.set_mode(window_size)
pygame.display.set_caption("Console Wars GUI")

# Manager
manager = pygame_gui.UIManager(window_size)

clock = pygame.time.Clock()
is_running = True


# Build the main UI
button_width = 200
button_height = 50
margin = 10

button_names = [
    "Attack", "Retreat", "Level", "Inventory", "Relics", "Other", "Stats", "Exit"
]

buttons = {}
for i, name in enumerate(button_names):
    buttons[name] = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((30, 30 + i * (button_height + margin)), (button_width, button_height)),
        text=name,
        manager=manager
    )

# Main Loop
while is_running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                button_id = event.ui_element.text
                print(f"[DEBUG] {button_id} button clicked")
                if button_id == "Attack":
                    # Call your combat logic or function
                    pass
                if button_id == "Retreat":
                    pass
                elif button_id == "Exit":
                    is_running = False

        manager.process_events(event)

    manager.update(time_delta)
    window_surface.fill((25, 25, 25))  # Background
    manager.draw_ui(window_surface)

    pygame.display.update()
