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
counter = 1
chosenKanto = False
chosenJohto = False
chosenSinnoh = False
compKanto = False
compJohto = False
compSinnoh = False
# validInput = False

# empty list of all three of the player's pokemon
playerspokemon = []
attributeplayerpoke = [] #list of dictionary

compsPkmn = []
attributeCompPkmn = []


mybattlepoke = ''
compbattlepoke = ''  # empty string, represents the pokemon used at the battle

mytype = ''
comptype = ''

class User(object):
    def __init__(self, myname):
        self.myname = myname

    def list_pokemon(self):
        global chosenKanto
        global chosenJohto
        global chosenSinnoh
        global mybattlepoke
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
        self.remainingpokemonlist = pokemonlist
        self.battlepokeuser = mybattlepoke
        return mybattlepoke

class Computer(object):
    def __init__(self, opponentname):
        self.opponentname = opponentname
    def set_pokemon(self):
        computerspokemon = []
        computersbattlepoke = ''
        global compKanto
        global compJohto
        global compSinnoh
        global compbattlepoke

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
        print("The opponent's Pokemon are", compsPkmn)

        i = randint(0, 2)
        compbattlepoke = compsPkmn[i]
        print(f"The opponent chose {compbattlepoke}")
        self.compbattlepoke = compbattlepoke
        return compbattlepoke
    #calling function now
    #set_pokemon(object)

# WORKING UP TO HERE
class Pokemon(object):
    def __init__(self, name, HP, AP, type):
        self.name = name
        self.HP = HP
        self.AP = AP
        self.type = type

    def get_attack_power(self):
        return self.name + " has " + str(self.AP) + " AP."

    def heal(self):
        HP = self.HP + 20
        return "You have now refilled your energy. You now have " + str(HP) + " HP."


class Grass(Pokemon):
    def __init__(self, name, HP, AP, type):
        Pokemon.__init__(self, name, HP, AP, type)
    def set_type(self):
        return self.name + " is of type Grass."
    def set_attacks(self):
        self.grassattacks_dict = {
            'Leaf Storm' : '130 power',
            'Mega Drain' : '50 power',
            'Razor Leaf' : '55 power'
        }
class Water(Pokemon):
    def __init__(self, name, HP, AP, type):
        Pokemon.__init__(self, name, HP, AP, type)
    def set_type(self):
        return self.name + " is of type Water."
    def set_attacks(self):
        self.waterattacks_dict = {
            'Bubble' : '40 power',
            'Hydro Pump' : '185 power',
            'Surf' : '70 power'
        }


class Fire(Pokemon):
    def __init__(self, name, HP, AP, type):
        Pokemon.__init__(self, name, HP, AP, type)
    def set_type(self):
        return self.name + " is of type Fire."
    def set_attacks(self):
        self.fireattacks_dict = {
            'Ember' : '60 power',
            'Fire Punch' : '85 power',
            'Flame Wheel' : '70 power'
        }


