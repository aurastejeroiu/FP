class Expense:
    '''
    Creating a new expense
    '''
    def __init__(self, day, amount, type):
        self.__day=day
        self.__amount=amount
        self.__type=type

    def get_day(self):
        """

        :return: the day
        """
        return self.__day

    def get_amount(self):
        '''

        :return: the amount
        '''
        return self.__amount

    def get_type(self):
        '''
        returns the type
        '''
        return self.__type

def test_Create():
    expense=Expense("12","123","water")
    assert expense.get_day()=="12"
    assert expense.get_amount()=="123"
    assert expense.get_type()=="water"

test_Create()

