# Takes the result list iterates to show each result
def show_result(result, i=0):
    if i >= len(result):
        return
    print(result[i])
    show_result(result, i+1)


def sq_sum(num_char, result):
    clean_list = map(lambda x: max(0, int(x)), num_char.split(" "))
    result.append(sum(list(map(lambda x: int(x)**2, clean_list))))
# num_list = A list of integer numbers (str/int).
# n = the length of the list (int)
# result_carry = empty list
        # returns an int value result of the sum of squares
    # Converts the negative values into 0 to avoid counting them in the final result then it squares the number.


# cycle = the amount of times we want to repeat the process (int).
# result = is an empty list to store the values obtained from sq_sum().
def compute(cycle, result):
    if cycle == 0:
        return
    n = int(input("length"))
    num_str = input()
    sq_sum(num_str, result)
    compute(cycle-1, result)


def main():
    cycle = int(input())
    result = []
    compute(cycle, result)
    show_result(result)


if __name__ == "__main__":
    main()


