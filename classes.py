class Move:
    def __init__(self, id: int, name, effect, type, kind, power: int, accuracy: float, pp: int):
        self.id = id
        self.name = name
        self.effect = effect
        self.type = type
        self.kind = kind
        self.power = power
        self.accuracy = accuracy
        self.pp = pp

class Pokemon:
    def __init__(self, id, name, type1, type2, total: int, hp: int, attack: int, defense: int, spAtk: int, spDef: int, speed: int, generation: int, legendary: bool, moves: list):
        self.id = id
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.spAtk = spAtk
        self.spDef = spDef
        self.speed = speed
        self.generation = generation
        self.legendary = legendary
        self.moves = moves

