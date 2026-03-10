class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(f'{vertex=}: {self.adj_list[vertex]=}')

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):

        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():

            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):

        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try: ## this is for an edge case where vertex is present but is not connected to the edge we wanna disconnect it from
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):

        if vertex in self.adj_list:
            for vertex in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False