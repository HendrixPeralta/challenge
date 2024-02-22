# init

ls = [1, -3, 5, 6, 10]
counter = 0
suma = 0


def check_neg(lst, i):
    if lst[i] < 0:
        i += 1
        check_neg(lst, i)
    return i


def show_result(lst, i=None):
    # print("im here")
    # print(i)
    print("print: " + str(lst[0]))
    if i is None:
        i = 0
    # print("print" + str(lst[i]))
    if lst[i] >= len(lst):
        # print("second if")
        return
    i += 1
    show_result(lst, i)


def sq_sum(num_list, i=0, result_carry=None):
    if i >= len(num_list):
        print(sum(result_carry))
        return sum(result_carry)

    if result_carry is None:
        result_carry = []

    result_carry.append(num_list[i] ** 2)
    sq_sum(num_list, i+1, result_carry)


def fill_num(num_list, n):
    if n == 0:
        return
    num_list.append(max(0, int(input())))
    fill_num(num_list, n-1)


def compute(cycle, result):
    if cycle == 0:
        return
    num = int(input())
    num_list = []
    fill_num(num_list, num)
    print(num_list)
    result.append(sq_sum(num_list))
    compute(cycle-1, result)


def main():
    cycle = int(input())
    result = []
    compute(cycle, result)
    print(result)
    show_result(result)
    print("finished")


if __name__ == "__main__":
    main()

