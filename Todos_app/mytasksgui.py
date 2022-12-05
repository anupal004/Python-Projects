import todofunctions
import PySimpleGUI as gui

label = gui.Text("Enter a task")
input_box = gui.InputText(tooltip='Enter the task', key='Task')
add_button = gui.Button("Add")

window = gui.Window("MY TASKS", layout=[[label, input_box, add_button]],
                    font=('Times New Roman', 14))
# each list in the layout argument represents a row so in the above argument it will be a single row since it's
# a single list

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            tasks = todofunctions.get_tasks()
            new_task = values['Task'] + '\n'
            tasks.append(new_task)
            todofunctions.write_tasks(tasks)
        case gui.WIN_CLOSED:
            break

window.close()
