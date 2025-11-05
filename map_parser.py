import json
from typing import Tuple, Optional, List


class MapParser:
    @staticmethod
    def parse_json_map(file_path: str) -> Tuple[List[List[int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]]]:
        with open(file_path, 'r') as f:
            data = json.load(f)

        layers_data = data['layers'][0]['data']
        rows = data['layers'][0]['height']
        cols = data['layers'][0]['width']

        grid = []
        start_pos = None
        target_pos = None

        for row in range(rows):
            grid_row = []
            for col in range(cols):
                idx = row * cols + col
                value = layers_data[idx]

                if value == 0:
                    start_pos = (row, col)
                    grid_row.append(-1)
                elif value == 8:
                    target_pos = (row, col)
                    grid_row.append(-1)
                elif value == 3:
                    grid_row.append(3)
                else:
                    grid_row.append(-1)

            grid.append(grid_row)

        return grid, start_pos, target_pos

    @staticmethod
    def create_output_json(input_file: str, output_file: str, path: List[Tuple[int, int]],
                          start: Tuple[int, int], target: Tuple[int, int]) -> None:
        with open(input_file, 'r') as f:
            data = json.load(f)

        layers_data = data['layers'][0]['data']
        rows = data['layers'][0]['height']
        cols = data['layers'][0]['width']

        output_data = layers_data.copy()

        for row, col in path:
            idx = row * cols + col
            if (row, col) != start and (row, col) != target:
                output_data[idx] = 5

        output_json = data.copy()
        output_json['layers'][0]['data'] = output_data

        with open(output_file, 'w') as f:
            json.dump(output_json, f, indent=2)

    @staticmethod
    def create_simple_grid(size: int = 32) -> List[List[int]]:
        grid = [[-1 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            if i % 4 == 0:
                for j in range(size):
                    if j % 8 != 0:
                        grid[i][j] = 3

        return grid

    @staticmethod
    def print_grid(grid: List[List[int]], path: Optional[List[Tuple[int, int]]] = None,
                   start: Optional[Tuple[int, int]] = None, target: Optional[Tuple[int, int]] = None) -> None:
        path_set = set(path) if path else set()

        symbols = {
            -1: '.',
            3: '#',
        }

        for i, row in enumerate(grid):
            line = ''
            for j, cell in enumerate(row):
                pos = (i, j)
                if start and pos == start:
                    line += 'S'
                elif target and pos == target:
                    line += 'T'
                elif pos in path_set:
                    line += '*'
                else:
                    line += symbols.get(cell, '?')
            print(line)
