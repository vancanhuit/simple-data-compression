class Node(object):
    ''' This class represents a node in the binary tree '''
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if not isinstance(self, other.__class__):
            return False
        return self.char == other.char and self.freq == other.freq

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '({}: {})'.format(self.char, self.freq)
