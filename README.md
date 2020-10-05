# Pokemon
Django app to make request to [PokéAPI](https://pokeapi.co/docs/v2).

## Usage
PokéAPI Request section just require you to put an ID and it will show you the data, and store it in an SQLite database
WebService Section will ask you for a Pokemon name and consult the data on the database mentioned above, you can make requests by:

```
/poke_service/?name={name}
```
Example:
```
http://localhost:8080/poke_service/?name=magnemite
```

Which will return a Json formatted data, such as:
```json
{
    "name": "magnemite",
    "height": 14,
    "weight": 620,
    "id": 34,
    "base_stats": [
        "hp",
        "attack",
        "defense",
        "special-attack",
        "special-defense",
        "speed"
    ],
    "evolutions": {
        "1": "magnemite",
        "2": "magneton",
        "3": "magnezone"
    }
}
```
## Important
Web Service only will return data about pokemon previously requested by ID in the PokéAPI Request section.

## Requirements
Do not forget to install pip packages needed from the requirements file.
```
pip install -r requirements.txt
```