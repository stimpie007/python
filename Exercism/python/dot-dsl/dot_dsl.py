NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    # g = Graph([
    #             (NODE, "a", {"color": "green"})
    #         ])
    def __init__(self, data=None):
        self.nodes = list()
        self.edges = list()
        self.attrs = dict()

        if data is list and data:
            for item in data:
                type = item[0]

                if type is NODE:

                    self.nodes.append(Node(item[1], item[2]))
                if type is EDGE:
                    self.edges.append(Edge(item[1], item[2], item[3]))
                if type is ATTR:
                    self.attrs[item[1]] = item[2]
        else:
            raise TypeError("Malformed graph")

