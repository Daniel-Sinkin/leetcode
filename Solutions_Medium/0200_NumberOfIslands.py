class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if len(grid) == 0:
            return 0
        island_counter = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    island = self.BFS((y, x), grid)
                    for y2, x2 in island:
                        grid[y2][x2] = "2"

                    island_counter += 1
        return island_counter

    def BFS(self, starting_position: tuple[int, int], grid) -> list[tuple[int, int]]:
        """Returns a list of connected positions."""
        neighbors = self.get_neighbors(starting_position, grid)

        seen_nodes = {starting_position}
        nodes_to_look_at = neighbors

        while len(nodes_to_look_at) > 0:
            node = nodes_to_look_at.pop()
            seen_nodes.add(node)

            neighbors = self.get_neighbors(node, grid)

            nodes_to_look_at = nodes_to_look_at | {
                node for node in neighbors if node not in seen_nodes
            }

        return seen_nodes

    def is_valid(self, position: tuple[int, int], grid: list[list[str]]) -> bool:
        y_size = len(grid)
        if y_size == 0:
            return False
        x_size = len(grid[0])
        y, x = position
        return (y_size > y >= 0) and (x_size > x >= 0)

    def get_neighbors(
        self, pos: tuple[int, int], grid: list[list[str]]
    ) -> set[tuple[int, int]]:
        y, x = pos
        potential_neighbors = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]

        return {
            pos
            for pos in potential_neighbors
            if self.is_valid(pos, grid) and grid[pos[0]][pos[1]] == "1"
        }
