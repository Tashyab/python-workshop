import binarytree as bt
root = bt.tree() # Gives random tree
root_size = root.size
root_height = root.height
all_nodes = list(root)

print(all_nodes)
values = [1, 4, 5, 2, 6, 7]

tree = bt.build(values) # Build level order tree from values
print(tree)