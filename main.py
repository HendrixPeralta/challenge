# Iterates a given list to print each if the results individually
def show_result(num_list, i=0):
    if i >= len(num_list):
        return
    print(num_list[i])
    show_result(num_list, i+1)


# Creates a list with the squared input
# Negative numbers are converted to 0 to comply with the challenge rules
def fill_num(num_list, n):
    if n == 0:
        return
    num_list.append(max(0, int(input()))**2)
    fill_num(num_list, n-1)


# Negative numbers are converted to 0  to avoid unintended behaviour
# the sum of squares is done when appending the squared list from fill_num() to the result list
def compute(cycle, result):
    if cycle == 0:
        return
    num = max(0, int(input()))
    num_list = []
    fill_num(num_list, num)
    result.append(sum(num_list))
    compute(cycle-1, result)


# Negative numbers are converted to 0  avoid unintended behaviour
def main():
    cycle = max(0, int(input()))
    result = []
    compute(cycle, result)
    show_result(result)


if __name__ == "__main__":
    main()

