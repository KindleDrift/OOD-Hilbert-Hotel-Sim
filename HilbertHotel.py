import AVLTree as AVL

class Infinite_Hotel:
    def __init__ (self, room_count, log_count = 0):
        self.avl = AVL.AVLTree()
        for num in range(room_count):
            self.avl.add(num + 1, 'init', num + 1)
        self.room_count = room_count
        self.log_count = log_count

    def inputGuest(self, channel_lst, amount_lst):
        n = len(channel_lst) + 1
        self.moveGuest(n)
        for i in range(n - 1):
            for j in range(amount_lst[i]):
                room_num = (n * j) + i + 1
                room = self.search_room_by_id(room_num)
                if room is None:
                    self.addRoom(room_num, channel_lst[i], j + 1)
                else:
                    room.method = channel_lst[i]
                    room.method_id = j + 1
            
    def moveGuest(self, step):
        root = self.avl.root
        def reverse_inorder(root):
            if root != None:
                reverse_inorder(root.right)
                if root.method != None:
                    new_id = root.room_id * step
                    room = self.search_room_by_id(new_id)
                    if room is None:
                        self.addRoom(new_id, root.method, root.method_id)
                    else:
                        room.method = root.method
                        room.method_id = root.method_id
                    root.method = None
                    root.method_id = None
                reverse_inorder(root.left)
        reverse_inorder(root)

    def addRoom(self, room_number, method = None, method_id = None):
        room = self.search_room_by_id(room_number)
        if room != None:
            return False
        else:
            self.room_count += 1
            self.avl.add(room_number, method, method_id)
            self.logging('add', room_number)
            return True
		
    def removeRoom(self, room_number):
        room = self.search_room_by_id(room_number)
        if room != None:
            self.room_count -= 1
            self.avl.removeRoom(room_number)
            self.logging('remove', room_number)
            return True
        else:
            return False
    
    def search_room_by_id(self, room_id):
        room = self.avl.root
        while room != None:
            if room_id > room.room_id:
                room = room.right
            elif room_id < room.room_id:
                room = room.left
            else: break
        return room
    
    def sorted_room(self, file_name = "sorted_room.csv"):
        root = self.avl.root
        lst = []
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("room_number, transport, transport_id\n")
        def inorder(root):
            if root != None:
                inorder(root.left)
                lst.append(root)
                with open(file_name, "a", encoding="utf-8") as f:
                    f.write(f"{root.room_id}, {root.method}, {root.method_id}\n")
                inorder(root.right)
        inorder(root)

    def rooms_to_csv(self):
        self.sorted_room("room.csv")

    def logging(self, method, room_id):
        self.log_count += 1      
        with open("log.csv", "a", encoding="utf-8") as f:
            f.write(f"{self.log_count}, {method}, room #{room_id}\n")