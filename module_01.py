from ObjectsandClassesLibrary import character, RogueTrader
count = 1
Genhuman = []
RT_human = []

for i in range (0,4):
    A = 'Human'
    genNPC = character.AutoMaker(A)
    Genhuman.append(genNPC)
    count += 1
    genNPC = RogueTrader.AutoMaker(A)
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

