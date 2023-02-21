from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name": "",
    "due": None,  # datetime
    "lastActivity": None,  # datetime
    "description": "",
    "done": False  # False if not done, datetime otherise
}


# don't edit, intentionaly left an unhandled exception possibility


def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')


def diff_in_secs(dt2, dt1):
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds


def format_time_diff(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return (abs(days), abs(hours), abs(minutes), abs(seconds))


def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()


def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")

    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")


def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        # print(_tasks)
        print(
            f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line


def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() #template is copied here
    # update lastActivity with the current datetime value
    lastActivity = datetime.now()
    try:
        if len(name) == 0: #The function returns 0 if the argument is empty 
            raise Exception("Task name is missing")
        if len(description) == 0:
            raise Exception("Task due date is missing")
        if len(due) == 0:
            raise Exception("Task due date is missing")
        # set the name, description, and due date (all must be provided)
        task = {
           "name": name,
           "description": description,
           "due": str_to_datetime(due),# due date must match one of the formats mentioned in str_to_datetime()
           "lastActivity": lastActivity,
           "done": False
        }
        task_copy = task.copy()
        tasks.append(task_copy)  #new task is added to the tasks list
        print(f'''Task: {task["name"]} added new task''')
        # make sure save() is still called last in this function
        save()
    except Exception as e:
        print("something else went wrong:", e) #implies that the save() function is available somewhere else
    #summary
    #ucid:vc435, date: 02/18/2023
    #task_template.copy() is to create new task with empty values.
    #str_to_datetime is used to convert string due time to datetime object.
    #datetime.now is used to replace lastactivity value to current date and time
    #append is to add new task to task list
    #finally, checks if all the required fiels for a task are included.
    #save() is to save the updated to tasks
 
def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
   
    if index in range(len(tasks)): # to generates the indexes of the stuff inside the list
        # gets the task by index and checking if index is out of bound
        task = tasks[index]
         # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
        name = input(f"What's the name of this task? (TODO name) \n").strip() 
        desc = input(
            f"What's a brief descriptions of this task? (TODO description) \n").strip()
        due = input(
            f"When is this task due (format: m/d/y H:M:S) (TODO due) \n").strip()
        print(f"name is updated:", name) #prints name is updated
        print(f"description is updated:", desc) #prints description is updated
        print(f"udue date is updated:", due) #prints due date is updated
    else:
        print("Invalid Index Number") 
        # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    update_task(index, name=name, description=desc, due=due)
 #summary 
 #ucid: vc435, date:02/18/2023
 #Firstly, it identifies the task that has to be updated.
 #Later stores tasks in an index, which is used to locate tasks that need to be updated.
 #Finally, calls update task() function having values updated, which passes through the index to be updated

def update_task(index: int, name: str, description: str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    if index < 0 or index >= len(tasks):
        print("Invalid Index") # consider index out of bounds scenarios and include appropriate message(s) for invalid index
        retun

    task = tasks[index]
      # update incoming task data if it's provided (if it's not provided use the original task property value)
    if name:
        task['name'] = name
    if description:
        task['description'] = description
    if due:
        task['due'] = due
    task['lastActivity'] = datetime.now()  # update lastActivity with the current datetime value

    if name or description or due:
    # output that the task was updated if any items were changed, otherwise mention task was not updated
        print("task is update")
    else:
        print("Task is not updated")
    # make sure save() is still called last in this function
    save()

#summary
#ucid: vc435 , date: 02/18/2023
#update_task : index , name, description, and due date
#finds the tasks by index and checks if it within the bounds
#if name , desc, due date values given, the values in task are updated simultaneously.
#task's activity is set to date and time and if any attributes are modified, a message is displayed stating the task has been updated.

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    if index in range(len(tasks)):
        task = tasks[index] #obtain the task via index
        if task['done'] == False:
            task['done'] = datetime.now()
            task['lastActivity'] = datetime.now()
            print("complete task")
        else:
            print("task completed already") #checking if the task is completed 
    else:
        print("invalid index")# if it's not completed then displayes invalid index

    # if it is done, print a message saying it's already completed
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    save()
    #summary
    #ucid: vc435 , date: 02/18/2023
    #mark_done() function: updates only one task to be done by assuming index as argument
    #verifies if index falls within the bound
    #index-valid ,then pulls the task from list and checks if it is completed
    #index-invalid , error message is displayed


def view_task(index):
    """ View more info about a specific task fetch by index """

    if index in range(len(tasks)): # to find if the index is within the bound
        task = tasks[index] #using index get the task
        print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))
    else:
        print("Index is out of range,please enter valid number")
        #summary
        # #ucid: vc435 , date: 02/18/2023
        # view_task : to get all the information about a particular task 
        #this function uses index as argument and finds if it is valid or not
        #the task is obtained by index , and attributes of the task are printted. If its invalid index error is displayed.


def delete_task(index):
    """ deletes a task from the tasks list by index """
    if index in range(len(tasks)):# to find if the index is within the bound
        del tasks[index] #checks is task is deleted
        print(index+1, "Deleted successful")
    else:
        print("Index is out of range,please enter valid number")
    save()
        #summary
        #ucid: vc435 , date: 02/18/2023
        #delete_task function deletes the task from the list 
        #Firstly find if the index is within the bound , if it is valid the it deletes the task from the list else the shows the error.
        #if it is deleted then the revalent message is dispalyed and calls save() function to do the changes and save.

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    _tasks = []
    # ts=[]
    # task = tasks[index]
    for index in range(len(tasks)): # to find if the index is within the bound
        task = tasks[index] #checks is task is incomplete
        if task['done'] == False:
            _tasks.append(task)
    # pass that list into list_tasks()
    list_tasks(_tasks)
    #summary
    #ucid: vc435 , date: 02/18/2023
    #incomplete task is used to create a list of incomplete taskes from the available list of tasks.
    #if task(done) is false then that task is added to incomplete task list.
    # lastly, if the incomplete task is not available it prints no incomplete tasks .
    # else,  list_tasks(_tasks)fuction is called and passes incomplete tasks to the list.




def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    _tasks = []
    for index in range(len(tasks)): # to find if the index is within the bound
        task = tasks[index] #checks is task is incomplete
        print(task)
        if str_to_datetime(task['due']) < datetime.now():
            _tasks.append(task)
    # pass that list into list_tasks()
    # _tasks = []
    list_tasks(_tasks)
    #summary
    #ucid: vc435 , date: 02/19/2023
    #overdue task consists of list of info , like task due date.
    #str to datetime converts string data and time into datetime object.
    #list_tasks prints list of task carried.


def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """

    if index < 0 or index > len(tasks):# to find if the index is within the bound
        print("Index is out of range or invalid. Please try again")
    else:
        task = tasks[index] #gets the task by index
        task_due_datetime = str_to_datetime(task['due']) #feteches the difference between  due date time and now
        days, hours, minutes, seconds = format_time_diff(diff_in_secs(
            task_due_datetime, datetime.now()))

        if (task_due_datetime > datetime.now()): #shows the time remaining using print in days, hours, minutes , seconds
            print(
                f'''\nRemaining time: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds''')
        else:
            print(
                f'''\nOver due by: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds''')
         #ucid: vc435 , date: 02/19/2023
         #time_remaining fuction shows the remaining time  for a task mentioning if it is overdue or not.
         #The remaining time is calculated by finding the difference betweern the current date and time and the due date time of the task
         #Finally, it is coverted into days, hours , minutes and seconds using divmod function.

# no changes needed below this line
command_list = ["add", "view", "update", "list", "incomplete",
                "overdue", "delete", "remaining", "help", "quit", "exit", "done"]


def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")


def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while (True):
        # strip removes whitespace from beginning/end
        opt = input("What would you like to do?\n").strip()
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input(
                "When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(
                input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(
                input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(
                input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(
                input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input(
                "Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()


if __name__ == "__main__":
    run()
