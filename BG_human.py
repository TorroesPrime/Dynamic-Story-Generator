import random
from import3 import *
from library import *

def BackGroundSelector():
    CharBG = {"Homeworld Type":"","Homeworld":"","Birth Right":"","Lure of the Void":"","Trial":"","Motive":""}
    CharBG['Homeworld Type'] = random.choice(homeworld)
    selectHW = ""
    selectBR = ""
    selectVL = ""
    selectTrial = ""
    selectMotive = ""
    if selectHW == "Death World":
        selectBR = random.choice(birthright_1)
        CharBG['Homeworld'] = random.choice(DeathWorldNames)
    elif selectHW == "Void Born":
        selectBR = random.choice(birthright_2)
        CharBG['Homeworld'] = random.choice(VoidBornNames)
    elif selectHW == "Forge World":
        selectBR = random.choice(birthright_3)
        CharBG['Homeworld'] = random.choice(ForgeWorldNames)
    elif selectHW == "Hive World":
        selectBR = random.choice(birthright_4)
        CharBG['Homeworld'] = random.choice(HiveWorldNames)
    elif selectHW == "Imperial World":
        selectBR = random.choice(birthright_5)
        CharBG['Homeworld'] = random.choice(ImpWorldNames)
    else:
        selectBR = random.choice(birthright_6)
        CharBG['Homeworld'] = random.choice(NobleBornWorldNames)
    
    CharBG['Birth Right'] = selectBR
    if selectBR == "Scavenger":
        selectVL = random.choice(voidLure_1)
    elif selectBR == "Scapegrace":
        selectVL = random.choice(voidLure_2)
    elif selectBR == "Stubjack":
        selectVL = random.choice(voidLure_3)
    elif selectBR == "Child of the Creed":
        selectVL = random.choice(voidLure_4)
    elif selectBR == "Savant":
        selectVL = random.choice(voidLure_5)
    else:
        selectVL = random.choice(voidLure_6)
    CharBG['Lure of the Void'] = selectVL
    if selectVL == "Tainted":
        selectTrial = random.choice(trials_1)
    elif selectVL == "Criminal":
        selectTrial = random.choice(trials_2)
    elif selectVL == "Renegade":
        selectTrial = random.choice(trials_3)
    elif selectVL == "Duty Bound":
        selectTrial = random.choice(trials_4)
    elif selectVL == "Zealot":
        selectTrial = random.choice(trials_5)
    else:
        selectTrial = random.choice(trials_6)
    CharBG['Trial'] = selectTrial
    if selectTrial == "The Hand of war":
        selectMotive = random.choice(motives_1)
    elif selectTrial == "Press-Ganged":
        selectMotive = random.choice(motives_2)
    elif selectTrial == "Calamity":
        selectMotive = random.choice(motives_3)
    elif selectTrial == "Ship Lorn":
        selectMotive = random.choice(motives_4)
    elif selectTrial == "Dark Voyage":
        selectMotive = random.choice(motives_5)
    else:
        selectMotive = random.choice(motives_6)
    CharBG['Motive'] = selectMotive
    #print("Homeworld: "+selectHW)
    #print("Birth Right: "+selectBR)
    #print("Lure of the Void: "+selectVL)
    #print("Trial: "+selectTrial)
    #print("Motive: "+selectMotive)
    #for key in CharBG:
    #    print(key+": "+CharBG[key])
    
    
    
BackGroundSelector()
