import heapq
import random

def generate_cave():
    """random cave layout, graph."""
    cave = {
        'Mount Moon': {'Room1': 2, 'Room2': 4},
        'Room1': {'Room3': 1, 'Room4': 7},
        'Room2': {'Room4': 3},
        'Room3': {'Exit': 5},
        'Room4': {'Exit': 2},
        'Exit': {}
    }
    return cave

def heuristic(room, goal):
    """Calculate heuristic for A*.
    The heuristic is an estimated cost from a given room to the goal. 
    """
    # Example heuristic values for demonstration; adjust based on real layout
    heuristic_values = {
        'Mt Moon': 6,
        'Floor1': 4,
        'Floor2': 5,
        'Floor3': 2,
        'Floor4': 1,
        'Exit': 0
    }
    return heuristic_values.get(room, float('inf'))

def find_best_route_a_star(cave, start, goal):
    """Find the best route using the A* algorithm.
    This function calculates the shortest path based on the combined actual cost (g_scores)
    and estimated future cost (heuristic).
    """
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    g_scores = {room: float('inf') for room in cave}
    g_scores[start] = 0
    previous_nodes = {room: None for room in cave}

    while priority_queue:
        current_f_score, current_room = heapq.heappop(priority_queue)

        if current_room == goal:
            break

        for neighbor, weight in cave[current_room].items():
            tentative_g_score = g_scores[current_room] + weight
            if tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(priority_queue, (f_score, neighbor))
                previous_nodes[neighbor] = current_room

    # Create path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return path, g_scores[goal]

def simulate_pokemon_encounter():
    pokemon = ["Zubat", "Geodude", "Onix", "Golbat"]
    encounter = random.choice(pokemon)
    print(f"A wild {encounter} appeared!")
    return encounter

def battle_pokemon(pokemon):
    print(f"You engage in battle with {pokemon}!")
    player_hp = 20
    pokemon_hp = random.randint(10, 20)

    while player_hp > 0 and pokemon_hp > 0:
        # Player attacks
        player_damage = random.randint(3, 8)
        pokemon_hp -= player_damage
        print(f"You dealt {player_damage} damage to {pokemon}. {pokemon} HP: {max(pokemon_hp, 0)}")

        if pokemon_hp <= 0:
            print(f"You defeated {pokemon}!")
            break

        # Pokémon attacks
        pokemon_damage = random.randint(2, 6)
        player_hp -= pokemon_damage
        print(f"{pokemon} dealt {pokemon_damage} damage to you. Your HP: {max(player_hp, 0)}")

        if player_hp <= 0:
            print("You were defeated by the wild Pokémon!")
            break

def main():
    """Main function to run the Pokémon Cave Navigator.
    It initializes the cave, calculates the best route, and simulates encounters and battles.
    """
    print("Welcome to the Pokémon Cave Navigator!")

    cave = generate_cave()
    print("Generated Cave Layout:")
    for room, connections in cave.items():
        print(f"{room}: {connections}")

    start = 'Mount Moon'
    goal = 'Exit'

    print("\nCalculating the best route...")
    path, cost = find_best_route_a_star(cave, start, goal)

    print(f"Best route: {' -> '.join(path)} with a total cost of {cost}")

    print("\nSimulating Pokémon encounters along the way:")
    for room in path[1:-1]:  
        encountered_pokemon = simulate_pokemon_encounter()
        battle_pokemon(encountered_pokemon)

if __name__ == "__main__":
    main()
