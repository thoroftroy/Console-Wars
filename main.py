import random
import time
from colorama import Fore, Back, Style
import os
import sys

# Variables
# Player Varibles
class playerValriables:
    name = "Comment"
    baseHealth = 25
    baseDamage = 3.5
    baseDefense = 0
    actionList = ["Attack","Dodge","Retreat","Level"]
    xp = 10
class monsterVariables:
    names = ["Slime","Skeleton","Zombie",]
    maxHealth = [10,20,50]
    maxDamage = [3,  7,12]
    minDamage = [1,  3, 7]
    Defense =   [0.5,  1.2, 3.0]

# Current Variables
currentHealth = playerValriables.baseHealth
currentDamage = playerValriables.baseDamage
currentDefense = playerValriables.baseDefense

monsterId = random.randint(0,len(monsterVariables.names)-1)
currentMonsterFight = monsterVariables.names[monsterId-1]
currentMonsterHealth = monsterVariables.maxHealth[monsterId-1]
currentMonsterDefense = monsterVariables.Defense[monsterId-1]

healthboostCost = 3
damageBoostCost = 3
DefenseBoostCost = 3
dodgeBoostCost = 5
escapeBoostCost = 2

healthboostCostFactor = 1.3
damageBoostCostFactor = 1.4
DefenseBoostCostFactor = 1.9
dodgeBoostCostFactor = 1.9
escapeboostCostFactor = 1.4

healthBoostMod = 5
damageBoostMod = 3
defenseBoostMod = 1
dodgeBoostMod = 50
escapeBoostMod = 25

# Functions
def resetMonster():
    global currentHealth,currentDamage,currentDefense,monsterId,currentMonsterFight,currentMonsterHealth,currentMonsterDefense
    monsterId = random.randint(0,len(monsterVariables.names))
    currentMonsterFight = monsterVariables.names[monsterId-1]
    currentMonsterHealth = monsterVariables.maxHealth[monsterId-1]
    currentMonsterDefense = monsterVariables.Defense[monsterId-1]

def showCombatStats():
    global currentHealth,currentDamage,currentDefense,monsterId,currentMonsterFight,currentMonsterHealth,currentMonsterDefense,dodgeBoostMod,escapeBoostMod
    os.system('cls')
    print(Style.RESET_ALL)
    monsterHealthPercentage = round((currentMonsterHealth / monsterVariables.maxHealth[monsterId-1]) * 100,2)
    print(Fore.WHITE +"You are currently fighting a",currentMonsterFight)
    print(Fore.BLACK +"|")
    print(Fore.RED +currentMonsterFight,"Health:")
    print(Fore.BLACK +"|",end='')
    for i in range(round(monsterHealthPercentage/5)): print(Fore.RED +'=',end='')
    print("",monsterHealthPercentage,"%")
    print(Fore.BLACK +"|")
    print(Fore.BLACK +"|")
    print(Fore.GREEN +"Player Stats:  \n","Health:",currentHealth," |  Damage:",currentDamage, " |  Defense:",currentDefense," |  Xp:",playerValriables.xp)
    print(Fore.GREEN +" Dodge Chance:",dodgeBoostMod,"% |  Retreat Chance:",escapeBoostMod,"%")
    print(Fore.BLUE +"Actions:",playerValriables.actionList)
    print(Style.RESET_ALL)
    
