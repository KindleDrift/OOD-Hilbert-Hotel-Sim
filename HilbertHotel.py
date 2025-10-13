import AVLTree as AVL
import time
import tracemalloc

class Infinite_Hotel:
    def __init__ (self, room_count = 0, log_count = 0):
        self.all_room = AVL.AVLTree()
        self.room_count = room_count
        self.log_count = log_count
        self.log = []

    def inputGuest(self, input_guests, method):
        self.moveGuest(1)
        for i in range(input_guests):
            room_id = 2**i
            self.all_room.add(room_id, method)

    def moveGuest(self, step):
        root = self.all_room.root
        def inorder(root):
            if root != None:
                inorder(root.left)
                id = root.room_id
                root.room_id = (2**id) + step
                inorder(root.right)
        inorder(root)
	# // maybe don’t need

    def addRoom(self, room_number):
        room = self.search_room_by_id(room_number)
        if room != None:
            self.inputGuest(1, room.method)
            self.all_room.removeRoom(room_number)
        self.all_room.add(room_number, None)
		
    def removeRoom(self, room_number):
        room = self.search_room_by_id(room_number)
        if room != None:
            self.inputGuest(1, room.method)
            self.all_room.removeRoom(room_number)
    
    def search_room_by_id(self, room_id):
        room = self.all_room.root
        while room != None:
            if room_id > room.room_id:
                room = room.right
            elif room_id < room.room_id:
                room = room.left
            else:
                break
        return room

    def __str__(self):
        root = self.all_room.root
        def inorder(root):
            if root != None:
                inorder(root.left)
                id = str(root.room_id)
                print('-'*(len(id)+2) + f'\n|{id}|\n' + '-'*(len(id)+2))
                inorder(root.right)
        inorder(root)
        return ''

    def logging(self, room):
        # self.log
        # curr = time.ctime(time.time())
        # print("Current time:", curr)
        pass
# 	// anytime after edited the hotel
# 	// log as list/linklist
# 	// logging data include room_id method
# // time of log
# 	Move:
# 		F”{}move person in room:{room[0]} to room{newroom[0]}”
# 	Remove:
# i don't know how to do this



hotel = Infinite_Hotel()
end_program = False
while not end_program:
    print('Welcome to Hilbert Hotel')
    ins = input('What do you want to do? \n[AG] to add guest\n[AR] to add room\n[RR] to remove room\ntype and enter: ')
    
    if ins == 'AG':
        start = time.time()
        tracemalloc.start()
        n, m = input('How many guest and what method that they come [N/Method]: ').split('/')
        try: 
            n = int(n)
            hotel.inputGuest(n, m)
        except:
            print('wrong input type!!!')
    elif ins == 'AR':
        start = time.time()
        tracemalloc.start()
        number = input('Enter room ID: ')
        try: 
            number = int(number)
            hotel.addRoom(number)
        except:
            print('wrong input type!!!')
    else:
        start = time.time()
        tracemalloc.start()
        number = input('Enter room ID: ')
        try: 
            number = int(number)
            hotel.removeRoom(number)
        except:
            print('wrong input type!!!')
            
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f'\nProgram work time = {end - start}')
    print(f'Program space usage = {current}\n')
    
    print(hotel)          
    if input('Do you want to end program [T/F]: ') == 'T': end_program = True
        


