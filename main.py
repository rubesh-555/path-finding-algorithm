import sys
import random
from pathfinder import PathFinder
from map_parser import MapParser


def print_banner():
    print("=" * 60)
    print(" RTS Battle Unit Pathfinding Algorithm")
    print("=" * 60)
    print()


def print_menu():
    print("\nOptions:")
    print("1. Load map from JSON file")
    print("2. Generate random map")
    print("3. Run pathfinding demo")
    print("4. Exit")
    print()


def get_user_input(prompt: str, default=None):
    user_input = input(prompt)
    return user_input if user_input else default


def run_from_json():
    file_path = get_user_input("Enter JSON file path: ", "sample_map.json")

    try:
        grid, start, target = MapParser.parse_json_map(file_path)

        if start is None or target is None:
            print("Error: Map must contain both start (0) and target (8) positions")
            return

        print(f"\nMap loaded: {len(grid)}x{len(grid[0])}")
        print(f"Start position: {start}")
        print(f"Target position: {target}")

        pathfinder = PathFinder(grid)
        path = pathfinder.find_path(start, target)

        if path:
            print(f"\nPath found! Length: {len(path)} steps")
            print("\nVisualization (S=Start, T=Target, *=Path, #=Obstacle, .=Ground):")
            MapParser.print_grid(grid, path, start, target)

            print("\nPath coordinates:")
            for i, pos in enumerate(path):
                print(f"  Step {i}: {pos}")

            save = get_user_input("\nSave output to JSON? (y/n): ", "n")
            if save.lower() == 'y':
                output_file = get_user_input("Output file name: ", "output_map.json")
                MapParser.create_output_json(file_path, output_file, path, start, target)
                print(f"Output saved to {output_file}")
        else:
            print("\nNo path found! Target is unreachable.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
    except Exception as e:
        print(f"Error: {e}")


def run_random_map():
    size = int(get_user_input("Enter map size (default 32): ", "32"))

    grid = MapParser.create_simple_grid(size)

    available_positions = []
    for i in range(size):
        for j in range(size):
            if grid[i][j] == -1:
                available_positions.append((i, j))

    if len(available_positions) < 2:
        print("Error: Not enough space for start and target positions")
        return

    start = random.choice(available_positions)
    available_positions.remove(start)
    target = random.choice(available_positions)

    print(f"\nGenerated {size}x{size} map")
    print(f"Start position: {start}")
    print(f"Target position: {target}")

    pathfinder = PathFinder(grid)
    path = pathfinder.find_path(start, target)

    if path:
        print(f"\nPath found! Length: {len(path)} steps")
        print("\nVisualization (S=Start, T=Target, *=Path, #=Obstacle, .=Ground):")
        MapParser.print_grid(grid, path, start, target)

        print("\nPath coordinates:")
        for i, pos in enumerate(path):
            print(f"  Step {i}: {pos}")
    else:
        print("\nNo path found! Target is unreachable.")


def run_demo():
    print("\nRunning demo with a simple 10x10 map...")

    grid = [
        [-1, -1, -1, -1,  3,  3, -1, -1, -1, -1],
        [-1,  3, -1, -1,  3,  3, -1,  3, -1, -1],
        [-1,  3, -1, -1, -1, -1, -1,  3, -1, -1],
        [-1,  3, -1,  3,  3,  3, -1,  3, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1,  3, -1, -1],
        [-1,  3,  3,  3,  3,  3, -1,  3, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1,  3, -1, -1],
        [-1,  3, -1,  3,  3,  3,  3,  3, -1, -1],
        [-1,  3, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    ]

    start = (0, 0)
    target = (9, 9)

    print(f"Start position: {start}")
    print(f"Target position: {target}")

    pathfinder = PathFinder(grid)
    path = pathfinder.find_path(start, target)

    if path:
        print(f"\nPath found! Length: {len(path)} steps")
        print("\nVisualization (S=Start, T=Target, *=Path, #=Obstacle, .=Ground):")
        MapParser.print_grid(grid, path, start, target)

        print("\nPath coordinates:")
        for i, pos in enumerate(path):
            print(f"  Step {i}: {pos}")
    else:
        print("\nNo path found! Target is unreachable.")


def main():
    print_banner()

    while True:
        print_menu()
        choice = get_user_input("Select an option (1-4): ", "4")

        if choice == "1":
            run_from_json()
        elif choice == "2":
            run_random_map()
        elif choice == "3":
            run_demo()
        elif choice == "4":
            print("\nExiting. Thank you!")
            sys.exit(0)
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
