from ObjectsandClassesLibrary import *
count = 1
Genhuman = []
RT_human = []

for i in range (0,4):
    genNPC = character.AutoMaker("Human")
    Genhuman.append(genNPC)
    count += 1
    genNPC = RogueTrader.AutoMaker("Human")
    RT_human.append(genNPC)
    count += 1

print(str(count)+" characters Generated")
count = 1
for chars in Genhuman:
    print('Generic character')
    print("Entry=========="+str(count))
    chars.character_sheet()
    count += 1
for chars in RT_human:
    print('Rogue Trader')
    print("Entry=========="+str(count))
    chars.character_sheet()
    count += 1    

