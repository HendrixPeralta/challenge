# init

ls = [1, 3, 5, 5, 10]
counter = 0
suma = 0


def sq_sum(lst, i, total):
    if i == 0:
        total = 0

    print("i: " + str(i))
    print("number: " + str(lst[i]))
    result = lst[i] ** 2 + total
    i += 1

    if i >= len(lst):
        result = 0
        print("total is: " + str(result))
        return result

    sq_sum(lst, i, result)


sq_sum(ls, counter, suma)
