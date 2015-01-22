def insert(item, tree):
    if (item < tree.entry):
        if (tree.left != None):
            insert(item, tree.left)
        else:
            tree.left = Tree(item)
    else:
        if (tree.right != None):
            insert(item, tree.right)
        else:
            tree.right = Tree(item)
