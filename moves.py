from battlesim import PhysicalMove, StatModMove, StatusMove, SpecialMove


#moves
dragon_claw = PhysicalMove("Dragon Claw", 80, 1.0, "DRAGON")
dragon_dance = StatModMove("Dragon Dance", ["atk", "spd"], 1, 1.0, "DRAGON")
thunder_wave = StatusMove("Thunder Wave", "PARALYZED", 1.0, "ELECTR")
dragon_pulse = SpecialMove("Dragon Pulse", 90, 1.0, "DRAGON")
cross_poison = PhysicalMove("Cross Poison", 70, 1.0, "POISON")
confuse_ray = StatusMove("Confuse Ray", "CONFUSION", 1.0, "GHOST")
toxic = StatusMove("Toxic", "BADLY POISONED", 1.0, "POISON")
wing_attack = PhysicalMove("Wing Attack", 60, 1.0, "FLYING")
will_o_wisp = StatusMove("Will O Wisp", "BURNED", 1.0, "FIRE")
