from random import randint

# add a dictionary for each pokemon's properties: of name, type, hp, attack, and defesne
# make HP, Attack and Defense all add up to 150 for simplicity
# ie:

# Kanto
Bulbasaur = {'Name': 'Bulbasaur', 'Type': 'Grass', 'HP': 50, 'Attack': 48, 'Defense': 52}
Charmander = {'Name': 'Charmander', 'Type': 'Fire', 'HP': 55, 'Attack': 46, 'Defense': 49}
Squirtle = {'Name': 'Squirtle', 'Type': 'Water', 'HP': 48, 'Attack': 52, 'Defense': 50}

# Johto
Chikorita = {'Name': 'Chikorita', 'Type': 'Grass', 'HP': 50, 'Attack': 48, 'Defense': 52}
Cyndaquil = {'Name': 'Cyndaquil', 'Type': 'Fire', 'HP': 55, 'Attack': 46, 'Defense': 49}
Totodile = {'Name': 'Totodile', 'Type': 'Water', 'HP': 48, 'Attack': 52, 'Defense': 50}

# Sinnoh
Turtwig = {'Name': 'Turtwig', 'Type': 'Grass', 'HP': 50, 'Attack': 48, 'Defense': 52}
Chimchar = {'Name': 'Chimchar', 'Type': 'Fire', 'HP': 55, 'Attack': 46, 'Defense': 49}
Piplup = {'Name': 'Piplup', 'Type': 'Water', 'HP': 48, 'Attack': 52, 'Defense': 50}

# List
pokemonlistKanto = [Bulbasaur, Charmander, Squirtle]
pokemonlistJohto = [Chikorita, Cyndaquil, Totodile]
pokemonlistSinnoh = [Turtwig, Chimchar, Piplup]

totalPkmn = []
totalPkmn.append(pokemonlistKanto)
totalPkmn.append(pokemonlistJohto)
totalPkmn.append(pokemonlistSinnoh)



# since we need to prompt the user three times, making a counter variable

# chosenKanto = False
# chosenJohto = False
# chosenSinnoh = False

# empty list of all three of the player's pokemon
playerspokemon = []
attributeplayerpoke = []
# global PickThree
# PickThree = 1000  # index of pokemon

