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


################################################
#FUNCTIONS
################################################

# (A) Add the result of a new participant

def add_participant(participants, p1, p2, p3):
    """
    Introduces the name from the console
    Params:
        number -nomber of participants

    """
    """p1 = int(participant_info[0])
    p2=int(participant_info[1])
    p3=int(participant_info[2])
    participant=make_Participant(p1,p2,p3)
    participants.append(participant)"""

    """
    Introduces the name from the console
    Params:
        number -nomber of participants
    """
    participants.append(make_Participant(p1, p2, p3))


def test_add():
    test_Participants = []
    test_Participants.append(make_Participant(1, 8, 6))
    test_Participants.append(make_Participant(2, 8, 8))
    test_Participants.append(make_Participant(3, 8, 3))
    test_Participants.append(make_Participant(3, 4, 9))
    test_Participants.append(make_Participant(4, 9, 10))
    test_Participants.append(make_Participant(5, 5, 6))
    test_Participants.append(make_Participant(6, 7, 6))
    assert len(test_Participants) == 7


# (B) Modify scores
def update_participant(participants, new_p1, new_p2, new_p3, index):
    """
    The function updates the parameters of one participant
    :param participants:
    :param new_p1: integer
    :param new_p2: integer
    :param new_p3: integer
    :return: -
    """
    participants[index]['p1'] = new_p1
    participants[index]['p2'] = new_p2
    participants[index]['p3'] = new_p3

    return participants


def test_update():
    """
    Function tests the update functionality
    """
    test_Participants = make_Participant(1, 8, 6)
    assert update_participant(test_Participants, 7, 5, 9, 0)
    assert update_participant(test_Participants, 7, 3, 5, 0)
    assert update_participant(test_Participants, 2, 5, 4, 0)


# (B).1 REMOVE

def remove_participant(participants, index):
    """
    The function removes a participants with a given index
    :param participants: the list of participants
    :param index: integer
    :return: the list
    """
    del participants[index]
    return participants


def remove_participants_between_positions(participants, index_begin, index_end):
    """
    The function removes a participants between 2 positions
    :param participants: list of participants
    :param index_begin: integer>0
    :param index_end: integer<len(participants)
    :return: the modifieed list
    """
    while index_begin < index_end:
        del participants[index_begin]
        index_begin = index_begin + 1
    return participants


def test_remove():
    '''
    TEST the remove functionality
    '''
    test_Participants = []
    test_Participants.append(make_Participant(1, 8, 6))
    test_Participants.append(make_Participant(2, 8, 8))
    test_Participants.append(make_Participant(3, 8, 3))
    test_Participants.append(make_Participant(3, 4, 9))
    test_Participants.append(make_Participant(4, 9, 10))
    test_Participants.append(make_Participant(5, 5, 6))
    test_Participants.append(make_Participant(6, 7, 6))

    test_Participants = remove_participants_between_positions(test_Participants, 2, 4)
    assert len(test_Participants) == 5


# (C) Display participants


def Average(p1, p2, p3):
    """
    calculates the average of the scores of a participant
    :param p1: integer
    :param p2: integer
    :param p3: integer
    :return: the average
    """
    average = p1 + p2 + p3
    average = average // 3
    return average


def average_participants(participants):
    """

    :param participants: the list
    :return: the average between all the participants
    """
    average = 0
    for index in range(len(participants)):
        average = average + Average(participants[index]['p1'], participants[index]['p2'], participants[index]['p3'])
    average = average // len(participants)
    return average


def average_participants_positions(participants, index_begin, index_end):
    """

    :param participants: the list
    :return: the average between all the participants
    """
    average = 0
    while (index_begin < index_end):
        index = index_begin
        average = average + Average(participants[index]['p1'], participants[index]['p2'], participants[index]['p3'])
        index_begin = index_begin + 1
    average = average // len(participants)
    return average


def lowest_average(participants, index_begin, index_end):
    minim = 100
    while (index_begin < index_end):
        index = index_begin
        average = Average(participants[index]['p1'], participants[index]['p2'], participants[index]['p3'])
        if average < minim:
            minim = average
        index_begin = index_begin + 1
    return minim


def decreasing_order(participants):
    for index in range(len(participants) - 1):
        for index1 in range(len(participants)):
            average1 = Average(participants[index]['p1'], participants[index]['p2'], participants[index]['p3'])
            average2 = Average(participants[index1]['p1'], participants[index1]['p2'], participants[index1]['p3'])
            if average1 > average2:
                new_p1 = participants[index]['p1']
                new_p2 = participants[index]['p2']
                new_p3 = participants[index]['p3']
                participants[index]['p1'] = participants[index1]['p1']
                participants[index]['p2'] = participants[index1]['p2']
                participants[index]['p3'] = participants[index1]['p3']
                participants[index1]['p1'] = new_p1
                participants[index1]['p2'] = new_p2
                participants[index1]['p3'] = new_p3
    return participants


