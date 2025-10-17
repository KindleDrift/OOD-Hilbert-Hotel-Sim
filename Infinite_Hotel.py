import AVLTree as AVL

class Infinite_Hotel:
    def __init__ (self, room_count):
        self.avl = AVL.AVLTree()
        for num in range(room_count):
            self.avl.add(num + 1, 'init', num + 1)

    def input_guest(self, method_lst, amount_lst):
        n = len(method_lst) + 1
        self.move_guest(n)
        for i in range(1, n):
            for j in range(amount_lst[i - 1]):
                room_id = (n * j) + i
                self.add_room(room_id, method_lst[i - 1], j + 1)
            
    def move_guest(self, n):
        rooms = self.all_rooms()
        self.avl.clear()
        for room in rooms:
            new_id = n * room.room_id
            self.avl.add(new_id, room.method, room.method_id)

    def add_room(self, room_id, method = None, method_id = None):
        room = self.search_room_by_id(room_id) if method == None else None
        if room == None:
            self.avl.add(room_id, method, method_id)
            return True
        else:
            return False
		
    def remove_room(self, room_id):
        room = self.search_room_by_id(room_id)
        if room != None:
            self.avl.remove_room(room_id)
            return True
        else:
            return False
    
    def search_room_by_id(self, room_id):
        return self.avl.search(room_id)

    def all_rooms(self):
        root = self.avl.root
        lst = []
        def inorder(root):
            if root != None:
                inorder(root.left)
                lst.append(root)
                inorder(root.right)
        inorder(root)
        return lst
    
    def rooms_to_csv(self):
        with open("room.csv", "w", encoding="utf-8") as f:
            f.write("room_id, transport, transport_id\n")
        with open("room.csv", "a", encoding="utf-8") as f:
            for root in self.all_rooms():
                f.write(f"{root.room_id}, {root.method}, {root.method_id}\n")