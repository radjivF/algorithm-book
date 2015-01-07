class Tree(object):
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

t = Tree(5, Tree(1, None, Tree(4)), Tree(7, Tree(6), Tree(8)))
