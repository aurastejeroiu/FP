from src.domain.entity import*
from src.functions.functions import *

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
            #undoList = makeUndo_good(undoList, participants)
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

