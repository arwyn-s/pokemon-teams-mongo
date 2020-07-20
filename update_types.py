
import sqlite3
import pprint
from os import path
import pymongo

filename = path.join('data', 'veekun-pokedex.sqlite')

liteconn = sqlite3.connect(filename)
print('CONNECTED TO SQLITE DATABASE')

mongoclient = pymongo.MongoClient('mongodb://localhost:27017/')
database = mongoclient['pokemon-teams']
all_pokemon = database['all_pokemon']

all_pokemon.create_index([("pokedex_id", pymongo.ASCENDING)], unique=True)

litecur = liteconn.execute(
    "SELECT id,identifier,generation_id,forms_switchable FROM pokemon_species")

# UPDATE types of the pokemons in all_pokemon
litecur = liteconn.execute(''' 
    SELECT pokemon_types.pokemon_id, pokemon_types.slot, types.identifier FROM pokemon_types
    INNER JOIN types ON pokemon_types.type_id=types.id ;''')
for row in litecur:
    if row[1] == 1:
        result = all_pokemon.update_one({'pokedex_id': row[0]},{"$set" :{"types.primary": row[2]}})
    else :
        result = all_pokemon.update_one({'pokedex_id': row[0]},{"$set" :{"types.secondary": row[2]}})

    pprint.pprint(result)


mongoclient.close()
liteconn.close()
