import tkinter

class GUI:
    def __init__(self):
        self.mainframe = None
        self.locationEntryField = None
        self.budgetEntryField = None
        self.bhkEntryField = None
        self.websiteEntry = None
        self.location = None
        self.budget = None
        self.bhk = None
    def initialSearchFunc(self):
        self.location = self.locationEntryField.get()
        self.budget = float(self.budgetEntryField.get())
        self.bhk = str(self.bhkEntryField.get())
        self.websiteEntry = self.websiteEntry.get()
        self.mainframe.destroy()

        # print(location)
        # print(budget)
        # print(bhk)
    def buildGUI(self):


        self.mainframe = tkinter.Tk()
        self.mainframe.title('Rented House Hunter Bot')
        self.mainframe.minsize(width=700, height=500)
        self.mainframe.config(bg='#020403')

        titleLabel = tkinter.Label(text='Rented House Hunter Bot', font=('Bahnschrift SemiBold', 25, 'bold'), fg='white',
                                   bg='#020403')
        titleLabel.place(x=120, y=175)

        elementWidth = 22

        self.locationEntryField = tkinter.Entry(bg='#26282A', fg='white', font=('Bahnschrift SemiBold Condensed', 20, 'bold'),
                                           width=elementWidth + 11)
        self.locationEntryField.insert(0, 'Enter The Desired Location')
        self.locationEntryField.bind("<FocusIn>", lambda args: self.locationEntryField.delete('0', 'end'))
        self.locationEntryField.place(x=125, y=220)

        self.budgetEntryField = tkinter.Entry(bg='#26282A', fg='white', font=('Bahnschrift SemiBold Condensed', 20, 'bold'),
                                         width=elementWidth // 2, justify='left')
        self.budgetEntryField.insert(0, 'Budget ?')
        self.budgetEntryField.bind("<FocusIn>", lambda args: self.budgetEntryField.delete('0', 'end'))
        self.budgetEntryField.place(x=125, y=260)

        self.bhkEntryField = tkinter.Entry(bg='#26282A', fg='white', font=('Bahnschrift SemiBold Condensed', 20, 'bold'),
                                      width=elementWidth // 2)
        self.bhkEntryField.insert(0, 'Enter BHK')
        self.bhkEntryField.bind("<FocusIn>", lambda args: self.bhkEntryField.delete('0', 'end'))
        self.bhkEntryField.place(x=253, y=260)

        searchButton = tkinter.Button(bg='#7CFC00', fg='#26282A', activebackground='#7CFC00', text='Search',
                                      font=('Bahnschrift SemiBold Condensed', 14, 'bold'), width=13, command=self.initialSearchFunc)
        searchButton.place(x=381, y=260)

        self.websiteEntry = tkinter.Entry(bg='#26282A', fg='white',
                                                font=('Bahnschrift SemiBold Condensed', 20, 'bold'),
                                                width=elementWidth + 11)
        self.websiteEntry.insert(0, 'Enter Link Of The SpeadSheet')
        self.websiteEntry.bind("<FocusIn>", lambda args: self.websiteEntry.delete('0', 'end'))
        self.websiteEntry.place(x=125, y=300)

        self.mainframe.mainloop()
