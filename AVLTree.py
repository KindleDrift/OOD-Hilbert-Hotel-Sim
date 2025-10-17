class AVLTree:
    class AVLNode:

        def __init__(self, room_id, method, method_id, left=None, right=None):
            self.room_id = room_id
            self.method = method
            self.method_id = method_id
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = -1


        def set_height(self):
            a = self.get_height(self.left)
            b = self.get_height(self.right)
            self.height = 1 + max(a, b)
            return self.height

        def get_height(self, node):
            return -1 if node is None else node.height

        def balance_value(self):
            return self.get_height(self.left) - self.get_height(self.right)

    def __init__(self, root=None):
        self.root = None if root is None else root

    def clear(self):
        self.root = None
        
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
        # x.setHeight()
        balance = x.balance_value()
        if balance == -2:
            if x.right.balance_value() == 1:
                x.right = self.rotate_left_child(x.right)
            x = self.rotate_right_child(x)
        elif balance == 2:
            if x.left.balance_value() == -1:
                x.left = self.rotate_right_child(x.left)
            x = self.rotate_left_child(x)
        x.set_height()
        return x

    def rotate_left_child(self, root):
        y = root.left
        root.left = y.right
        y.right = root
        
        y.set_height()
        root.set_height()
        return y

    def rotate_right_child(self, root):
        y = root.right
        root.right = y.left
        y.left = root
        
        y.set_height()
        root.set_height()
        return y

    def remove_room(self, room_id):
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
            temp = self.get_min(node.right)
            node.room_id, node.method = temp.room_id, temp.method
            node.right = self._remove(node.right, temp.room_id)
        node = self.rebalance(node)
        return node

    def get_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, room_id):
        p = self.root
        while p is not None and p.room_id != room_id:
            if room_id > p.room_id:
                p = p.right
            elif room_id < p.room_id:
                p = p.left
        return p