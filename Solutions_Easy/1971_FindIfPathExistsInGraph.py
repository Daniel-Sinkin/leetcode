from collections import deque


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        # Iterating through the Edge list is terribly slow, this is a much better way of storing the edge relationship
        adj_list = {}
        for u, v in edges:
            if u not in adj_list:
                adj_list[u] = []
            if v not in adj_list:
                adj_list[v] = []
            adj_list[u].append(v)
            adj_list[v].append(u)

        queue = deque([source])
        seen_nodes = {source}

        while queue:
            current_node = queue.popleft()

            if current_node == destination:
                return True

            for neighbor in adj_list.get(current_node, []):
                if neighbor not in seen_nodes:
                    seen_nodes.add(neighbor)
                    queue.append(neighbor)

        return False
