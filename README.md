# 🤖 RTS Battle Unit Pathfinding Algorithm (A*)

This project implements the **A\* (A-star) search algorithm** in Python to simulate efficient pathfinding for units on a 2D grid, mimicking the movement logic often found in Real-Time Strategy (RTS) games.

---

## 💡 Design Decisions and Problem-Solving

Developing an effective pathfinding system required several key architectural and algorithmic decisions to ensure performance and correctness.

### 1. Algorithm Selection: A*

* **Decision:** The **A\*** algorithm was chosen over simpler algorithms like Dijkstra's or Breadth-First Search (BFS).
* **Rationale:** A\* guarantees the **shortest path** while being significantly more performant because it uses a **heuristic** to guide its search towards the target. In the context of an RTS game, units need optimal movement (shortest path) without creating undue computational load.
* **Implementation:** The core logic utilizes a **priority queue** (implemented via Python's `heapq` module) to efficiently retrieve the node with the lowest **F-score** ($F = G + H$). 

### 2. Heuristic Choice: Manhattan Distance

* **Decision:** The **Manhattan distance** ($H$) was selected for the heuristic function.
* **Rationale:** Since unit movement is restricted to the **four cardinal directions** (up, down, left, right), Manhattan distance is the most appropriate and **admissible** heuristic.
* **Formula:**
    $$H = |x_1 - x_2| + |y_1 - y_2|$$

### 3. Grid and Node Representation

* **Decision:** The map is a simple **Python list of lists** (a 2D array). Nodes (tiles) are represented by their **(row, col) integer tuples**.
* **Rationale:** This structure is efficient for grid lookups. Using tuples for coordinates makes them easily **hashable**, allowing them to be used as keys in critical dictionaries (`g_score`, `f_score`, `came_from`) and sets (`closed_set`).

### 4. Handling Map Data (The Tiled Format)

* **Challenge:** Input map files (e.g., `sample_map1.json`) store tile data as a single, flattened list.
* **Solution:** The `MapParser.parse_json_map` method converts the 1D list index back into **2D (row, col) coordinates** using the map's `height` and `width`.
* **Standardization:** The parser converts map's semantic IDs (0, 8, 3) into a consistent numerical format for the PathFinder: **-1 for open space** and **3 for obstacle**.

---

## 💻 Project Structure Overview

The repository is modularized into three primary Python files, ensuring a clear separation of concerns.

| File | Role | Key Functions | Dependencies |
| :--- | :--- | :--- | :--- |
| **`pathfinder.py`** | **Core Algorithm:** Implements the A\* search and its supporting logic. | `find_path()`, `heuristic()`, `get_neighbors()`, `reconstruct_path()` | `heapq`, `typing` |
| **`map_parser.py`** | **Data Handler:** Manages reading, processing, and visualizing map data (JSON I/O). | `parse_json_map()`, `create_output_json()`, `print_grid()` | `json`, `typing` |
| **`main.py`** | **Application Driver:** Provides the command-line interface, handles user input, and orchestrates the process. | `run_from_json()`, `run_random_map()`, `run_demo()` | `sys`, `random`, `pathfinder`, `map_parser` |

### Map Legend

| Value (Code) | Symbol (Console) | Description |
| :---: | :---: | :--- |
| -1 | **.** | Open Ground (Traversable) |
| 3 | **\#** | Obstacle (Non-Traversable) |
| N/A | **S** | Start Position |
| N/A | **T** | Target Position |
| N/A | **\*** | Found Path |

---

## ⚙️ Build and Run Instructions

This project is a self-contained Python application using only standard libraries.

### Prerequisites

You must have **Python 3.x** installed on your system.

### Running the Application

1.  **Placement:** Ensure all `.py` and `.json` files are placed in the same directory.
2.  **Execution:** Open your terminal or command prompt, navigate to the project directory, and run the main script:

    ```bash
    python main.py
    ```

### Usage

The application will display a menu. Select the option you wish to run:

1.  **Load map from JSON file:** Allows you to test with `sample_map1.json`, `sample_map2.json`, etc.
2.  **Generate random map:** Quickly creates and solves a random pathfinding scenario.
3.  **Run pathfinding demo:** Executes a simple 10x10 test case.

### Output Options

* The `main.py` script automatically prints the grid visualization to the console upon finding a path.
* To save the solved path back into a new JSON file (e.g., `solved_map.json`), uncomment the line calling `MapParser.create_output_json` in the `run_from_json` or `run_demo` functions in `main.py`.