def userattacking():
    global mybattlepoke, mytype
    global compbattlepoke, comptype
    global myAP, myHP
    global compAP, compHP

    if mybattlepoke in ['Bulbasaur','Chikorita','Turtwig']:
        mytype = "Grass" 
    if mybattlepoke in ['Charmander','Cyndaquil','Chimchar']:
        mytype = "Fire"
    if mybattlepoke in ['Squirtle','Totodile','Piplup']:
        mytype = "Water"
        

    if mybattlepoke == "Bulbasaur":
        myHP = Bulbasaur.get('HP')
        myAP = Bulbasaur.get('AP')
    if mybattlepoke == 'Chikorita':
        myHP = Chikorita.get('HP')
        myAP = Chikorita.get('AP')
    if mybattlepoke == 'Turtwig':
        myHP = Turtwig.get('HP')
        myAP = Turtwig.get('AP')
    if mybattlepoke == 'Charmander':
        myHP = Charmander.get('HP')
        myAP = Charmander.get('AP')
    if mybattlepoke == 'Cyndaquil':
        myHP = Cyndaquil.get('HP')
        myAP = Cyndaquil.get('AP')
    if mybattlepoke == 'Chimchar':
        myHP = Chimchar.get('HP')
        myAP = Cyndaquil.get('AP')
    if mybattlepoke == 'Squirtle':
        myHP = Squirtle.get('HP')
        myAP = Squirtle.get('AP')
    if mybattlepoke == 'Totodile':
        myHP = Totodile.get('HP')
        myAP = Totodile.get('AP')
    if mybattlepoke == 'Piplup':
        myHP = Piplup.get('HP')
        myAP = Piplup.get('AP')


    # if mybattlepoke == Bulbasaur or Psyduck:
    #     myAP = 40
    # if mybattlepoke == Bellsprout:
    #     myAP = 60
    # if mybattlepoke == Ninetails or Polywag or Oddish:
    #     myAP = 50
    # if mybattlepoke == Charmander:
    #     myAP = 70
    # if mybattlepoke == Ponyta:
    #     myAP = 60
    # if mybattlepoke == Squirtle:
    #     myAP = 20

    compbattlepoke = computer.compbattlepoke
    if compbattlepoke in ['Bulbasaur','Bellsprout','Oddish']:
        comptype = "Grass"
    if compbattlepoke in ['Charmander','Ninetails','Ponyta']:
        comptype = "Fire"
    if compbattlepoke in ['Polywag','Psyduck','Squirtle']:
        comptype = "Water"
    print(compbattlepoke)

    print('Your type is: ', mytype)
    print("Your opponent's type is: " + comptype)

    if compbattlepoke == "Bulbasaur":
        compHP = Bulbasaur.get('HP')
        compAP = Bulbasaur.get('AP')
    if compbattlepoke == 'Chikorita':
        compHP = Chikorita.get('HP')
        compAP = Chikorita.get('AP')
    if compbattlepoke == 'Turtwig':
        compHP = Turtwig.get('HP')
        compAP = Turtwig.get('AP')
    if compbattlepoke == 'Charmander':
        compHP = Charmander.get('HP')
        compAP = Charmander.get('AP')
    if compbattlepoke == 'Cyndaquil':
        compHP = Cyndaquil.get('HP')
        compAP = Cyndaquil.get('AP')
    if compbattlepoke == 'Chimchar':
        compHP = Chimchar.get('HP')
        compHP = Cyndaquil.get('AP')
    if compbattlepoke == 'Squirtle':
        compHP = Squirtle.get('HP')
        compAP = Squirtle.get('AP')
    if compbattlepoke == 'Totodile':
        compHP = Totodile.get('HP')
        compAP = Totodile.get('AP')
    if compbattlepoke == 'Piplup':
        compHP = Piplup.get('HP')
        compAP = Piplup.get('AP')

    # if compbattlepoke == Bulbasaur:
    #     compHP = 60
    # if compbattlepoke == Bellsprout:
    #     compHP = 40
    # if compbattlepoke == Oddish or Polywag:
    #     compHP = 50
    # if compbattlepoke == Charmander:
    #     compHP = 25
    # if compbattlepoke == Ninetails:
    #     compHP = 30
    # if compbattlepoke == Ponyta:
    #     compHP = 40
    # if compbattlepoke == Squirtle:
    #     compHP = 80
    # if compbattlepoke == Psyduck:
    #     compHP = 70

    # if compbattlepoke == Bulbasaur or Psyduck:
    #     compAP = 40
    # if compbattlepoke == Bellsprout:
    #     compAP = 60
    # if compbattlepoke == Ninetails or Polywag or Oddish:
    #     compAP = 50
    # if compbattlepoke == Charmander:
    #     compAP = 70
    # if compbattlepoke == Ponyta:
    #     compAP = 60
    # if compbattlepoke == Squirtle:
    #     compAP = 50

    grassattacks_dict = {
        'Leaf Storm' : 130,
        'Mega Drain' : 50,
        'Razor Leaf' : 55
        }
    waterattacks_dict = {
        'Bubble' : 40,
        'Hydro Pump' : 185,
        'Surf' : 70
        }
    fireattacks_dict = {
        'Ember' : 60,
        'Fire Punch' : 85,
        'Flame Wheel' : 70
        }

    if (mytype == comptype and comptype == "Fire"):
        print("Entering same Fire")
        print(fireattacks_dict)
        mymove = input("What move do you want from this ")
        if mymove == 'Ember':
            damage = 0
            if fireattacks_dict['Ember'] >= myAP:
                damage = myAP
            if fireattacks_dict['Ember'] < myAP:
                damage = fireattacks_dict['Ember']

            compHP = compHP - damage
            if compHP <= 0:
                print("Computer Pokemon has fainted. Now, you have won. Computer will switch now.")
            if compHP > 0:
                print("Computer Pokemon was hit.. Now it is Computer's turn")
            print("Pokemon\tHP\n remaining")
            print(str(compbattlepoke) + "\t" + str(compHP)
            print(str(mybattlepoke) + "\t" + str(myHP))


        if mymove == 'Fire Punch':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)

            if accurpercentage <= 7:
                if fireattacks_dict['Fire Punch'] >= myAP:
                    damage = myAP
                if fireattacks_dict['Fire Punch'] < myAP:
                    damage = fireattacks_dict['Fire Punch']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)

        if mymove == 'Flame Wheel':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)
            if accurpercentage <= 8:
                if fireattacks_dict['Flame Wheel'] >= myAP:
                    damage = myAP
                if fireattacks_dict['Flame Wheel'] < myAP:
                    damage = fireattacks_dict['Flame Wheel']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)

    if (mytype == comptype and comptype == "Water"):
        print waterattacks_dict
        mymove = raw_input("What move do you want from this ")
        if mymove == 'Bubble':
            damage = 0
            if waterattacks_dict['Bubble'] >= myAP:
                damage = myAP
            if waterattacks_dict['Bubble'] < myAP:
                damage = waterattacks_dict['Bubble']

            compHP = compHP - damage
            if compHP <= 0:
                print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
            if compHP > 0:
                print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


        if mymove == 'Hydro Pump':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)

            if accurpercentage <= 2:
                if waterattacks_dict['Hydro Pump'] >= myAP:
                    damage = myAP
                if waterattacks_dict['Hydro Pump'] < myAP:
                    damage = waterattacks_dict['Hydro Pump']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)

        if mymove == 'Surf':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)
            if accurpercentage <= 8:
                if waterattacks_dict['Surf'] >= myAP:
                    damage = myAP
                if waterattacks_dict['Surf'] < myAP:
                    damage = waterattacks_dict['Surf']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


    if (mytype == comptype and comptype == "Grass"):
        print grassattacks_dict
        mymove = raw_input("What move do you want from this ")
        if mymove == 'Mega Drain':
            damage = 0
            if grassattacks_dict['Mega Drain'] >= myAP:
                damage = myAP
            if grassattacks_dict['Mega Drain'] < myAP:
                damage = grassattacks_dict['Mega Drain']

            compHP = compHP - damage
            if compHP <= 0:
                print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
            if compHP > 0:
                print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


        if mymove == 'Leaf Storm':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)

            if accurpercentage <= 8:
                if grassattacks_dict['Leaf Storm'] >= myAP:
                    damage = myAP
                if grassattacks_dict['Leaf Storm'] < myAP:
                    damage = grassattacks_dict['Leaf Storm']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


        if mymove == 'Razor Leaf':
            damage = 0
            import random
            accuracy = random.uniform(0, 10)
            accurpercentage = float(accuracy)
            if accurpercentage <= 9.5:
                if grassattacks_dict['Razor Leaf'] >= myAP:
                    damage = myAP
                if grassattacks_dict['Razor Leaf'] < myAP:
                    damage = grassattacks_dict['Razor Leaf']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


    if (mytype == "Grass" and comptype == "Water"):
        print grassattacks_dict
        mymove = raw_input("What move do you want from this ")
        if mymove == 'Mega Drain':
            damage = 0
            if (grassattacks_dict['Mega Drain']*1.5) >= myAP:
                damage = myAP
            if (grassattacks_dict['Mega Drain']*1.5) < myAP:
                damage = grassattacks_dict['Mega Drain']

            compHP = compHP - damage
            if compHP <= 0:
                print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
            if compHP > 0:
                print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


        if mymove == 'Leaf Storm':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)

            if accurpercentage <= 8:
                if (grassattacks_dict['Leaf Storm']*1.5) >= myAP:
                    damage = myAP
                if (grassattacks_dict['Leaf Storm']*1.5) < myAP:
                    damage = grassattacks_dict['Leaf Storm']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


        if mymove == 'Razor Leaf':
            damage = 0
            import random
            accuracy = random.uniform(0, 10)
            accurpercentage = float(accuracy)
            if accurpercentage <= 9.5:
                if (grassattacks_dict['Razor Leaf']*1.5) >= myAP:
                    damage = myAP
                if (grassattacks_dict['Razor Leaf']*1.5) < myAP:
                    damage = grassattacks_dict['Razor Leaf']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


    if (mytype == "Grass" and comptype == "Fire"):
        print grassattacks_dict
        mymove = raw_input("What move do you want from this ")
        if mymove == 'Mega Drain':
            damage = 0
            if grassattacks_dict['Mega Drain'] >= (myAP*1.5):
                damage = myAP
            if (grassattacks_dict['Mega Drain']*1.5) < (myAP*1.5):
                damage = grassattacks_dict['Mega Drain']

            compHP = compHP - damage
            if compHP <= 0:
                print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
            if compHP > 0:
                print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


        if mymove == 'Leaf Storm':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)

            if accurpercentage <= 8:
                if (grassattacks_dict['Leaf Storm']*1.5) >= (myAP*1.5):
                    damage = myAP
                if (grassattacks_dict['Leaf Storm']*1.5) < (myAP*1.5):
                    damage = grassattacks_dict['Leaf Storm']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


        if mymove == 'Razor Leaf':
            damage = 0
            import random
            accuracy = random.uniform(0, 10)
            accurpercentage = float(accuracy)
            if accurpercentage <= 9.5:
                if (grassattacks_dict['Razor Leaf']*1.5) >= (myAP*1.5):
                    damage = myAP
                if (grassattacks_dict['Razor Leaf']*1.5) < (myAP*1.5):
                    damage = grassattacks_dict['Razor Leaf']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


    if (mytype == "Water" and comptype == "Fire"):
        print waterattacks_dict
        mymove = raw_input("What move do you want from this ")
        if mymove == 'Bubble':
            damage = 0
            if (waterattacks_dict['Bubble']*1.5) >= myAP:
                damage = myAP
            if (waterattacks_dict['Bubble']*1.5) < myAP:
                damage = waterattacks_dict['Bubble']

            compHP = compHP - damage
            if compHP <= 0:
                print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
            if compHP > 0:
                print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


        if mymove == 'Hydro Pump':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)

            if accurpercentage <= 2:
                if (waterattacks_dict['Hydro Pump']*1.5) >= myAP:
                    damage = myAP
                if (waterattacks_dict['Hydro Pump']*1.5) < myAP:
                    damage = waterattacks_dict['Hydro Pump']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


        if mymove == 'Surf':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)
            if accurpercentage <= 8:
                if (waterattacks_dict['Surf']*1.5) >= myAP:
                    damage = myAP
                if (waterattacks_dict['Surf']*1.5) < myAP:
                    damage = waterattacks_dict['Surf']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)

    print mytype, comptype
    if (mytype == "Water" and comptype == "Grass"):
        print waterattacks_dict
        mymove = raw_input("What move do you want from this ")
        if mymove == 'Bubble':
            damage = 0
            if waterattacks_dict['Bubble'] >= (myAP*1.5):
                damage = myAP
            if waterattacks_dict['Bubble'] < (myAP*1.5):
                damage = waterattacks_dict['Bubble']

            compHP = compHP - damage
            if compHP <= 0:
                print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
            if compHP > 0:
                print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


        if mymove == 'Hydro Pump':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)

            if accurpercentage <= 2:
                if waterattacks_dict['Hydro Pump'] >= (myAP*1.5):
                    damage = myAP
                if waterattacks_dict['Hydro Pump'] < (myAP*1.5):
                    damage = waterattacks_dict['Hydro Pump']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


        if mymove == 'Surf':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)
            if accurpercentage <= 8:
                if waterattacks_dict['Surf'] >= (myAP*1.5):
                    damage = myAP
                if waterattacks_dict['Surf'] < (myAP*1.5):
                    damage = waterattacks_dict['Surf']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


    if (mytype == "Fire" and comptype == "Water"):
        print fireattacks_dict
        mymove = raw_input("What move do you want from this ")
        if mymove == 'Ember':
            damage = 0
            if fireattacks_dict['Ember'] >= (myAP*1.5):
                damage = myAP
            if fireattacks_dict['Ember'] < (myAP*1.5):
                damage = fireattacks_dict['Ember']

            compHP = compHP - damage
            if compHP <= 0:
                print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
            if compHP > 0:
                print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


        if mymove == 'Fire Punch':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)

            if accurpercentage <= 7:
                if fireattacks_dict['Fire Punch'] >= (myAP*1.5):
                    damage = myAP
                if fireattacks_dict['Fire Punch'] < (myAP*1.5):
                    damage = fireattacks_dict['Fire Punch']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)

        if mymove == 'Flame Wheel':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)
            if accurpercentage <= 8:
                if fireattacks_dict['Flame Wheel'] >= (myAP*1.5):
                    damage = myAP
                if fireattacks_dict['Flame Wheel'] < (myAP*1.5):
                    damage = fireattacks_dict['Flame Wheel']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)

    if (mytype == "Fire" and comptype == "Grass"):
        print fireattacks_dict
        mymove = raw_input("What move do you want from this ")
        if mymove == 'Ember':
            damage = 0
            if (fireattacks_dict['Ember']*1.5) >= myAP:
                damage = myAP
            if (fireattacks_dict['Ember']*1.5) < myAP:
                damage = fireattacks_dict['Ember']

            compHP = compHP - damage
            if compHP <= 0:
                print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
            if compHP > 0:
                print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)


        if mymove == 'Fire Punch':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)

            if accurpercentage <= 7:
                if (fireattacks_dict['Fire Punch']*1.5) >= myAP:
                    damage = myAP
                if (fireattacks_dict['Fire Punch']*1.5) < myAP:
                    damage = fireattacks_dict['Fire Punch']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print str(mybattlepoke) + "\t" + str(myHP)

        if mymove == 'Flame Wheel':
            damage = 0
            import random
            accuracy = random.choice('0123456789')
            accurpercentage = int(accuracy)
            if accurpercentage <= 8:
                if (fireattacks_dict['Flame Wheel']*1.5) >= myAP:
                    damage = myAP
                if (fireattacks_dict['Flame Wheel']*1.5) < myAP:
                    damage = fireattacks_dict['Flame Wheel']

                compHP = compHP - damage
                if compHP <= 0:
                    print "Computer Pokemon has fainted. Now, you have won. Computer will switch now."
                if compHP > 0:
                    print "Computer Pokemon was hit.. Now it is Computer's turn"                    
            else:
                print "This attack failed."
            print "Pokemon\tHP\n remaining"
            print str(compbattlepoke) + "\t" + str(compHP)
            print(str(mybattlepoke) + "\t" + str(myHP))




