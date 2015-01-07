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


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
insertValue = 4

insert(insertValue, testlist)

print testlist
