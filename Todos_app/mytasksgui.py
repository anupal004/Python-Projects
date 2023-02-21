import todofunctions
import PySimpleGUI as gui

label = gui.Text("Enter a task")
input_box = gui.InputText(tooltip='Enter the task', key='Task')
add_button = gui.Button("Add")
my_tasks = gui.Listbox(values=todofunctions.get_tasks(), key='Tasks', enable_events=True, size=[40, 10])
edit_button = gui.Button("Edit")

window = gui.Window("MY TASKS", layout=[[label, input_box, add_button], [my_tasks, edit_button]],
                    font=('Times New Roman', 14))
# each list in the layout argument represents a row so in the above argument it will be a single row since it's
# a single list

while True:
    event, values = window.read()
    print("user_action:", event)
    print(values['Task'])
    print(values['Tasks'])
    match event:
        case "Add":
            tasks = todofunctions.get_tasks()
            new_task = values['Task'] + '\n'
            tasks.append(new_task)
            todofunctions.write_tasks(tasks)
            window['Tasks'].update(values=tasks)
        case "Edit":
            task_to_edit = values['Tasks'][0]
            new_task = values['Task'] + '\n'

            tasks = todofunctions.get_tasks()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task
            todofunctions.write_tasks(tasks)
            window['Tasks'].update(values=tasks)
        case "Tasks":
            window['Task'].update(value=values['Tasks'][0])
        case gui.WIN_CLOSED:
            break

window.close()
