
def get_fibonacci_number(position):
    pass





def get_fibonacci_number_sequence(number):
    pass
    if number==1 or number== 2:
        return 1
    elif number==0:
        return 0
    else:
        return fibonacci_number(number-2)+fibonacci_number(number-1)
number = 3
fibonacci_number=1,1,2,3,5,8,13


if __name__ == "__main__":
    print(get_fibonacci_number_sequence)