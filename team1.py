def generate_num():
    numbers = list(range(1, 11))
    for number in numbers:
        print(number)
    return numbers 


    pass 

def avg(list_num):
    if not list_num:   #arvind change
        return 0
    return sum(list_num)/len(list_num)

def sd():
    pass

def add(list_num):
    return sum(list_num)


def main():
    nums_liz = generate_num()
    print(nums_liz)
    sum = add(nums_liz)
    print(sum)
    mean = avg(nums_liz)
    print(mean)
    std = sd(nums_liz)
    print(std)
main()