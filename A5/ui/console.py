"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""
from src.domain.entity import*
from src.domain.validators import*
from src.services.repository import*
from src.services.controller import*

class console():
    def __init__(self,ExpensesController):
        self.ExpensesController=ExpensesController

    def __add_expense(self):
        day=int(input("Give day: "))
        amount=int(input("Give amount: "))
        type=(input("Give type: "))

        expense=self.__ExpensesController.add_expense(day,amount,type)
        print("DAY: ", expense.get_day, "|| Amount: ", expense.get_amount, "|| Type: ", expense.get_type)

    def __showAll(self):
        expense_list=self.__ExpenseController.get_all()
        print("DAY   AMOUNT   TYPE")
        for expense in expense_list:
            print(expense.get_day(),expense.get_amount(), expense.get_type())

    def __delete(self):
        value=int(input("Give amount: "))
        expense_list = self.__ExpenseController.get_all()
        for index in len(expense_list):
            if expense_list[index].get_amount < value:
                delete(expense_list[index])

    def UI_run(self):
        print("1.Add expense")
        print("2.Show expenses")
        print("3.Filter")
        print("4.UNDO")

        while True:
            command=int(input("Give command:"))
            if command==1:
                print("Add expense")
                self.__add_expense()
            if command==2:
                print("Show:")
                self.__showAll()
            if command==3:
                print("Delete expenses")
                self.__delete()
            if command==4:
                print("Undo")
            self.__undo_operation()

repository=ExpenseRepo()
validator=ExpenseValidator()
controller=ExpensesController
UI=console(controller)
UI.UI_run()