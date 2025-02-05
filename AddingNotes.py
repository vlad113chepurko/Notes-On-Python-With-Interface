import tkinter as tk
from tkinter import Button, Label, Entry, Tk

root = Tk()
root.title('Notes')
root.geometry('400x400')

command = tk.StringVar()

class Notes():
    def __init__(self, notes):
        self.notes = notes

    def get_notes(self):
        return self.notes
    
    def add_notes(self, title, text, date):
        self.notes.append({
            'title': title,
            'text': text,
            'date': date
        })
        with open('savedNotes.txt', 'w') as file:
            for note in self.notes:
                file.write(f"Title: {note['title']}\n")
                file.write(f"Text: {note['text']}\n")
                file.write(f"Date: {note['date']}\n")
                file.write("\n")

    def load_notes(self):
        with open('savedNotes.txt', 'r') as file:
            for line in file.readlines():
                title = Label(root, text=line)
                title.pack()
                text = Label(root, text=line)
                text.pack()
                date = Label(root, text=line)
                date.pack()

notes = Notes([])

# Labelst
greeting = Label(root, text='Hello in Notes!')
instruction = Label(root, text='You can add, delete and show your notes.')
enter = Label(root, text='Enter command: That add note write "add" or if you have saved notes write "load"', pady=10)

# Packing Labels
greeting.pack()
instruction.pack()
enter.pack()   

# Input
inputCommmandLabel = Label(root, text='Enter command: ', pady=5)
inputCommmandLabel.pack()
inputCommand = Entry(root, width=50, textvariable=command)
inputCommand.pack()

# ButtonAppendCommand
def get_input():
    inputValue = command.get()
    if inputValue == 'add':
        titleLabel = Label(root, text='Enter title: ')
        titleInput = Entry(root, width=50)
        titleLabel.pack()
        titleInput.pack()
        textLabel = Label(root, text='Enter text: ')
        textInput = Entry(root, width=50)
        textLabel.pack()
        textInput.pack()
        dateLabel = Label(root, text='Enter date: ')
        dateInput = Entry(root, width=50)
        dateLabel.pack()
        dateInput.pack()
        saveButton = Button(root, text='Save', command=lambda: notes.add_notes(titleInput.get(), textInput.get(), dateInput.get()))
        saveButton.pack()
    elif inputValue == 'load':
        notes.load_notes()
    else:
        error = Label(root, text='Invalid command', fg='red')
        error.pack()

buttonApped = Button(root, text='Append', command=get_input)
buttonApped.pack()
root.mainloop()