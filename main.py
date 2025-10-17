import time
import tracemalloc
import Infinite_Hotel as HH

print('Welcome to Hilbert Hotel')
initial = int(input("Enter the initial guest amount : "))
hotel = HH.Infinite_Hotel(initial)
        
while True:
    print('-------------------------------------------------------------------------------------------')
    
    ins = input('What would you like to do? ("HELP" to see all command): ').split(' ')
    
    print()
    
    if ins[0] == 'HELP': 
        print(' -> "AG <method,amount|...>" to add guest. Ex AG Car,10|Bus,6 .')
        print(' -> "AR <room_id>" to add that room.')
        print(' -> "SER <room_id>" to search that room.')
        print(' -> "RR <room_id>" to remove that room')
        print(' -> "SOR" to sort room and export to csv')
        print(' -> "S" to save data to csv')
        print(' -> "END" to end the program')
        continue
    
    if ins[0] == 'END': break
    
    start = time.time()
    tracemalloc.start()
        
    if ins[0] == 'AG':
        method_list = []
        amount_list = []
        try: 
            for ch in ins[1].split('|'):
                method, amount = ch.split(',')
                method_list.append(method)
                amount_list.append(int(amount))
        except:
            print('wrong input type!!!')
            continue
        hotel.input_guest(method_list, amount_list)
            
    elif ins[0] == 'AR':
        try: 
            room_id = int(ins[1])
        except:
            print('wrong input type!!!')
            continue
        if hotel.add_room(room_id):
            print(f'Add room {room_id} succesfully')
        else:
            print('This room is already exist!!!')

    elif ins[0] == 'SER':
        try: 
            room_id = int(ins[1])
        except:
            print('wrong input type!!!')
            continue
        room = hotel.search_room_by_id(room_id)
        if room is None:
            print("This room doesn't exist!!!")
        else:
            print(f'Room {room_id}, method {room.method}({room.method_id})')
    
    elif ins[0] == 'SOR':
        hotel.rooms_to_csv()
        print('Sort room and export to csv successfully')
    
    elif ins[0] == 'RR':
        try: 
            room_id = int(ins[1])
        except:
            print('wrong input type!!!')
            continue
        if hotel.remove_room(room_id):
            print(f'Remove room {room_id} succesfully')
        else:
            print("This room doesn't exist!!!")
            
    elif ins[0] == 'S':
        hotel.rooms_to_csv()
        print('Export to csv successfully')
            
    else:
        print("That command doesn't exist!!!")
        
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
        
    print(f'\nProgram work time = {end - start} s')
    print(f'Current memory usage = {current / 1024:.2f} KB')
    print(f'Peak memory usage = {peak / 1024:.2f} KB')
