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

def ui_add_command(participants, commandInformation):
    """This is the UI function for <add> command. When called, it adds a participant to the participant list (after calling another non-UI function)
    :param participants: a participants list
    :param commandInformation: <add> command parameters: parameters[0] is the apartment number, parameters[1] is the expense type and parameters[2] is the expense amount
    :return: -"""

    parameters = commandInformation.split(' ')
    if len(parameters) != 4:
        raise ValueError("Invalid parameters for command 'add'.")
    p1=parameters[0]
    p2=parameters[1]
    p3=parameters[2]
    add_participant(participants, p1, p2, p3)



def ui_remove_command(participants, commandInformation):

    parameters = commandInformation.split(' ')
    if len(parameters) ==1:
        index=parameters[0]
        remove_participant(participants, index)
    if len(parameters) ==2:
        index_begin=parameters[0]
        index_end=parameters[1]
        remove_participants_between_positions(participants, index_begin, index_end)
    if  len(parameters) != 1 and len(parameters)!=2:
        raise ValueError("Invalid parameters for command 'remove'.")



def ui_modify_command(participants, commandInformation):
    parameters = commandInformation.split(' ')
    if len(parameters) != 4:
        raise ValueError("Invalid parameters for command 'add'.")
    new_p1 = parameters[0]
    new_p2 = parameters[1]
    new_p3 = parameters[2]
    index=parameters[3]
    update_participant(participants, new_p1, new_p2, new_p3, index)



def display_all(participants):
    for index in range(len(participants)):
        print(index, " p1:", participants[index]['p1'], "||", "p2:", participants[index]['p2'], "||", "p3:",participants[index]['p3'])

def display_decreasing_order(participants):
    participants1 = participants
    decreasing_order(participants1)
    for index in range(len(participants)):
        print(index, " p1:", participants1[index]['p1'], "||", "p2:", participants1[index]['p2'], "||", "p3:",
              participants1[index]['p3'])

def display_smaller_point(participants, commandInformation):
    parameters = commandInformation.split(' ')
    if  len(parameters) != 1:
        raise ValueError("Invalid parameters for command 'display'.")
    score=parameters[0]
    for index in range(len(participants)):
        average1 = Average(participants[index]['p1'], participants[index]['p2'], participants[index]['p3'])
        if average1 < score:
            print(index, " p1:", participants[index]['p1'], "||", "p2:", participants[index]['p2'], "||", "p3:",participants[index]['p3'])

def display_equal_point(participants, commandInformation):
    parameters = commandInformation.split(' ')
    if  len(parameters) != 1:
        raise ValueError("Invalid parameters for command 'display'.")
    score=parameters[0]
    for index in range(len(participants)):
        average1 = Average(participants[index]['p1'], participants[index]['p2'], participants[index]['p3'])
        if average1 == score:
            print(index, " p1:", participants[index]['p1'], "||", "p2:", participants[index]['p2'], "||", "p3:",participants[index]['p3'])

def display_average(participants, commandInformation):
    parameters = commandInformation.split(' ')
    if len(parameters) == 1:
        average=average_participants(participants)
        print("The average is: ", average)
    if len(parameters) == 2:
        index_begin = parameters[0]
        index_end = parameters[1]
        average=average_participants_positions(participants, index_begin, index_end)
        print("The average between positions is: ", average)
        if len(parameters) != 1 and len(parameters) != 2:
            raise ValueError("Invalid parameters for command 'display'.")

def display_the_PODIUM(participants, commandInformation):
    parameters = commandInformation.split(' ')
    if len(parameters) != 1:
        raise ValueError("Invalid parameters for command 'display'.")
    people_on_podium=parameters[0]
    participants1 = participants
    Podium(participants1, people_on_podium)
    while index < people_on_podium:
        print(index, " p1:", participants[index]['p1'], "||", "p2:", participants[index]['p2'], "||", "p3:",
              participants[index]['p3'])
        index = index + 1

"""function that splits a comand given by the user"""
def split_command(command):
    # Splits a user command
    #:param command: a user command
    #:return: a list containing the user command and its parameters

    splitedCommand = command.split(' ', 1)
    return splitedCommand[0].strip().lower(), splitedCommand[1].strip() if len(splitedCommand) == 2 else ''


def undo_command(participants,undo_list,commandInformation):
    parameters = commandInformation.split(' ')
    if parameters == ['']:
        parameters = []
    if len(parameters) != 0:
        raise ValueError("Invalid parameters from command 'undo'.")
    if not len(undo_list):
        raise ValueError("Cannot do 'undo' command anymore.")
    undo(undo_list,participants)

def print_commands():
    print("List of commands:")
    print("1. Add new participant, using the structure:")
    print("   add <p1> <p2> <p3>")
    print("2.Modify an existing participant")
    print("  modify <new_p1> <new_p2> <new_p3> <index>")
    print("3.Delete")
    print("  remove <index>")
    print("  remove <index_begin> <index_end>")
    print("4.    Display")
    print("4.1.  displayALL")
    print("4.2.  displayDecreasing")
    print("4.3.  displaySmaller <score>")
    print("4.4.  displayEqual <score>")
    print("4.5.  displayAverage")
    print("4.6.  displayAveragePositions, <index_begin> <index_end>")
    print("4.7.  displayPODIUM <people_on_podium>")
    print("5.Undo")
    print("6.Exit")
    print("\n")

def Ui_commands():
    print_commands()
    participants=newList()
    Populate(participants)

    commands={"add":ui_add_command, "modify":ui_modify_command, "delete":ui_remove_command,"diplayAll":display_all,
              "DisplayDecreasing":decreasing_order,"displaySmaller":display_smaller_point,"displayEqual":display_equal_point,
              "displayAverage":display_average,"displayPodium":display_the_PODIUM,"undo":undo_command}
    done = False
    undo_list=[[]]
    while not done:
        try:
            uiCommand = input('Enter command: ').strip()
            Word, commandInformation = split_command(uiCommand)
            if Word in ["add", "modify", "delete", "diplayAll", "DisplayDecreasing", "displaySmaller", "displayEqual", "displayAverage", "displayPodium"]:
                undo_list=make_undo(undo_list,participants)
            if Word in commands:
                if Word=="undo":
                    undo_command(participants, undo_list, commandInformation)
                else:
                    commands[Word](participants,commandInformation)
            elif 'exit' == Word:
                done = True
                print("Bye!")
            else:
                print("This command is not a valid command.")

        except ValueError as value_error:
            print(str(value_error))
