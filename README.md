# Dynamic Story Generator

So this is a learning project that started out as an effort to build a program that could A- Randomly generate the materials or B- allow a user to select the materials for a  Character Sheet based on the Death Watch RPG. The goals of the project have grown and it is now being used to develop a program that will generate multiple characters, load an external system that will then use the generated/supplied characters to proceed through a series of action based tests and use the result of those tests to build a story piece by piece.

## Example of what it will do

You have a character who's stats have been generated. We'll say the character is 'Invictus'. The character Invictus is then called on to make a weapon skill test agaisnt a target drone.
if the attack is passed the program would generate the follow passage:
"Invictus brought the sword around in a downward slash, bifurcating the target drone in a flurry of sparks, the image of a cultist being projected by it momentarily showing the simulated injury of having been sliced from left shoulder to right hip before flickering out of existence."
if the attack is failed the program would generate the follow passage:
"The heft of the sword sliced through nothing but air, the combined weight of the weapon and the inertia of the failed attack pulling Invictus off balance. The cogitator controlling the target drone having calculated that the cultist would be able to dodge Invictus' attack."

## Background information and rules

Whenever a character is called on to do something, that is referred to has a 'test'. A test is conducted by generating a number between 1 and 100, and comparing that to the skill or attribute being tested on. If the number generated is higher then the skill or characteristic being tested, the tast is 'failed'. If the number generated is lower the test is passed. The difference between the two numbers is then %10 and that number is returned as the degree of success/failure. Sometimes it will need to be known by how much the character passed or failed. 

Example:
Invictus has a Weapon Skill of 39. the generated number is 53. 

All characters have 12 characteristics:
1. Weapon Skill: the characters ability with melee weapon
2. Ballistic Skill: the characters ability to shoot a weapon
3. Strength: A character's strength
4. Toughness: How capable a character is of ignoring damage
5. Agility: How fast the character is.
6. Intelligence: How intelligent the character is
7. Perception: A rating of the characters ability to notice the world around them.
8. Will Power: how mentally resilient a character is
9. Fellowship: A rating of the characters charisma.
10. Wounds: the number of wounds a character can take before being killed.
11. Fatigue: a rating of how tired a character is.
12. Insanity: a rating of how insane a character has been driven by events.

All characters have the following attributes:
1. Race
2. Name
3. Gender
4. A selection of skills
5. An inventory 

All characters that are race 'Space Marine' are gender == 'male' and have the following Attributes:
1. Chapter
all Characters have a class. Class is affected by race, and gender and may be affected by chapter if character is a space marine.

All characters that are race 'Human' and class 'Rogue Trader' have the following Attributes:
1. Title
if a Rogue Trader gender == 'female' they may not have the following titles:
1. Duke
2. Lord
3. Baron
if a Rogue Trader gender == 'female' they may have the following titles:
1. Duchess
2. Lady
3. Damme 
4. Barroness
if a Rogue Trader gender == 'male' they may not have the following titles:
1. Lady
2. Duchess
3. Dame
4. Barroness
if a Rogue Trader gender == 'male' they may have the following titles:
1. Duke
2. Lord
3. Baron

All characters have a bonus for each of their characteristics that is determined by take the generated stat, and % it by 10. 
Example: Ballistic Skill of 39 would have a Ballistic Skill Bonus of 3

All characters can perform the following actions:
1. characteristic test
2. skill test

## Step by step process explination
### Generating characters with no supplied information or specifications
1. Randomly select race by selecting string from list of availible races
2. Randomly select select class by selecting string from list of availible classes. Lists vary by race.
3. Randomly Select Gender
3a. if race = 'Space Marine' set gender to 'male'
4. Randomly select name from list of names
4a. if class = 'Rogue Trader' and gender = 'male', randomly select first name from maleFirstNames list.
4b. if class = 'Rogue Trader' and gender = 'female', randomly select first name from femaleFirstNames list.
4c. if class = 'Rogue Trader', randomly select last name from humanLastNames list.
4d. if race = 'Space Marine', randomly select chapter from list.
4c1. if chapter = 'Blood Angels' randomly select name from BloodAngelsNames list 
4c2. if chapter = 'Space Wolves' randomly select name from SpaceWolvesNames list
4c3. if chapter = 'Dark Angels' randomly select name from DarkAngelsNames list
4c4. if chapter = 'Ultramarines' randomly select name from UltramarinesNames list
4c5. if chapter = 'BlackTemplars' randomly select name from BlackTemplarsNames list
5. Randomly generate integer for Ballistic Skill characteristic
6. Randomly generate integer for Weapon Skill characteristic
7. Randomly generate integer for Strength characteristic
8. Randomly generate integer for Toughness characteristic
9. Randomly generate integer for Agility characteristic
10. Randomly generate integer for Intelligence characteristic
11. Randomly generate integer for Perception characteristic
12. Randomly generate integer for Fellowship characteristic
13. Randomly generate integer for wounds characteristic
14. set fatigue to 0
15. fill out skill listing.
- what skills a character has, and what level those skills are will vary based on race and class.

