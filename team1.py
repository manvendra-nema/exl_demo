def generate_num():
    numbers = list(range(1, 11))
    for number in numbers:
        print(number)
    return numbers 


def avg(list_num):
    if not list_num:   #arvind change
        return 0
    return sum(list_num)/len(list_num) #manvendra comment2
 
def sd():
    pass

def add(list_num):
    #Ujjwal_start
    if not list_num:
        print("list is empty")
        return 0
    #Ujjwal_end

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