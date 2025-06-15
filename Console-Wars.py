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

# Define libraries and classes

# Monster Stuff
class monsterVariables:
    names = ["Rat", "Maggot", "Bat", "Spider", "Ant Swarm", "Beetle", "Moss Imp", "Cave Mite", "Slime", "Goblin", "Skeleton", "Zombie", "Wasp Fiend", "Carrion Crow", "Feral Dog", "Bog Rat", "Dustling", "Gremlin", "Gnoll", "Lizardman", "Bone Whelp", "Murkstain", "Shade", "Bandit", "Orc", "Warg", "Ghoul", "Drowned One", "Banshee", "Dire Wolf", "Witch", "Harpy", "Troll", "Mire Hag", "Ent", "Ogre", "Swamp Horror", "Cave Troll", "Wight", "Stone Golem", "Barrow Fiend", "Gnoll Shaman", "Hill Giant", "Brute", "Minotaur", "Forest Guardian", "Ice Wraith", "Fire Beetle", "Mud Serpent", "Ravager", "Grave Knight", "Bone Construct", "Warlock", "Cursed Beast", "Blood Bat", "Venomfang", "Chimera Cub", "Cave Basilisk", "Corrupted Treant", "Stormling", "Vile Sorcerer", "Razorbeak", "Flesh Eater", "Wyrmling", "Lava Golem", "Specter", "Flayed Stalker", "Thorn Fiend", "Ash Walker", "Drake", "Frost Giant", "Hell Hound", "Screechling", "Bogmire Shambler", "Maggot Queen", "Ironbound", "Shard Serpent", "Darkfang", "Pyre Warden", "Ice Revenant", "Blood Mage", "Sunken Horror", "Blackscale", "Manticore", "Vampire", "Runebound Knight", "Skull Crawler", "Hexslinger", "Sand Wyrm", "Plague Bearer", "Fungal Horror", "Brimstone Fiend", "Wyrm", "Shadow Reaver", "Crystal Guardian", "Hellfire Drake", "Soulstealer", "Twilight Howler", "Arcane Shade", "Bone Hydra", "Tempest Djinn", "Doomcaller", "Obsidian Giant", "Iron Tyrant", "Void Spawn", "Behemoth", "Abyss Crawler", "Crimson Moth", "Storm Revenant", "Warped Templar", "Nether Hound", "Blackthorn Beast", "Sunbreaker", "Rift Warden", "Lich", "Scourge Knight", "Chaos Imp", "Runescarred", "Flame Serpent", "Ancient Treant", "Doom Serpent", "Wailing Horror", "Night Gaunt", "Blight Witch", "Crystal Serpent", "Ashbound Giant", "Stone Colossus", "Flayer Lord", "Infernal Hound", "Chasm Horror", "Dark Herald", "Sky Terror", "Aether Drake", "Vortex Golem", "Witherfang", "Bloodroot Horror", "Ash Tyrant", "Gloom Crawler", "Void Knight", "Eclipse Wraith", "Thunder Wyrm", "Lurking Terror", "Frost Revenant", "Brine Lord", "Elder Hydra", "Oblivion Fiend", "Arcane Horror", "Nethermancer", "Cursed Juggernaut", "Shatter Golem", "Stormcaller", "Venom Hydra", "Phantom King", "Dire Revenant", "Soul Warden", "Hollow Knight", "Elder Wyrm", "Abyss Knight", "Crag Behemoth", "Pyre Lord", "Nether Shade", "Corruption Spawn", "Ash Wyrm", "Flesh Colossus", "Titanborn", "Wretched Seer", "Blood Wyrm", "Skull Titan", "Skybreaker", "Maw Serpent", "Bone Titan", "Flame Reaper", "Frost Tyrant", "Iron Juggernaut", "Storm Sovereign", "Oblivion Beast", "Warping Horror", "Celestial Reaver", "Flesh Tyrant", "Void Reaver", "Shadow Sovereign", "Titan of Cinders", "Storm Wyrm", "Blackfire Colossus", "Abyss Tyrant", "Soul Flayer", "Dread Revenant", "Flesh Reaver", "Elder Horror", "Titan Wraith", "Lord of Ruin", "Doom Sovereign", "Nether Titan", "Ember Wyrm", "Shattered Titan", "Cinder Reaver", "Ruinborn Horror", "Blood Sovereign", "Demon Lord"]
    maxHealth = [11, 12, 13, 14, 16, 18, 20, 23, 26, 29, 33, 37, 42, 48, 55, 63, 72, 82, 94, 108, 124, 142, 163, 187, 215, 247, 284, 326, 374, 430, 494, 568, 653, 750, 862, 991, 1139, 1309, 1505, 1730, 1989, 2287, 2630, 3024, 3477, 3998, 4597, 5286, 6078, 6989, 8037, 9242, 10628, 12222, 14055, 16163, 18587, 21375, 24581, 28268, 32508, 37384, 42991, 49439, 56854, 65382, 75189, 86467, 99437, 114352, 131504, 151229, 173913, 199999, 229998, 264497, 304171, 349796, 402265, 462604, 531994, 611793, 703561, 809095, 930459, 1070027, 1230531, 1415110, 1627376, 1871482, 2152204, 2475034, 2846289, 3273232, 3764216, 4328848, 4978175, 5724901, 6583636, 7571181, 8706858, 10012886, 11514818, 13242040, 15228345, 17512596, 20139485, 23160407, 26634468, 30629638, 35224083, 40507695, 46583849, 53571426, 61607139, 70848209, 81475440, 93696756, 107751269, 123913959, 142501052, 163876209, 188457640, 216726285, 249235227, 286620511, 329613587, 379055625, 435913968, 501301063, 576496222, 662970655, 762416253, 876778690, 1008295493, 1159539816, 1333470788, 1533491406, 1763515116, 2028042383, 2332248740, 2682086051, 3084398958, 3547058801, 4079117621, 4690985264, 5394633053, 6203828010, 7134402211, 8204562542, 9435246923, 10850533961, 12478114055, 14349831163, 16502305837, 18977651712, 21824299468, 25097944388, 28862636046, 33192031452, 38170836169, 43896461594, 50480930833, 58053070457, 66761031025, 76775185678, 88291463529, 101535183058, 116765460516, 134280279593, 154422321531, 177585669760, 204223520223, 234857048256, 270085605494, 310598446318, 357188213265, 410766445254, 472381412042, 543238623848, 624724417425, 718433080038, 826198042043, 950127748349, 1092646910601, 1256543947191, 1445025539269, 1661779370159, 1911046275682, 2197703217034, 2527358699589, 2906462504527, 3342431880206, 3843796662236, 4420366161571, 5083421085806, 5845934248676, 6722824385977, 7731248043873]
    maxDamage = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 23, 26, 29, 33, 37, 42, 48, 55, 63, 72, 82, 94, 108, 124, 142, 163, 187, 215, 247, 284, 326, 374, 430, 494, 568, 653, 750, 862, 991, 1139, 1309, 1505, 1730, 1989, 2287, 2630, 3024, 3477, 3998, 4597, 5286, 6078, 6989, 8037, 9242, 10628, 12222, 14055, 16163, 18587, 21375, 24581, 28268, 32508, 37384, 42991, 49439, 56854, 65382, 75189, 86467, 99437, 114352, 131504, 151229, 173913, 199999, 229998, 264497, 304171, 349796, 402265, 462604, 531994, 611793, 703561, 809095, 930459, 1070027, 1230531, 1415110, 1627376, 1871482, 2152204, 2475034, 2846289, 3273232, 3764216, 4328848, 4978175, 5724901, 6583636, 7571181, 8706858, 10012886, 11514818, 13242040, 15228345, 17512596, 20139485, 23160407, 26634468, 30629638, 35224083, 40507695, 46583849, 53571426, 61607139, 70848209, 81475440, 93696756, 107751269, 123913959, 142501052, 163876209, 188457640, 216726285, 249235227, 286620511, 329613587, 379055625, 435913968, 501301063, 576496222, 662970655, 762416253, 876778690, 1008295493, 1159539816, 1333470788, 1533491406, 1763515116, 2028042383, 2332248740, 2682086051, 3084398958, 3547058801, 4079117621, 4690985264, 5394633053, 6203828010, 7134402211, 8204562542, 9435246923, 10850533961, 12478114055, 14349831163, 16502305837, 18977651712, 21824299468, 25097944388, 28862636046, 33192031452, 38170836169, 43896461594, 50480930833, 58053070457, 66761031025, 76775185678, 88291463529, 101535183058, 116765460516, 134280279593, 154422321531, 177585669760, 204223520223, 234857048256, 270085605494, 310598446318, 357188213265, 410766445254, 472381412042, 543238623848, 624724417425, 718433080038, 826198042043, 950127748349, 1092646910601, 1256543947191, 1445025539269, 1661779370159, 1911046275682, 2197703217034, 2527358699589, 2906462504527, 3342431880206]
    minDamage = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 23, 26, 29, 33, 37, 42, 48, 55, 63, 72, 82, 94, 108, 124, 142, 163, 187, 215, 247, 284, 326, 374, 430, 494, 568, 653, 750, 862, 991, 1139, 1309, 1505, 1730, 1989, 2287, 2630, 3024, 3477, 3998, 4597, 5286, 6078, 6989, 8037, 9242, 10628, 12222, 14055, 16163, 18587, 21375, 24581, 28268, 32508, 37384, 42991, 49439, 56854, 65382, 75189, 86467, 99437, 114352, 131504, 151229, 173913, 199999, 229998, 264497, 304171, 349796, 402265, 462604, 531994, 611793, 703561, 809095, 930459, 1070027, 1230531, 1415110, 1627376, 1871482, 2152204, 2475034, 2846289, 3273232, 3764216, 4328848, 4978175, 5724901, 6583636, 7571181, 8706858, 10012886, 11514818, 13242040, 15228345, 17512596, 20139485, 23160407, 26634468, 30629638, 35224083, 40507695, 46583849, 53571426, 61607139, 70848209, 81475440, 93696756, 107751269, 123913959, 142501052, 163876209, 188457640, 216726285, 249235227, 286620511, 329613587, 379055625, 435913968, 501301063, 576496222, 662970655, 762416253, 876778690, 1008295493, 1159539816, 1333470788, 1533491406, 1763515116, 2028042383, 2332248740, 2682086051, 3084398958, 3547058801, 4079117621, 4690985264, 5394633053, 6203828010, 7134402211, 8204562542, 9435246923, 10850533961, 12478114055, 14349831163, 16502305837, 18977651712, 21824299468, 25097944388, 28862636046, 33192031452, 38170836169, 43896461594, 50480930833, 58053070457, 66761031025, 76775185678, 88291463529, 101535183058, 116765460516, 134280279593, 154422321531, 177585669760, 204223520223, 234857048256, 270085605494, 310598446318, 357188213265, 410766445254, 472381412042, 543238623848, 624724417425, 718433080038, 826198042043, 950127748349, 1092646910601, 1256543947191, 1445025539269, 1661779370159, 1911046275682, 2197703217034, 2527358699589]
    defense =   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 23, 26, 29, 33, 37, 42, 48, 55, 63, 72, 82, 94, 108, 124, 142, 163, 187, 215, 247, 284, 326, 374, 430, 494, 568, 653, 750, 862, 991, 1139, 1309, 1505, 1730, 1989, 2287, 2630, 3024, 3477, 3998, 4597, 5286, 6078, 6989, 8037, 9242, 10628, 12222, 14055, 16163, 18587, 21375, 24581, 28268, 32508, 37384, 42991, 49439, 56854, 65382, 75189, 86467, 99437, 114352, 131504, 151229, 173913, 199999, 229998, 264497, 304171, 349796, 402265, 462604, 531994, 611793, 703561, 809095, 930459, 1070027, 1230531, 1415110, 1627376, 1871482, 2152204, 2475034, 2846289, 3273232, 3764216, 4328848, 4978175, 5724901, 6583636, 7571181, 8706858, 10012886, 11514818, 13242040, 15228345, 17512596, 20139485, 23160407, 26634468, 30629638, 35224083, 40507695, 46583849, 53571426, 61607139, 70848209, 81475440, 93696756, 107751269, 123913959, 142501052, 163876209, 188457640, 216726285, 249235227, 286620511, 329613587, 379055625, 435913968, 501301063, 576496222, 662970655, 762416253, 876778690, 1008295493, 1159539816, 1333470788, 1533491406, 1763515116, 2028042383, 2332248740, 2682086051, 3084398958, 3547058801, 4079117621, 4690985264, 5394633053, 6203828010, 7134402211, 8204562542, 9435246923, 10850533961, 12478114055, 14349831163, 16502305837, 18977651712, 21824299468, 25097944388, 28862636046, 33192031452, 38170836169, 43896461594, 50480930833, 58053070457, 66761031025, 76775185678, 88291463529, 101535183058, 116765460516, 134280279593, 154422321531, 177585669760, 204223520223, 234857048256, 270085605494, 310598446318, 357188213265, 410766445254, 472381412042, 543238623848, 624724417425, 718433080038, 826198042043, 950127748349, 1092646910601, 1256543947191, 1445025539269, 1661779370159, 1911046275682]

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

    "actionList": ["Attack", "Retreat", "Level", "Inventory", "Minigames/Other", "Stats", "Exit"],
    "buyList": ["Health", "Damage", "Defense", "Dodge", "Retreat", "Drop"],
    "gameList": ["Tamagachi", "Gambling", "Fishing", "Gatcha", "Wishing Well", "Reborn", "Portal Travel"],

    "xp": 0.0,
    "coins": 0,
    "inventory": [],

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
    
    "kills_sense_reborn": 0,
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