def levelup():
    global currentHealth,currentDamage,currentDefense,monsterId,currentMonsterFight,currentMonsterHealth,currentMonsterDefense,healthboostCost,damageBoostCost,DefenseBoostCost, healthBoostMod, damageBoostMod, defenseBoostMod,dodgeBoostMod,escapeBoostMod, dodgeBoostCost, dodgeBoostCostFactor, escapeBoostCost, escapeboostCostFactor
    os.system('cls')
    print(Style.RESET_ALL)
    print(Fore.BLACK+"|")
    print(Fore.GREEN+"Ugrade Costs (Current Xp:",playerValriables.xp,")")
    print(Fore.GREEN+"Health Boost:",healthboostCost," |  Damage Boost:",damageBoostCost," |  Defense Boost:",DefenseBoostCost," |  Dodge Boost:",dodgeBoostCost," |  Retreat Boost:",escapeBoostCost)
    print(Fore.BLACK+"|")
    print(Fore.BLACK+"|")
    print(Fore.BLUE+"Type 'health', 'damage', 'defense', 'dodge', or 'retreat' to purchase! (Type 'exit' to go back to combat)")
    choice = input().lower()
    if choice == "health":
        if playerValriables.xp >= healthboostCost:
            currentHealth += healthBoostMod
            healthBoostMod = round(healthBoostMod * healthboostCostFactor,1)
            playerValriables.xp -= healthboostCost
            healthboostCost = round(healthboostCost * healthboostCostFactor)
        else:
            print(Fore.RED+"You don't have enough xp for this!")
    elif choice == "damage":
        if playerValriables.xp >= damageBoostCost:
            currentDamage += damageBoostMod
            damageBoostMod = round(damageBoostMod * damageBoostCostFactor,1)
            playerValriables.xp -= damageBoostCost
            damageBoostCost = round(damageBoostCost * damageBoostCostFactor)
        else:
            print(Fore.RED+"You don't have enough xp for this!")
    elif choice == "defense":
        if playerValriables.xp >= DefenseBoostCost:
            currentDefense += defenseBoostMod
            defenseBoostMod = round(defenseBoostMod * DefenseBoostCostFactor,1)
            playerValriables.xp -= DefenseBoostCost
            DefenseBoostCost = round(DefenseBoostCost * DefenseBoostCostFactor)
        else:
            print(Fore.RED+"You don't have enough xp for this!")
    elif choice == "dodge":
        if playerValriables.xp >= dodgeBoostCost:
            if escapeBoostMod >= 90:
                print(Fore.RED+"You can't have a higher dodge chance!")
            else:
                dodgeBoostMod += 2
                playerValriables.xp -= dodgeBoostCost
                dodgeBoostCost = round(dodgeBoostCost * dodgeBoostCostFactor)
        else:
            print(Fore.RED+"You don't have enough xp for this!")
    elif choice == "retreat":
        if playerValriables.xp >= escapeBoostCost:
            if escapeBoostMod >= 90:
                print(Fore.RED+"You can't have a higher retreat chance!")
            else:
                escapeBoostMod += 5
                playerValriables.xp -= escapeBoostCost
                escapeBoostCost = round(escapeBoostCost * escapeboostCostFactor)
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
    global currentHealth,currentDamage,currentDefense,monsterId,currentMonsterFight,currentMonsterHealth,currentMonsterDefense, healthBoostMod,dodgeBoostMod,escapeBoostMod
    dodged = False
    escaped = False
    
    showCombatStats()
    # Player's actions
    choice = input().lower()
    if choice == "attack":
        print(Fore.YELLOW +"You are attacking!")
        damage = round((currentDamage + random.uniform(0,(currentDamage*1.5))) - currentMonsterDefense,2) 
        if damage <= 1:
            damage = 1
        currentMonsterHealth -= damage
        print(Fore.RED +"You dealt",damage,"to",currentMonsterFight)
        time.sleep(0.3)
    elif choice == "dodge":
        print(Fore.YELLOW +"You are attempting to dodge!")
        dodgeChange = random.randrange(0,100)
        if dodgeChange >= dodgeBoostMod:
            print(Fore.YELLOW+"You dodged!")
            dodged = True
        else:
            print(Fore.YELLOW+"You failed to dodge!")
            dodged = False
        time.sleep(0.3)
    elif choice == "retreat":
        print(Fore.YELLOW +"You are attempting to retreat!")
        retreatChance = random.randrange(0,100)
        if retreatChance >= escapeBoostMod:
            print(Fore.YELLOW+"You escaped!")
            escaped = True
        else:
            print(Fore.YELLOW+"You failed to escape!")
            escaped = False
        time.sleep(0.3)
    elif choice == "level":
        levelup()
    elif choice == "exit":
        sys.exit()
    else:
        print(Fore.RED +"Invalid input")
        time.sleep(0.8)
        combat()
    time.sleep(0.5)
    if currentMonsterHealth <= 0:
        print(Fore.GREEN +"You win!")
        currentHealth = round(healthBoostMod+currentHealth,2)
        print(Fore.GREEN+"Healing some health back...")
        playerValriables.xp += round(monsterVariables.maxHealth[monsterId-1]/10)
        resetMonster()
        time.sleep(0.5)
        combat()
    # Section for the monster to fight back
    else:
        if dodged == True:
            time.sleep(0.8)
            combat()
        if escaped == True:
            resetMonster()
        else:
            print(Fore.YELLOW +currentMonsterFight,"is attacking you!")
            damage = round(random.uniform(monsterVariables.minDamage[monsterId-1],monsterVariables.maxDamage[monsterId-1]) - currentDefense,2)
            if damage <= 1:
                damage = 1
            currentHealth = round(currentHealth - damage,2)
            print(Fore.RED +currentMonsterFight,"deals",damage,"damage!")
    if currentHealth <= 0:
        print("You died!")
        time.sleep(1)
        print(Style.RESET_ALL)
        sys.exit()
    else:
        time.sleep(0.8)
        combat()
    
def main():
    print(Style.RESET_ALL)
    os.system('cls')
    combat()

if __name__ == "__main__":
    main()
