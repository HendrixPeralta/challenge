def show_result(result, i=0):
    result_str = str(result).replace("[", "").replace("]", "").replace(", ", "\n")
    print(result_str)


def sq_sum(num_char, result):
    clean_list = map(lambda x: max(0, int(x)), num_char.split(" "))
    result.append(sum(list(map(lambda x: int(x)**2, clean_list))))


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