gatcha_data = {
    "gatcha_pulls_available": 0,
    "gatchas_pulled": 0,
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
    "soulMirrorFloor": 30,
    "portalAttractorFloor": 15,
    
    "eyeCost": 500,
    "weightedDiceCost": 10500,
    "monsterBaitCost": 500,
    "dogHouseCost": 5000,
    "mirrorPendantCost": 10000,
    "escapeKeyCost": 25000,
    "reaperTokenCost": 150000,
    "greedGulletCost": 5550,
    "soulMirrorCost": 18000,
    "portalAttractorCost": 600,

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
    "escapeBoostCap": 99,
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
tamagatchi_thread = None
tamagatchi_stop_event = threading.Event()
gatcha_thread = None
gatcha_stop_event = threading.Event()

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
    {"name": "Ultimate Form", "desc": "Ascend to greatness. (+200000 health, +200000 damage, +20000 defense)",
     "boosts": {"health": 200000, "damage": 200000, "defense": 20000}},
    {"name": "Ultimate Soul", "desc": "Above all else. (+1500000 health, +2000 damage, +2000 defense)",
     "boosts": {"health": 1500000, "damage": 2000, "defense": 2000}},
    {"name": "Ultimate Hammer",
     "desc": "Let the judgment of god strike. (+1000 health, +200000 damage, +20000 defense)",
     "boosts": {"health": 1000, "damage": 200000, "defense": 20000}},
    {"name": "Op Blessing", "desc": "The best one, makes you overpowered (+10000000 health, damage, and defense)",
     "boosts": {"health": 10000000, "damage": 10000000, "defense": 10000000}},
]
curses = [  # Small rare penalties from the wishing well
    {"name": "Curse of Weakness", "desc": "Your strength fades. (-10 damage)", "boosts": {"damage": -10}},
    {"name": "Curse of Fragility", "desc": "You feel frail. (-30 health)", "boosts": {"health": -30}},
    {"name": "Curse of Vulnerability", "desc": "Your armor fails you (-10 defense).", "boosts": {"defense": -10}},
    {"name": "Hex of Misfortune", "desc": "You lose your edge in luck. (-5 drop chance)", "boosts": {"drop": -5}},
    {"name": "Curse of Confusion", "desc": "Your mind blurs, XP drops. (-2500 xp)", "boosts": {"xp": -2500}},
    {"name": "Curse of Loss", "desc": "You lose some coins. (-500 coins)", "boosts": {"coins": -500}},
    {"name": "Crippling Wound", "desc": "You bleed long after the blow. (-200 health)", "boosts": {"health": -200}},
    {"name": "Crack in Armor", "desc": "Your defenses fall apart. (-100 defense)", "boosts": {"defense": -100}},
    {"name": "Broken Blade", "desc": "Your weapon weakens. (-150 damage)", "boosts": {"damage": -150}},
    {"name": "Hex of Exhaustion", "desc": "You feel weary. XP halved. (-3 sparks)", "boosts": {"divine_spark": -3}},
    {"name": "Weakening Fog", "desc": "Your body fades. (-10 health and defense)",
     "boosts": {"health": -10, "defense": -10}},
    {"name": "Sluggish Blood", "desc": "Your lifeforce drains. (-1000 health)", "boosts": {"health": -1000}},
    {"name": "Shattered Luck", "desc": "Fortune slips away. (-10 drop chance)", "boosts": {"drop": -10}},
    {"name": "Doom’s Brand", "desc": "All gains halved temporarily (-5 spark).", "boosts": {"divine_spark": -5}}
]

