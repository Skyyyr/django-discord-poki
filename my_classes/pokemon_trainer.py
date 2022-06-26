
class PokemonTrainer:
    all_trainers = []

    def __init__(self, trainer_id, trainer_name, trainer_pokedex, trainer_inventory, trainer_current_pokemon):
        self.trainer_current_pokemon = trainer_current_pokemon
        self.trainer_inventory = trainer_inventory
        self.trainer_pokedex = trainer_pokedex
        self.trainer_id = trainer_id
        self.trainer_name = trainer_name

    def __str__(self):
        return f'Trainer Name: {self.trainer_name}\n' \
               f'Current Pokemon ID: {self.trainer_current_pokemon}\n'

    def UpdatePokedex(self, pokemon_id):
        self.trainer_pokedex.append(pokemon_id)
        return self.trainer_pokedex
