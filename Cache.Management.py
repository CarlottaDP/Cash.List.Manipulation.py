# Carlotta Dipede, Student ID : 201537058

#                                                 Designing the logic of the program

# define an empty Request list

requests = []

# Defining an empty cache list
cache = []
# Setting the environment for the program to function
main_program = True


# Designing a function for the menu-user interaction
def program():
    print('Hello human')
    get_value() # defining an empty variable for us to store prompt values and pass any parameter into the function

# Definig a function to prompt user into Menu selection
def option():
    global requests
    global main_program

    option = input('Please select 1 for FIFO, 2 for LFU or q for exit: ')
    if(option == '1'):
        print(fifo())  # Calling the Method fifo function that is not yet defined 
    elif(option == '2'):
        print(lfu())  # Calling the Method Lfu function that is not yet defined 
    elif(option == 'q'):
        print('See ya')
        main_program = False


def get_value():
    global requests
    while True:
        try:
            value = int(input('please enter a value or 0 to go back to cache selection: '))
            requests.append(value)
            option()
            if (value < 0):
                raise ValueError
            elif (value == 0):
                option()
            break
        except ValueError:
            print('my processors cannot understand the input')
    return value


# A method fifo()- Defining a function to run the FIFO cache management on cache and requests
def fifo():
    global requests  #  iterating over requests- Global environment allows the function to access the lists 
    global cache
    reqlist = [] # Declaring an empty list to optimize manipulation of indexes in requests list 
    reqlist = requests[:: -1] # storing in the empty list the elements in request list but reversed. 

    # Reversing elements as per above allows me to place the last page requested into index position [0].
    # this technique allows me to check if the last requested page is in the list, by accessing index [0].

    # defining a condition for the program to locate pages upon their existence in the cache.
    if(reqlist[0] in cache): 
        print('hit')
        print('page ' + str(reqlist[0]) + ' already inside cache') 
    else:
        cache.append(reqlist[0])
        print('miss')
        if(len(cache) <= 8):
            print('page ' + str(reqlist[0]) + ' added to the cache')
        else:
            cache.pop(0)
            print('page ' + str(reqlist[0]) + ' added and ' + str(cache[0]) + ' removed')


# A method lfu()- Defining a function to run the LFU cache management on cache and requests
def lfu():
    global requests  # iterating over requests
    global cache
    
    freq = {} # holding the pages frequencies 
    for i in requests:
        if i in freq.keys(): # creating a for loop - using dictionary access key 
             print('hit', i, ' exist in cache already')
       
        # if i is present then increase the frequency to 1 only.
             freq[i] += 1 # 
        else:
            print('miss', i, ' added into cache')
            freq[i] = 1

            if len(cache) < 8: 
                cache.append(i) # appending i to the cache when its length is below 8 ( indices) 

            else: # search and remove the least accessed page 
                leastAccessed_page = { x: freq [x] for x in cache if x in cache }
                # removing the page used the least ( i.e. less hit count ) and remove , then append new page
                leastUsed_page = min(leastAccessed_page, key = leastAccessed_page(*get_value))
                cache.remove(leastUsed_page)
                # adding i to the cache list 
                cache.append(i)


    print(freq) # printing the  dictionary (frequency holder)
    print(cache) 

lfu()



while main_program:
    program()