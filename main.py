# init

ls = [1, -3, 5, 5, 10]
counter = 0
suma = 0


def sq_sum(lst, i=None, total=None, result_carry=None):
    if i is None:
        i = 0
        total = 0
        result_carry = []

    # Delete before sending *************
    print("i: " + str(i))
    print("number: " + str(lst[i]))

    # checks if the number in the list is negative
    if lst[i] < 0:
        print("im here")
        i += 1
        sq_sum(lst, i, total, result_carry)

    result = lst[i] ** 2 + total
    i += 1
    print("result: " + str(result))

    if i >= len(lst):
        print("*" * 40)
        print("total is: " + str(result))

        result_carry.append(result)
        print(result_carry)
        return result_carry

    sq_sum(lst, i, result, result_carry)


def show_result(lst, i=None):
    print(lst[i])
    if lst[i] >= len(lst):
        return
    i += 1
    show_result(lst, i)


sq_sum(ls)
