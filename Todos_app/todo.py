import todofunctions
# or we can also write - from functions import get_tasks, write_tasks
import time
print("It is", time.strftime("%d-%m-%Y, %H:%M:%S"))

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        task = user_action[4:]
        task_new = task.capitalize()

        # file_read = open('tasks.txt', 'r')
        # tasks = file_read.readlines()
        # file_read.close()

        # using, with context manager case, we do not need to close the files
        # with open('tasks.txt', 'r') as file_read:
        # tasks = file_read.readlines()

        tasks = todofunctions.get_tasks()

        tasks.append(task_new + '\n')

        todofunctions.write_tasks(tasks)

        # file_write = open('tasks.txt', 'w')
        # file_write.writelines(tasks)
        # file_write.close()

    elif user_action.startswith('show'):
        tasks = todofunctions.get_tasks()

        for index, work in enumerate(tasks):
            work = work.strip('\n')
            # to remove the extra spaces between each line, or we can also use list comprehensions as given below:
            # new_work = [work.strip('\n') for work in tasks]

            organised = f"{index + 1}. {work}"
            print(organised)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            tasks = todofunctions.get_tasks()

            print(tasks[number])
            new_task = input("Edit the current task: ")
            tasks[number] = new_task.capitalize()

            todofunctions.write_tasks(tasks)
        except ValueError:
            print("Wrong input syntax. Try again.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            tasks = functions.get_tasks()

            index = number - 1
            task_to_remove = tasks[index].strip('\n')
            tasks.pop(index)

            functions.write_tasks(tasks)

            message = f"Task: {task_to_remove} has been removed"
            print(message)
        except ValueError and IndexError:
            print("Wrong input syntax. Try again.")
            continue

    elif user_action.startswith('exit'):
        print("Thank You!")

    else:
        print("Invalid command")
