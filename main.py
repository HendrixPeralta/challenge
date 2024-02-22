# Iterates a given list to print each if the results individually
def show_result(num_list, i=0):
    if i >= len(num_list):
        return
    print(num_list[i])
    show_result(num_list, i+1)


# Must pass a list.
# def sq_sum(num_list, i=0, n=None, result_carry=None):
#     if n == 0:
#         return sum(result_carry)
#
#     if result_carry is None:
#         result_carry = []
#         n = len(num_list)
#
#     result_carry.append(num_list[i] ** 2)
#     return sq_sum(num_list, i+1, n-1, result_carry)

# Do not know if its possible to use lambda
# def sq_sum(num_lst):
#     return sum(list(map(lambda x: x**2, num_lst)))


# Negative numbers are converted to 0 to comply with the challenge rules
# Creates a list with the squared input
def fill_num(num_list, n):
    if n == 0:
        return
    num_list.append(max(0, int(input()))**2)
    fill_num(num_list, n-1)


# Negative numbers are converted to 0  to avoid unintended behaviour
def compute(cycle, result):
    if cycle == 0:
        return
    num = max(0, int(input()))
    num_list = []
    fill_num(num_list, num)
    result.append(sum(num_list))
    compute(cycle-1, result=result)


# Negative numbers are converted to 0  avoid unintended behaviour
def main():
    cycle = max(0, int(input()))
    result = []
    compute(cycle, result)
    show_result(result)


if __name__ == "__main__":
    main()

