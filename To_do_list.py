
TD_list = []
CT_list = []

def main_menu():
    print("="*15, "MAIN MENU", "=" *15)
    print(f"[1] ADD TASK TO YOUR TO DO LIST: ")
    print(f"[2] SHOW ALL TASK IN TO DO LIST: ")
    print(f"[3] MARK TASK AS COMPLETED: ")
    print(f"[4] SHOW ALL COMPLETED TASK: ")
    print(f"[5] REMOVE TASK FROM TO TO LIST: ")
    print(f"[6] USER GUIDELINES: ")
    print(f"[7] ABOUT US: ")
    print(f"[8] EXIT PROGRAM: ")

    n = input("\n Choose number corresponding to action you want to take: ")

    if n == '1':
        Add_Items_to_LIst()
    elif n == '2':
        Show_All_Items_in_TD(TD_list)
    elif n == '4':
        Show_All_Completed_Task(CT_list)
    elif n == '3':
        Mark_Task_AsComplete(TD_list)
    elif n == '5':
        Remove_Task(TD_list)
    elif n == '6':
        User_guidelines()
    elif n == '7': 
        About_us()
    else:
        Exit()
    exit()
       

def User_guidelines():
    print("*"*10, "THIS IS OUR USER GUIDELINES", "*"*10)
    print("""\n 
    To use the to do list app, 
    You must follow the instructions properly,
    specifically only ['b'] for back and [0] to exit totally exit""")

    print("""
    IF YOU CARELESSLY PRESS ANY BUTTON OTHER 
    THAN 'b' FOR BACK, YOUR SESSION WILL END""")

    print("\n", "*"*10, "ENJOY", "*"*10)

    Go_back_or_Exit()

def About_us():
    print("*"*10, "ABOUT US", "*"*10)
    print("\n", "*"*10, "I am called <<'THE MAN IN CHARGE'>> ", "*"*10)
    print("""\n 
    I am a young student learning Python programming 
    Language from the National higher polytechnic
    intitute of Bamenda, decided to try out this exercise """)
    Go_back_or_Exit()

    

def Go_back_or_Exit():
    n = input("Press ['b'] to go back or [0] to Exit program ")

    if n == "b":
        main_menu()
    elif n == '0':
        Exit()
    

def Exit():
    print("="*10, "THANKS FOR USING OUR SERVICES", "="*10)
    exit()

def Add_Items_to_LIst():
    i = 1
    while True:
        To_do = input(f"Enter task{i}: ")
        TD_list.append(To_do)
        i += 1
        n = input("Press any key to continue adding task, else press ['b']")
        if n == 'b':
            main_menu()
            return TD_list
            break
        else:
            continue


def Show_All_Items_in_TD(TD_list):
    i = 1
    for task in TD_list:
        print(f"Task{i} is {task}")
        i += 1
    Go_back_or_Exit()


def Mark_Task_AsComplete(TD_list):
    if TD_list == []:
        print("no task added")
        Go_back_or_Exit()
    i = 1
    for task in TD_list:
        print(f" [{i}]>> {task}")
        i += 1
    count = 0
    while True:

        n = int(input("Enter task you have completed or [99] to stop entering task: "))
        count = n
        if count == 99:
            break
        CT_list.append(TD_list[n - 1])
    Go_back_or_Exit()
    return CT_list


def Show_All_Completed_Task(CT_list):
    i = 1
    for items in CT_list:
        print(f"Task{i} which is {items} is completed ")
        i += 1
    Go_back_or_Exit()

def Remove_Task(TD_list):
    if TD_list == []:
        print("no task available to remove")
        Go_back_or_Exit()

    count = 0
    while True:
        i = 1
        for task in TD_list:
            print(f"[{i}] >> {task}")
            i += 1
        
        n = int(input("Enter the number corresponding to the task you want to remove or [99] to stop removing task: "))
        count = n
        if count == 99:
            break
        TD_list.remove(TD_list[n - 1])
    Go_back_or_Exit()
    return TD_list


def main():
    TD_list = []
    CT_list = []
    main_menu()


if __name__ == "__main__":
    main()
