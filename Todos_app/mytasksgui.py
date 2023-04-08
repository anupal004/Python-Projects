import time
import todofunctions
import PySimpleGUI as gui

gui.theme("LightPurple")

clock = gui.Text('', key='clock')
label = gui.Text("Enter a task")
input_box = gui.InputText(tooltip='Enter the task', key='Task')
add_button = gui.Button(image_source="add.png", tooltip="Add task", key="Add")
my_tasks = gui.Listbox(values=todofunctions.get_tasks(), key='Tasks', enable_events=True, size=[55, 10])
edit_button = gui.Button(image_source="edit.png", tooltip="Edit task", key="Edit")
complete_button = gui.Button(image_source="complete.png", tooltip="Complete task", key="Complete")
exit_button = gui.Button("Exit")

window = gui.Window("MY TASKS", layout=[[clock],
                                        [label, input_box, add_button],
                                        [my_tasks, edit_button, complete_button],
                                        [exit_button]],
                    font=('Times New Roman', 14))
# each list in the layout argument represents a row so in the above argument it will be a single row since it's
# a single list

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(time.strftime("%d-%m-%Y, %H:%M:%S"))
    match event:
        case "Add":
            tasks = todofunctions.get_tasks()
            new_task = values['Task'] + '\n'
            tasks.append(new_task)
            todofunctions.write_tasks(tasks)
            window['Tasks'].update(values=tasks)
        case "Edit":
            try:
                task_to_edit = values['Tasks'][0]
                new_task = values['Task'] + '\n'

                tasks = todofunctions.get_tasks()
                index = tasks.index(task_to_edit)
                tasks[index] = new_task
                todofunctions.write_tasks(tasks)
                window['Tasks'].update(values=tasks)
            except IndexError:
                gui.popup("Please select a task to edit.", font=("Lato", 14))
        case "Complete":
            try:
                task_to_complete = values['Tasks'][0]
                tasks = todofunctions.get_tasks()
                tasks.remove(task_to_complete)
                todofunctions.write_tasks(tasks)
                window['Tasks'].update(values=tasks)
                window['Task'].update(value="")
            except IndexError:
                gui.popup("Please select a task to remove.", font=("Lato", 14))
        case "Exit":
            break
        case "Tasks":
            window['Task'].update(value=values['Tasks'][0])
        case gui.WIN_CLOSED:
            break

window.close()