# (D) Obtain different characteristics of participants

def Podium(participants, number):
    for index in range(len(participants) - 1):
        for index1 in range(len(participants)):
            average1 = Average(participants[index]['p1'], participants[index]['p2'], participants[index]['p3'])
            average2 = Average(participants[index1]['p1'], participants[index1]['p2'], participants[index1]['p3'])
            if average1 > average2:
                new_p1 = participants[index]['p1']
                new_p2 = participants[index]['p2']
                new_p3 = participants[index]['p3']
                participants[index]['p1'] = participants[index1]['p1']
                participants[index]['p2'] = participants[index1]['p2']
                participants[index]['p3'] = participants[index1]['p3']
                participants[index1]['p1'] = new_p1
                participants[index1]['p2'] = new_p2
                participants[index1]['p3'] = new_p3


"""def lower_score(participants,score):
    for index in range(len(participants)):
        average1 = Average(participants[index]['p1'], participants[index]['p2'], participants[index]['p3'])
        if average1<score:
            print(index, " p1:", participants[index]['p1'], "||", "p2:", participants[index]['p2'], "||", "p3:",participants[index]['p3'])
"""
"""def same_score(participants,score):
    for index in range(len(participants)):
        average1 = Average(participants[index]['p1'], participants[index]['p2'], participants[index]['p3'])
        if average1==score:
            print(index, " p1:", participants[index]['p1'], "||", "p2:", participants[index]['p2'], "||", "p3:",participants[index]['p3'])
"""


# (E) Establish the podium


# (F) Undo
def make_undo(undo_list, participants):
    """
    We store here the last opperation done
    :param undo_list: the list from the last opperation done
    :param participants: the modified list
    :return: undo_list
    """
    undo_list.append([])
    for index in participants:
        undo_list[len(undo_list) - 1].append(index.copy)
    return undo_list


def undo(undo_list, participants):
    """
    The undo function
    :param undo_list:the undo list
    :return:the old undo list
    """
    participants[:] = undo_list.pop


def add_undo(participants):
    undo_list = {}
    undo_list = list(participants)
    return undo_list


def undo1(undo_list):
    return undo_list[len(undo_list) - 2]


def test_make_undo():
    test_Participants = [make_Participant(1, 2, 3), make_Participant(5, 6, 7)]
    undoList = []
    undoList = make_undo(undoList, test_Participants)

    assert len(undoList) == len(test_Participants)


def test_undo():
    test_Participants = []
    undo_list = []

    test_Participants.append(make_Participant(1, 2, 3))
    undo_list = make_undo(undo_list, test_Participants)

    test_Participants.append(make_Participant(7, 2, 3))

    # test_Participants=undo(undo_list)
    # assert test_Participants==[make_Participant(1,2,3),make_Participant(7,2,3)]

    test_Participants = undo(undo_list)
    assert test_Participants == [make_Participant(1, 2, 3)]


def TEST_ALL():
    test_add()
    test_update()
    test_remove()
    test_make_undo()
    test_undo()


# TEST_ALL()

def makeUndo_good(undoList, participants):
    undoList.append(list(participants))
    return undoList


def undo_good(undoList):
    old_list = undoList[-1]
    del undoList[-1]
    return old_list

################################################
#CONSOLE
################################################

def Populate(participants):
    #participants=[]
    participants.append(make_Participant(1, 8, 6))
    participants.append(make_Participant(2, 8, 8))
    participants.append(make_Participant(3, 8, 3))
    participants.append(make_Participant(3, 4, 9))
    participants.append(make_Participant(4, 9, 10))
    participants.append(make_Participant(5, 5, 6))
    participants.append(make_Participant(6, 7, 6))
    participants.append(make_Participant(10,9,9))
    participants.append(make_Participant(10,5,10))
    participants.append(make_Participant(10,10,10))
    participants.append(make_Participant(1, 1, 1))


