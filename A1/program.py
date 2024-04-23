# Source code for Test 1 program. Success!
#import importlib

def sum(first_param,second_param,third_param):
    return first_param+second_param+third_param

def alternative_sum(first_param,second_param,third_param,fourth_param):
    return first_param - second_param + third_param - fourth_param

def negative(param):
    return 0-param

    """
    Add is a function that receives a command from the console and solves that mathematical function
    cmd is the command and final si the final result 
    it returns the final result 
    """

def add_command (cmd,Final):
    #cmd = input("give command: ")
    if (cmd == "add"):
        first_param = int(input("first_param="))
        second_param = int(input("second_param="))
        third_param = int(input("third_param="))
        sum_final = sum(first_param, second_param, third_param)
        Final =Final+sum_final
        #print(sum_final)
    if (cmd == "alternate"):
        first_param = int(input("first_param="))
        second_param = int(input("second_param="))
        third_param = int(input("third_param="))
        fourth_param = int(input("fourth_param="))
        alternative_final = alternative_sum(first_param, second_param, third_param, fourth_param)
        Final = Final + alternative_final
        #print(alternative_final)
    if (cmd == "neg"):
        param = int(input("param="))
        neg_param = negative(param)
        Final = Final + neg_param
        #print(neg_param)

    return Final

def list_command(cmd,Final):
    # cmd = input("give command: ")
    if (cmd == "add"):
        print("first_param+second_param+third_param=")
        first_param = int(input("first_param="))
        second_param = int(input("second_param="))
        third_param = int(input("third_param="))
        sum_final = sum(first_param, second_param, third_param)
        Final = Final + sum_final
        print("Final=",first_param,"+",second_param,"+",third_param)
        print(Final,"=", first_param, "+", second_param, "+", third_param)
        # print(sum_final)
    if (cmd == "alternate"):
        first_param = int(input("first_param="))
        second_param = int(input("second_param="))
        third_param = int(input("third_param="))
        fourth_param = int(input("fourth_param="))
        alternative_final = alternative_sum(first_param, second_param, third_param, fourth_param)
        Final = Final + alternative_final
        print("Final=", first_param, "+", second_param, "-", third_param,"+",fourth_param)
        print(Final, "=", first_param, "+", second_param, "-", third_param,"+",fourth_param)
        # print(alternative_final)
    if (cmd == "neg"):
        param = int(input("param="))
        neg_param = negative(param)
        Final = Final + neg_param
        print("Final=0-",neg_param)
        print(Final,"=0-", neg_param)
        # print(neg_param)

"""def one_operation():
    if (cmd == "add"):
        first_param = int(input("first_param="))
        second_param = int(input("second_param="))
        third_param = int(input("third_param="))
        sum_final = sum(first_param, second_param, third_param)
        Final =Final+sum_final
        print(sum_final)
    if (cmd == "alternate"):
        first_param = int(input("first_param="))
        second_param = int(input("second_param="))
        third_param = int(input("third_param="))
        fourth_param = int(input("fourth_param="))
        alternative_final = alternative_sum(first_param, second_param, third_param, fourth_param)
        Final = Final + alternative_final
        print(alternative_final)
    if (cmd == "neg"):
        param = int(input("param="))
        neg_param = negative(param)
        Final = Final + neg_param
        print(neg_param)

    return Final"""

def main():
    cmd="none"
    op=1
    Final=0
    while (op!=0):
        op = (int(input("for add press 1~~~for list press 2~~~for one operation press 3~~~ for exit press 0: ")))
        cmd=input("give command: ")
        if (op==1):
            Final=add_command(cmd, Final)
            print(Final)

        if (op==2):
            Final=list_command(cmd,Final)
            #print(Final)

        """if (op==3):
            Final = one_operation(cmd, Final)
            #print(Final)"""


        op=(int(input("if you want to continue type 1 else press 0: ")))

        if(op==0):
            print("Finished")
main()
