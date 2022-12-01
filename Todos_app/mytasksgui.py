import todofunctions
import PySimpleGUI as gui

label = gui.Text("Enter a task")
input_box = gui.InputText(tooltip='Enter the task')
add_button = gui.Button("Add")

window = gui.Window("MY TASKS", layout=[[label, input_box, add_button]])
window.read()
window.close()
