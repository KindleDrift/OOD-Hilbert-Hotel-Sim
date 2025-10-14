import time
import tracemalloc
import HilbertHotel as HH

hotel = HH.Infinite_Hotel()
end_program = False

with open("log.csv", "w", encoding="utf-8") as f:
        f.write("log, type, room number\n")
        
while not end_program:
    print('Welcome to Hilbert Hotel')
    ins = input('What do you want to do? \n[AG] to add guest\n[AR] to add room\n[RR] to remove room\ntype and enter: ')
    
    if ins == 'AG':
        n, m = input('How many guest and what method that they come [N/Method]: ').split('/')
        start = time.time()
        tracemalloc.start()
        try: 
            n = int(n)
            hotel.inputGuest(n, m)
        except:
            print('wrong input type!!!')
            
    elif ins == 'AR':
        number = input('Enter room ID: ')
        start = time.time()
        tracemalloc.start()
        try: 
            number = int(number)
            hotel.addRoom(number)
        except:
            print('wrong input type!!!')

    else:
        number = input('Enter room ID: ')
        start = time.time()
        tracemalloc.start()
        try: 
            number = int(number)
            hotel.removeRoom(number)
        except:
            print('wrong input type!!!')
        
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
        
    print(f'\nProgram work time = {end - start} s')
    print(f'Program space usage = {peak - current} byte\n')
    
    print(hotel) 
             
    if input('Do you want to end program [T/F]: ') == 'T': end_program = True