# Problem Identification: People not being able to create an optimised schedule that is suitable for them and provides maximum efficiency and comfortability. 

# Objective: # Schedailor allows the user especially university students to optimise their existing or non existing schedule into a new efficient schedule tailor made for anyone
            # who makes use of this program!
# Initial Planning for python implementation 

    # Asking subjective inputs: 

        # What we can fetch from user related to his schedule, what he does in a day?

        # Is he a day scholar or hosteller?

        # When does he wake up?
            # Is it consistent?
            # or if not then the schedule should be made according to when he wakes up

        # How,what and how many activities he performs in a day?

        # What's his organisation's schedule (Work or Classes duration)?

        # Unpredictable changes in organisation's schedule.

        # Extra time spend for events organised by organisation depending on its priority to attend.

        # How much time does he spends in breakfast,lunch,dinner or possibly any other time when he's eating ?

        # How long and how frequent breaks he takes while doing work?

        # When does he usually sleeps?

# Scope : Mainly college students along with corporate sector

# Proposed Solution and Approach:

    # Converting subjective inputs into a schedule.

# Priority Levels and Toughness of task criteria Implementation

# When does he prefer to study and assigning tasks of low priority level at other time of the day.

# Toughness of task criteria asks an input of whether user prefers to move from easy to difficult task or vice versa or performing task of a favourite subject is preferred more or the least one

# Priority levels of deadlines 

# --------------------------------------------------------------------------------------------------------------------------------- #

# Ag: Initialised before , added condition for making sure the inputted format matches the asked format

list_tasks = []

while True :
    store_tasks = input('Task : Duration(in hrs) to complete the task : Toughness level of the task(1-10) : Priority level of the task(1-10) ')
    split_tasks = store_tasks.split(':')

    if store_tasks=='end':
        break
    
    if len(split_tasks) != 4:                                   # dtp should be in integer 
        print("Error: Invalid input format. Please write in required format(e.g., Study:2:8:10)")
        continue                   # Skips code below it for invalid input , and restarts the loop

    list_tasks.append(split_tasks)

# --------------------------------------------------------------------------------------------------------------------------------- #

    # Ag : Formatting ; Ag,Sh,Pr : Brainstorming

        # To - do's - 1 (Storing,Filtering,Retrieval):

            # Sh : Assigning values to dictionaries and sorting tasks according to priority level {Tasks : [D,T,P]}

            # Pr : Confining inputs by using conditions and printing invalid input if invalid request recieved

            # Ag : Providing user with values associated with the respective tasks at the end of the loop and when asked 
                # along with returning the values(D:T:P) of inputted task by the user

            # To implement after above tasks are completed:

                # Strikethrough font on completed tasks when asked by the user to display status of tasks

# --------------------------------------------------------------------------------------------------------------------------------- #

#Sh ; ( Ag : Polished ):

sorted_tasks=[]
while list_tasks:
    first_task = list_tasks[0]
    for task in list_tasks:
        if int(task[3])>int(first_task[3]):         # Priority of task at index 3 of each task nested list
            first_task=task
    sorted_tasks.append(first_task)
    list_tasks.remove(first_task)

new_tasks_dict = {}

for task_as_key in sorted_tasks:
    new_tasks_dict[task_as_key[0]]=task_as_key[1:]

print(new_tasks_dict)

# --------------------------------------------------------------------------------------------------------------------------------- #

# Ag: 

while True:
    y_n = input('Do you want to retrieve inputted information associated with a task inputted earlier ? (Yes/No) ')
    if y_n.lower() == 'yes':
        retrieval_of_task = input('Enter the task ')
        if retrieval_of_task in new_tasks_dict:
            print(new_tasks_dict[retrieval_of_task])
    else:
        break

# --------------------------------------------------------------------------------------------------------------------------------- #

    # Ag : Formatting ; Ag,Sh,Pr,Bh : Brainstorming

        # To - do's - 2 (Polishing Output,Completion and Deleltion of tasks):

            # Sh : Polishing of output -> Current output    --> {'eating': ['5', '3', '8'], 'sleeping': ['7', '1', '3']}

            #                        Output to achieve --> 1. ☑ 'eating'   --> [' 5 hours ',' Toughness - 3 ',' Priority - 8 '] 
            #                                              2. ◻ 'sleeping' --> [' 7 hours ',' Toughness - 1 ',' Priority - 3 '] 

            # Implementation of completion of a task -->

                # Ag: Transferring the tasks that are completed into a diffrent dictionary consisting of completed tasks(being done on a daily or weekly task)
                #     along with having same format to be achieved whilst polishing the orignial one.

                # Conditions required to delete a task forever directly or delete the tasks from the completed tasks dictionary

                # A bigger while loop encapsuling the other smaller while loop code blocks inside of which a input would be asked,
                # for the user whether if he wants to add task,delete tasks forever,check out completed tasks or retrieve tasks

                # Pr : A non - interactive checkbox showing whether if a task is completed beside the task
                #      and a task number for the convienience of marking a task as complete or incomplete by the user's input as the task number itself
                #      when asked using another while loop

            # Showing the top 5 tasks according to priority level, and if inputted to see the remaining tasks , print the next 5
            # or if inputted to show all of them, print all of the tasks.


        # After logic & backend completion, moving on to UI implementation connected to python

# --------------------------------------------------------------------------------------------------------------------------------- #


    # Ag : Brainstorming ; Ai : Formatting

        # To - do's - 3 (Implementation of file handling due to working of current loops whilst requiring a bigger while loop) -->

            # Saving state (Write): Exporting the active tasks and completed tasks dictionaries into a .txt or .csv file before the program exits so data isn't lost.

            # Loading state (Read): Fetching and parsing the saved file when the program launches to rebuild the dictionaries, allowing the user to pick up where they left off.

            # Auto-update mechanism: Overwriting or appending to the save file dynamically whenever a user adds, completes, or deletes a task in the main menu loop.
            
# --------------------------------------------------------------------------------------------------------------------------------- #