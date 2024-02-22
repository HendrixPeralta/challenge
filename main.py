
def show_result(num_list, i=0):
    if i >= len(num_list):
        return
    print(num_list[i])
    show_result(num_list, i+1)


def sq_sum(num_list, i=0, n=None, result_carry=None):
    if n == 0:
        return sum(result_carry)

    if result_carry is None:
        result_carry = []

    result_carry.append(num_list[i] ** 2)
    return sq_sum(num_list, i+1, n-1, result_carry)

# def sq_sum(num_lst):
#     return sum(list(map(lambda x: x**2, num_lst)))


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
    result.append(sq_sum(num_list, n=len(num_list)))
    compute(cycle-1, result=result)


def main():
    cycle = int(input())
    result = []
    compute(cycle, result)
    print(result)
    show_result(result)
    print("finished")


if __name__ == "__main__":
    main()

