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


def sq_sum(lst, i=None, total=None, result_carry=None):
    if i is None:
        i = 0
        total = 0
        result_carry = []

    # Delete before sending *************
    # print(lst)
    print("i: " + str(i))
    print("number: " + str(lst[i]))

    # checks if the number in the list is negative
    i = check_neg(lst, i)

    result = lst[i] ** 2 + total
    i += 1
    print("result: " + str(result))

    if i >= len(lst):
        print("*" * 40)
        print("total is: " + str(result))

        result_carry.append(result)
        print(result_carry)
        # return result_carry
        show_result(result_carry)
        return

    sq_sum(lst, i, result, result_carry)

# def user_input):
#     value = int(input())
#     return value


def main(cycle=None, num=None, num_lst=None, i=None, j=None, result_list=None):

    if cycle is None:
        cycle = int(input())
        print("cycle: " + str(cycle))
        i = 0

    if num is None:
        num = int(input())
        print("num: " + str(num))
        num_lst = []
        j = 0

    if j < num:
        num_lst.append(int(input()))
        print("num_list: " + str(num_lst))
        j += 1
        main(cycle, num, num_lst, i, j)

    i += 1

    if i >= cycle:
        print("finished")
        return

    main(cycle=cycle, i=i)

    # print("i: " + str(i))
    # print("cycle: " + str(cycle))


main()
#sq_sum(ls)

