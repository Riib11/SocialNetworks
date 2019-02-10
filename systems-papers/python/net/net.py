class NET:

    def __init__(self, name):
        self.name = name
        self.node_count = 0
        self.nodes = {}
        self.edges = {}

    def addNode(self, label, attributes=None):
        if not label in self.nodes:
            node = {
                "id"         : self.node_count+1,
                "label"      : label,
                "attributes" : attributes or {}
            }
            self.nodes[label] = node
            self.node_count += 1
            return self.node_count - 1
        return False

    def addEdge(self, label, source, target, weight=1, attributes=None):
        edge = {
            "label"     : label,
            "source"    : source,
            "target"    : target,
            "weight"    : weight,
            "attributes": attributes or {}
        }
        self.edges[label] = edge
        
    def write(self, directory):
        file = open(directory + self.name + ".net", "w+")
        # vertices header
        file.write("*Vertices "+str(self.node_count)+"\n")
        # vertices
        for (label, node) in self.nodes.items():
            s = str(node["id"]) + " " # id
            s += "\"" + label + "\"" # label
            # attributes
            # for k,v in node["attributes"].items(): s += " "+str(k)+" "+str(v)
            file.write(s+"\n")

        # edges header
        file.write("*Edges\n")
        # edges
        for (label, edge) in self.edges.items():
            s = str(self.nodes[edge["source"]]["id"]) + " "
            s += str(self.nodes[edge["target"]]["id"])
            file.write(s+"\n")

        file.close()


def demo():
    n = NET("pytest")
    n.addNode("A")
    n.addNode("B")
    n.addEdge("A-B", "A", "B", weight=1, attributes=None)
    n.write("/Users/Henry/Documents/Drive/SystemsAnalysis/systems-papers/net/")