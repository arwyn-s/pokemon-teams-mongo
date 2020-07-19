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
# for row in litecur:
#     print('id: %d, identifier: %s, generation_id %d, forms_switchable: %d' % row)
print(all_pokemon.count_documents({}))
# Adds all pokemons name and generation.
# Ordered=false, all inserts will happen and in random order.
# Default set it Ordered=true
result = all_pokemon.insert_many(
    [{'_id': row[0], 'pokedex_id':row[0], 'name': row[1], 'generation': row[2], 'types':{}} for row in litecur],
    ordered=False)
print(all_pokemon.count_documents({}))
## UPDATE types of the pokemons in all_pokemon

mongoclient.close()
liteconn.close()