def youChose():
    PickThree = 1000  # index of pokemon

    chosenKanto = False
    chosenJohto = False
    chosenSinnoh = False
    for i in totalPkmn:
        if (str(i) == str(pokemonlistKanto)):
            print(
                "Pick a Kanto Region Starter Pokemon from the list below. You can only choose one. Enter the number you see next to the Pokemon you want. ")
            print("#1", pokemonlistKanto[0].get('Name'))
            print("#2", pokemonlistKanto[1].get('Name'))
            print("#3", pokemonlistKanto[2].get('Name'))
            PickThree = int(input("\nPick a Pokemon to use in battle! "))
            if PickThree > 3:
                print("error - pick a pokemon from this list")
            print("You have chosen " + i[PickThree - 1].get('Name'))
            playerspokemon.append(pokemonlistKanto[PickThree - 1].get('Name'))
            attributeplayerpoke.append(pokemonlistKanto[PickThree - 1])
            print("Your current pokemon are: ", playerspokemon, "\n")
            chosenKanto = True
            if PickThree > 3:
                chosenKanto = False
            PickThree = 0
        elif (str(i) == str(pokemonlistJohto)):
            print(
                "Pick a Johto Region Starter Pokemon from the list below. You can only choose one. Enter the number you see next to the Pokemon you want. ")
            print("#1", pokemonlistJohto[0].get('Name'))
            print("#2", pokemonlistJohto[1].get('Name'))
            print("#3", pokemonlistJohto[2].get('Name'))
            PickThree = int(input("\nPick a Pokemon to use in battle! "))
            if PickThree > 3:
                print("error - pick a pokemon from this list")
            print("You have chosen " + i[PickThree - 1].get('Name'))
            playerspokemon.append(pokemonlistJohto[PickThree - 1].get('Name'))
            attributeplayerpoke.append(pokemonlistJohto[PickThree - 1])
            print("Your current pokemon are: ", playerspokemon, "\n")
            chosenJohto = True
            if PickThree > 3:
                chosenJohto = False
            PickThree = 0
        elif (str(i) == str(pokemonlistSinnoh)):
            print(
                "Pick a Kanto Region Starter Pokemon from the list below. You can only choose one. Enter the number you see next to the Pokemon you want. ")
            print("#1", pokemonlistSinnoh[0].get('Name'))
            print("#2", pokemonlistSinnoh[1].get('Name'))
            print("#3", pokemonlistSinnoh[2].get('Name'))
            PickThree = int(input("\nPick a Pokemon to use in battle! "))
            if PickThree > 3:
                print("error - pick a pokemon from this list")
            print("You have chosen " + i[PickThree - 1].get('Name'))
            playerspokemon.append(pokemonlistSinnoh[PickThree - 1].get('Name'))
            attributeplayerpoke.append(pokemonlistSinnoh[PickThree - 1])
            print("Your current pokemon are: ", playerspokemon, "\n")
            chosenSinnoh = True
            if PickThree > 3:
                chosenSinnoh = False
            PickThree = 0
        if chosenKanto is True and chosenJohto is True and chosenSinnoh is True:
            break
    print("The Pokemon you chose are: ", playerspokemon)
    print('Here\'s some more information: ')
    for i in playerspokemon:
        ind = playerspokemon.index(i)
        print(playerspokemon[ind], attributeplayerpoke[ind])

    mybattlepoke = ''  # empty string, represents the pokemon used at the battle
    pokeindex = 5

    while pokeindex > 2:
        pokeindex = int(input(
            "\nNow pick ONE of these to use in battle: " + "#1 " + playerspokemon[0] + ", " + "#2 " +
            playerspokemon[
                1] + ", and " + "#3 " + playerspokemon[2] +
            ". Enter the number... "))
        if pokeindex == 1:
            mybattlepoke = playerspokemon[0]
        elif pokeindex == 2:
            mybattlepoke = playerspokemon[1]
        elif pokeindex == 3:
            mybattlepoke = playerspokemon[2]
        else:
            print('error : choose one from the list')
            continue
        print(mybattlepoke)
        print(pokeindex)
        pokeindex = 0
    print("You have picked... " + mybattlepoke + "! Best of luck!")
    return mybattlepoke

def compChose():
    global compKanto
    global compJohto
    global compSinnoh

    compsPkmn = []
    attributeCompPkmn = []

    compbattlepoke = ''  # empty string, represents the pokemon used at the battle

    for i in totalPkmn:
        if (str(i) == str(pokemonlistKanto)):
            k = randint(0, 2)
            compsPkmn.append(pokemonlistKanto[k].get('Name'))
            attributeCompPkmn.append(pokemonlistKanto[k])
            compKanto = True
        elif (str(i) == str(pokemonlistJohto)):
            j = randint(0, 2)
            compsPkmn.append(pokemonlistJohto[j].get('Name'))
            attributeCompPkmn.append((pokemonlistJohto[j]))
            compJohto = True
        elif (str(i) == str(pokemonlistSinnoh)):
            s = randint(0, 2)
            compsPkmn.append(pokemonlistSinnoh[s].get('Name'))
            attributeCompPkmn.append(pokemonlistSinnoh[s])
            compSinnoh = True
    print("\nThe opponent's Pokemon are", compsPkmn)


    i = randint(0, 2)
    compbattlepoke = compsPkmn[i]
    print(f"The opponent chose {compbattlepoke}")

    return compbattlepoke

def usrAttacks():
    f = 0

def enemyAttack():
    m = 0


def battle():
    user = youChose()
    enemy = compChose()
    print("Your Pokemon, a " + user, "encountered a " + enemy)
    if user == "Bulbasaur":
        myHP = Bulbasaur.get('HP')
        print(myHP)
    return enemy

def runGame():
    battle()



runGame()