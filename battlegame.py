wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

orc_hp = 100
orc_damage = 50

dragon_hp = 300
dragon_damage = 50

while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    print("4) Orc")
    print("5) Exit()")
    character = input("Chose your character: ")
    character = character.capitalize()
    if character == "1" or character == "Wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == "2" or character == "Elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == "3" or character == "Human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    if character == "4" or character == "Orc":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    if character == "5" or character == "Exit":
        exit()
    else:
        print("Unknown character")
print(f"you have chosen the character: {character}!")
print(f"my_hp= {my_hp}")
print(f"my_damage={my_damage}")

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now: ", dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print("The", character, "has been damaged by the dragon")
    print("The", character, "hitpoints are now: ", my_hp)
    if my_hp <= 0:
        print("The", character, "has lost the battle")
        break
