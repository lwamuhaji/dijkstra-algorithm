class Tree:
    def __init__(self, node_count: int, edge_list: 'list[Edge]'):
        self.node_count = node_count
        self.edge_list = edge_list


class Edge:
    def __init__(self, start: int, end: int, cost: int):
        self.start = start
        self.end = end
        self.cost = cost

    def __str__(self):
        return f'({self.start} to {self.end}, cost: {self.cost})'


def dijkstra(tree: Tree, start_node: int = 1):
    visited: list[int] = [start_node]
    costs: dict[int, int] = {start_node: 0}

    while len(visited) != tree.node_count:
        candidates = [(edge, edge.cost + costs[edge.start])
                      for edge in tree.edge_list if edge.start in visited and edge.end not in visited]
        edge, cost = min(candidates, key=lambda x: x[1])
        visited.append(edge.end)
        costs[edge.end] = cost
        print(f'# STEP {len(visited) - 1}')
        print('candidates:', *map(lambda x: x[0], candidates))
        print(f'selected edge: {edge}\nvisited: {visited}\ncosts: {costs}\n')
    print('# Solved\n')


# initialize trees
node_count = 5
edge_list = [(1, 2, 7), (1, 3, 4), (1, 4, 6), (1, 5, 1),
             (3, 2, 2), (3, 4, 5), (4, 2, 3), (5, 4, 1)]
tree1 = Tree(node_count=node_count, edge_list=[
             Edge(*edge) for edge in edge_list])

node_count = 6
edge_list = [(1, 2, 10), (1, 3, 30), (1, 4, 15), (2, 5, 20),
             (3, 6, 5), (4, 3, 5), (4, 6, 20), (5, 6, 20), (6, 4, 20)]
tree2 = Tree(node_count=node_count, edge_list=[
             Edge(*edge) for edge in edge_list])

node_count = 5
edge_list = [(1, 4, 3), (1, 3, 6), (2, 1, 3), (3, 4, 2),
             (4, 3, 1), (4, 2, 1), (5, 2, 4), (5, 4, 2)]
tree3 = Tree(node_count=node_count, edge_list=[
             Edge(*edge) for edge in edge_list])

# solve
dijkstra(tree1)
dijkstra(tree2)
dijkstra(tree3, start_node=5)
