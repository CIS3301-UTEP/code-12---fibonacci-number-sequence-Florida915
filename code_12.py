1,1,2,3,5,8,13
def get_fibonacci_number(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fibonacci_number(position-2)+ get_fibonacci_number(position-1)
    
    
    
def get_fibonacci_number_sequence(number):
    if number == 1:
        return 1
    elif number ==2:
        return 1,1
    elif number ==3:
        return 1,1,2
    elif number==4:
        return 1,1,2,3
    elif number ==5:
        return 1,1,2,3,5
    elif number == 6:
        return 1,1,2,3,5,8
    elif number == 7:
        return 1,1,2,3,5,8,13
    else:
        return None
    
list=[1,1,2,3,5,8,13]

if __name__ == "__main__":
    print(get_fibonacci_number(6))
    print(get_fibonacci_number_sequence(8))