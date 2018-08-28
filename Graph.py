class graph:
    def __init__(self,gdict):
        if gdict is None:
            graph = {}
        self.gdict = gdict

    def getEdges(self):
        edges = []
        noOfEdges = 0
        for x in self.gdict:
            for y in self.gdict[x]:
                if x+y and y+x not in edges:
                    edges.append(x+y)
                    noOfEdges = noOfEdges + 1
        print "Number of Edges in this graph are: " + str(noOfEdges)
        return edges

    def getListOfNodes(self):
        lx = []
        for x in self.gdict.keys():
            lx.append(x)
        return lx

    def searchelement(self,key):
        list = []
        flag = -1
        list = self.getListOfNodes()
        for x in list:
            if x == key:
                flag = 1
                break
        if flag == 1:
            print "Element exists"
        else:
            print "Element doesn't exists"

    def deleteElement(self,key):

        list = []
        flag = -1
        temp = None
        temp1 = None

        list = self.getListOfNodes()
        for x in list:
            if x == key:
                flag = 1
                break
        if flag == 1:
            temp = self.gdict.get(key)
            del self.gdict[key]
        for x in temp:
            temp1 = self.gdict.get(x)
            temp1.remove(key)
        print self.gdict

    def insert_element_at_to_node(self,keyname,nodelist):
        self.gdict[keyname] = nodelist
        temp = None
        for x in nodelist:
            temp = self.gdict.get(x)
            temp.append(keyname)

    def calculate_degree(self,node):
        temp = self.gdict.get(node)
        count = len(temp)
        return count

''' You can setup graphs as per your requirement, Sample graph setup is shown below '''
g1 = {
    "a" : ["c","b","d"],
    "b" : ["c","e","a"],
    "c" : ["a","b","d","e"],
    "d" : ["a","c","e","f"],
    "e" : ["f","d","b","c"],
    "f" : ["d","e"]
    }