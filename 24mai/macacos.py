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

        greatest_tree.insert(0, i + 2)
        greatest_tree.append(int(trees_input[2]))


def define_line(ith_tree, greatest_tree):

    coefficient_a = (greatest_tree[1] - trees[ith_tree]) / (greatest_tree[0] - 1)
    coefficient_b = trees[ith_tree]

    line_values = [coefficient_a, coefficient_b]

    return line_values


first_line = define_line(0, greatest_tree)

ith_tree = 0

while ith_tree != greatest_tree:

    if (first_line[0] * ith_tree + first_line[1]) >= trees[ith_tree]:
        jumps += 1
        ith_tree += 1
        continue
    else:
        first_line = define_line(ith_tree, greatest_tree)


print(trees, greatest_tree, define_line(trees, greatest_tree))
