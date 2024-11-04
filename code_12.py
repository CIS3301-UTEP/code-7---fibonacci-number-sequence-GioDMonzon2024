def get_fibonacci_number(position):

    if position == 1:
        return 1
    elif position == 2:
        return 1 
    else:
        return get_fibonacci_number(position - 1) + get_fibonacci_number (position - 2)

def get_fibonacci_number_sequence(number):
# One of my CS friends recommneded using an empty sequence bracket
    fibonacci_sequence = []
    for i in range(1, number + 1):
        fibnacci_number = get_fibonacci_number(i)
        fibonacci_sequence.append(fibnacci_number)
    return fibonacci_sequence
# This part of the sequence wasn't running
# My CS friend told me to append the list
# I had to do 20 minutes worth of research to find out what that meant

if __name__ == "__main__":
    print(get_fibonacci_number(5))  
    print(get_fibonacci_number_sequence(7)) 
# I also need assistance with the testing functions.
# He provided insight