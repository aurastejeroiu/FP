"""The sequence a = a1, ..., an with distinct integer elements is given. Determine all subsets of at least two elements with the property:
The elements in the subset are in increasing order
Any two consecutive elements in the subsequence have at least one common digit"""


def solution(list):
    number_of_elements = len(list)

    if number_of_elements == 4:
        return True

    return False


def go_forward(list):
    number_of_elements = len(list)
    ok = 1
    if number_of_elements != 2:
        for i in range(1, number_of_elements - 1):
            if list[i] != list[i + 1] - 1:
                ok = 0
            if ok == 0:
                return False
    return True


def task(list, aparition_list):
    number_of_elements_first_list = len(aparition_list)
    number_of_elements_second_list = len(list)
    if number_of_elements_first_list > 2 and number_of_elements_second_list > 1:
        ok = 1
        ok2 = 0
        # The elements in the subset are in increasing order
        for index in range(1, number_of_elements_first_list - 1):
            a = list[aparition_list[index] - 1]
            b = list[aparition_list[index + 1] - 1]
            c = str(b)
            if a > b:
                ok = 0
            # Any two consecutive elements in the subsequence have at least one common digit
            while a > 0:
                last_digit = a % 10

                if str(last_digit) in c:
                    ok2 = ok2 + 1
                a = a // 10
            if ok2 == 0:
                ok = 0
        if ok == 1:
            final_subset = []
            for index in range(1, number_of_elements_first_list):
                final_subset.append(list[aparition_list[index] - 1])
            print(final_subset)


def backtracking_iterative(list):
    aparition_list = [0]
    index = 1
    aparition_list.append(0)
    while index > 0:

        if aparition_list[index] < len(list):
            aparition_list[index] = aparition_list[index] + 1
            if go_forward(aparition_list):
                task(list, aparition_list)
                index = index + 1
                aparition_list.append(0)
        else:
            index = index - 1
            aparition_list.pop()


def backtracking_recursive(list, aparition_list, index):
    if index > 0:
        if aparition_list[index] < len(list):
            aparition_list[index] = aparition_list[index] + 1
            if go_forward(aparition_list):
                task(list, aparition_list)
                index = index + 1
                aparition_list.append(1)
            backtracking_recursive(list, aparition_list, index)

        else:
            index = index - 1
            aparition_list.pop()
            backtracking_recursive(list, aparition_list, index)


list = [12, 23, 32, 33, 4, 5, 45, 7, 177, 777]
#backtracking_iterative(list)
#backtracking_recursive(list, [0, 0], 1)

def run(list):
    print("Choose option 1 for iterative backtracking or 2 for recursive backtracking!")
    option = int(input("Give option:"))
    if option == 1:
        backtracking_iterative(list)
    else:
        if option==2:
            backtracking_recursive(list, [0, 0], 1)

run(list)