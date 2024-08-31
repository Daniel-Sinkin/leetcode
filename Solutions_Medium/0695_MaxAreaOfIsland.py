class Solution:
    def is_valid(self, grid: List[List[int]], pos: tuple[int, int]) -> bool:
        if len(grid) == 0:
            return False
        y, x = pos
        y_size = len(grid)
        x_size = len(grid[0])
        return (y_size > y >= 0) and (x_size > x >= 0)

    def get_neighbors(
        self, grid: List[List[int]], pos: tuple[int, int]
    ) -> set[tuple[int, int]]:
        y, x = pos
        potential_neighbors = [(y - 1, x), (y + 1, x), (y, x + 1), (y, x - 1)]
        return {
            (y2, x2)
            for y2, x2 in potential_neighbors
            if self.is_valid(grid, (y2, x2)) and grid[y2][x2] == 1
        }

    def DFS(self, grid: List[List[int]], starting_node: tuple[int, int]) -> int:
        seen_nodes = {starting_node}
        count = 1
        nodes_to_be_visited = self.get_neighbors(grid, starting_node)

        while len(nodes_to_be_visited) > 0:
            node = nodes_to_be_visited.pop()
            seen_nodes.add(node)
            grid[node[0]][node[1]] = 2
            neighbors = self.get_neighbors(grid, node)
            nodes_to_be_visited = nodes_to_be_visited | {
                neighbor for neighbor in neighbors if neighbor not in seen_nodes
            }
            count += 1

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_length = 0
        for y, row in enumerate(grid):
            for x, node in enumerate(row):
                if node == 1:
                    max_length = max(max_length, self.DFS(grid, (y, x)))
        return max_length
