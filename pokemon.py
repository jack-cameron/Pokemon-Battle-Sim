from battlesim import Pokemon
import moves as move
import natures as nature

flygon = Pokemon("FLYGON", 67, nature.adamant, 80, 17, 250, 100, 31, 252, 80, 31, 0, 80, 4, 0, 80, 20, 4, 100, 28, 1, [move.dragon_claw, move.dragon_dance, move.thunder_wave, move.dragon_pulse], "GROUND", "DRAGON")
crobat = Pokemon("CROBAT", 67, nature.jolly, 85, 31, 252, 90, 18, 252, 80, 11, 0, 70, 6, 0, 80, 31, 0, 130, 31, 6, [move.cross_poison, move.confuse_ray, move.toxic, move.wing_attack], "POISON", "FLYING")

pokemon = [flygon, crobat]