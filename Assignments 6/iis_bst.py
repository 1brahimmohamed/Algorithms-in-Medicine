#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def IsBinarySearchTree(tree):

    def check_sub_trees(index=0):

        nonlocal result

        # get the node at the given index
        node = tree[index]

        # node [1] -> Left child of the node
        # node [2] -> Right child of the node
        # node [0] -> Current node key

        # if the left & right children of the current node exists -> condition is ture (tree has children)
        # check the subtree at the left child .. add the current node to result array then check subtree at
        # the right child
        if node[1] != -1 and node[2] != -1:
            check_sub_trees(node[1])
            result += [node[0]]
            check_sub_trees(node[2])

        # if the node has left child only .. check the left subtree only
        elif node[1] != -1:
            check_sub_trees(node[1])
            result += [node[0]]

        # if the node has right child only .. check the right subtree only
        elif node[2] != -1:
            result += [node[0]]
            check_sub_trees(node[2])

        # if there is no children add the current nodes to the result array
        else:
            result += [node[0]]

    # if the tree is empty return true
    if not tree:
        return True
    result = []

    # check the tree from the first node
    check_sub_trees(0)

    # get the max node value
    max_node = result[0]

    # check if the current node is not bigger then the max then it's not a BST
    for current_node in result[1:]:
        if current_node < max_node:
            return False
        max_node = current_node

    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
