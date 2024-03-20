import battlesim as pokesim

import pokemon as poke

import time

import random


def main():

    flag = True
    print("player one, pick a pokemon: \n")
    for i, x in enumerate(poke.pokemon, start=1):
        print(f"{i}. {x}")

    player1_pokemon = input("Enter the number of the pokemon you want.")

    

    print("player two, pick a pokemon: \n")
    for i, x in enumerate(poke.pokemon, start=1):
        print(f"{i}. {x}")

    player2_pokemon = input("Enter the number of the pokemon you want.")

    poke1 = poke.pokemon[int(player1_pokemon)-1]
    poke2 = poke.pokemon[int(player2_pokemon)-1]
    print("player one, you have chosen: " + poke1.name)
    print("player two, you have chosen: " + poke2.name)


    print("player one: Go! " + poke1.name + "\n")
    time.sleep(2)
    print("player two: Go! " + poke2.name + "\n")
    time.sleep(2)

    while(flag):

        #determine fastest pokemon
        

        if(poke2.spd> poke1.spd):
            temp = poke1
            poke1 = poke2
            poke2 = temp
        elif(poke2.spd == poke2.spd):
            tiebreaker = random.randint(1,2)
            if(tiebreaker == 2):
                temp = poke1
                poke1 = poke2
                poke2 = temp
            

        print(
        f'''        
                                                        {poke2.name}
                                                        {int(poke2.hp)}




            {poke1.name}
            {int(poke1.hp)}
        '''
        )

        time.sleep(2)

        print(f"player one, what do you want {poke1.name} to do?")
        for i, x in enumerate(poke1.moves, start=1):
            print(f"{i}. {x}")
        
        p1move_input = input("Enter the number of the move you want to use")

        p1move = poke1.moves[int(p1move_input)-1]

        print(f"{poke1.name} used, {p1move.name}")

        dmg1 = pokesim.battle(poke1, p1move, poke2)

        poke2.hp -= dmg1

        if(poke2.hp < 0):
            print(f"{poke2.name} has feinted")
            flag = False
            break

        time.sleep(2)

        print(f"player two, what do you want {poke2.name} to do?")
        for i, x in enumerate(poke2.moves, start=1):
            print(f"{i}. {x}")
        
        p2move_input = input("Enter the number of the move you want to use")

        p2move = poke2.moves[int(p2move_input)-1]

        print(f"{poke2.name} used, {p2move.name}")

        dmg2 = pokesim.battle(poke2, p2move, poke1)

        poke1.hp -= dmg2

        if(poke1.hp < 0):
            print(f"{poke1.name} has feinted")
            flag = False
            break

main()

#print(isinstance(poke.pokemon[0].moves[2], pokesim.PhysicalMove))