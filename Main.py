import time
import tracemalloc
import HilbertHotel as HH

print('Welcome to Hilbert Hotel')
initial = int(input("Enter the initial guest amount : "))
hotel = HH.Infinite_Hotel(initial)

with open("log.csv", "w", encoding="utf-8") as f:
        f.write("log, type, room number\n")
        
while True:
    print('-------------------------------------------------------------------------------------------')
    
    ins = input('What would you like to do? ("HELP" to see all command): ').split(' ')
    
    print()
    
    if ins[0] == 'HELP': 
        print(' -> "AG <channel,amount|...>" to add guest. Ex AG Car,10|Bus,6 .')
        print(' -> "AR <Room_number>" to add that room.')
        print(' -> "SER <Room_number>" to search that room.')
        print(' -> "RR <Room_number>" to remove that room')
        print(' -> "SOR" to sort room and export to csv')
        print(' -> "S" to save data to csv')
        print(' -> "END" to end the program')
        continue
    
    if ins[0] == 'END': break
    
    start = time.time()
    tracemalloc.start()
        
    if ins[0] == 'AG':
        channel_list = []
        amount_list = []
        try: 
            for ch in ins[1].split('|'):
                channel, amount = ch.split(',')
                channel_list.append(channel)
                amount_list.append(int(amount))
        except:
            print('wrong input type!!!')
            continue
        hotel.inputGuest(channel_list, amount_list)
            
    elif ins[0] == 'AR':
        try: 
            number = int(ins[1])
        except:
            print('wrong input type!!!')
            continue
        if hotel.addRoom(number):
            print(f'Add room {number} succesfully')
        else:
            print('This room is already exist!!!')

    elif ins[0] == 'SER':
        try: 
            number = int(ins[1])
        except:
            print('wrong input type!!!')
            continue
        room = hotel.search_room_by_id(number)
        if room is None:
            print('This room is not exist!!!')
        else:
            print(f'Room {number}, channel {room.method}({room.method_id})')
    
    elif ins[0] == 'SOR':
        try: 
            number = int(ins[1])
            hotel.addRoom(number)
        except:
            print('wrong input type!!!')
            continue
    
    elif ins[0] == 'RR':
        try: 
            number = int(ins[1])
        except:
            print('wrong input type!!!')
            continue
        if hotel.removeRoom(number):
            print(f'Remove room {number} succesfully')
        else:
            print('This room is not exist!!!')
            
    elif ins[0] == 'S':
        hotel.rooms_to_csv()
            
    else:
        print("That command doesn't exist!!!")
        
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
        
    print(f'\nProgram work time = {end - start} s')
    print(f'Program space usage = {peak - current} byte')