# Gatcha Table
gatcha = [  # The gatcha characters will passively earn XP over time as they fight for you in other battles
    # Common = 1-4
    # Normal = 5-10
    # Rare = 11-20
    # Super Rare = 21-30
    # Ultra Rare = 31-40
    # MEGA rare = 41-100
    {"name": "Catgirl", "desc": "Why?", "rank": "Common", "boosts": {"xp_bonus": 1}},
    {"name": "Sticky Champion", "desc": "Built for hugs.", "rank": "Common", "boosts": {"xp_bonus": 2}},
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
    {"name": "Cyber Fighter", "desc": "Built for hugs.", "rank": "Rare", "boosts": {"xp_bonus": 19}},
    {"name": "Sticky Witch", "desc": "Glows slightly.", "rank": "Rare", "boosts": {"xp_bonus": 20}},

    {"name": "Moody Knight", "desc": "Cries in plate armor.", "rank": "Super Rare", "boosts": {"xp_bonus": 21}},
    {"name": "Broccoli Mage", "desc": "Eat your greens or else.", "rank": "Super Rare", "boosts": {"xp_bonus": 22}},
    {"name": "Angry Librarian", "desc": "Shhh... or perish.", "rank": "Super Rare", "boosts": {"xp_bonus": 23}},
    {"name": "Cyberpunk Slug", "desc": "Slow but digitally enhanced.", "rank": "Super Rare",
     "boosts": {"xp_bonus": 24}},
    {"name": "Sticky Champion", "desc": "Prefers chaos.", "rank": "Super Rare", "boosts": {"xp_bonus": 25}},
    {"name": "Funky Snail", "desc": "Tastes like victory.", "rank": "Super Rare", "boosts": {"xp_bonus": 30}},
    {"name": "Wandering Ghost", "desc": "Comes with a manual.", "rank": "Super Rare", "boosts": {"xp_bonus": 35}},
    {"name": "Iron Fighter", "desc": "Built for hugs.", "rank": "Super Rare", "boosts": {"xp_bonus": 45}},
    {"name": "Tiny Witch", "desc": "Glows slightly.", "rank": "Super Rare", "boosts": {"xp_bonus": 40}},
    {"name": "Cyber Tank", "desc": "Screams when idle.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 50}},

    {"name": "Moss Wizard", "desc": "Photosynthesis and fireballs.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 110}},
    {"name": "Tax Goblin", "desc": "You owe XP this quarter.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 120}},
    {"name": "Haunted Barista", "desc": "Your latte is cursed.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 130}},
    {"name": "Sticky Archer", "desc": "Hates stairs.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 140}},
    {"name": "Funky Mystic", "desc": "Tastes like victory.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 150}},
    {"name": "Wandering Beast", "desc": "Built for hugs.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 160}},
    {"name": "Iron Agent", "desc": "Only eats moonlight.", "rank": "Ultra Rare", "boosts": {"xp_bonus": 170}},

    {"name": "Banana Paladin", "desc": "He slips... into battle.", "rank": "MEGA Rare", "boosts": {"xp_bonus": 410}},
    {"name": "Bird Lawyer", "desc": "Caws for justice!", "rank": "MEGA Rare", "boosts": {"xp_bonus": 420}},
    {"name": "Bread Prophet", "desc": "Foretells gluten-based doom.", "rank": "MEGA Rare", "boosts": {"xp_bonus": 430}},
    {"name": "Doombot 3000", "desc": "Will explode for fun and profit.", "rank": "MEGA Rare",
     "boosts": {"xp_bonus": 44}},
    {"name": "Teacup Berserker", "desc": "Tiny, angry, porcelain.", "rank": "MEGA Rare", "boosts": {"xp_bonus": 450}},
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

def update_last_action():
    with idle_lock:
        global last_user_action
        last_user_action = time.time()

# Define the current os and clear screen properly
def clear_screen():
    print(Style.RESET_ALL)
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

# Idle Checker functions
def idle_checker_thread():
    global last_user_action
    IDLE_TIMEOUT = 120 # The number of seconds before a timeout
    while True:
        time.sleep(1)
        with idle_lock:
            if time.time() - last_user_action >= IDLE_TIMEOUT:
                save_to_file()
                print(Fore.BLACK + "|")
                print(Fore.RED + "\nYou have been idle for too long!")
                print(Fore.GREEN + "Saving game...\n" + Fore.RED + "Exiting...")
                time.sleep(0.1)
                print(Style.RESET_ALL)
                os._exit(0) # Should exit the entire program

# Grace period timer: During the start of the program don't allow the tamagatchi or the gatcha to do anything
def grace_period_timer():
    global startup_grace_period
    time.sleep(30)
    startup_grace_period = False

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

    print(Fore.RED + (
        "===== PLAYER IS DECEASED =====\n" if stats.get("is_dead", False) else "===== PLAYER STATISTICS =====\n"))

    print(Fore.YELLOW + f"Name: {player_data.get('name', 'Unknown')}  |  Difficulty: {player['difficulty']}")
    print(Fore.GREEN + f"Current Floor: {stats.get('floor', 0)}.{stats.get('room', 0)}")
    print(f"XP: {round(player_data.get('xp', 0), 1)}  |  Coins: {round(player_data.get('coins', 0), 1)}")
    print(
        f"Max Health: {round(player_data.get('maxHealth', 0), 1)}  |  Damage: {round(player_data.get('damage', 0), 1)}  |  Defense: {round(player_data.get('defense', 0), 1)}")
    print(
        f"Dodge Chance: {round(player_data.get('dodge', 0), 1)}%  |  Retreat Chance: {round(player_data.get('escape', 0), 1)}%  |  Drop Chance: {round(player_data.get('drop', 0), 1)}%")
    print(f"Reborns Used: {stats.get('reborns_used', 0)}  |  Highest Floor Reached: {persistentStats['highest_floor']}")

    print(Fore.MAGENTA + "\n--- Combat Stats ---")
    print(f"Monsters Killed: {stats.get('monsters_killed', 0)}")
    print(f"Demon Lords Defeated: {demon_lord_data.get('demonLordsDefeated', 0)}")
    print(f"Times Escaped: {persistentStats['escapes_used']}  |  Coins Looted: {persistentStats['coins_from_escapes']}")

    print(Fore.MAGENTA + "\n--- Permanent Upgrades ---")
    print(f"Hackers Eye: {player['eye_purchased']}  |  Weight Dice: {player['weighted_dice_purchased']}")
    print(f"Monster Bait: {player['monster_bait_purchased']}  |  Dog(?) House: {player['dog_house_purchased']}")
    print(f"Mirror Pendant: {player['mirror_pendant_purchased']}  |  Escape Key: {player['escape_key_purchased']}")
    print(f"Reaper's Token: {player["reaper's_token_purchased"]}  |  Greed's Gullet: {player["greed's_gullet_purchased"]}")
    print(f"Soul Mirror: {player['soul_mirror_purchased']}")

    print(Fore.CYAN + "\n--- Gambling Stats ---")
    print(f"Gambles: {gambling_data.get('gamblingBets', 0)}")
    print(
        f"Coins Gambled: {gambling_data.get('gamblingCoinsSpent', 0)} | Coins Won: {gambling_data.get('gamblingCoinsWon', 0)}")
    print(
        f"Items Sold: {gambling_data.get('itemsSold', 0)} | Coins from Selling: {gambling_data.get('coinsFromSelling', 0)}")
    print(f"Coins Converted to XP: {gambling_data.get('coinsConvertedToXP', 0)}")

    print(Fore.CYAN + "\n--- Fishing ---")
    print(f"Fish Caught: {fishing_data.get('fish_caught', 0)} | Items Fished: {fishing_data.get('items_fished', 0)}")

    print(Fore.CYAN + "\n--- Tamagatchi ---")
    print(f"Active: {tama.get('active', False)} | Hunger: {tama.get('hunger', 0)} | Bond: {tama.get('bond', 0)}")
    print(f"Boosts: {tama.get('boosts', {})}")

    print(Fore.CYAN + "\n--- Wishing Well ---")
    print(f"Wishes Made: {well.get('wishing_coins_used', 0)}")
    print(f"Blessings Received: {well.get('blessings_received', 0)}")
    print(f"Curses Received: {well.get('curses_received', 0)}")
    print(f"Divine Spark Charges: {well.get('divine_spark', 0)}")

    print(Fore.CYAN + "\n--- Gatcha ---")
    print(f"Gatches Done: {gatcha_data.get('gatchas_pulled', 0)} | Xp Earned: {gatcha_data.get('xp_earned', 0)}")
    print(Fore.BLACK + "|" + Fore.CYAN)

    characters = gatcha_data.get("characters_owned", [])
    if characters:
        for i, name in enumerate(characters, 1):
            # Find the full character data from the gatcha list
            full_data = next((char for char in gatcha if char["name"] == name), None)
            if full_data:
                print(f"-{full_data['name']}  ({full_data['rank']})", end='     ')
            else:
                print(f"-{name}  (Unknown Data)", end='     ')
            if i % 3 == 0:
                print()  # Newline after every 3 items
        if len(characters) % 3 != 0:
            print()  # Ensure final line ends properly
    else:
        print("(None)")

    print(Fore.BLUE + "\n--- Inventory ---")
    inventory = player_data.get("inventory", [])
    if inventory:
        for i, item in enumerate(inventory, 1):
            print(f"-{item['name']}   ", end='  ')
            if i % 5 == 0:
                print()  # Newline after every 5 items
        if len(inventory) % 5 != 0:
            print()  # Ensure final line ends properly
    else:
        print("(Empty)")

    if persistentStats["is_dead"]:
        print(Fore.RED + "\nThis character is dead. You must create a new one.\n")
        print(Style.RESET_ALL)
        sys.exit()

    print(Fore.BLUE + "\n(Press Enter to return to combat...)")
    input(Fore.GREEN + "> ")

    combat()


def get_item_coin_value(item):
    # Calculate the coin value of an item based on its boosts and rarity.
    #    - Each point of boost contributes some coins depending on stat type.
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
            value += amount * 25  # utility stats are rarer and therefore worth more
        elif stat == "xp":
            value += amount * 13.5
        elif stat == "coins":
            value += amount
        elif stat == "divine_spark":  # I don't think this or the coins/xp are being used
            value += amount * 30
        elif stat == "heal" and amount == "full":
            value += 500

    # Rarity multiplier (inverse of weight; capped to avoid extreme inflation)
    rarity_bonus = min(50, round(25 / weight)) if weight > 0 else 100
    floorBonus = persistentStats["floor"] / 2.5
    if floorBonus <= 1:
        floorBonus = 1
    value = round(value * (1 + rarity_bonus / 100) * floorBonus * ((persistentStats["reborns_used"] * 10) + 1)) + 100

    return max(1, int(value))  # Ensure at least 1 coin


def show_inventory():  # Shows the inventory
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


def show_combat_stats():  # this is the main function to show all the stats during combat, it runs after each turn (or when coming back to combat after playing a minigame or something else) to refresh the page and show what the current stats of all enemies and players are.
    global currentMonsterFight, currentMonsterHealth, monsterId, player, monster, persistentStats
    clear_screen()
    print(Fore.BLACK + "|")
    monsterHealthPercentage = round((currentMonsterHealth / monster.maxHealth[monsterId]) * 100, 2)
    print(Fore.WHITE + "You are currently fighting a", currentMonsterFight,"  (Floor:" + str(persistentStats["floor"]) + "." + str(persistentStats["room"]) + ")")
    print(Fore.BLACK + "|")
    print(Fore.RED + currentMonsterFight, "Health:")
    print(Fore.BLACK + "|", end='')
    # Cap health bar
    bar_length = min(round(monsterHealthPercentage / 2), 1000)
    print(Fore.RED + '=' * bar_length, end='')
    if monsterHealthPercentage > 2000 or player["eye_purchased"] == True:
        print(Fore.RED + f" {monsterHealthPercentage}%" + Fore.YELLOW + " |  HP: " + str(int(currentMonsterHealth)) + f"  |  Defense: {monster.defense[monsterId]}")
    else:
        print(Fore.RED + f" {monsterHealthPercentage}%")
    print(Fore.BLACK + "|")
    if player["eye_purchased"] == True:
        damageAverage = round((monster.minDamage[monsterId] + monster.maxDamage[monsterId]) / 2,1)
        damageMin = monster.minDamage[monsterId] 
        damageMax = monster.maxDamage[monsterId]
        # Scales the  damage with the difficulty
        if player["difficulty"] == "easy":
            damageAverage = round(damageAverage * 0.75)
            damageMin = round(damageMin * 0.75)
            damageMax = round(damageMax * 0.75)
        if player["difficulty"] == "normal":
            damageAverage = round(damageAverage * 1)
            damageMin = round(damageMin * 1)
            damageMax = round(damageMax * 1)
        if player["difficulty"] == "hard":
            damageAverage = round(damageAverage * 1.5)
            damageMin = round(damageMin * 1.5)
            damageMax = round(damageMax * 1.5)
        if player["difficulty"] == "impossible":
            damageAverage = round(damageAverage * 2)
            damageMin = round(damageMin * 2)
            damageMax = round(damageMax * 2)
        else:
            damageAverage = round(damageAverage * 1)
            damageMin = round(damageMin * 1)
            damageMax = round(damageMax * 1)
        print(Fore.YELLOW + f"Hacker Eye Info |  Average Damage: {damageAverage} (Min: {damageMin} - Max: {damageMax})")
    print(Fore.BLACK + "|")
    currentHealthPercentage = round((player["health"] / player["maxHealth"]) * 100, 2)
    print(Fore.GREEN + "Player Stats:")
    print(Fore.GREEN + " Health: ", end='')
    for i in range(round(currentHealthPercentage / 2.4)): print(Fore.GREEN + '=', end='')
    print("", str(currentHealthPercentage) + "%  (" + str(round(player["health"], 1)) + ")")
    print(Fore.GREEN + " Damage:", round(player["damage"], 1), " |  Defense:", round(player["defense"], 1), " |  Xp:",
          round(player["xp"], 1))
    print(Fore.GREEN + " Dodge Chance:", str(round(player["dodge"], 1)) + "% |  Retreat Chance:",
          str(round(player["escape"], 1)) + "%", " |  Item Drop Chance:", str(round(player["drop"], 1)) + "%")
    print(Fore.BLACK + "|")
    if tamagatchi_data["active"]:
        print(
            Fore.CYAN + f"Tamagatchi → Bond: {tamagatchi_data['bond']} | Hunger: {tamagatchi_data['hunger']} | Boosts: {tamagatchi_data['boosts']}")
        print(Fore.BLACK + "|")
    print(Fore.BLACK + "|")
    print(Fore.BLUE + "Actions:", player["actionList"])
    print(Style.RESET_ALL)


# Minigame/Other Functions

# Portal Travel Funcitons
def portal_travel(): # The idea of this is to let you travel to any floor (50-max) that you have been to before
    global persistentStats
    clear_screen()
    if persistentStats["floor"] < 75:
        print(Fore.RED + "You can't do portal travel till floor 75!")
        print(Fore.BLACK + "|")
        input(Fore.BLUE + "Press Enter to return to combat.")
        return

    while True:
        clear_screen()
        print(Fore.BLUE + "===Portal Travel===")
        print(Fore.BLACK + "|")
        print(Fore.BLUE + f"You can access floors " + Fore.YELLOW + f"50 to {persistentStats['highest_floor']}")
        print(Fore.BLUE + "What floor would you like to go to? (or type 'exit')")
        choice = input(Fore.GREEN + "> ").lower()

        if choice in ["exit", "no", "leave"]:
            print(Fore.CYAN + "Returning to combat")
            time.sleep(0.8)
            return

        if choice.isdigit():
            floor_num = int(choice)
            if 50 <= floor_num <= persistentStats['highest_floor']:
                print(Fore.MAGENTA + f"You enter the portal and travel to floor {floor_num}")
                time.sleep(0.8)
                persistentStats["floor"] = floor_num
                persistentStats["room"] = 1
                reset_monster() # This makes it a free retreat butttt I don't care
                return
            else:
                print(Fore.RED + "You cannot enter this floor")
                time.sleep(0.5)
        else:
            print(Fore.RED + "Invalid input. Please enter a floor number or 'exit'.")
            time.sleep(0.5)

# Gatcha functions
def start_gatcha_thread():  # Starts the passive gatcha thread to earn xp based on earned characters if you have characters
    global gatcha_thread, gatcha_data
    # print(Fore.GREEN +
    #    f"Starting gatcha thread? thread={gatcha_thread}, alive={gatcha_thread.is_alive() if gatcha_thread else 'N/A'}, owned={gatcha_data['characters_owned']}")
    if gatcha_thread and gatcha_thread.is_alive() and not gatcha_data["characters_owned"]:
        return
    gatcha_stop_event.clear()

    def loop():
        while gatcha_data["active"] and not gatcha_stop_event.is_set():
            # if gatcha_data["last_update"] is not None:
            update_gatcha()
            time.sleep(random.uniform(5, 10))  # How long it takes for the gatcha to update

    gatcha_thread = threading.Thread(target=loop, daemon=True)
    gatcha_thread.start()
    # print("Gatcha thread started")


def update_gatcha():  # The actual gatcha thread which updates your XP over time
    global player, persistentStats, gatcha_data, gatcha, gatcha_thread, startup_grace_period

    if gatcha_data["active"] and not startup_grace_period:  # Don't do it if it's during startup
        # Total up XP bonuses from player's active gatcha characters
        xp_gain = 0
        for name in gatcha_data.get("characters_owned", []):
            for char in gatcha:
                if char["name"] == name:
                    xp_gain += char["boosts"]["xp_bonus"]
                    break  # Stop after the first match

        # Apply multipliers
        reborns = (persistentStats["reborns_used"] + 1) * 5
        floor = persistentStats["floor"] + 1
        xp_gain *= reborns + floor

        # Wait and apply the XP gain
        time.sleep(10)
        gatcha_data["xp_earned"] += xp_gain
        player["xp"] += xp_gain

def try_gatcha_drop(garentee):  # Is called whenever a monster is killed past the 10th floor, tries to drop a gatcha pass
    global gatcha_data, persistentStats
    if garentee == 0:  # Garentees a gatach drop
        print(
            Fore.CYAN + "You found a " + Fore.RED + "G" + Fore.YELLOW + "a" + Fore.GREEN + "t" + Fore.CYAN + "c" + Fore.BLUE + "h" + Fore.MAGENTA + "a" + Fore.CYAN + " pass! Go to the gatcha minigame to use it!")
        gatcha_data["gatcha_pulls_available"] += 1
        time.sleep(1)
    elif random.randint(0, 100) <= 5:  # 5% chance
        print(
            Fore.CYAN + "You found a " + Fore.RED + "G" + Fore.YELLOW + "a" + Fore.GREEN + "t" + Fore.CYAN + "c" + Fore.BLUE + "h" + Fore.MAGENTA + "a" + Fore.CYAN + " pass! Go to the gatcha minigame to use it!")
        gatcha_data["gatcha_pulls_available"] += 1
        time.sleep(1)

    return

def gatcha_game():  # When you type gatcha into the minigame screen this is shown
    global persistentStats, gatcha_data, gatcha, player, persistentStats
    clear_screen()
    if persistentStats["floor"] < 30 and persistentStats["reborns_used"] <= 0:
        print(Fore.RED + "You can't do gatcha pulls until floor 30!")
        print(Fore.BLACK + "|")
        input(Fore.BLUE + "Press Enter to return to combat.")
        return

    gatcha_data["active"] = True
    start_gatcha_thread()  # ensures the thread is running

    while True:
        clear_screen()
        print(Fore.BLUE + "====Gatcha=====")
        if gatcha_data["characters_owned"]:
            print(Fore.CYAN + "You have: " + Fore.YELLOW + str(gatcha_data["characters_owned"]))
            print(Fore.BLACK + "|")
            print(Fore.CYAN + "They have earned you: " + Fore.YELLOW + str(gatcha_data["xp_earned"]))

        if gatcha_data["gatcha_pulls_available"] <= 0:  # Ensures you have some gatcha passes to use
            print(Fore.RED + "You don't have any pulls available!")
            print(Fore.YELLOW + "Go kill some monsters to get more pulls.")
            print(Fore.BLACK + "|")
            input(Fore.BLUE + "Press Enter to return to combat.")
            return
        print(Fore.CYAN + "You have " + Fore.YELLOW + str(gatcha_data["gatcha_pulls_available"]) + Fore.CYAN + " pulls!")
        print(Fore.BLACK + "|")
        print(Fore.YELLOW + "Would you like to do a draw? [ENTER -> yes  |  no -> exit]")
        choice = input()
        update_last_action()
        if choice in ["yes", "y", ""]:
            if gatcha_data["gatcha_pulls_available"] >= 1:
                print(Fore.BLACK + "|")
                gatcha_data["gatcha_pulls_available"] -= 1
                gatcha_data["gatchas_pulled"] += 1
                gatcha_chance = random.randint(0, 100)
                if gatcha_chance <= 20:
                    if set(gatcha_data["characters_owned"]) >= {c["name"] for c in
                                                                gatcha}:  # Tests if you have every character
                        print(Fore.RED + "You have unlocked all characters so you can't unlock more")
                        print(Fore.BLUE + "You can still earn xp and coins from the draws!")
                        time.sleep(2)
                    else:
                        unlocked = random.choice(gatcha)  # chooses a random character
                        while unlocked["name"] in gatcha_data[
                            "characters_owned"]:  # Ensures the character is not a duplicate
                            unlocked = random.choice(gatcha)
                        gatcha_data["characters_owned"].append(unlocked["name"])
                        print(Fore.BLUE + f"You unlocked an {unlocked['rank']} rank! {unlocked['name']}!")
                        print(Fore.MAGENTA + f"{unlocked['desc']}")
                        time.sleep(1.5)
                elif gatcha_chance <= 40:
                    xp_earned = random.randint(10, 200) * (persistentStats["floor"] + 1) * (persistentStats["reborns_used"] + 1)
                    print(Fore.BLUE + f"You earned {xp_earned} xp!")
                    player["xp"] += xp_earned
                elif gatcha_chance <= 70:
                    coins_earned = random.randint(10, 500) * (persistentStats["floor"] + 1) * (persistentStats["reborns_used"] + 1)
                    print(Fore.BLUE + f"You earned {coins_earned} coins!")
                    player["coins"] += coins_earned
                else:
                    print(Fore.RED + "You didn't earn anything...")
                time.sleep(1)
            else:
                print(Fore.RED + "You don't have any pulls remaining")
                time.sleep(0.8)
        elif choice in ["no", "n", "exit", "leave"]:
            return
        else:
            print(Fore.RED + "Invalid input")
            time.sleep(1)
    return

# Reborn functions
def reborn():
    global player, shop_data, well_data, persistentStats, endlessMode

    clear_screen()

    if persistentStats["floor"] < 30:
        print(Fore.RED + "You must reach floor 30 to use Reborn.")
        print(Fore.BLACK + "|")
        input(Fore.BLUE + "Press Enter to return to combat.")
        return
    
    if player["kills_sense_reborn"] < 50:
        monsters_left = 50 - player["kills_sense_reborn"]
        print(Fore.RED + "You haven't killed enough monsters sense your last reborn.")
        print(Fore.RED + "You need to kill " + Fore.YELLOW + str(monsters_left) + Fore.RED + " monsters!")
        print(Fore.BLACK + "|")
        input(Fore.BLUE + "Press Enter to return to combat.")
        return

    print(Fore.YELLOW + "--- Reborn ---")
    if persistentStats["floor"] <= 50:
        print(Fore.CYAN + "Reset to Floor 0 while keeping all stat boosts and inventory.")
    else:
        print(Fore.CYAN + "Reset to Floor 50 while keeping all stat boosts and inventory.")
    print(Fore.CYAN + "All minigames improve, and well cost resets.")
    print(Fore.CYAN + "Cost: All XP  →  Reward: 100,000 coins")
    print(Fore.YELLOW + "\nReborn? (yes/no)")

    choice = input(Fore.GREEN + "> ").strip().lower()
    update_last_action()
    if choice in ["yes", "y"]:
        if player["xp"] <= 1000:
            print(Fore.RED + "You don't have enough XP, requires at least 1000")
            time.sleep(2)
            combat()
            return

        persistentStats["highest_floor"] = persistentStats["floor"]
        player["xp"] = 0.0
        player["coins"] += 100000
        well_data["wishing_well_cost"] = 50000
        if persistentStats["floor"] <= 50:
            persistentStats["floor"] = 0
        else:
            persistentStats["floor"] = 50
        persistentStats["room"] = 0
        persistentStats["reborns_used"] += 1
        player["kills_sense_reborn"] = 0

        print(Fore.GREEN + "You have been reborn. The climb begins anew...")
        if endlessMode:
            print(Fore.RED + "You thought you could escape me????")
        time.sleep(3)

        reset_monster()
        combat()
    else:
        print(Fore.YELLOW + "Rebirth canceled.")
        time.sleep(1.5)
        combat()


# Section for managing the wishing well
def wishing_well():
    global player, well_data, persistentStats

    clear_screen()
    if persistentStats["monsters_killed"] < 550 or persistentStats["floor"] < 50:
        print(Fore.RED + "You must defeat 550 monsters and make it to floor 50 to unlock the Wishing Well.")
        print(Fore.BLACK + "|")
        input(Fore.BLUE + "Press Enter to return to combat.")
        return

    while True:
        clear_screen()
        cost = well_data["wishing_well_cost"]
        print(Fore.CYAN + "--- The Wishing Well ---")
        print(Fore.YELLOW + f"Cost to Wish: {cost} coins")
        print(f"You have: {player['coins']} coins")
        print(Fore.BLACK + "|")
        print(Fore.YELLOW + "Health:", str(round(player["maxHealth"])), "  | Damage:", str(round(player["damage"])),
              "  | Defense:", str(round(player["defense"])))
        print(Fore.BLACK + "|")

        if player["coins"] <= well_data["wishing_well_cost"]:  # Ensures you have some coins
            print(Fore.RED + "You don't have enough coins!")
            print(Fore.RED + "The wishing well costs " + Fore.YELLOW + str(well_data["wishing_well_cost"]) + Fore.RED +" coins")
            print(Fore.BLACK + "|")
            input(Fore.BLUE + "Press Enter to return to combat.")
            return

        print(Fore.MAGENTA + "Make a wish? (ENTER -> Yes   |  Exit -> No)")

        choice = input(Fore.GREEN + "> ").strip().lower()
        update_last_action()
        if choice in ["no","n","exit","leave"]:
            print(Fore.CYAN + "Returning to combat..")
            time.sleep(0.8)
            return
        if choice in ["yes", "y",""]:
            if player["coins"] < cost:
                print(Fore.RED + "Not enough coins!")
            else:
                player["coins"] -= cost
                well_data["wishing_well_cost"] = int(cost * 1.25)
                well_data["wishing_coins_used"] += 1

                roll = random.randint(1, 100)
                result_type = "blessing" if roll <= 60 else "curse" if roll <= 95 else "spark"

                if result_type == "spark":
                    print(Fore.CYAN + "A Divine Spark ignites within you. +1 charge!")
                    well_data["divine_spark"] += 1
                    time.sleep(2)

                elif result_type == "blessing":
                    blessing = random.choice(blessings)
                    if blessing["name"] in well_data["obtained_blessings"]:
                        print(Fore.YELLOW + f"You already received {blessing['name']}. Refund: {cost // 2} coins.")
                        player["coins"] += cost // 2
                    else:
                        apply_boost(blessing["boosts"])
                        well_data["obtained_blessings"].append(blessing["name"])
                        well_data["blessings_received"] += 1
                        print(Fore.GREEN + f"Blessing: {blessing['name']} → {blessing['desc']}")
                else:  # curse
                    curse = random.choice(curses)
                    if curse["name"] in well_data["obtained_curses"]:
                        print(Fore.YELLOW + f"You already endured {curse['name']}. Refund: {cost // 2} coins.")
                        player["coins"] += cost // 2
                    else:
                        apply_boost(curse["boosts"])
                        well_data["obtained_curses"].append(curse["name"])
                        well_data["curses_received"] += 1
                        print(Fore.RED + f"Curse: {curse['name']} → {curse['desc']}")
        else:
            print(Fore.RED + "Invalid Input")

        apply_boosts()
        time.sleep(1)

def apply_boost(
        boost_dict):  # This is for the well specifically, not to be confused with the apply boost(s) function down below
    for key, value in boost_dict.items():
        if key == "heal" and value == "full":
            player["health"] = player["maxHealth"]
        elif key == "divine_spark":
            well_data["divine_spark"] += value
        elif key == "xp":
            player["xp"] += value
        elif key == "coins":
            player["coins"] += value
        elif key in ["health", "damage", "defense", "dodge", "escape", "drop"]:
            boost_key = f"{key}Boost"
            if boost_key in player:
                player[boost_key] += value
            else:
                # fallback in case a stat exists without a boost counterpart
                player[key] += value
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
        global persistentStats, fishing_data
        
        max_fish = (persistentStats["floor"] + 1) * 4 * (persistentStats["reborns_used"] + 1)
        
        if fishing_data["fish_caught"] >= max_fish:
                print(Fore.RED + "You have caught all the fish here, try again next floor!")
                print(Fore.BLUE + "Type EXIT to continue (you may have to type it several times)")
                input(Fore.GREEN + "> ")
                return
        
        while fishing_active and not fishing_stop_event.is_set():
            
            if fishing_data["fish_caught"] >= max_fish:
                print(Fore.RED + "You have caught all the fish here, try again next floor!")
                print(Fore.BLUE + "Type EXIT to continue (you may have to type it several times)")
                input(Fore.GREEN + "> ")
                return
            
            if fishing_penalty or time.time() < cooldown_until:
                time.sleep(0.2)
                continue
            print(Fore.BLUE + "Waiting for a bite...")
            if player["monster_bait_purchased"] == True:
                time.sleep(random.uniform(2, 4))
            else:
                time.sleep(random.uniform(3, 8))
            if not fishing_active or fishing_stop_event.is_set():
                break
            fish_ready = True
            print(Fore.YELLOW + "\nA fish is on the line! Press Enter quickly!")

            response = timed_input(timeout=1.0)
            fish_ready = False

            if response is None:
                print(Fore.RED + "Too slow! The fish got away.")
                cooldown_until = time.time() + 2
                continue

            fish_ready = False

            if fishing_penalty:
                print(Fore.RED + "Rod tangled from spam. No reward.")
                continue

            if random.random() < 0.8:
                update_last_action()
                scale = 1 + (persistentStats["floor"] / 2)
                mult = 10 * int(persistentStats["floor"] * 1.5) if persistentStats["floor"] >= 50 else 1
                xp_gain = round(random.uniform(0.5, 2.0) * scale * mult, 1)
                player["xp"] += xp_gain
                print(Fore.GREEN + f"You caught a fish and earned {xp_gain} XP!")
                fishing_data["fish_caught"] += 1
            else:
                update_last_action()
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
                fishing_data["items_fished"] += 1
                apply_boosts()
            cooldown_until = time.time() + 1

    if fishing_thread and fishing_thread.is_alive():
        print(Fore.RED + "Fishing is already active. (You should NOT be seing this message)")
        print(Fore.RED + "Exit the fishing and reopen it to (hopfully) fix it")
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
            update_last_action()
            fishing_active = False
            fishing_stop_event.set()
            print(Fore.GREEN + "You pack up and return to combat...")
            time.sleep(1)
            break
        if cmd.strip() == "" and not fish_ready:
            update_last_action()
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
def gamble_stat_change(amount):  # Returns how much the stats change when doing a high risk gamble
    global persistentStats, player
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
        if player["weighted_dice_purchsed"] == True:
            print(Fore.YELLOW + "The weighted dice twists your fate")
            return amount * 3 * (persistentStats["floor"] / 7.5)
        else:
            return amount * 2 * (persistentStats["floor"] / 7.5)  # Lets the big wins and big losses scale with the floor slightly

def gambling():  # Manages the gambling screen
    global player, persistentStats
    clear_screen()
    print(Style.RESET_ALL)
    print(Fore.YELLOW + "Welcome to the Gambling Den")
    if persistentStats["floor"] < 15 and persistentStats["reborns_used"] <= 0:
        print(Fore.BLACK + "|")
        print(Fore.RED + "You must reach floor 15 to gamble!")
        print(Fore.BLACK + "|")
        input(Fore.BLUE + "Press Enter to return to combat.")
        return
    print(Fore.CYAN + f"You have {player['coins']} coins.")
    if persistentStats["floor"] >= 45:
        print(Fore.BLACK + "|")
        print(Fore.YELLOW + "Health:", str(round(player["maxHealth"])), "  | Damage:", str(round(player["damage"])),
              "  | Defense:", str(round(player["defense"])))
    print(Fore.BLACK, "|")

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
    if persistentStats["floor"] >= 45:
        print(Fore.GREEN + " [highrisk] → Gamble health, damage, or defense stats (costs 10,000 coins)")
    else:
        print(Fore.RED + " [highrisk] → Unlocks at Floor 45+")
    print(Fore.GREEN + " [leave]   → Exit back to combat")
    print(Fore.BLACK, "|")

    choice = input(Fore.CYAN + "\nYour choice: ").strip().lower()

    update_last_action()

    if choice in ["sell"]:
        if not player["inventory"]:
            print(Fore.RED + "You have no items to sell.")
        else:
            for i, item in enumerate(player["inventory"]):
                value = get_item_coin_value(item)
                print(Fore.MAGENTA + f"[{i}] {item['name']} → {value} coins")

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
            elif sel in ["exit", "leave"]:
                print(Fore.BLUE + "You chose to sell nothing!")
                time.sleep(1)
            else:
                print(Fore.RED + "Invalid input.")
        apply_boosts()

    elif choice in ["gamble", "gam"]:
        if player["weighted_dice_purchased"] == True:
            max_winnings = (10000 * (((persistentStats["floor"] + 1) / 5) * (persistentStats["reborns_used"] + 1)))
        else:
            max_winnings = (5000 * (((persistentStats["floor"] + 1) / 5) * (persistentStats["reborns_used"] + 1)))
        if gambling_data["gamblingCoinsWon"] >= max_winnings:
            print(Fore.BLACK + "|")
            print(Fore.MAGENTA + "Casino Man: " + Fore.RED + "You have gambled too much! You need to take a break!")
            print(Fore.BLUE + "(You can try to gamble again next floor)")
            time.sleep(2)
        else:
            try:
                amt = int(input(Fore.YELLOW + "Enter coin amount to bet: ").strip())
                if amt <= 0 or amt > player["coins"]:
                    print(Fore.RED + "Invalid bet amount.")
                else:
                    if player["weighted_dice_purchased"] == True:
                        mults = [0.5, 0.6, 0.7, 0.8, 1.1, 1.2, 1.3, 1.4, 1.5]
                    else:
                        mults = [0, 0.3, 0.4, 0.5, 1.0, 1.025, 1.05, 1.1, 1.2]
                    weights = [10, 20, 10, 7, 12, 10, 20, 5, 2]
                    scale = 1 + (persistentStats["floor"] / 10)
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
                        if player["weighted_dice_purchased"] == True:
                            print(Fore.YELLOW + "Your weighted dice twists your fate")
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
        if persistentStats["floor"] < 45:
            print(Fore.RED + "High Risk unlocked at Floor 45")
        else:
            stat = input(Fore.YELLOW + "Which stat? [health/damage/defense]: ").strip().lower()
            if stat in ["health", "damage", "defense"]:
                try:
                    amt = int(input(Fore.CYAN + f"Points of {stat} to gamble: ").strip())
                    key = f"{stat}Boost"
                    if amt <= 0 or amt > player[key]:
                        print(Fore.RED + "Invalid amount.")
                    else:
                        player["coins"] -= 10000
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
            time.sleep(random.uniform(30, 200))  # How long it takes for the tamagatchi to update (30 - 200)

    tamagatchi_thread = threading.Thread(target=loop, daemon=True)
    tamagatchi_thread.start()

def update_tamagatchi():
    global startup_grace_period
    hunger = tamagatchi_data["hunger"]
    bond = tamagatchi_data["bond"]
    kills = persistentStats.get("monsters_killed", 0)
    max_bond = 20 * (persistentStats["reborns_used"] + 1)
    if player["dog_house_purchased"] == True:
        max_bond = (max_bond * 2)

    # Hunger increases
    if hunger < 100 and startup_grace_period == False:
        if random.randint(0, 100) <= 50:  # only increases hunger half the time
            tamagatchi_data["hunger"] += 1

    # Bond slowly increases if well-fed (under 20 hunger)
    if hunger < 20 and random.random() < 0.5 and startup_grace_period == False:  # 50% chance to gain a bond each update if the hunger is low enough (also don't update during the start of the progam)
        if tamagatchi_data["bond"] < max_bond:
            tamagatchi_data["bond"] += 1
        else:
            tamagatchi_data["bond"] = max_bond
    elif hunger >= 20:
        pass

    if tamagatchi_data[
        "bond"] >= max_bond:  # Ensure the cap is enforced (maybe like actually, please work please work please work)
        tamagatchi_data["bond"] = max_bond

    # Recalculate boosts
    if bond > 0:
        scale = 1
        if persistentStats["reborns_used"] >= 1:
            scale = 2 * (persistentStats["reborns_used"] + 1)
        floorBoost = (persistentStats["floor"] / 1.5) + 1

        tamagatchi_data["boosts"]["health"] = int(bond * (floorBoost / 2) * scale * (1 + (kills / 20) * 0.2))
        tamagatchi_data["boosts"]["damage"] = int(bond * (floorBoost / 2) * scale * (1 + (kills / 21) * 0.005))
        tamagatchi_data["boosts"]["defense"] = int(bond * (floorBoost / 2) * scale * (1 + (kills / 22) * 0.0005))

    apply_boosts()

def tamagatchi():
    global player, persistentStats
    max_bond = 20 * (persistentStats["reborns_used"] + 1)
    if player["dog_house_purchased"] == True:
        max_bond = (max_bond * 2)
    clear_screen()
    print(Style.RESET_ALL)

    if persistentStats["floor"] < 10 and persistentStats["reborns_used"] <= 0:
        print(Fore.BLACK + "|")
        print(Fore.RED + "You must reach floor 10 to unlock the Tamagatchi!")
        print(Fore.BLACK + "|")
        input(Fore.BLUE + "Press Enter to return to combat.")
        return

    if not tamagatchi_data["active"]:
        if player["xp"] < 500:
            print(Fore.RED + "It costs 500 XP to adopt a Tamagatchi, you do not have that much!")
            print(Fore.BLACK + "|")
            input(Fore.BLUE + "Press Enter to return to combat.")
            return
        player["xp"] -= 500
        tamagatchi_data.update({
            "active": True,
            "last_update": datetime.now().isoformat(),
            "hunger": 1,
            "bond": 5
        })
        start_tamagatchi_thread()
        print(Fore.YELLOW + "You adopted a strange creature!")
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
        print(Fore.BLACK + "|")
        print(Fore.YELLOW + "Tamagatchi will be much happier if hunger is kept under 20")
        print(Fore.BLACK + "|")

        if hunger < 5:
            print(Fore.YELLOW + "It's not hungry enough to feed.")
        else:
            cost = round(hunger * 1.2 * (tamagatchi_data["tamagatchiFeeds"] + 1), 1)
            print(Fore.YELLOW + f"Feeding cost: {round(cost, 1)} XP")

        print(Fore.CYAN + "\nType 'feed' to feed, or 'exit' to return to combat.")
        choice = input().strip().lower()

        update_last_action()

        if choice in ["exit", "leave"]:
            combat()
            return
        elif choice == "feed":
            if hunger < 5:
                print(Fore.YELLOW + "It's not hungry enough to feed.")
            elif player["xp"] >= cost:  # type: ignore
                tamagatchi_data["hunger"] = max(hunger - 4, 0)
                tamagatchi_data["bond"] = min(bond + 1, max_bond)
                player["xp"] -= cost  # type: ignore
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
    global persistentStats
    clear_screen()
    print(Fore.BLACK + "|")
    print(Fore.YELLOW + "Welcome to the Minigame/Other section!")
    print(Fore.BLUE + "  Complete minigames to earn boosts, XP, and more!")
    print(Fore.BLACK + "|")
    print(Fore.YELLOW + "Fishing        → Relax and earn items or XP.")
    if persistentStats["floor"] < 10 and persistentStats["reborns_used"] <= 0:
        print(Fore.RED + "Tamagatchi     → Feed a friend for passive stat boosts.")
    else:
        print(Fore.YELLOW + "Tamagatchi     → Feed a friend for passive stat boosts.")
    if persistentStats["floor"] < 15 and persistentStats["reborns_used"] <= 0:
        print(Fore.RED + "Gambling       → Risk coins/items to multiply rewards.")
    else:
        print(Fore.YELLOW + "Gambling       → Risk coins/items to multiply rewards.")
    if persistentStats["floor"] < 30 and persistentStats["reborns_used"] <= 0:
        print(Fore.RED + "Gatcha         → Randomly draw characters to earn xp passivly")
    else:
        print(Fore.YELLOW + "Gatcha         → Randomly draw characters to earn xp passivly")
    if persistentStats["monsters_killed"] < 550 or persistentStats["floor"] < 50:
        print(Fore.RED + "Wishing Well   → Spend coins for powerful blessings—or curses.")
    else:
        print(Fore.YELLOW + "Wishing Well   → Spend coins for powerful blessings—or curses.")
    if persistentStats["floor"] < 30:
        print(Fore.RED + "Reborn         → Reset with your stats intact after high progress.")
    else:
        print(Fore.YELLOW + "Reborn         → Reset with your stats intact after high progress.")
    if persistentStats["floor"] < 75:
        print(Fore.RED + "Portal Travel  → Travel through unlocked floors with ease!")
    else:
        print(Fore.YELLOW + "Portal Travel  → Travel through unlocked floors with ease!")
    print(Fore.BLACK + "|")
    print(Fore.BLUE + "Options:", player["gameList"])
    print(Fore.BLACK + "|")
    print(Style.RESET_ALL)

    choice = input(Fore.GREEN + "> ").strip().lower()
    update_last_action()

    if choice in ["tamagatchi", "tama"]:
        tamagatchi()
    elif choice in ["gambling", "gamble", "gamb"]:
        gambling()
    elif choice in ["fishing", "fish"]:
        fishing()
    elif choice in ["wishing well", "wish", "wishingwell", "wsh", "well"]:
        wishing_well()
    elif choice in ["gatcha", "gat", "draw"]:
        gatcha_game()
    elif choice in ["reborn", "re", "born"]:
        reborn()
    elif choice in ["portal","travel","port","trav","tele","teleport"]:
        portal_travel()
    elif choice in ["exit", "leave"]:
        combat()
    else:
        print(Fore.RED + "Invalid input. Try again.")
        time.sleep(1)
        minigame_selection()


# Saving and Loading Functions
def save_to_file():  # Saves the file
    global globalSavePath, player, persistentStats, tamagatchi_data, well_data, gatcha_data, monsterAttack
    player["name"] = os.path.splitext(currentSaveName)[0]

    persistentStats["currentVersion"] = "2.3.3"

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
        "currentMonsterHealth": currentMonsterHealth,
        "monsterAttack": monsterAttack,
        "gatcha_data": gatcha_data,
    }

    with open(globalSavePath, "w") as f:
        json.dump(data, f, indent=4)


def list_saved_files():  # lists saved files
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

def load_from_file(filename):  # Load data from files
    global globalSavePath, player, persistentStats, tamagatchi_data, well_data, gatcha_data, monsterAttack
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
        gatcha_data.update(data.get("gatcha_data", {}))
        fishing_data.update(data.get("fishing_data", {}))
        gambling_data.update(data.get("gambling_data", {}))
        endlessMode = data.get("endlessMode", False)
        endlessKills = data.get("endlessKills", 0)
        monsterId = data.get("monsterId", 0)
        currentMonsterFight = monster.names[monsterId]
        currentMonsterHealth = data.get("currentMonsterHealth", monster.maxHealth[monsterId])
        currentMonsterDefense = monster.defense[monsterId]
        monsterAttack = data.get("monsterAttack", 0)

        # Stats the tamagatchi thread
        if tamagatchi_data.get("active"):
            start_tamagatchi_thread()

        if gatcha_data.get("active"):
            start_gatcha_thread()

        # Starts the idle checker
        idle_thread = threading.Thread(target=idle_checker_thread, daemon=True)
        idle_thread.start()

        # Grace period
        threading.Thread(target=grace_period_timer, daemon=True).start()

        print(Fore.GREEN + f"Loaded from {filename}")

        # Ensures some old variables are set correctly
        if player["difficulty"] not in ["easy", "normal", "hard", "impossible"]:
            player["difficulty"] = "Unknown" # This is needed beacuse difficulty used to save as an int when creating a save file and was never initialized anywhere else

        # Version check
        if "currentVersion" not in persistentStats:
            print(Fore.RED + "WARNING")
            print(Fore.RED + "This save file does not have a version number.")
            print(Fore.RED + "It may be from an old version of the game and may not load correctly.")
            print(Fore.RED + "Expect to have MAJOR compatability issues")
            print(Fore.RED + "These issues can be totally GAMEBREAKING")
            input(Fore.BLUE + "Press ENTER to continue...")
        elif persistentStats["currentVersion"] != "2.3.3":
            print(Fore.RED + "WARNING")
            print(Fore.RED + "This save file is not from the current version of the game")
            print(Fore.RED + "This save is from " + Fore.MAGENTA + persistentStats["currentVersion"])
            print(Fore.RED + "Expect to have some minor compatability issues")
            input(Fore.BLUE + "Press ENTER to continue...")

        return True

    except Exception as e:
        print(Fore.RED + f"\nError loading save '{filename}': {e}")
        print(Fore.RED + "Your save may be corrupted.")
        print(Fore.YELLOW + "If a backup exists, you can try restoring it by renaming:")
        print(Fore.CYAN + f"  {filename}.bak  →  {filename}")
        print(Fore.YELLOW + "Then restart the game.")
        print(Style.RESET_ALL)
        sys.exit(1)

# Other Main Functions
def try_drop_item():
    # Attempts to drop an item after combat or fishing, based on player's drop chance.
    # If an item is already in inventory, it is auto-sold for coins instead.
    # Applies item boosts immediately if obtained.

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
            gambling_data["itemsSold"] += 1
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
    # Recalculate and apply all stat boosts from level-ups, items, tamagatchi, and blessings.
    # This function resets stats to base values and then adds all applicable bonuses.

    # Base stats
    base_health = 25.0
    base_damage = 3.5
    base_defense = 1.0
    base_dodge = 5.0
    base_escape = 50.0
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
    global monsterId, player, monster, currentMonsterFight, currentMonsterHealth, currentMonsterDefense, persistentStats, monsterAttack

    monsterAttack = 0
    
    if persistentStats["boss_fight_ready"]:
        boss_index = min(monsterId + 1, len(monster.names) - 1)
        monsterId = boss_index
        # persistentStats["boss_fight_ready"] = False

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

        if persistentStats["boss_fight_ready"] and persistentStats["room"] == 10:
            print(Fore.RED + "A boss monster approaches... defeat this enemy to move on to the next floor")
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
        print(Fore.BLACK + "|")

        # Define all boost types
        boosts = ["Health", "Damage", "Defense", "Dodge", "Escape", "Drop"]

        # Build the output string with individual coloring
        output_parts = []

        for i, boost in enumerate(boosts):  # Use enumerate to get index i
            base_cost = shop_data[f'base{boost}BoostCost']
            current_mod = shop_data[f'{boost.lower()}BoostMod']
            cap = shop_data[f'{boost.lower()}BoostCap']

            can_buy = player["xp"] >= base_cost and current_mod < cap
            color = Fore.GREEN if can_buy else Fore.RED

            output_parts.append(f"{color} {boost}: {base_cost}")

            # Add newline after each entry
            output_parts.append("\n")

        # Join and print everything
        print("".join(output_parts) + Style.RESET_ALL)

        # Manage upgrades like the eye and weighted dice
        if player["eye_purchased"] == False and persistentStats["floor"] >= shop_data["eyeFloor"]:
            if player["xp"] >= shop_data["eyeCost"]:
                print(Fore.GREEN + f" Hackers Eye: {shop_data['eyeCost']}  -> See things you shouldn't be able to see")
            else:
                print(Fore.RED + f" Hackers Eye: {shop_data['eyeCost']}  -> See things you shouldn't be able to see")
        if player["monster_bait_purchased"] == False and persistentStats["floor"] >= shop_data["monsterBaitFloor"]:
            if player["xp"] >= shop_data["monsterBaitCost"]:
                print(Fore.GREEN + f" Monster Bait: {shop_data['monsterBaitCost']}  -> Increase how fast fish will bite")
            else:
                print(Fore.RED + f" Monster Bait: {shop_data['monsterBaitCost']}  -> Increase how fast fish will bite")
        if player["weighted_dice_purchased"] == False and persistentStats["floor"] >= shop_data["weightedDiceFloor"]:
            if player["xp"] >= shop_data["weightedDiceCost"]:
                print(Fore.GREEN + f" Weighted Dice: {shop_data['weightedDiceCost']}  -> Change gambling luck in your favor")
            else:
                print(Fore.RED + f" Weighted Dice: {shop_data['weightedDiceCost']}  -> Change gambling luck in your favor")
        if player["dog_house_purchased"] == False and persistentStats["floor"] >= shop_data["dogHouseFloor"]:
            if player["xp"] >= shop_data["dogHouseCost"]:
                print(Fore.GREEN + f" Dog(?) House: {shop_data['dogHouseCost']}  -> Make your Tamagatchi happier")
            else:
                print(Fore.RED + f" Dog(?) House: {shop_data['dogHouseCost']}  -> Make your Tamagatchi happier")
        if player["mirror_pendant_purchased"] == False and persistentStats["floor"] >= shop_data["mirrorPendantFloor"]:
            if player["xp"] >= shop_data["mirrorPendantCost"]:
                print(Fore.GREEN + f" Mirror Pendant: {shop_data['mirrorPendantCost']}  -> Mosters can't seem to hit you")
            else:
                print(Fore.RED + f" Mirror Pendant: {shop_data['mirrorPendantCost']}  -> Mosters can't seem to hit you")
        if player["escape_key_purchased"] == False and persistentStats["floor"] >= shop_data["escapeKeyFloor"]:
            if player["xp"] >= shop_data["escapeKeyCost"]:
                print(Fore.GREEN + f" Escape Key: {shop_data['escapeKeyCost']}  -> Escape is garenteed")
            else:
                print(Fore.RED + f" Escape Key: {shop_data['escapeKeyCost']}  -> Escape is garenteed")
        if player["reaper's_token_purchased"] == False and persistentStats["floor"] >= shop_data["reaperTokenFloor"]:
            if player["xp"] >= shop_data["reaperTokenCost"]:
                print(Fore.GREEN + f" Reaper's Token: {shop_data['reaperTokenCost']}  -> Heal more from killing")
            else:
                print(Fore.RED + f" Reaper's Token: {shop_data['reaperTokenCost']}  -> Heal more from killing")
        if player["greed's_gullet_purchased"] == False and persistentStats["floor"] >= shop_data["greedGulletFloor"]:
            if player["xp"] >= shop_data["greedGulletCost"]:
                print(Fore.GREEN + f" Greed's Gullet: {shop_data['greedGulletCost']}  -> Killing grants coins")
            else:
                print(Fore.RED + f" Greed's Gullet: {shop_data['greedGulletCost']}  -> Killing grants coins")
        if player["soul_mirror_purchased"] == False and persistentStats["floor"] >= shop_data["soulMirrorFloor"]:
            if player["xp"] >= shop_data["soulMirrorCost"]:
                print(Fore.GREEN + f" Soul Mirror: {shop_data['soulMirrorCost']}  -> Reflect monsters attacks back at them")
            else:
                print(Fore.RED + f" Soul Mirror: {shop_data['soulMirrorCost']}  -> Reflect monsters attacks back at them")
        if player["portal_attractor_purchased"] == False and persistentStats["floor"] >= shop_data["portalAttractorFloor"]:
            if player["xp"] >= shop_data["portalAttractorCost"]:
                print(Fore.GREEN + f" Portal Attractor: {shop_data['portalAttractorCost']}  -> Portals will spawn much more often")
            else:
                print(Fore.RED + f" Portal Attractor: {shop_data['portalAttractorCost']}  -> Portals will spawn much more often")

        print(Fore.BLACK + "|\n" + Fore.BLUE + "Options:", player["buyList"])
        print(Fore.BLUE + "(Type 'exit' to return to combat)")

        choice = input(Fore.GREEN + "> ").strip().lower()

        # More upgrade management
        if player["eye_purchased"] == False and persistentStats["floor"] >= shop_data["eyeFloor"] and choice in ["eye", "hacker", "hack", "hackerseye", "hackers"]:
            if player["xp"] >= shop_data["eyeCost"]:
                print(Fore.GREEN + f"Hackers Eye Purchased! You can now see extra monster stats during battle.")
                player["xp"] -= shop_data["eyeCost"]
                player["eye_purchased"] = True
                time.sleep(1)
            else:
                print(Fore.RED + f"Not Enough Xp!")
        elif player["weighted_dice_purchased"] == False and persistentStats["floor"] >= shop_data["weightedDiceFloor"] and choice in ["weight", "weighted", "dice", "die", "weighteddice"]:
            if player["xp"] >= shop_data["weightedDiceCost"]:
                print(Fore.GREEN + f"Weighted Dice Purchased! Gambling is tipped in your favor!")
                player["xp"] -= shop_data["weightedDiceCost"]
                player["weighted_dice_purchased"] = True
                time.sleep(1)
            else:
                print(Fore.RED + f"Not Enough Xp!")
        elif player["dog_house_purchased"] == False and persistentStats["floor"] >= shop_data["dogHouseFloor"] and choice in ["dog", "doghouse","house"]:
            if player["xp"] >= shop_data["dogHouseCost"]:
                print(Fore.GREEN + f"Dog(?) House Purchased! Tamagatchi has a higher max bond!")
                player["xp"] -= shop_data["dogHouseCost"]
                player["dog_house_purchased"] = True
                time.sleep(1)
            else:
                print(Fore.RED + f"Not Enough Xp!")
        elif player["monster_bait_purchased"] == False and persistentStats["floor"] >= shop_data["monsterBaitFloor"] and choice in ["monster","bait","monsterbait"]:
            if player["xp"] >= shop_data["monsterBaitCost"]:
                print(Fore.GREEN + f"Monster Bait Purchased! Fishing is faster!")
                player["xp"] -= shop_data["monsterBaitCost"]
                player["monster_bait_purchased"] = True
                time.sleep(1)
            else:
                print(Fore.RED + f"Not Enough Xp!")
        elif player["mirror_pendant_purchased"] == False and persistentStats["floor"] >= shop_data["mirrorPendantFloor"] and choice in ["pendant","mirrorpendant","pend"]:
            if player["xp"] >= shop_data["mirrorPendantCost"]:
                print(Fore.GREEN + f"Mirror Pendant Purchased! The fist attack from any monster will deal 0 damage!")
                player["xp"] -= shop_data["mirrorPendantCost"]
                player["mirror_pendant_purchased"] = True
                time.sleep(1)
            else:
                print(Fore.RED + f"Not Enough Xp!")
        elif player["escape_key_purchased"] == False and persistentStats["floor"] >= shop_data["escapeKeyFloor"] and choice in ["escapekey","key","esckey"]:
            if player["xp"] >= shop_data["escapeKeyCost"]:
                print(Fore.GREEN + f"Escape Key Purchased! You escape every time!")
                player["xp"] -= shop_data["escapeKeyCost"]
                player["escape_key_purchased"] = True
                time.sleep(1)
            else:
                print(Fore.RED + f"Not Enough Xp!")
        elif player["reaper's_token_purchased"] == False and persistentStats["floor"] >= shop_data["reaperTokenFloor"] and choice in ["reaper","token","reapertoken"]:
            if player["xp"] >= shop_data["reaperTokenCost"]:
                print(Fore.GREEN + f"Reaper's Token Purchased! Healing from monster kills is trippled!")
                player["xp"] -= shop_data["reaperTokenCost"]
                player["reaper's_token_purchased"] = True
                time.sleep(1)
            else:
                print(Fore.RED + f"Not Enough Xp!")        
        elif player["greed's_gullet_purchased"] == False and persistentStats["floor"] >= shop_data["greedGulletFloor"] and choice in ["greed","greedgullet","greedsgullet","gullet"]:
            if player["xp"] >= shop_data["greedGulletCost"]:
                print(Fore.GREEN + f"Greed's Gullet Purchased! Every monster kill has a 50% chance to grant some coins!")
                player["xp"] -= shop_data["greedGulletCost"]
                player["greed's_gullet_purchased"] = True
                time.sleep(1)
            else:
                print(Fore.RED + f"Not Enough Xp!")
        elif player["soul_mirror_purchased"] == False and persistentStats["floor"] >= shop_data["soulMirrorFloor"] and choice in ["soul","soulmirror","mirror"]:
            if player["xp"] >= shop_data["soulMirrorCost"]:
                print(Fore.GREEN + f"Soul Mirror Purchased! 25% of damage taken is reflected on attacker!")
                player["xp"] -= shop_data["soulMirrorCost"]
                player["soul_mirror_purchased"] = True
                time.sleep(1)
            else:
                print(Fore.RED + f"Not Enough Xp!")
        elif player["portal_attractor_purchased"] == False and persistentStats["floor"] >= shop_data["portalAttractorFloor"] and choice in ["portal","portalattractor","attractor"]:
            if player["xp"] >= shop_data["portalAttractorCost"]:
                print(Fore.GREEN + f"Portal Attractor Purchased! Portals will spawn much more often")
                player["xp"] -= shop_data["portalAttractorCost"]
                player["portal_attractor_purchased"] = True
                time.sleep(1)
            else:
                print(Fore.RED + f"Not Enough Xp!")
                
        else:
            upgrade_map = {
                "health": ("healthBoost", "baseHealthBoostCost", "baseHealthBoostCostFactor", "healthBoostMod",
                           "healthBoostCap"),
                "damage": ("damageBoost", "baseDamageBoostCost", "baseDamageBoostCostFactor", "damageBoostMod",
                           "damageBoostCap"),
                "defense": ("defenseBoost", "baseDefenseBoostCost", "baseDefenseBoostCostFactor", "defenseBoostMod",
                            "defenseBoostCap"),
                "dodge": ("dodgeBoost", "baseDodgeBoostCost", "baseDodgeBoostCostFactor", "dodgeBoostMod", "dodgeBoostCap"),
                "escape": ("escapeBoost", "baseEscapeBoostCost", "baseEscapeBoostCostFactor", "escapeBoostMod",
                           "escapeBoostCap"),
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
                current_cost = (shop_data[cost_key])
                boost_mod = shop_data[mod_key]
                cap = shop_data[cap_key]

                if player["xp"] < current_cost:
                    update_last_action()
                    print(Fore.RED + "Not enough XP!")
                elif player[boost_key] >= cap:
                    update_last_action()
                    print(Fore.RED + f"{boost_key.capitalize()} boost is capped at {cap}.")
                else:  # applies stat boosts
                    update_last_action()
                    player["xp"] -= current_cost

                    if choice == "health":
                        base_health = 25.0

                        if player[boost_key] <= 0:
                            player[boost_key] = 1.0  # Starting point

                        current_boost = player[boost_key]
                        proposed_boost = current_boost + boost_mod

                        # Calculate new maxHealth
                        current_max = player["maxHealth"]
                        proposed_max = (base_health + proposed_boost) / 5
                        increase = proposed_max - current_max
                        max_increase = current_max / 10

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

            elif choice in ["exit", "leave", ""]:
                update_last_action()
                print(Fore.CYAN + "Returning to combat...")
                return
            else:
                update_last_action()
                print(Fore.RED + "Invalid input.")
        time.sleep(1)

def portal():
    global persistentStats, player
    print(Fore.CYAN + "A strange portal opens up, would you like to go in?")
    print(Fore.CYAN + "This will skip some floors " + Fore.RED + "(WARNING: You may not be equiped to handle the higher floors)")
    print(Fore.BLACK + "|")
    choice = input(Fore.BLUE + ">").strip().lower()
    print()
    if choice in ["yes", "y"]:
        print(Fore.YELLOW + "You enter the portal and exit in a random location!")
        time.sleep(0.8)
        if random.randint(0,100) <= 5 and persistentStats["floor"] <= 100: #adds a really small chance to move super far
            print(Fore.RED + "The portal took you really far... good luck")
            persistentStats["floor"] += random.randint(6, 90)
        else:
            persistentStats["floor"] += random.randint(3, 9)
        persistentStats["room"] = random.randint(0, 8)
        reset_monster()
    else:
        print(Fore.YELLOW + "You choose to ignore the portal and move on!")
        time.sleep(0.5)
    return

def try_portal():
    global persistentStats, player
    # have a small chance to skip a couple floors this will also not happen if the floor is too high
    if player["portal_attractor_purchased"] == True:
        if random.randint(1, 100) <= 20 and persistentStats["floor"] <= 190:
            portal()
    else:
        if random.randint(1, 100) <= 2 and persistentStats["floor"] <= 190:
            portal()
    return

def monster_death_check():
    global currentMonsterHealth, monsterId, player, persistentStats, endlessMode, endlessKills
    if currentMonsterHealth <= 0:
        if persistentStats["reborns_used"] >= 1:
            player["kills_sense_reborn"] += 1
        # Activate Endless Mode when Demon Lord dies
        if currentMonsterFight == "Demon Lord" and not endlessMode:
            endlessMode = True
            endlessKills = 0
            print(Fore.RED + "\n--- ENDLESS MODE UNLOCKED ---")
            print(Fore.MAGENTA + "Demon Lords will now respawn stronger each time.")
            time.sleep(5)

        max_bond = 20 * (persistentStats["reborns_used"] + 1)
        if player["dog_house_purchased"] == True:
            max_bond = (max_bond * 2)
        if tamagatchi_data.get("active") and tamagatchi_data["hunger"] < max_bond:
            if random.random() < 0.2:
                max_bond = 20 * (persistentStats["reborns_used"] + 1)
                if tamagatchi_data["bond"] < max_bond:
                    tamagatchi_data["bond"] += 1
        print(Fore.GREEN + "You defeated the monster!")

        if persistentStats["floor"] >= 30 or persistentStats["reborns_used"] >= 1:
            try_gatcha_drop(1)  # Tries to drop a gatcha pass/ticket

        persistentStats["monsters_killed"] += 1
        
        # Heals the player
        if player["reaper's_token_purchased"] == True:
            player["health"] += round(monster.maxHealth[monsterId] / 3)
            print(Fore.YELLOW + "Your Reaper's Token Glows...")
        else:
            player["health"] += round(monster.maxHealth[monsterId] / 10)
        
        # The player earns some money maybe
        if player["greed's_gullet_purchased"] == True and random.randint(0,1) == 1:
            greedCoins = round(random.uniform(1,2) * 100 * (persistentStats["floor"] / 5))
            player["coins"] += greedCoins
            print(Fore.YELLOW + f"Your greed has manifested {greedCoins} coins!")

        if persistentStats.get("boss_fight_ready", False):
            persistentStats["floor"] += 1
            persistentStats["room"] = 0
            persistentStats["boss_fight_ready"] = False
            persistentStats["loop_times"] = 0
            if persistentStats["floor"] >= 30 or persistentStats["reborns_used"] >= 1:
                try_gatcha_drop(0)
            print(Fore.GREEN + f"You conquered the boss! Now entering floor {persistentStats['floor']}.")

            # Save a backup before progressing to next floor
            print(Fore.BLACK + "|")
            try:
                backup_path = globalSavePath + ".bak"
                save_to_file()  # Save current state
                shutil.copy(globalSavePath, backup_path)
            except Exception as e:
                print(Fore.RED + f"Failed to create backup: {e}")
                time.sleep(2)

            time.sleep(1)
        else:
            persistentStats["room"] += 1

        xp_gain = round(monster.maxHealth[monsterId] / 12, 1)
        if well_data["divine_spark"] > 0:
            xp_gain *= 2
            well_data["divine_spark"] -= 1
            print(Fore.YELLOW + f"The Divine Spark doubles your XP to {xp_gain}!")

        player["xp"] += xp_gain
        try_drop_item()

        if currentMonsterFight == "Demon Lord":
            endlessKills += 1
            print(Fore.MAGENTA + f"Demon Lord defeated! Total defeated: {endlessKills}")
        elif endlessMode:
            endlessKills += 1

        try_portal()
        time.sleep(0.8)
        reset_monster()
        apply_boosts()
    else:
        monster_turn()

def monster_turn():
    global currentMonsterHealth, monsterId, player, persistentStats, endlessMode, endlessKills, monsterAttack
    # Doding and other effects
    if random.randint(0, 100) < player["dodge"]:
        print(Fore.YELLOW + "You dodged the attack!")
    elif player["mirror_pendant_purchased"] == True and monsterAttack == 0:
        print(Fore.CYAN + "The monster's attack glances off of you!")
        time.sleep(0.8)
    # The monsters turn
    else:
        print(Fore.YELLOW + f"{currentMonsterFight} attacks!")
        monsterAttack += 1
        if endlessMode:
            scale = 2 ** endlessKills
            dmg = round(random.uniform(demon_lord_data["minDamage"], demon_lord_data["maxDamage"]) * scale - player["defense"],2)
        else:
            dmg = round(random.uniform(monster.minDamage[monsterId], monster.maxDamage[monsterId]) - player["defense"],2)

        # Scales the damage with the difficulty
        if player["difficulty"] == "easy":
            dmg = round(dmg * 0.75,2)
        if player["difficulty"] == "normal":
            dmg = round(dmg * 1,2)
        if player["difficulty"] == "hard":
            dmg = round(dmg * 1.5,2)
        if player["difficulty"] == "impossible":
            dmg = round(dmg * 2,2)
        else:
            dmg = round(dmg * 1,2)
            
        if dmg <= 1: # Ensures negative damage is never delt
            damagechance = random.randint(0,100)
            if damagechance >= 50: # 50% Chance to not take damage
                dmg = 0
                print(Fore.CYAN + f"The {currentMonsterFight}'s attack glances off of you!")
            else:
                dmg = 1

        player["health"] -= dmg
        print(Fore.RED + f"{currentMonsterFight} deals {dmg} damage!")
        if player["soul_mirror_purchased"] == True: # Damage reflection
            dmgReflect = round(dmg * .25,1)
            currentMonsterHealth -= dmgReflect
            if currentMonsterHealth <= 1:
                currentMonsterHealth = 1
            print(Fore.YELLOW + f"Your soul mirror reflects {dmgReflect} damage back onto the {currentMonsterFight}")
        time.sleep(0.8)

# Main Functions
def combat():
    global currentMonsterHealth, monsterId, player, persistentStats, endlessMode, endlessKills

    while True:
        show_combat_stats()
        save_to_file()

        # Handle boss prompt if room is at 10 and not already in a boss fight
        if persistentStats["room"] >= 10 and persistentStats["boss_fight_ready"] is False:
            print(Fore.YELLOW + "A powerful presence blocks your path... Boss fight?")
            choice = input(Fore.GREEN + "Do you wish to challenge it? (yes/no) > ").strip().lower()
            if persistentStats["loop_times"] >= 3:
                print(Fore.RED + "You can't ignore this fight any longer...")
                time.sleep(0.8)
                persistentStats["boss_fight_ready"] = True
                reset_monster()
            else:
                if choice in ["yes", "y", "", "confirm"]:
                    if choice == "":
                        print(Fore.RED + "(Not typing anything counts as a yes)")
                    persistentStats["boss_fight_ready"] = True
                    reset_monster()
                else:
                    print(Fore.RED + "You chose to wait and reset the floor.")
                    print(Fore.YELLOW + "You may reset", str(2 - persistentStats["loop_times"]), "more times!")
                    persistentStats["room"] = 1
                    persistentStats["loop_times"] += 1
                    reset_monster()
                    time.sleep(1.5)
        else:
            choice = input(Fore.BLUE + "What will you do? ").strip().lower()
            print()

            if choice in ["attack", "atk", ""]:
                update_last_action()
                print(Fore.YELLOW + "You attack!")
                damage = max(1, round(player["damage"] * random.uniform(0.75, 1.25) - currentMonsterDefense, 2))
                currentMonsterHealth -= damage
                print(Fore.RED + f"You dealt {damage} to {currentMonsterFight}.")
                time.sleep(0.2)
                monster_death_check()

            elif choice in ["retreat", "ret", "escape", "esc"]:
                update_last_action()
                if persistentStats.get("boss_fight_ready", False):
                    print(Fore.RED + "You cannot retreat from a boss fight!")
                    time.sleep(1)
                    monster_death_check()
                    continue
                print(Fore.YELLOW + "Attempting to retreat...")
                if player["escape_key_purchased"] == True:
                        print(Fore.YELLOW + "Your escape key activates but you find no loot")
                        persistentStats["escapes_used"] += 1
                        time.sleep(2.2)
                        reset_monster()
                        continue
                elif random.randint(0, 100) < player["escape"]:
                    print(Fore.GREEN + "You successfully escaped!")
                    loot_gain = round(random.uniform(5, (currentMonsterHealth * (persistentStats["reborns_used"] + 1))))
                    print(Fore.CYAN + f"You loot the room on the way out and gain {loot_gain} coins!")
                    player["coins"] += loot_gain
                    persistentStats["escapes_used"] += 1
                    persistentStats["coins_from_escapes"] += loot_gain
                    time.sleep(2.2)
                    reset_monster()
                    continue
                else:
                    print(Fore.RED + "Retreat failed!")
                    monster_turn()

            elif choice in ["level", "lvl", "shop", "shp"]:
                update_last_action()
                level_up()

            elif choice in ["inventory", "inv", "inven"]:
                update_last_action()
                show_inventory()

            elif choice in ["minigames", "mini", "games", "min", "other", "oth"]:
                update_last_action()
                minigame_selection()

            elif choice in ["stats", "st"]:
                update_last_action()
                show_stats_screen()

            elif choice in ["exit", "leave"]:
                save_to_file()
                print(Fore.GREEN + "Saving game...")
                print(Fore.RED + "Exiting...")
                time.sleep(0.1)
                print(Style.RESET_ALL)
                os._exit(0)

            else:
                update_last_action()
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

# Startup code
def startup():
    global currentSaveName, savedGames, globalSavePath, endlessMode, endlessKills

    clear_screen()
    print(Fore.YELLOW + "Console Wars v2.3.3 loaded!")
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
            print(Style.RESET_ALL)
            sys.exit()
        if persistentStats.get("is_dead", False):
            show_stats_screen()
            print(Fore.RED + "\nThis character is dead. You must create a new one.\n")
            print(Style.RESET_ALL)
            sys.exit()
    else:
        print(Fore.YELLOW + f"Creating new save file: {currentSaveName}")

    if currentSaveName not in savedGames:
        print(Fore.YELLOW + "Choose difficulty: Easy / Normal / Hard / Impossible")
        print(Fore.CYAN + "(Difficulty effects monster damage and starting xp)")
        choice = input(Fore.GREEN + "> ").strip().lower()

        if choice in ["easy","eas"]:
            player["difficulty"] = "easy"
            startingXp = 30
        elif choice in ["normal", "norm"]:
            player["difficulty"] = "normal"
            startingXp = 20
        elif choice in ["hard", "drd"]:
            player["difficulty"] = "hard"
            startingXp = 10
        elif choice in ["impossible", "imp"]:
            player["difficulty"] = "impossible"
            startingXp = 0
        else:
            player["difficulty"] = "normal"  # Default to normal
            startingXp = 20
        update_last_action()
        player["xp"] += startingXp
    combat()

if __name__ == "__main__":
    startup() 
