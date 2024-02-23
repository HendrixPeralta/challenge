# Iterates a given list to print each if the results individually
def show_result(num_list, i=0):
    if i >= len(num_list):
        return
    print(num_list[i])
    show_result(num_list, i+1)


# Creates a list with the squared input
# Negative numbers are converted to 0 to comply with the challenge rules
# def fill_num(num_list, n):
#     if n == 0:
#         return
#     num_list.append(max(0, int(input()))**2)
#     fill_num(num_list, n-1)

def sq_sum(num_char, result):
    clean_list = map(lambda x: max(0, int(x)), num_char.split(" "))
    result.append(sum(list(map(lambda x: int(x)**2, clean_list))))


# the sum of squares is done when appending the squared list from fill_num() to the result list
def compute(cycle, result):
    if cycle == 0:
        return
    n = int(input("length"))
    #num_list = []
    #fill_num(num_list, num)
    num_str = input()

    #char_to_list(num_list, n, num_str)
    #result.append(sum(num_list))
    sq_sum(num_str, result)
    compute(cycle-1, result)


def main():
    cycle = int(input())
    result = []
    compute(cycle, result)
    show_result(result)


if __name__ == "__main__":
    main()


