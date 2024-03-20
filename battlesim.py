import random

types = ["NORMAL", "FIGHT", "FLYING", "POISON", "GROUND", "ROCK", "BUG", "GHOST", "STEEL", "FIRE", "WATER", "GRASS", "ELECTR", "PSYCHIC", "ICE", "DRAGON", "DARK", "FAIRY"]
type_matrix = [[1, 1, 1, 1, 1, 0.5, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [2, 1, 0.5, 0.5, 1, 2, 0.5, 0, 2, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5], 
               [1, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1, 1],
               [1, 1, 1, 0.5, 1, 0.5, 1, 0.5, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2],
               [1, 1, 0, 2, 1, 2, 0.5, 1, 2, 2, 1, 0.5, 2, 1, 1, 1, 1, 1],
               [1, 0.5, 2, 1, 0.5, 1, 2, 1, 0.5, 2, 1, 1, 1, 2, 1, 1, 1],
               [1, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 1, 2, 1, 2, 1, 1, 2, 0.5],
               [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1],
               [1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 1, 2],
               [1, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5, 0.5, 2, 1, 1, 2, 0.5, 1, 1],
               [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 0.5, 1],
               [1, 1, 0.5, 0.5, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 1, 0.5, 1, 1],
               [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 0.5, 1, 1],
               [1, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 0, 1],
               [1, 1, 2, 1, 2, 1, 1, 1, 0.5, 0.5, 0.5, 2, 1, 1, 0.5, 2, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 0],
               [1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5],
               [1, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 1]]

class Pokemon:
    def __init__(self, name, level, nature, hp, hpiv, hpev, atk, atkiv, atkev, dfc, dfciv, dfcev, spatk, spatkiv, spatkev, spdfc, spdfciv, spdfcev, spd, spdiv, spdev, moves, type1, type2):
        self.name = name
        self.level = level
        self.nature = nature
        self.hp = hp
        self.hpiv = hpiv
        self.hpev = hpev
        self.atk = atk
        self.atkiv = atkiv
        self.atkev = atkev
        self.dfc = dfc
        self.dfciv = dfciv
        self.dfcev = dfcev
        self.spatk = spatk
        self.spatkiv = spatkiv
        self.spatkev = spatkev
        self.spdfc = spdfc
        self.spdfciv = spdfciv
        self.spdfcev = spdfcev
        self.spd = spd
        self.spdiv = spdiv
        self.spdev = spdev
        self.moves = moves
        self.type1 = type1
        self.type2 = type2
        self.accuracy = 1
        self.status = "HEALTHY"

    
        #hp calc
        self.hp = ((self.hpiv + 2 * self.hp + (self.hpev/4)) * self.level/100) + 10 + self.level

        #other stats calc
        self.atk = (((self.atkiv + 2 * self.atk + (self.atkev/4)) * self.level/100) + 5) * self.nature.atkvalue
        self.dfc = (((self.dfciv + 2 * self.dfc + (self.dfcev/4)) * self.level/100) + 5) * self.nature.dfcvalue
        self.spatk = (((self.spatkiv + 2 * self.spatk + (self.spatkev/4)) * self.level/100) + 5) * self.nature.spatkvalue
        self.spdfc = (((self.spdfciv + 2 * self.spdfc + (self.spdfcev/4)) * self.level/100) + 5) * self.nature.spdfcvalue
        self.spd = (((self.spdiv + 2 * self.spd + (self.spdev/4)) * self.level/100) + 5) * self.nature.spdvalue

    def __str__(self):
        return "----------" + self.name + "----------" + "\n\n" + "    [" +self.type1 + "]" + " [" + self.type2 + "]" + "\n\n" + "   " +str(self.moves[0]) + "\n   " + str(self.moves[1]) + "\n   " + str(self.moves[2]) + "\n   " + str(self.moves[3]) + "\n\n" + "HP:          " + str(int(self.hp)) + "\n" + "ATTACK:      " + str(int(self.atk)) + "\n" + "SP. ATTACK:  " + str(int(self.spatk)) + "\n" + "DEFENCE:     " + str(int(self.dfc))+ "\n" +  "SP. DEFENCE: " + str(int(self.spdfc)) + "\n" + "SPEED:       " + str(int(self.spd)) + "\n"

class Nature:
    def __init__(self, name):
        self.name = name
        
        match name:
            case "Bashful":
                self.atkvalue = 1
                self.dfcvalue = 1
                self.spatkvalue = 1
                self.spdfcvalue = 1
                self.spdvalue = 1
            case "Docile":
                self.atkvalue = 1
                self.dfcvalue = 1
                self.spatkvalue = 1
                self.spdfcvalue = 1
                self.spdvalue = 1
            case "Hardy":
                self.atkvalue = 1
                self.dfcvalue = 1
                self.spatkvalue = 1
                self.spdfcvalue = 1
                self.spdvalue = 1
            case "Quirky":
                self.atkvalue = 1
                self.dfcvalue = 1
                self.spatkvalue = 1
                self.spdfcvalue = 1
                self.spdvalue = 1
            case "Serious":
                self.atkvalue = 1
                self.dfcvalue = 1
                self.spatkvalue = 1
                self.spdfcvalue = 1
                self.spdvalue = 1
            case "Adamant":
                self.atkvalue = 1.1
                self.dfcvalue = 1
                self.spatkvalue = 0.9
                self.spdfcvalue = 1
                self.spdvalue = 1
            case "Brave":
                self.atkvalue = 1.1
                self.dfcvalue = 1
                self.spatkvalue = 1
                self.spdfcvalue = 1
                self.spdvalue = 0.9
            case "Lonely":
                self.atkvalue = 1.1
                self.dfcvalue = 0.9
                self.spatkvalue = 1
                self.spdfcvalue = 1
                self.spdvalue = 1
            case "Naughty":
                self.atkvalue = 1.1
                self.dfcvalue = 1
                self.spatkvalue = 1
                self.spdfcvalue = 0.9
                self.spdvalue = 1
            case "Bold":
                self.atkvalue = 0.9
                self.dfcvalue = 1.1
                self.spatkvalue = 1
                self.spdfcvalue = 1
                self.spdvalue = 1
            case "Impish":
                self.atkvalue = 1
                self.dfcvalue = 1.1
                self.spatkvalue = 0.9
                self.spdfcvalue = 1
                self.spdvalue = 1
            case "Lax":
                self.atkvalue = 1
                self.dfcvalue = 1.1
                self.spatkvalue = 1
                self.spdfcvalue = 0.9
                self.spdvalue = 1
            case "Relaxed":
                self.atkvalue = 1
                self.dfcvalue = 1.1
                self.spatkvalue = 1
                self.spdfcvalue = 1
                self.spdvalue = 0.9
            case "Modest":
                self.atkvalue = 0.9
                self.dfcvalue = 1
                self.spatkvalue = 1.1
                self.spdfcvalue = 1
                self.spdvalue = 1
            case "Mild":
                self.atkvalue = 1
                self.dfcvalue = 0.9
                self.spatkvalue = 1.1
                self.spdfcvalue = 1
                self.spdvalue = 1
            case "Quiet":
                self.atkvalue = 1
                self.dfcvalue = 1
                self.spatkvalue = 1.1
                self.spdfcvalue = 1
                self.spdvalue = 0.9
            case "Rash":
                self.atkvalue = 1
                self.dfcvalue = 1
                self.spatkvalue = 1.1
                self.spdfcvalue = 0.9
                self.spdvalue = 1
            case "Calm":
                self.atkvalue = 0.9
                self.dfcvalue = 1
                self.spatkvalue = 1
                self.spdfcvalue = 1.1
                self.spdvalue = 1
            case "Careful":
                self.atkvalue = 1
                self.dfcvalue = 1
                self.spatkvalue = 0.9
                self.spdfcvalue = 1.1
                self.spdvalue = 1
            case "Gentle":
                self.atkvalue = 1
                self.dfcvalue = 0.9
                self.spatkvalue = 1
                self.spdfcvalue = 1.1
                self.spdvalue = 1
            case "Sassy":
                self.atkvalue = 1
                self.dfcvalue = 1
                self.spatkvalue = 1
                self.spdfcvalue = 1.1
                self.spdvalue = 0.9
            case "Hasty":
                self.atkvalue = 1
                self.dfcvalue = 0.9
                self.spatkvalue = 1
                self.spdfcvalue = 1
                self.spdvalue = 1.1
            case "Jolly":
                self.atkvalue = 1
                self.dfcvalue = 1
                self.spatkvalue = 0.9
                self.spdfcvalue = 1
                self.spdvalue = 1.1
            case "Naive":
                self.atkvalue = 1
                self.dfcvalue = 1
                self.spatkvalue = 1
                self.spdfcvalue = 0.9
                self.spdvalue = 1.1
            case "Timid":
                self.atkvalue = 0.9
                self.dfcvalue = 1
                self.spatkvalue = 1
                self.spdfcvalue = 1
                self.spdvalue = 1.1

class PhysicalMove():
    def __init__(self, name, damage, accuracy, typing):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy
        self.typing = typing
    def __str__(self):
        return self.name + "[" + self.typing + "]"


class PhysicalMove():
    def __init__(self, name, damage, accuracy, typing):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy
        self.typing = typing
    def __str__(self):
        return self.name + "[" + self.typing + "]"

class SpecialMove():
    def __init__(self, name, damage, accuracy, typing):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy
        self.typing = typing
    def __str__(self):
        return self.name + "[" + self.typing + "]"

class StatusMove():
    def __init__(self, name, status, accuracy, typing):
        self.name = name
        self.status= status
        self.accuracy = accuracy
        self.typing = typing
    def __str__(self):
        return self.name + "[" + self.typing + "]"

class StatModMove():
    def __init__(self, name, stat, step, accuracy, typing):
        self.name = name
        self.stat = stat
        self.step = step
        self.accuracy = accuracy
        self.typing = typing
    def __str__(self):
        return self.name + "[" + self.typing + "]"


def battle(atkpoke, move, defpoke):

    print(isinstance(move, StatusMove))

    if(atkpoke.status != "HEALTHY"):

        if(atkpoke.status == "PARALYZED"):
            para_role = random.randint(1, 4)
            if(para_role == 1):
                return f"{atkpoke.name} is paralyzed, it can't move"
            
    dmg_calc = 0

    accuracy_role = random.random()

    accuracy_role += move.accuracy

    if(accuracy_role >= 1.0):


        if(isinstance(move, PhysicalMove)):
            print('phys move test')
            dmg_role = random.randint(85, 100) / 100

            crit_num = random.randint(0, 10000)
            crit_factor = 2 if crit_num <= 625 else 1

            burn = 0.5 if atkpoke.status == "BURNED" else 1

            stab = 1.5 if (move.typing == atkpoke.type1 or move.typing == atkpoke.type2) else 1

            move_type_index = -1
            deftype1_index = -1
            deftype2_index = -1

            for index, x in enumerate(types):
                if x == move.typing:
                    move_type_index = index

            for index, x in enumerate(types):
                if x == defpoke.type1:
                    deftype1_index = index
            
            if defpoke.type2:
                for index, x in enumerate(types):
                    if x == defpoke.type2:
                        deftype2_index = index

            type1_dmg = type_matrix[move_type_index][deftype1_index]
            if deftype2_index > -1:
                type2_dmg = type_matrix[move_type_index][deftype2_index] 


            dmg_calc = (( (2*atkpoke.level/5 + 2) * move.damage * atkpoke.atk/defpoke.dfc / 50) * burn + 2 ) * crit_factor * dmg_role * stab * type1_dmg * type2_dmg

        elif(isinstance(move, SpecialMove)):
            dmg_role = random.randint(85, 100) / 100

            crit_num = random.randint(0, 10000)
            crit_factor = 2 if crit_num <= 625 else 1

            burn = 0.5 if atkpoke.status == "BURNED" else 1

            stab = 1.5 if (move.typing == atkpoke.type1 or move.typing == atkpoke.type2) else 1

            move_type_index = -1
            deftype1_index = -1
            deftype2_index = -1

            for index, x in enumerate(types):
                if x == move.typing:
                    move_type_index = index

            for index, x in enumerate(types):
                if x == defpoke.type1:
                    deftype1_index = index
            
            if defpoke.type2:
                for index, x in enumerate(types):
                    if x == defpoke.type2:
                        deftype2_index = index

            type1_dmg = type_matrix[move_type_index][deftype1_index]
            if deftype2_index > -1:
                type2_dmg = type_matrix[move_type_index][deftype2_index] 


            dmg_calc = (( (2*atkpoke.level/5 + 2) * move.damage * atkpoke.atk/defpoke.dfc / 50) * burn + 2 ) * crit_factor * dmg_role * stab * type1_dmg * type2_dmg
        
        elif(isinstance(move, StatusMove)):
            print("status test")
            defpoke.status = move.status
            if(move.status == "PARALYZED"):
                defpoke.spd /= 2
            print (f"{defpoke.name} is now {defpoke.status}")

    return dmg_calc