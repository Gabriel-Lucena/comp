number_of_trees = int(input())
trees = []
greatest_tree = []
jumps = 0

trees_input = input()

greatest_tree.insert(1, 1)
greatest_tree.insert(2, int(trees_input[2]))

trees.append(int(trees_input[2]))

for i in range(number_of_trees - 1):

    trees_input = input()
    trees.append(int(trees_input[2]))

    if int(trees_input[2]) > greatest_tree[1]:
        greatest_tree.pop(1)
        greatest_tree.pop(0)

        greatest_tree.insert(0, i + 1)
        greatest_tree.append(int(trees_input[2]))


def define_line(ith_tree, nth_tree, trees):

    coefficient_a = (trees[ith_tree] - trees[nth_tree]) / (ith_tree - nth_tree)
    coefficient_b = trees[ith_tree] - coefficient_a * ith_tree

    line_values = [coefficient_a, coefficient_b]

    return line_values


ith_tree = 0

line = define_line(greatest_tree[0], ith_tree, trees)

jumps += 1

while ith_tree != greatest_tree[0]:

    if ith_tree == 0:
        ith_tree += 1
        continue

    if (line[0] * ith_tree + line[1]) >= trees[ith_tree]:
        ith_tree += 1
    else:
        jumps += 1

        if ith_tree != greatest_tree[0]:
            line = define_line(greatest_tree[0], ith_tree,  trees)
            ith_tree += 1


line = define_line(len(trees) - 1, greatest_tree[0], trees)

jumps += 1


while ith_tree != (len(trees) - 1):

    if ith_tree == greatest_tree[0]:
        ith_tree += 1
        continue

    if (line[0] * ith_tree + line[1]) >= trees[ith_tree]:
        ith_tree += 1
    else:
        jumps += 1

        if ith_tree != (len(trees) - 1):
            line = define_line(len(trees) - 1, ith_tree, trees)
            ith_tree += 1

print(jumps)