def UI_menu_based():
    participants=newList()
    undo_list=[]
    undoList=[]
    new_copied_list=[]
    Populate(participants)

    while True:
        print ("1 <--Add a new participant with a score")
        print ("2 <--Modify a score")
        print ("3 <--Delete a score")
        print ("4 <--Delete scores between 2 positions")
        print("5 <--Display the average of the average scores for participants")
        print ("6 <--Display the average of the average scores for participants between positions ")
        print ("7 <--Display the lowest average score of the participants between positions")
        print ("8 <--Print in decreasing order of average scores") #;;;copie la listaaa
        print ("9 <--Print the participants with scores < than a given score")
        print ("10 <--Print the participants with the average score = given score")
        print ("11<--Display ALL")
        print ("12<--THE PODIUM (the first x participants)")
        print ("13<--UNDO")
        print("14<--UNDO_ADD")
        print("15<--Working one_undo")
        print("16<--The Undo that actually works :)")
        print ("0 <--Exit")

        option=int(input("Operation: "))

        if option==1:
            print("Add a participant:")
            p1=int(input("p1= "))
            p2 = int(input("p2= "))
            p3 = int(input("p3= "))
            #new_copied_list = participants.copy()
            #undo_list=make_undo(undo_list,participants)
            undoList=makeUndo_good(undoList,participants)
            add_participant(participants,p1,p2,p3)

        if option == 2:
            #new_copied_list = participants.copy()
            #undo_list = make_undo(undo_list, participants)
            print("Modify a score")
            index=int(input("Give index:"))
            new_p1=int(input("new_p1= "))
            new_p2=int(input("new_p2= "))
            new_p3=int(input("new_p3= "))
            undoList=makeUndo_good(undoList,participants)
            update_participant(participants, new_p1, new_p2, new_p3,index)

        if option == 3:
            print("Remove")
            index=int(input("Give index:"))
            new_copied_list = participants.copy()
            undoList=makeUndo_good(undoList,participants)
            remove_participant(participants, index)

        if option == 4:
            print("Delete scores between 2 positions")
            index_begin= int(input("Give index_begin:"))
            index_end = int(input("Give index_end:"))
            undoList=makeUndo_good(undoList,participants)
            remove_participants_between_positions(participants, index_begin, index_end)

        if option==5:
            average=average_participants(participants)
            print("The average is:",average)

        if option==6:
            index_begin = int(input("Give index_begin:"))
            index_end = int(input("Give index_end:"))
            average = average_participants_positions(participants,index_begin,index_end)
            print("The average is:", average)

        if option==7:
            index_begin = int(input("Give index_begin:"))
            index_end = int(input("Give index_end:"))
            average=lowest_average(participants,index_begin,index_end)
            print("The lowest average is:", average)

        if option==8:
            participants1=participants
            decreasing_order(participants1)
            for index in range(len(participants)):
                print(index, " p1:", participants1[index]['p1'], "||", "p2:", participants1[index]['p2'], "||", "p3:",participants1[index]['p3'])

        if option == 9:
            score=int(input("Give score:"))
            for index in range(len(participants)):
                average1 = Average(participants[index]['p1'], participants[index]['p2'], participants[index]['p3'])
                if average1 < score:
                    print(index, " p1:", participants[index]['p1'], "||", "p2:", participants[index]['p2'], "||", "p3:",
                          participants[index]['p3'])

        if option ==10:
            score = int(input("Give score:"))
            for index in range(len(participants)):
                average1 = Average(participants[index]['p1'], participants[index]['p2'], participants[index]['p3'])
                if average1 < score:
                    print(index, " p1:", participants[index]['p1'], "||", "p2:", participants[index]['p2'], "||", "p3:",
                          participants[index]['p3'])

        if option==11:
            for index in range(len(participants)):
                print(index, " p1:", participants[index]['p1'], "||", "p2:", participants[index]['p2'], "||", "p3:",participants[index]['p3'])

        if option==12:
            participants1 = participants
            x=int(input("Give how many people will be on the podium:"))
            Podium(participants1,x)
            index = 0
            while index < x:
                print(index, " p1:", participants[index]['p1'], "||", "p2:", participants[index]['p2'], "||", "p3:",
                      participants[index]['p3'])
                index = index + 1

        if option==13:
            undo_list = make_undo(undo_list, participants)
            for index in range(len(undo_list)):
                print(index, " p1:", participants[index]['p1'], "||", "p2:", participants[index]['p2'], "||", "p3:",
                      participants[index]['p3'])

        if option==14:
            participants=undo1(undo_list)
            del(undo_list[-1])
            for index in range(len(participants)):
                print(index, " p1:", participants[index]['p1'], "||", "p2:", participants[index]['p2'], "||", "p3:",participants[index]['p3'])


        if option==15:
            for index in range(len(new_copied_list)):
                print(index, " p1:", new_copied_list[index]['p1'], "||", "p2:", new_copied_list[index]['p2'], "||", "p3:",new_copied_list[index]['p3'])


        if option==16:
            participants=undo_good(undoList)

UI_menu_based()
