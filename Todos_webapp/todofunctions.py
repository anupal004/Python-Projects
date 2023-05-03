FILEPATH = "tasks.txt"


def get_tasks(filename=FILEPATH):
    """ Read a text file and return the list of tasks """
    # """ """ represents a doc-string
    with open(filename, 'r') as file_local:
        tasks_local = file_local.readlines()
    return tasks_local


def write_tasks(tasks_local, filename=FILEPATH):
    """ Write the list of tasks in a text file """
    with open(filename, 'w') as file:
        file.writelines(tasks_local)


if __name__ == "__main__":
    print("The file is executed directly here and not being imported.")
