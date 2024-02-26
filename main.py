# Takes the result list iterates to show each result
def show_result(result, i=0):
    if i >= len(result):
        return
    print(result[i])
    show_result(result, i+1)


# num_list = A list of integer numbers (str/int).
# n = the length of the list (int)
# result_carry = empty list
def sq_sum(num_list, i=0, n=None, result_carry=None):
    if n == 0:
        # returns an int value result of the sum of squares
        return sum(result_carry)
    # Converts the negative values into 0 to avoid counting them in the final result then it squares the number.
    result_carry.append(max(0, int(num_list[i]))**2)
    return sq_sum(num_list, i+1, n-1, result_carry)


# cycle = the amount of times we want to repeat the process (int).
# result = is an empty list to store the values obtained from sq_sum().
def compute(cycle, result):
    if cycle == 0:
        return
    n = int(input("length"))
    num_list = input().split(" ")  # Converts the string into a string list.
    result_carry = []
    result.append(sq_sum(num_list=num_list, n=n, result_carry=result_carry))
    compute(cycle-1, result)


def main():
    cycle = int(input())
    result = []
    compute(cycle, result)
    show_result(result)


if __name__ == "__main__":
    main()

