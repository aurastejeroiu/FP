"""
Domain file includes code for entity management
entity = number, transaction, expense etc.
"""
def make_Participant(p1,p2,p3):
    """
    Function that creates a participant
    :param p1: integer between 0-10
    :param p2: integer between 0-10
    :param p3: integer between 0-10
    :return: a new participant
    :exception: ValueError if p1 or p2 or p3 are not between 0 and 10
    """
    if p1<0 and p1>10:
        raise ValueError("The score must be a number between 0 and 10")
    if p2<0 and p2>10:
        raise ValueError("The score must be a number between 0 and 10")
    if p3<0 and p3>10:
        raise ValueError("The score must be a number between 0 and 10")
    return {'p1': p1,'p2': p2,'p3': p3, }

def newList():
    '''
    creating a partcipants list
    the elements will pe stored as [p1,p2,p3]
    '''
    return []


def getP1(participant):
    '''
    returns the score for the problem 1
    participant-dictionary of participants
    '''
    return participant["p1"]


def getP2(participant):
    '''
    returns the score for the problem 2
    participant-dictionary of participants
    '''
    return participant["p2"]


def getP3(participant):
    '''
    returns the score for the problem 3
    participant-dictionary of participants
    '''
    return participant["p3"]


def set_p1(participant,p1):
    participant["p1"]= p1

def set_p1(participant,p2):
    participant["p2"]= p2

def set_p3(participant,p3):
    participant["p3"]= p3


