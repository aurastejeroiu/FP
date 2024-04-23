from domain.entity import Expense

class ValidatorException(Exception):
    def __init__(self, errors):
        self.errors = errors

    def getErrors(self):
        return self.errors

class ExpenseValidator:
    def validate(self, expense):
        """
        throw ValidatorException if fields are empty
        """
        errors = []
        if (expense.get_day() == ""): errors.append("Day can not be empty!")
        if (expense.get_amount() == ""): errors.append("Amount can not be empty!")
        if (expense.get_type() == ""): errors.append("Type can not be empty!")
        if len(errors) > 0:
            raise ValidatorException(errors)

def testValidator():
    validator=ExpenseValidator()
    expense=Expense("", "", "")
    try:
        validator.validate(expense)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors())==3
    expense = Expense("12", "", "")
    try:
        validator.validate(expense)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors())==2
    expense = Expense("12", "123", "water")
    try:
        validator.validate(expense)
        assert True
    except ValidatorException as ex:
        assert False

testValidator()