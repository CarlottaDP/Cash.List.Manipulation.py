  
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


# creando prima funzione
def fifo():
    global requests  # iterating over requests
    global cache  # iterating over cache
    global value
    i = value

    requests = set(requests)
    if i in requests:
        print('hit')
    else:
        print('miss')
        cache.append(i)
    return requests


# creando la seconda funzione
def ulf():
    global requests  # iterating over requests
    return requests


def get_value():
    global value
    value = int(input('please enter a value: '))
    requests.append(value)
    return value


program()