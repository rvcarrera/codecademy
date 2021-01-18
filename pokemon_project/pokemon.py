class Pokemon:
    def __init__(self, name, level, type, max_health, current_health, knocked_out=False):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.current_health = current_health
        self.knocked_out = knocked_out
    def check_knocked_out(self):
        if self.current_health <= 0:
            self.knocked_out = True
            return '{} is knocked out.'.format(self.name)
        else:
            return '{} is still able to fight.'.format(self.name)
    def lose_health(self, health_points):
        self.current_health -= health_points
        if self.current_health < 0:
            self.current_health = 0
        print('{} has lose {} health points.'.format(self.name, health_points))
        print(self.check_knocked_out())
        return
    def regain_health(self, health_points):
        self.current_health += health_points
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        print('{} has regain {} health points.'.format(self.name, health_points))
        print(self.check_knocked_out())
        return
    def attack(self, other, health_points):
        if self.type == 'Fire' and other.type == 'Grass':
            self.lose_health(health_points*0.5)
        elif self.type == 'Fire' and other.type == 'Water':
            self.lose_health(health_points*2)
        elif self.type == 'Grass' and other.type == 'Fire':
            self.lose_health(health_points*2)
        elif self.type == 'Grass' and other.type == 'Water':
            self.lose_health(health_points*0.5)
        elif self.type == 'Water' and other.type == 'Fire':
            self.lose_health(health_points*0.5)
        elif self.type == 'Water' and other.type == 'Grass':
            self.lose_health(health_points*2)
        else:
            self.lose_health(health_points)
        return
    
class Trainer:
    def __init__(self, name, potions, active_pokemon, pokemons):
        self.name = name
        self.potions = potions
        self.active_pokemon = active_pokemon
        self.pokemons = pokemons
    def use_potion(self):
        print('{} use a potion.'.format(self.name))
        self.pokemons[self.active_pokemon].regain_health(15)
        return
    def attack_other(self, other):
        other_pokemon = other.pokemons[other.active_pokemon]
        if self.pokemons[self.active_pokemon].knocked_out:
            print('{} is knocked out, he cant fight.'.format(self.pokemons[self.active_pokemon].name))
            return
        print('{} has been attacked.'.format(other_pokemon.name))
        other_pokemon.attack(self.pokemons[self.active_pokemon], 5)
        return
    
charmander = Pokemon('Charmander', 5, 'Fire', 20, 20)
bulbasaur  =Pokemon('Bulbasaur', 5, 'Grass', 20, 20)

ash = Trainer('Ash Ketchup', 5, 0, [charmander])
gary = Trainer('Gary Oak', 5, 0, [bulbasaur])

ash.attack_other(gary)
ash.attack_other(gary)
gary.attack_other(ash)