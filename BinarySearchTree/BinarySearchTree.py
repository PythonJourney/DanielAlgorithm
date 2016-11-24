from BinarySearchTree.Node import Node

class BST(object):

    def __init__(self):
        self.rootNode = None;

    def insert(self, data):
        if not self.rootNode:
            self.rootNode = Node(data)
        else: