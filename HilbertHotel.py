import AVLTree as AVL

class Infinite_Hotel:
    def __init__ (self, room_count = 0, log_count = 0):
        self.all_room = AVL.AVLTree()
        self.room_count = room_count
        self.log_count = log_count

    def inputGuest(self, input_guests, method):
        self.moveGuest()
        for i in range(input_guests):
            room_id = 2*i
            room = self.search_room_by_id(room_id)
            if room is None:
                self.addRoom(room_id, method)
            else:
                room.method = method

    def moveGuest(self):
        root = self.all_room.root
        def reverse_inorder(root):
            if root != None:
                reverse_inorder(root.right)
                if root.method != None:
                    new_id = (root.room_id * 2) + 1
                    if self.search_room_by_id(new_id) is None:
                        self.addRoom(new_id)
                    self.search_room_by_id(new_id).method = root.method
                    root.method = None
                reverse_inorder(root.left)
        reverse_inorder(root)

    def addRoom(self, room_number, method = None):
        room = self.search_room_by_id(room_number)
        if room != None:
            print('This room is already exist!!')
        else:
            self.room_count += 1
            self.all_room.add(room_number, method)
            self.logging('add', room_number)
		
    def removeRoom(self, room_number):
        room = self.search_room_by_id(room_number)
        if room != None:
            self.room_count -= 1
            self.all_room.removeRoom(room_number)
            self.logging('remove', room_number)
        else:
            print('This room is not exist!!')
    
    def search_room_by_id(self, room_id):
        room = self.all_room.root
        while room != None:
            if room_id > room.room_id:
                room = room.right
            elif room_id < room.room_id:
                room = room.left
            else: break
        return room

    def __str__(self):
        root = self.all_room.root
        lst = []
        with open("room.csv", "w", encoding="utf-8") as f:
            f.write("room, transport\n")
        def inorder(root):
            if root != None:
                inorder(root.left)
                lst.append(f'room #{root.room_id}: {root.method if root.method != None else ''}')
                with open("room.csv", "a", encoding="utf-8") as f:
                    f.write(f"room #{root.room_id}, {root.method if root.method != None else ''}\n")
                inorder(root.right)
        inorder(root)
        return '\n'.join(lst)

    def logging(self, method, room_id):
        self.log_count += 1      
        with open("log.csv", "a", encoding="utf-8") as f:
            f.write(f"{self.log_count}, {method}, room #{room_id}\n")