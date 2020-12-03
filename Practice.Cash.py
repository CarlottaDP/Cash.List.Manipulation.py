  
# introduzione studente
# design menu

value = 0
requests = []
# set limit of list to 8 int
cache = [] * 8
main_program = True


# menu
def program():
    print('Hello human')
    get_value()
    option = input('Please select 1 for FIFO, 2 for LFU or q for exit: ')
    if(option == '1'):
        print(fifo())  # chiamando funzione ancora non definita
    elif(option == '2'):
        print(ulf())  # chiamando funzione ancora non definita
    elif(option == 'q'):
        print('See ya')

# defining a function to collect a value from user into Program () function above
def get_value():
    global value
    value = int(input('please enter a value: '))
    requests.append(value)
while get_value(): # ask the user a value for an int repeatedly until 0 is entered
    if(value != 0) :  # here if the value is different from 0, then keep ask user for any other value 
         # ???
         # ??
        return


# creando prima funzione Fifo
def fifo():
    global requests  # iterating over requests
    global cache  # iterating over cache
    global value
    i = value

    requests = set(requests)
    if i in requests:
        print('hit', i, 'already exist in chace') 
    else:
        print('miss', i, 'now added')
    if len(cache) == 8: # IF chache is full, the page keept for the longest time is removed
        del cache[0]
        cache.append(i) # THEN keep adding the requested page into the chache
    else:
        cache.append(i) # if the chache is NOT full, just add requested page into the chache as normal
    return requests


# creando la seconda funzione
def ulf():
    global requests  # iterating over requests
    return requests




program()