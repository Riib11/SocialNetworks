from .xml import XML

class GEXF:

    version = "1.3"

    def __init__(self, name):
        self.name = name
        self.parameters = {
            "gexf"  : {"version":GEXF.version},
            "graph" : {"mode":"static"},
            "node" : {},
            "edge" : {}}
        self.attributes = {
            "node" : {},
            "edge" : {}}
        self.nodes = {}
        self.edges = {}

    def setParameter(self, tag, key, value):
        self.parameters[tag][key] = value

    def addAttribute(self, cls, title, type, default):
        self.attributes[cls][title] = {"id":title, "type":type, "default":default}

    def addNode(self, id, attributes=None):
        node = {
            "id"         : id,
            "attributes" : attributes or {}
        }
        self.nodes[id] = node

    def addEdge(self, id, source, target, weight=1, attributes=None):
        edge = {
            "id"        : id,
            "source"    : source,
            "target"    : target,
            "weight"    : weight,
            "attributes": attributes or {}
        }
        self.edges[id] = edge

    def getDegree(self, id):
        x = 0
        for e in self.edges.values():
            if id == e["target"] or id == e["source"]:
                x += e["weight"]
        return x

    def getIndegree(self, id):
        x = 0
        for e in self.edges.values():
            if id == e["target"]:
                x += e["weight"]
        return x

    def getAllIndegrees(self):
        return [ self.getIndegree(id) for id in self.nodes.keys() ]

    def getOutdegree(self, id):
        x = 0
        for e in self.edges.values():
            if id == e["source"]:
                x += e["weight"]
        return x

    def getAllOutdegrees(self):
        return [ self.getOutdegree(id) for id in self.nodes.keys() ]

    def write(self, directory):
        xml = XML(self.name + ".gexf")
        
        # start gexf
        xml.addHeader("gexf"  , self.parameters["gexf"])
        xml.addHeader("graph" , self.parameters["graph"])

        # attributes
        for cls, attrs in self.attributes.items():
            xml.addHeader("attributes" , {"class":cls})
            for title, data in attrs.items():
                # title
                data["title"] = title
                # default
                default = data["default"]
                del data["default"]
                # attribute
                xml.addHeader("attribute", data)
                xml.addTagSpan("default", default)
                xml.addFooter("attribute")
            xml.addFooter("attributes")

        # nodes
        xml.addHeader("nodes", self.parameters["node"])
        for node_id, node in self.nodes.items():
            # start edge
            xml.addHeader("node", {"id":node_id})
            # attributes
            node_attrs = node["attributes"]
            xml.addHeader("attvalues")
            for title, value in node_attrs.items():
                att_for_id = self.attributes["node"][title]["id"]
                xml.addTag("attvalue",{ "for":att_for_id, "value": value })
            xml.addFooter("attvalues")
            # end node
            xml.addFooter("node")
        xml.addFooter("nodes")

        # edges
        xml.addHeader("edges", self.parameters["edge"])
        for edge_id, edge in self.edges.items():
            # start edge
            xml.addHeader("edge", {"id":edge_id, "source":edge["source"], "target":edge["target"]})
            # attributes
            edge_attrs = edge["attributes"]
            xml.addHeader("attvalues")
            for title, value in edge_attrs.items():
                att_for_id = self.attributes["edge"][title]["id"]
                xml.addTag("attvalue",{ "for":att_for_id, "value": value })
            xml.addFooter("attvalues")
            # edge edge
            xml.addFooter("edge")
        xml.addFooter("edges")
        
        # end gexf
        xml.addFooter("graph")
        xml.addFooter("gexf")

        xml.write(directory)