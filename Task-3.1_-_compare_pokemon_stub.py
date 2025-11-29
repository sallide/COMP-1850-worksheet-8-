"""
Exercise 3.1: Fetch and Compare Pokémon Stats (Stub)
- Fetch data for two Pokémon from the PokéAPI.
- Calculate their stats at level 50.
- Compare their base stats (e.g., attack, defense, speed).
"""

import httpx

def calculate_stat(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's stat at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

def calculate_hp(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's HP at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

def compare_pokemon(pokemon1, pokemon2):
    """Compare the calculated stats of two Pokémon."""
    # TODO: Fetch data for both Pokémon from the PokéAPI
    url1 = f"https://pokeapi.co/api/v2/pokemon/{pokemon1.lower()}"
    url2 = f"https://pokeapi.co/api/v2/pokemon/{pokemon2.lower()}"

    data1 = httpx.get(url1)
    data2 = httpx.get(url2)

    if data1.status_code == 200:
            data1 = data1.json()
        
            name1 = data1['name']
            
            stats1 = {"name": name1
                      
                      }

            for stat_info in data1["stats"]:
                stats_name1 = stat_info['stat']["name"]
                base_stat1 = stat_info["base_stat"]
                stats1[stats_name1] = base_stat1
    
            data2 = data2.json()
        
            name2 = data2['name']
            
            stats2 = {"name": name2
                      
                      }

            for stat_info in data2["stats"]:
                stats_name2 = stat_info['stat']["name"]
                base_stat2 = stat_info["base_stat"]
                stats2[stats_name2] = base_stat2

        
    #print(stats1, stats2)
    
    # TODO: Extract relevant stats (HP, attack, defense, speed)
    
    # TODO: Calculate stats at level 50 for both Pokémon
    final1 = {
         "hp": calculate_hp(stats1["hp"]),
         "attack": calculate_stat(stats1["attack"]),
         "defense": calculate_stat(stats1["defense"]),
         "speed": calculate_stat(stats1["speed"])

    }

    final2 = {
         "hp": calculate_hp(stats2["hp"]),
         "attack": calculate_stat(stats2["attack"]),
         "defense": calculate_stat(stats2["defense"]),
         "speed": calculate_stat(stats2["speed"])

    }

    # TODO: Compare the calculated stats and print the results

    for stat in ["hp", "attack", "defense", "speed"]:
        if final1[stat] > final2[stat]:
            print(f"{name1} has higher {stat}")
        elif final1[stat] < final2[stat]:
            print(f"{name2} has higher {stat}")
        else:
            print(f"Both have equal {stat}.")

# Example usage
if __name__ == "__main__":
    compare_pokemon("pikachu", "bulbasaur")

"""
Hints:
- Use httpx.get(url) to fetch data for each Pokémon.
- Access base stats using data['stats'] and extract base_stat values.
- Use calculate_stat and calculate_hp to compute level 50 stats.
"""
