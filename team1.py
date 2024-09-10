def generate_num():
    pass

def avg(list_num):
    if not list_num:
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