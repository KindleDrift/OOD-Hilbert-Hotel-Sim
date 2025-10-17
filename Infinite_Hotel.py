import AVLTree as AVL

class InfiniteHotel:
    def __init__ (self, room_count):
        self.avl = AVL.AVLTree()
        for num in range(room_count):
            self.avl.add(num + 1, 'init', num + 1)

    def calculate_number(self, x, y):
        return ((x + y) * (x + y + 1) // 2) + y

    def input_guest(self, method_lst, amount_lst):
        i = 1
        self.move_guest()
        for method in method_lst:
            for j in range(amount_lst[i - 1]):
                room_id = self.calculate_number(i, j)
                self.add_room(room_id, method, j + 1)
            i += 1
            
    def move_guest(self):
        rooms = self.all_rooms()
        self.avl.clear()
        for room in rooms:
            new_id = self.calculate_number(0, room.room_id)
            self.avl.add(new_id, room.method.replace(' (NEW)', ''), room.method_id)

    def add_room(self, room_id, method = None, method_id = None):
        room = self.search_room_by_id(room_id) if method == None else None
        if room == None:
            self.avl.add(room_id, str(method) + ' (NEW)', method_id)
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