# POKEMON-TEAMS DATABASES.

This is a local database creator for the downloaded pokemon database.  
Download database from veekun.com or [direct Link](https://veekun.com/static/pokedex/downloads/veekun-pokedex.sqlite.gz) 

### Tools

* sqlite3, sqlite3(python pkg).  
* mongoDB, pymongo.  
* python 3.8

## Version 1.0

create mongodb database for all pokemons untill generation 6 (excludes mega-evolution).

tables used from sqlite db:  

* pokemon_species.  
* pokemon_types.
* types


#### Schema notes.

```
pokemon {
    _id:
    pokedex_id:
    name: 
    types: {
        primary: 
        secondary:
    }
    generation: 
    other_forms: 
}
```

### Commands.  

Install python\[version>=3.0\] , mongoDB, pymongo  

```
    $ python3 -m create_populate.py
    $ python3 -m update_types.py
```

