from src.domain.entity import Expense
from src.domain.validators import ExpenseValidator
from src.services.repository import ExpenseRepo

class ExpensesController(object):
    def __init__(self, repository, validator):
        """
          Initialise controller
          repository - reposirory - object to store expenses
          validator - validator - object to validate expenses
        """
        self.__repository = repository
        self.__validator = validator

    def create_Expense(self,day,amount,type):
        expense=Expense(day,amount,type)
        self.__validator.validate(expense)
        self.__repository.store(expense)

        return expense

    def delete(self,expense):
        print(expense)
        return self.__repository.delete(expense)

    def get_all(self):
        return self.__repository.get_AllExpenses()

def test_create():
    repository=ExpenseRepo
    validator=ExpenseValidator
    controller=ExpensesController(repository,validator)
    expense=controller.create_Expense("12", "144", "water")
    assert expense.get_day()=="12"
    assert expense.get_amount()=="144"
    assert expense.get_type()=="water"
    All_Expenses=controller.get_all()
    assert len(All_Expenses)==1

#test_create()