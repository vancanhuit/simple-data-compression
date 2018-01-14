from entity.node import Node
from queue import PriorityQueue


class TestNode(object):
    def test_is_leaf(self):
        n = Node('AA', 2)
        assert n.is_leaf() is True

    def test_compare_node(self):
        q = PriorityQueue()
        n1 = Node('aa', 2)
        n2 = Node('bb', 1)

        q.put((n1.freq, n1))
        q.put((n2.freq, n2))

        n3 = q.get()[1]
        n4 = q.get()[1]

        assert n1 == n4
        assert n2 == n3
