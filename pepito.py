


class Player:
    def __init__(self, name, health, coins,special,motivation):
        self.name = name
        self.health = health
        self.coins = coins
        self.special = special
        self.motivation = motivation
        self.key = False
        self.potion = 0
        self.spotion = 0
        self.aids = False
        self.aidsonce = False
        self.enemy1def = False
        self.enemy2def = False
        self.titandef = False
        self.titandef = False
        self.tarbought = False
        self.rapierbought = False
        self.gardenkey = False
        self.chestcusion = False
        self.burning = False
        self.demonper = False
    def stats(self):
            print(f"""
            CHARACTER STATS:
            Name: {self.name}
            Health: {self.health}
            Coins: {self.coins}
            amount of potions: {self.potion}
            aids: {self.aids}
            special attack: {self.special}
            """)
    def statshelll(self):
            print(f"""
            CHARACTER STATS:
            Name: {self.name}
            Health: {self.health}
            Coins: {self.coins}
            amount of potions: {self.potion}
            amount of super potions: {self.spotion}
            Motivation: {self.motivation}
            special attack: {self.special}
            """)
    def testkey(self):
        print(self.key)
   

class Weapon:
    def __init__(self, name, type, size, damage,):
        self.wpname = name
        self.type = type
        self.size = size
        self.damage = damage
    def stats(self):
        print(f"""
              WEAPON STATS:
              Name: {self.wpname}
              type: {self.type}
              size: {self.size}
              damage: {self.damage}
              """)
        
    

    

class NPC:
    def __init__(self, name, health, experience):
        
        self.Nname = name
        self.Nhealth = health
        self.Nexperience = experience
        self.hostility = False
        
    def talk(self):
        print(f"{self.Nname}: Hello man, cant do anything wichu but uh hi")
    def talk2(self):
        print(f"{self.Nname}: who am i you say?, im just some dude man, name's {self.Nname}")
    def treathened(self):
        print(f"{self.Nname}: Careful there chief, i might look dumb but i wont stand by it")
    def threathened2(self):
        print(f"THATS IT, IM OUT")
    


class Enemy(NPC):
    def __init__(self, name, health, experience, damage, faction):
      super().__init__(name, health, experience,)
      self.damage = damage
      self.faction = faction
      self.hostility = True
      self.potion = 1
      
    def talkE(self):
        print("gimme your shit nigga")
    def combatdamaged(self):
        print("AHH YOU NIGGA")
    def combatdead(self):
        print("FUUUUUUUUCK")