remainingpokemonlist = []
battlepokeuser = ''
compbattlepoke = ''

pokemonlist = ["Bulbasaur" , "Bellsprout" , "Oddish" , "Charmander" , "Ninetails" , "Ponyta" , "Squirtle" , "Psyduck" , "Polywag"]


action = ''

Bulbasaur = Grass("Bulbsaur", 60, 40, "Grass")
Bellsprout = Grass("Bellsprout", 40, 60, "Grass")
Oddish = Grass("Oddish", 50, 50, "Grass")

Squirtle = Water('Squirtle', 80, 20, 'Water')
Psyduck = Water("Psyduck", 70, 40, "Water")
Polywag = Water("Polywag", 50, 50, "Water")

Charmander = Fire("Charmander", 25, 70, "Fire")
Ninetails = Fire("Ninetails", 30, 50, "Fire")
Ponyta = Fire("Ponyta", 40, 60, "Fire")


#initialization statements and game instructions
print "Hello!"
print "Welcome to Pokemon by Anirudh Iyer! You will pick 3 Pokemon and then pick one to battle with!"
print "Then you'll go against your opponent! There are 3 possible moves, attack, switch, or heal."
print "Good luck!\n"

#getting user name and opponent name

myname = input("What is your name? ")
user = User(myname)
user.list_pokemon()

#more initialization
opponentname = input("What is your opponent's name? ")
print("\nReady? You, " + myname + " are going against the world-renowned Python Pokemoner, " + opponentname + "!\n")

computer=Computer(opponentname)
computer.set_pokemon()

# let the game begin
print('starting game')
continuegame = 1

while continuegame == 1:
    userattacking()
    #computerattacking()
    continuegame=input("Continue ? 1:YES 0:No ")
    
print("Ending game")