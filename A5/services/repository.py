"""
    Service class includes functionalities for implementing program features
"""
from src.domain.entity import Expense

class RepositoryException(Exception):
    pass

class ExpenseRepo:

    def __init__(self):
        '''
        The function to initialize a expense class
        slef- expenses object
        '''
        self.__expenses={}

    def store(self,expense_to_add):
        '''
        The fuction of adition of one expense to the expenses list
        '''
        #expense_to_add=Expense(day,amount,type)
        self.__expenses.append(expense_to_add)

    def delete(self,expenses,value,expense):
        for index in len(expenses):
            if self.__expenses[expense.get_amount] < value:
                del self.__expenses[expense.get_amount()]
        return expenses

    def size(self):
        """
          The number of __expenses in the repository
          return an integer number
        """
        return len(self.__expenses)

    def getAllExpenses(self):
        """
        return a list, list of all __expenses in the repository
        """
        return list(self.__expenses.values())


def test_store():
    expense=Expense("12","123","electricity")
    expense_repo=ExpenseRepo
    assert expense_repo.size() == 0
    expense_repo.store(expense)
    assert  expense_repo.size() == 1
    expense2 = Expense("12", "144", "water")
    expense_repo.store(expense2)
    assert expense_repo.size() == 1
    expense3 = Expense("19", "1404", "food")
    try:
        expense_repo.store(expense3)
        assert False
    except RepositoryException:
        pass

#test_store()