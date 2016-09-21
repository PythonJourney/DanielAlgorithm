# App for test the Linked list

from LinkedList import LinkedList
from Node import Node

linkedList = LinkedList();

linkedList.insertStart(12);
linkedList.insertStart(322);
linkedList.insertEnd(93);
linkedList.insertEnd(31);

linkedList.traverseList();

linkedList.remove(12);

linkedList.traverseList();
