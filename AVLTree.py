class AVLTree:
    class AVLNode:

        def __init__(self, room_id, method, method_id, left=None, right=None):
            self.room_id = room_id
            self.method = method
            self.method_id = method_id
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()

        def __str__(self):
            return str((self.room_id, self.method))

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a, b)
            return self.height

        def getHeight(self, node):
            return -1 if node is None else node.setHeight()

        def balanceValue(self):
            return self.getHeight(self.left) - self.getHeight(self.right)

    def __init__(self, root=None):
        self.root = None if root is None else root

    def add(self, room_id, method, method_id):
        self.root = self._add(self.root, room_id, method, method_id)

    def _add(self, root, room_id, method, method_id):
        if root is None:
            return self.AVLNode(room_id, method, method_id)
        else:
            if int(room_id) < int(root.room_id):
                root.left = self._add(root.left, room_id, method, method_id)
            else:
                root.right = self._add(root.right, room_id, method, method_id)
        root = self.rebalance(root)
        return root

    def rebalance(self, x):
        if x is None:
            return x
        balance = x.balanceValue()
        if balance == -2:
            if x.right.balanceValue() == 1:
                x.right = self.rotateLeftChild(x.right)
            x = self.rotateRightChild(x)
        elif balance == 2:
            if x.left.balanceValue() == -1:
                x.left = self.rotateRightChild(x.left)
            x = self.rotateLeftChild(x)
        return x

    def rotateLeftChild(self, root):
        y = root.left
        root.left = y.right
        y.right = root
        return y

    def rotateRightChild(self, root):
        y = root.right
        root.right = y.left
        y.left = root
        return y

    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node, level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)

    def removeRoom(self, room_id):
        self.root = self._remove(self.root, room_id)

    def _remove(self, node, room_id):
        if not node:
            return node
        if room_id < node.room_id:
            node.left = self._remove(node.left, room_id)
        elif room_id > node.room_id:
            node.right = self._remove(node.right, room_id)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                root = None
                return temp
            temp = self.getMin(node.right)
            node.room_id, node.method = temp.room_id, temp.method
            node.right = self._remove(node.right, temp.room_id)
        node = self.rebalance(node)
        return node

    def getMin(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, room_id):
        p = self.root
        while p.room_id != room_id and p is not None:
            if room_id > p.room_id:
                p = p.right
            elif room_id < p.room_id:
                p = p.left
        return p

    def leverOrder(self):
        q = []
        p = []
        q.append(self.root)
        while len(q) != 0:
            n = q.pop(0)
            p.append(n)
            if n.left is not None:
                q.append(n.left)
            if n.right is not None:
                q.append(n.right)
        return p

