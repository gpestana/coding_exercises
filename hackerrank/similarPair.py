class Node:
    def __init__(self, val):
        self.children = []
        self.val = val

    def addChild(self, child):
        self.children.append(child)

    def getChildren(self):
        return self.children    
    
    
class Tree:
    def __init__(self):
        self.root = None
        
    def addPair(self, p, c):
        #if tree is empty
        if root == None:
            parent = Node(p)
            child = Node(c)
            parent.addChild(child)
            self.root = parent
        else:
            node = self.searchNode(p)
            #child is always a new node
            child = Node(c)
            node.addChild(child)
            
            
    def searchNode(self, v):
        nodeHeap = []
        root = self.root
        nodeHeap+= root.getChildren()
        
        while nodeHeap:
            node = nodeHeap[0]
            nodeHeap+= node.getChildren()
            del nodeHeap[0]
            if node.val == v:
                return node
        return None
    
        
def calculateSimilarity(tree):
    
    
if __name__ == "__main__":
    meta = raw_input().split(" ")
    n = int(meta[0])
    T = int(meta[1])
    count = 0
    tree = Tree()
    
    for rawPair in xrange(n-1):
        pair = raw_input().split(" ")
        tree.addPair(int(pair[0]), int(pair[1])
    
    print calculateSimilarity(tree)
