# Import necessary libraries
from tkinter.filedialog import askopenfile
from PIL import ImageTk
from PIL import Image as IMG
import customtkinter as ctk
from tkinter import *
from ReadPDF import ExtractPDFData, ExtractData
from DatabaseManager import *
from tkinter.messagebox import showerror, showinfo
import webbrowser

# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________

# Create a custom Tkinter window
master = ctk.CTk()

# Set the width and height of the window
width = round(master.winfo_screenwidth() / 1.4)
height = round(master.winfo_screenheight() / 1.5)

# Set the geometry of the window
master.geometry("{}x{}+150+100".format(width, height))

# Bind the Escape key to quit the window
master.bind('<Escape>', lambda e: master.quit())

# Set the appearance mode of the window
ctk.set_appearance_mode("light")

# Set the title of the window
master.title("Text Extractor")

# Set the minimum size of the window
master.minsize(int(width / 1.15), int(height / 1.1))

# Set the background color of the window
master.config(bg="white")

# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________

# Open the logo image and resize it for use as a header image
logoNxn = IMG.open('assets/logo.png')
w, h = logoNxn.size
logoNxn1 = ImageTk.PhotoImage(logoNxn.resize((round((w / h) * (height / 3.5)), round((height / 3.5))), IMG.ANTIALIAS))
logoNxn2 = ImageTk.PhotoImage(logoNxn.resize((round((w / h) * (height / 8.5)), round((height / 9.5))), IMG.ANTIALIAS))

# Create a list of image icons for use in the main interface
f3_Icons2 = []

# Open the "computer" icon image and resize it
im = IMG.open("f3_icons/computer.png")
w, h = im.size
f3_Icons2.append(ImageTk.PhotoImage(im.resize((round(width / 40), round(width / 40)), IMG.ANTIALIAS)))

# Open the "collaborate" icon image and resize it
im = IMG.open("f3_icons/collaborate.png")
w, h = im.size
f3_Icons2.append(ImageTk.PhotoImage(im.resize((round(width / 25), round(width / 25)), IMG.ANTIALIAS)))

# Open the "database" icon image and resize it
im = IMG.open("f3_icons/database.png")
w, h = im.size
f3_Icons2.append(ImageTk.PhotoImage(im.resize((round(width / 25), round(width / 25)), IMG.ANTIALIAS)))



# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________

# Create several Frame objects for use in the main interface
f1 = Frame(master, bg="#ffffff")
f2 = Frame(master, bg="#ffffff")
f3 = Frame(master, bg="#ffffff")
f4 = Frame(master, bg="#ffffff")
f5 = Frame(master, bg="#ffffff")


# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________

# Initialize some variables
filePath = StringVar()
count = IntVar()
count.set(0)
count2 = IntVar()
count2.set(0)


# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________

# Define a function to send an email with a given subject
def SendEmail(x):
    email_address = 'it.support@hud.ac.uk'
    subject = x
    body = ''

    url = f"https://mail.google.com/mail/u/0/?view=cm&fs=1&to={email_address}&su={subject}&body={body}"
    webbrowser.open_new(url)

# Define a class SCROLL that inherits from ctk.CTkScrollableFrame.
class SCROLL(ctk.CTkScrollableFrame):

    # Initialize the SCROLL class.
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Initialize an empty list to hold buttons and call the update_() method.
        self.Buttons = []
        self.update_()

    # Define the update_() method to add widgets to the frame and populate the Buttons list.
    def update_(self):
        # Initialize an empty list to hold buttons.
        self.Buttons = []

        # Iterate over the data returned by the getAllData() function and create a widget for each item.
        count.set(0)
        for x, i in enumerate(getAllData()):
            f = ctk.CTkFrame(self, width=822, height=40, corner_radius=15, fg_color="grey95")

            # Create a label widget with text and add it to the frame.
            Label(f, text=" " * 5 + i[1] + " " * 10 + i[0], bg="grey95", fg="#1D1C9B", anchor=W,font=("Calibri", round((width / 300) * 2.8))).place(relwidth=0.2, relheight=0.7, relx=0.05, rely=0.15)

            # Create a button widget with a command to call the ExtractionPlace function with an argument num=i[1].
            # Add the button to the frame.
            ctk.CTkButton(f, width=822, height=40, bg_color="white", text="View", text_color="grey95",hover_color="white",font=("Calibri", round((width / 300) * 3.2)),command=lambda num=i[1]: [ExtractionPlace(num)]).place(relwidth=0.12, relheight=0.7,relx=0.87, rely=0.15)

            # Place the frame on the grid at row x and column 0 with a 5-pixel vertical padding.
            f.grid(row=x, column=0, pady=5)

            # Increment the count and count2 variables.
            count.set(count.get() + 1)
            count2.set(count2.get() + 0.01)


# Define the ExtractionPlace function that takes a single argument name.
def ExtractionPlace(name):
    # Access the global data variable and populate it with data for the given name.
    global data
    data = getUserData(name)

    # Call the setF4 function to update the GUI with the retrieved data.
    setF4()

    # Hide the f5 widget using the place_forget() method.
    f5.place_forget()

    # Display the f4 widget on the screen
    f4.place(relx=0, rely=0, relwidth=1, relheight=1)


# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________

# Create a label widget named img_f5 with a white background color and an NW anchor.
# Place the img_f5 label widget on the parent widget f5.
img_f5 = Label(f5, bg="white", anchor=NW)
img_f5.place(relx=-0.01, rely=0, relwidth=0.2, relheight=1)

# Create a label widget to display an image with the filename logoNxn2.
# The label widget is placed on the parent widget f5.
Label(f5, image=logoNxn2, bg="#ffffff", anchor=NW).place(relx=0, rely=0.15, relwidth=0.18)

# Define the testf5 function that takes an optional event parameter.
def testf5(event=None):
    # Load an image named left.png, resize it, and create a PhotoImage object named leftGra.
    leftGra = ImageTk.PhotoImage(
        IMG.open('assets/left.png').resize((round(round(master.winfo_screenwidth() / 1.4) / 5.7),f5.winfo_height()), IMG.ANTIALIAS))

    # Set the image of the img_f5 label widget to leftGra and update its image attribute.
    img_f5.config(image=leftGra)
    img_f5.image = leftGra


# Bind the testf5 function to the <Configure> event of the f5 widget.
f5.bind("<Configure>", testf5)

# Create three label widgets for FAQ, Donate, and Contact, respectively.
lf5a = Label(f5, text="FAQ", fg="white", bg="#1D1C9B", font=("Calibri", round((width / 300) * 2.2)), anchor=NW)
lf5b = Label(f5, text="Donate", fg="white", bg="#1F1CA3", font=("Calibri", round((width / 300) * 2.2)), anchor=NW)
lf5c = Label(f5, text="Contact", fg="white", bg="#1F1D9E", font=("Calibri", round((width / 300) * 2.2)), anchor=NW)

# Place the three labels on the f5 widget with different vertical offset and width.
lf5a.place(x=50, rely=0.352 + 0.4, width=32)
lf5b.place(x=50, rely=0.394 + 0.39, width=55)
lf5c.place(x=50, rely=0.436 + 0.38, width=55)

# Create a label widget to display the Desktop V1.1 text.
Label(f5, text="Desktop V1.1", fg="white", bg="#211FA6", font=("Calibri", round((width / 300) * 2)), anchor=NW).place(
    x=50, rely=0.52 + 0.42, width=round((width / 300) * 15.8))

# Bind email sending functions to the left labels when left mouse button is clicked.
lf5a.bind("<Button-1>", lambda event: SendEmail("Question About the Application"))
lf5b.bind("<Button-1>", lambda event: SendEmail("Donation"))
lf5c.bind("<Button-1>", lambda event: SendEmail("Contacting from Application"))
# Create a label widget with the first icon from f3_Icons2, with white text and white background.
Label(f5, image=f3_Icons2[0], anchor=NW, fg="white", bg="white").place(relx=0.225, rely=0.025, relwidth=0.13)

# Create a label widget to display the "Database" text with black text and white background.
Label(f5, text="Database", fg="black", bg="#ffffff", font=("Calibri", round((width / 300) * 4)), anchor=NW).place(relx=0.26, rely=0.03, relwidth=0.13)

# Create a label widget with white text and grey background to use as a separator.
Label(f5, anchor=NW, fg="white", bg="grey").place(relx=0.22, rely=0.1, relwidth=0.7, relheight=0.002)

# Create a button widget to go back to the f3 widget with blue border and white text.
ctk.CTkButton(master=f5, border_color="#3160DA", fg_color="#001B62", text="Back", border_width=1,font=("Calibri", round((width / 300) * 3.3)), corner_radius=12,command=lambda: [f5.place_forget(), ImagePath.delete(0,END) , f3.place(relx=0, rely=0, relheight=1, relwidth=1)]).place(relx=0.88, rely=0.93, relwidth=0.095, relheight=0.045)

# Create a SCROLL widget with white background and blue scrollbar button color and place it on the f5 widget.
SCROLL1 = SCROLL(f5, bg_color="white", fg_color="white", scrollbar_button_color="#3160DA")
SCROLL1.place(relx=0.22, rely=0.12, relwidth=0.7, relheight=0.75)



# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________


# Create a label widget with white background and NW anchor to use as a background image on the left side of f4.
img_f4 = Label(f4, bg="white", anchor=NW)
img_f4.place(relx=-0.01, rely=0, relwidth=0.2, relheight=1)

# Create a label widget with the logo image to be placed on the top left corner of f4.
Label(f4, image=logoNxn2, bg="#ffffff", anchor=NW).place(relx=0, rely=0.15, relwidth=0.18)

# Define a function to resize and set the left image of f4 based on window resize.
def testf4(event=None):
    leftGra = ImageTk.PhotoImage(IMG.open('assets/left.png').resize((round(round(master.winfo_screenwidth()/1.4) / 5.7), f4.winfo_height()), IMG.ANTIALIAS))
    img_f4.config(image=leftGra)
    img_f4.image = leftGra

# Bind the <Configure> event to call the testf4 function to resize the left image of f4.
f4.bind("<Configure>", testf4)

# Create label widgets for FAQ, Donate and Contact with specific styling and positioning.
lf4a = Label(f4, text="FAQ", fg="white", bg="#1D1C9B", font=("Calibri", round((width / 300) * 2.2)), anchor=NW)
lf4b = Label(f4, text="Donate", fg="white", bg="#1F1CA3", font=("Calibri", round((width / 300) * 2.2)), anchor=NW)
lf4c = Label(f4, text="Contact", fg="white", bg="#1F1D9E", font=("Calibri", round((width / 300) * 2.2)), anchor=NW)

# Place the labels with specific x,y coordinates and width.
lf4a.place(x=50, rely=0.352+0.4, width=32)
lf4b.place(x=50, rely=0.394+0.39, width=55)
lf4c.place(x=50, rely=0.436+0.38, width=55)

# Create a label widget to display the version information of the application.
Label(f4, text="Desktop V1.1", fg="white", bg="#211FA6", font=("Calibri", round((width / 300) * 2)), anchor=NW).place(x=50, rely=0.52+0.42, width=round((width / 300) * 15.8))

# Bind the <Button-1> event to call the SendEmail function with specific message based on the clicked label.
lf4a.bind("<Button-1>", lambda event: SendEmail("Question About the Application"))
lf4b.bind("<Button-1>", lambda event: SendEmail("Donation"))
lf4c.bind("<Button-1>", lambda event: SendEmail("Contacting from Application"))

# Create a label widget with an image and position it within a frame
Label(f4, image=f3_Icons2[1],anchor=NW,fg = "white",bg = "white").place(relx=0.225,rely=0.015,relwidth=0.13)

# Create a label widget with the text "Results" and position it within a frame
Label(f4,text = "Results",fg = "black",bg = "#ffffff", font=("Calibri", round((width / 300) * 4)),anchor=NW).place(relx=0.28,rely=0.03,relwidth=0.13)

# Create a horizontal line to separate the widgets within a frame
Label(f4,anchor=NW,fg = "white",bg = "grey").place(relx=0.22,rely=0.1,relwidth=0.7,relheight=0.002)


# Define a class for creating a table widget
class Table:
    def __init__(self, root,lst,wid):
        # Create a list to store the entry widgets
        self.Entries = []
        # Loop through the rows and columns of the list provided
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                # Create an entry widget and append it to the list of entries
                self.e = Entry(root, width=wid, fg='black',font=("Lato", round((width / 300) * 1.7),"bold"))
                self.Entries.append((self.e))
                # Position the entry widget within the table
                self.e.grid(row=i, column=j)
                # Insert the value from the list into the entry widget
                self.e.insert(END, lst[i][j])

    # Define a method to get the data from the entry widgets
    def getEntries(self):
        data=[]
        for i in self.Entries:
            # Append the value of each entry widget to the data list
            data.append(i.get())
        # Return the data list
        return data

data = {}  # initialize an empty dictionary called data
DataHeader = ['LEAD ACADEMIC', 'COLLABORATING INTERNATIONAL INSTITUTION/S', 'THE COLLABORATION', 'OUTPUTS', 'BUDGET', 'Additional Background Information']  # create a list of column names for the data

# Define a function called setF4
def setF4():
    Keys = list(data.keys())  # Get the keys of the dictionary data

    # Create a tkinter frame widget called F4a and place it on a specific position in another tkinter frame widget called f4
    F4a = Frame(f4,bg = "white")
    F4a.place(relx=0.22,rely=0.16,relwidth=0.7,relheight=0.5)
    # Create a tkinter label widget called Label and place it on F4a at a specific position with a specified font size, color and text
    Label(f4,text = Keys[0],font=("Lato", round((width / 300) * 2.4),"bold"),bg = "white",fg="blue").place(relx=0.22,rely=0.12)
    # create a list called lst
    lst = []
    # iterate over data[Keys[0]] and append the key and value to lst as a list
    for i in data[Keys[0]]:
        lst.append([i,str(data[Keys[0]][i]).replace("\uf0b7","")])
    # create a Table object called Tbl1 with parameters F4a, lst and 40
    Tbl1 = Table(F4a,lst,40)

    # Create a tkinter frame widget called F4b and place it on a specific position in another tkinter frame widget called f4
    F4b = Frame(f4,bg = "white")
    F4b.place(relx=0.22,rely=0.34,relwidth=0.7,relheight=0.5)
    # Create a tkinter label widget called Label and place it on F4b at a specific position with a specified font size, color and text
    Label(f4,text = Keys[1],font=("Lato", round((width / 300) * 2.4),"bold"),bg = "white",fg="blue").place(relx=0.22,rely=0.295)
    # create a list called lst
    lst = []
    # iterate over data[Keys[1]] and append the key and value to lst as a list
    for i in data[Keys[1]]:
        lst.append([i,data[Keys[1]][i].replace("\uf0b7 ","")])
    # create a Table object called Tbl2 with parameters F4b, lst and 40
    Tbl2 = Table(F4b,lst,40)

    # Create a tkinter frame widget called F4c and place it on a specific position in another tkinter frame widget called f4
    F4c = Frame(f4,bg = "white")
    F4c.place(relx=0.22,rely=0.55,relwidth=0.6,relheight=0.5)
    # Create a tkinter label widget called Label and place it on F4c at a specific position with a specified font size, color and text
    Label(f4,text = Keys[2],font=("Lato", round((width / 300) * 2.4),"bold"),bg = "white",fg="blue").place(relx=0.22,rely=0.51)

    lst = []  # create an empty list called "lst"
    TextBoxes1 = []  # create an empty list called "TextBoxes1"
    for i, x in enumerate(data[Keys[2]]):  # loop through the list stored in the "data" dictionary under "Keys[2]"
        Label(F4c,  # create a label within the "F4c" frame
              text=x,  # set the text of the label to "x"
              font=("Lato", round((width / 300) * 2), "bold"),  # set the font of the label
              bg="white",  # set the background color of the label
              fg="black"  # set the foreground color (text color) of the label
              ).place(relx=0, rely=0 + (i * 0.285))  # place the label within the frame at a specified location
        TextBoxes1.append(x)  # append the value of "x" to the "TextBoxes1" list
        F4c1 = Frame(F4c, bg="#ffffff")  # create a new frame within the "F4c" frame
        F4c1.place(relx=0, rely=0.07 + (i * 0.285), relheight=0.18,relwidth=0.6)  # place the new frame within the "F4c" frame at a specified location and size

        F4c1.grid_rowconfigure(0,weight=1)  # configure the first row of the new frame to have a weight of 1 (to allow it to expand)
        F4c1.grid_columnconfigure(0,weight=1)  # configure the first column of the new frame to have a weight of 1 (to allow it to expand)

        # create scrollable textbox
        tk_textbox = Text(F4c1,  # create a text box within the new frame
                          highlightthickness=0, bd=0,  # remove the highlight border and border around the text box
                          font=("Lato", round((width / 300) * 2)))  # set the font of the text box
        tk_textbox.delete("1.0", "end")  # delete any existing content in the text box
        tk_textbox.insert(INSERT, data[Keys[2]][x].replace("\uf0b7 ",""))  # insert the content of the text box from the "data" dictionary, removing any bullets that may be present
        TextBoxes1.append(tk_textbox)  # append the text box to the "TextBoxes1" list
        tk_textbox.grid(row=0, column=0,sticky="nsew")  # place the text box within the new frame at a specified location and size

        # create CTk scrollbar
        ctk_textbox_scrollbar = ctk.CTkScrollbar(F4c1,command=tk_textbox.yview)  # create a new scrollbar within the new frame
        ctk_textbox_scrollbar.grid(row=0, column=1,sticky="ns")  # place the scrollbar within the new frame at a specified location and size

        # connect textbox scroll event to CTk scrollbar
        tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)  # set the scroll command of the text box to the scrollbar

    F4d = Frame(f4, bg="#ffffff")  # create a new frame within the "f4" frame
    F4d.place(relx=0.6, rely=0.7, relwidth=0.38,relheight=0.142)  # place the new frame within the "f4" frame at a specified location and size
    Label(f4,  # create a label within the "f4" frame
          text=Keys[-1],  # set the text of the label to the value stored in "Keys[-1]"
          font=("Lato", round((width / 300) * 2.4), "bold"),  # set the font of the label
          bg="white",  # set the background color of the label
          fg="blue"  # set the foreground color (text color) of the label
          ).place(relx=0.6, rely=0.66, relheight=0.03)  # place the label within the "f4" frame at a specified location

    Tb = []  # create an empty list called "Tb"

    F4d.grid_rowconfigure(0,weight=1)  # configure the first row of the new frame to have a weight of 1 (to allow it to expand)
    F4d.grid_columnconfigure(0,weight=1)  # configure the first column of the new frame to have a weight of 1 (to allow it to expand)

    # create scrollable textbox
    tk_textbox2 = Text(F4d,  # create a text box within the new frame
                       highlightthickness=0, bd=0,  # remove the highlight border and border around the text box
                       font=("Lato", round((width / 300) * 2)))  # set the font of the text box
    tk_textbox2.delete("1.0", "end")  # delete any existing content in the text box
    tk_textbox2.insert(INSERT, data[Keys[-1]].replace("\uf0b7 ",""))  # insert the content of the text box from the "data" dictionary, removing any bullets that may be present
    tk_textbox2.grid(row=0, column=0,sticky="nsew")  # place the text box within the new frame at a specified location and size

    Tb.append(tk_textbox2)  # append the text box to the "Tb" list

    # create CTk scrollbar
    ctk_textbox_scrollbar = ctk.CTkScrollbar(F4d,command=tk_textbox2.yview)  # create a new scrollbar within the new frame
    ctk_textbox_scrollbar.grid(row=0, column=1,sticky="ns")  # place the scrollbar within the new frame at a specified location and size

    # connect textbox scroll event to CTk scrollbar
    tk_textbox2.configure(yscrollcommand=ctk_textbox_scrollbar.set)  # set the scroll command of the text box to the scrollbar

    F4e = Frame(f4, bg="#ffffff")  # create a new frame within the "f4" frame
    F4e.place(relx=0.6, rely=0.16, relwidth=0.38,relheight=0.142)  # place the new frame within the "f4" frame at a specified location and size
    Label(f4,  # create a label within the "f4" frame
          text=Keys[3],  # set the text of the label to the value stored in "Keys[3]"
          font=("Lato", round((width / 300) * 2.4), "bold"),  # set the font of the label
          bg="white",  # set the background color of the label
          fg="blue"  # set the foreground color (text color) of the label
          ).place(relx=0.6, rely=0.12, relheight=0.03)  # place the label within the "f4" frame at a specified location

    lst = [['Date', 'Type', 'Description']]  # create a new list with headers for the table
    for i in data[Keys[3]]['Planned Date 3* / VA /RF / O Description']:  # loop through the table data in "data[Keys[3]]"
        lst.append([i['Date'], i['Type'], i['Description']])  # append each row to the new list with the relevant columns

    class Table2:  # create a new class called "Table2"
        def __init__(self, root, lst, wid):
            self.Entries = []  # create an empty list called "Entries"
            for i in range(len(lst)):
                for j in range(len(lst[0])):
                    if j == 2:  # if it is the "Description" column, make the Entry widget wider
                        self.e = Entry(root, width=wid * 6, fg='black', font=("Lato", round((width / 300) * 1.7),"bold"))  # create a new Entry widget with a specified width and font
                        self.e.grid(row=i, column=j)  # place the Entry widget within the table at a specified location
                        self.e.insert(END,lst[i][j])  # insert the corresponding value from the list into the Entry widget
                    else:
                        self.e = Entry(root, width=wid, fg='black', font=("Lato", round((width / 300) * 1.7),"bold"))  # create a new Entry widget with a specified width and font
                        self.e.grid(row=i, column=j)  # place the Entry widget within the table at a specified location
                        self.e.insert(END,lst[i][j])  # insert the corresponding value from the list into the Entry widget

                    if i == 0:  # if it is the first row (i.e., the header row), make the text red
                        self.e.config(fg="red")
                    else:
                        self.Entries.append(self.e)  # append the Entry widget to the "Entries" list

        def getEntries(self):  # define a method called "getEntries" that returns the data entered into the table
            data = []
            for i in self.Entries:
                data.append(i.get())
            return data  # return the data as a list of strings

    # add the instance and the header to a list
    # Create Tbl3
    Tbl3 = ['Planned Date 3* / VA /RF / O Description']

    # create Table2 instance for Tbl3
    Tbl3_ = Table2(F4e, lst, 15)

    # append Tbl3_ to Tbl3 list
    Tbl3.append(Tbl3_)

    # add labels to f4
    Label(f4, text=list(data[Keys[3]].keys())[1], font=("Lato", round((width / 300) * 2)), bg="white", fg="red").place(relx=0.6, rely=0.3, relheight=0.03)
    Label(f4, text=list(data[Keys[3]].keys())[2], font=("Lato", round((width / 300) * 2)), bg="white", fg="red").place(relx=0.6, rely=0.33, relheight=0.03)
    Label(f4, text=data[Keys[3]][list(data[Keys[3]].keys())[1]], font=("Lato", round((width / 300) * 2), "bold"),bg="white", fg="black").place(relx=0.9, rely=0.3, relheight=0.03)
    Label(f4, text=data[Keys[3]][list(data[Keys[3]].keys())[2]], font=("Lato", round((width / 300) * 2), "bold"),bg="white", fg="black").place(relx=0.9, rely=0.33, relheight=0.03)

    # append values to Tbl3
    Tbl3.append(list(data[Keys[3]].keys())[1])
    Tbl3.append(data[Keys[3]][list(data[Keys[3]].keys())[1]])
    Tbl3.append(list(data[Keys[3]].keys())[2])
    Tbl3.append(data[Keys[3]][list(data[Keys[3]].keys())[2]])

    # Create F4f
    F4f = Frame(f4, bg="#ffffff")
    F4f.place(relx=0.6, rely=0.4, relwidth=0.38, relheight=0.142)

    # Add label to f4
    Label(f4, text=Keys[4], font=("Lato", round((width / 300) * 2.4), "bold"), bg="white", fg="blue").place(relx=0.6,rely=0.36,relheight=0.03)

    # create list for Table2 and populate with data
    lst = [['Date', 'Amount', 'Description']]
    for i in data[Keys[4]]['Funds requested and how to be spent Spending profile']:
        lst.append([i['Date'], i['Amount'], i['Description']])

    # Create Tbl4
    Tbl4 = ['Funds requested and how to be spent Spending profile']

    # create Table2 instance for Tbl4
    Tbl4_ = Table2(F4f, lst, 10)

    # append Tbl4_ to Tbl4 list
    Tbl4.append(Tbl4_)
    # create labels for each field and display them
    Label(f4, text=list(data[Keys[4]].keys())[1], font=("Lato", round((width / 300) * 2)), bg="white", fg="red").place(relx=0.6, rely=0.52, relheight=0.03)
    Label(f4, text=list(data[Keys[4]].keys())[2], font=("Lato", round((width / 300) * 2)), bg="white", fg="red").place(relx=0.6, rely=0.55, relheight=0.03)
    Label(f4, text=list(data[Keys[4]].keys())[3], font=("Lato", round((width / 300) * 2)), bg="white", fg="red").place(relx=0.6, rely=0.58, relheight=0.03)
    Label(f4, text=list(data[Keys[4]].keys())[4], font=("Lato", round((width / 300) * 2)), bg="white", fg="red").place(relx=0.6, rely=0.61, relheight=0.03)

    # display the values for each field
    Label(f4, text=data[Keys[4]][list(data[Keys[4]].keys())[1]], font=("Lato", round((width / 300) * 2), "bold"),bg="white", fg="black", anchor=W).place(relx=0.75, rely=0.52, relheight=0.03, relwidth=0.2)
    Label(f4, text=data[Keys[4]][list(data[Keys[4]].keys())[2]], font=("Lato", round((width / 300) * 2), "bold"),bg="white", fg="black", anchor=W).place(relx=0.75, rely=0.55, relheight=0.03, relwidth=0.2)
    Label(f4, text=data[Keys[4]][list(data[Keys[4]].keys())[3]], font=("Lato", round((width / 300) * 2), "bold"),bg="white", fg="black", anchor=W).place(relx=0.75, rely=0.58, relheight=0.03, relwidth=0.2)
    Label(f4, text=data[Keys[4]][list(data[Keys[4]].keys())[4]], font=("Lato", round((width / 300) * 2), "bold"),bg="white", fg="black", anchor=W).place(relx=0.75, rely=0.61, relheight=0.03, relwidth=0.2)
    # Create a list to store data from table Tbl4
    for i in range(1, 5):
        Tbl4.append(list(data[Keys[4]].keys())[i])
        Tbl4.append(data[Keys[4]][list(data[Keys[4]].keys())[i]])

    # Function to save data entered into the form
    def SaveData():
        dt = []

        # Get data from Tbl1 and Tbl2
        dt.append(Tbl1.getEntries())
        dt.append(Tbl2.getEntries())

        # Get data from TextBoxes1
        for i in range(len(TextBoxes1)):
            if i % 2 == 1:
                TextBoxes1[i] = TextBoxes1[i].get("1.0", "end-1c")
        dt.append(TextBoxes1)

        # Get data from Tbl3 and Tbl4
        Tbl3[1] = Tbl3[1].getEntries()
        Tbl4[1] = Tbl4[1].getEntries()

        # Get data from Tb
        Tb[0] = Tb[0].get("1.0", "end-1c")

        # Append all data into a single list
        dt.append(Tbl3)
        dt.append(Tbl4)
        dt.append(Tb)

        # Create a dictionary to store the entered data
        data_ = {}
        for i, x in enumerate(DataHeader[:-1]):
            temp = {}
            for j, y in enumerate(dt[i]):
                if j % 2 == 0:
                    temp[y] = dt[i][j + 1]
                data_[x] = temp

        # Add the data from the last textbox to the dictionary
        data_[DataHeader[-1]] = Tb[0]

        # Reformat the data for Funds requested table
        tempD = []
        for i, x in enumerate(data_["BUDGET"]['Funds requested and how to be spent Spending profile']):
            temp = {}
            if i % 3 == 0:
                temp["Date"] = data_["BUDGET"]['Funds requested and how to be spent Spending profile'][i]
                temp["Amount"] = data_["BUDGET"]['Funds requested and how to be spent Spending profile'][i + 1]
                temp["Description"] = data_["BUDGET"]['Funds requested and how to be spent Spending profile'][i + 2]
                tempD.append(temp)

        data_["BUDGET"]['Funds requested and how to be spent Spending profile'] = tempD

        # Reformat the data for Planned Date table
        tempD = []
        for i, x in enumerate(data_["OUTPUTS"]['Planned Date 3* / VA /RF / O Description']):
            temp = {}
            if i % 3 == 0:
                temp["Date"] = data_["OUTPUTS"]['Planned Date 3* / VA /RF / O Description'][i]
                temp["Type"] = data_["OUTPUTS"]['Planned Date 3* / VA /RF / O Description'][i + 1]
                temp["Description"] = data_["OUTPUTS"]['Planned Date 3* / VA /RF / O Description'][i + 2]
                tempD.append(temp)

        data_["OUTPUTS"]['Planned Date 3* / VA /RF / O Description'] = tempD

        try:
            GetData(data_)
            showinfo("Data Added","Database successfully updated.")
            f4.place_forget()
            ImagePath.delete(0, END)
            f3.place(relx=0, rely=0, relheight=1, relwidth=1)
            SCROLL1.update_()
        except:
            showerror("Data Failed","Might Already Exists!")

    ctk.CTkButton(master=f4, border_color="#3160DA", fg_color="#001B62", text="Back", border_width=1, font=("Calibri", round((width / 300) * 3.3)), corner_radius=12,command=lambda: [f4.place_forget(), ImagePath.delete(0,END) , f3.place(relx=0, rely=0, relheight=1, relwidth=1)]).place(relx=0.8, rely=0.93, relwidth=0.095, relheight=0.045)
    ctk.CTkButton(master=f4, border_color="#3160DA", fg_color="#001B62", text="Save", border_width=1, font=("Calibri", round((width / 300) * 3.3)), corner_radius=12,command=SaveData).place(relx=0.9, rely=0.93,relwidth=0.095, relheight=0.045)


# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________

def Extract():
    # This function extracts data from a file and displays it in f4
    global data
    # Hide f2 and display f4
    f2.place_forget()
    f4.place(relx=0, rely=0, relwidth=1, relheight=1)
    # Check if file is a PDF or document and extract data accordingly
    if "pdf" in filePath.get().split("/")[-1].lower():
        data = ExtractPDFData(filePath.get())
    else:
        data = ExtractData(filePath.get(),"doc")
    # Display the extracted data in f4 and update count and count2
    setF4()
    count.set(count.get()+1)
    count2.set(count2.get() + 0.01)

# Create label widget to display an image in f2
img_f2 = Label(f2, bg="white", anchor=NW)
img_f2.place(relx=-0.01, rely=0, relwidth=0.2, relheight=1)
# Display logo image in f2
Label(f2, image=logoNxn2, bg="#ffffff", anchor=NW).place(relx=0, rely=0.15, relwidth=0.18)

# This function configures the image displayed in img_f2
def testf2(event=None):
    # Resize and update image displayed in img_f2
    leftGra = ImageTk.PhotoImage(IMG.open('assets/left.png').resize((round(round(master.winfo_screenwidth()/1.4) / 5.7), f2.winfo_height()), IMG.ANTIALIAS))
    img_f2.config(image=leftGra)
    img_f2.image = leftGra

# Bind testf2() function to configure event for f2
f2.bind("<Configure>",testf2)

# Create labels for FAQ, Donate, and Contact options in f2
lf2a = Label(f2, text="FAQ", fg="white", bg="#1D1C9B", font=("Calibri", round((width / 300) * 2.2)), anchor=NW)
lf2b = Label(f2, text="Donate", fg="white", bg="#1F1CA3", font=("Calibri", round((width / 300) * 2.2)), anchor=NW)
lf2c = Label(f2, text="Contact", fg="white", bg="#1F1D9E", font=("Calibri", round((width / 300) * 2.2)), anchor=NW)

# Place labels for FAQ, Donate, and Contact options in f2
lf2a.place(x=50, rely=0.352+0.4, width=32)
lf2b.place(x=50, rely=0.394+0.39, width=55)
lf2c.place(x=50, rely=0.436+0.38, width=55)

# Add label for application version in f2
Label(f2, text="Desktop V1.1", fg="white", bg="#211FA6", font=("Calibri", round((width / 300) * 2)), anchor=NW).place(x=50, rely=0.52+0.42, width=round((width / 300) * 15.8))

# Bind FAQ, Donate, and Contact labels to email functions
lf2a.bind("<Button-1>", lambda event: SendEmail("Question About the Application"))
lf2b.bind("<Button-1>", lambda event: SendEmail("Donation"))
lf2c.bind("<Button-1>", lambda event: SendEmail("Contacting from Application"))

# Display image and text for "Extraction" in f2
Label(f2, image=f3_Icons2[1], anchor=NW, fg="white", bg="white").place(relx=0.225, rely=0.015, relwidth=0.13)
Label(f2, text="Extraction", fg="black", bg="#ffffff", font=("Calibri", round((width / 300) * 4)), anchor=NW).place(relx=0.28, rely=0.03, relwidth=0.13)
# Display grey line in f2
Label(f2, anchor=NW, fg="white", bg="grey").place(relx=0.22, rely=0.1, relwidth=0.7, relheight=0.002)

# This function opens a file dialog box to select a file path
def select():
    global XrayL
    # Open file dialog box and set filePath variable to selected file path
    file = askopenfile(mode='r', filetypes=[('Documents', '*.pdf'),('Documents', '*.docx')])
    if file is not None:
        # Enable ImagePath entry widget and display selected file path
        ImagePath.configure(state="normal")
        ImagePath.delete(0, END)
        ImagePath.insert(0, file.name)
        ImagePath.configure(state="disabled")
        # Create "Extract" button and set its command to the Extract() function
        ctk.CTkButton(master=f2, border_color="#3160DA", fg_color="#001B62", text="Extract", border_width=1, font=("Calibri", round((width / 300) * 3.3)), corner_radius=12, command=Extract).place(relx=0.32, rely=0.31, relwidth=0.095, relheight=0.045)
        filePath.set(str(file.name))

# Display "Select Path" text in f2
Label(f2,text = "Select Path",fg = "black",bg = "#ffffff", font=("Lato", round((width / 300) * 3.5)),anchor=NW).place(relx=0.22,rely=0.17,relwidth=0.13)
ctk.CTkButton(master=f2,border_color="#3160DA",fg_color="#001B62",text="Select", border_width=1, font=("Calibri", round((width / 300) * 3.3)), corner_radius=12, command=select).place(relx=0.22, rely=0.31,relwidth=0.095,relheight=0.045)
ImagePath = ctk.CTkEntry(master=f2, state = "disabled",placeholder_text="Path Here .. ",border_width=2,corner_radius=10)
ImagePath.place(relx=0.22, rely=0.24,relwidth=0.4,relheight=0.045)


# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________

img_f3 = Label(f3,bg = "white",anchor=NW)
img_f3.place(relx=-0.01,rely=0,relwidth=0.2,relheight=1)
Label(f3, image=logoNxn2, bg="#ffffff",anchor = NW).place(relx=0, rely=0.15, relwidth=0.18)

def testf3(event=None):
    leftGra = ImageTk.PhotoImage(IMG.open('assets/left.png').resize((round(width / 5.7), f3.winfo_height()), IMG.ANTIALIAS))
    img_f3.config(image=leftGra)
    img_f3.image = leftGra
    dashboardImg = IMG.open('assets/dashboard.PNG')
    w, h = dashboardImg.size
    dashboardImg = ImageTk.PhotoImage(dashboardImg.resize((round(f3.winfo_width() / 3.5), round((h / w) * (f3.winfo_width() / 3.5))), IMG.ANTIALIAS))
    img2_f3.config(image=dashboardImg)
    img2_f3.image = dashboardImg
    f3L1.config(wraplength=f3.winfo_width()/3, font=("Lato", round((f3.winfo_width() / 300) * 2)))

f3.bind("<Configure>",testf3)
lf3a = Label(f3,text = "FAQ",fg = "white",bg = "#1D1C9B", font=("Calibri", round((width / 300) * 2.2)),anchor=NW)
lf3b = Label(f3,text = "Donate",fg = "white",bg = "#1F1CA3", font=("Calibri", round((width / 300) * 2.2)),anchor=NW)
lf3c = Label(f3,text = "Contact",fg = "white",bg = "#1F1D9E", font=("Calibri", round((width / 300) * 2.2)),anchor=NW)

lf3a.place(x=50,rely=0.352+0.4,width=32)
lf3b.place(x=50,rely=0.394+0.39,width=55)
lf3c.place(x=50,rely=0.436+0.38,width=55)

Label(f3,text = "Desktop V1.1",fg = "white",bg = "#211FA6", font=("Calibri", round((width / 300) * 2)),anchor=NW).place(x=50,rely=0.52+0.42,width=round((width / 300) * 15.8))

lf3a.bind("<Button-1>", lambda event: SendEmail("Question About the Application"))
lf3b.bind("<Button-1>", lambda event: SendEmail("Donation"))
lf3c.bind("<Button-1>", lambda event: SendEmail("Contacting from Application"))

f3a = ctk.CTkFrame(master=f3, width=200, height=200, border_width=2,border_color="grey", corner_radius=40, fg_color="#ffffff")
f3a.place(relx=0.22, rely=0.7,relwidth=0.7,relheight=0.2)
Label(f3a,text = "Documents Converted",fg = "black",bg = "#ffffff", font=("Calibri", round((width / 300) * 3.5)),anchor=NW).place(relx=0.05,rely=0.4,relwidth=0.2)
Label(f3a,text = "Usage",fg = "black",bg = "#ffffff", font=("Calibri", round((width / 300) * 4),"bold"),anchor=NW).place(relx=0.05,rely=0.1,relwidth=0.2)
Label(f3a,textvariable = count,fg = "black",bg = "#ffffff", font=("Calibri", round((width / 300) * 3.8)),anchor=NW).place(relx=0.9,rely=0.4,relwidth=0.07)
cpb = ctk.CTkProgressBar(master=f3a,progress_color="#201EAA",variable=count2)
cpb.place(relx=0.05, rely=0.7,relwidth=1-0.1,relheight = 0.09)

# ////////////
# Display title and icon for f3
Label(f3, image=f3_Icons2[0], anchor=NW, fg="white", bg="white").place(relx=0.225, rely=0.025, relwidth=0.13)
Label(f3, text="Dashboard", fg="black", bg="#ffffff", font=("Calibri", round((width / 300) * 4)), anchor=NW).place(relx=0.26, rely=0.03, relwidth=0.13)

# Display separator line in f3
Label(f3, anchor=NW, fg="white", bg="grey").place(relx=0.22, rely=0.1, relwidth=0.7, relheight=0.002)

# Display welcome message in f3
Label(f3, text="Lets's get started", fg="black", bg="#ffffff", font=("Lato", round((width / 300) * 3)), anchor=NW).place(relx=0.55, rely=0.18, relwidth=0.15)
f3L1 = Label(f3, text="Effortlessly extract text from PDFs and Word documents with our powerful desktop application. Our PDF and DOC text extraction desktop application is designed to simplify document processing and save you valuable time. With our powerful tool, you can easily extract text from any PDF or Word document, regardless of its complexity.", wraplength=width / 3, justify=LEFT, fg="black", bg="#ffffff", font=("Lato", round((width / 300) * 2)), anchor=NW)
f3L1.place(relx=0.55, rely=0.23, relwidth=0.35, relheight=0.3)

# Display button options in f3
Label(f3,text = "Start Extraction",fg = "black",bg = "#ffffff", font=("Lato", round((width / 300) * 3)),anchor=NW).place(relx=0.55,rely=0.35,relwidth=0.2)
Label(f3, image=f3_Icons2[2],anchor=NW,fg = "white",bg = "white").place(relx=0.58,rely=0.425,relwidth=0.13)
Label(f3, image=f3_Icons2[1],anchor=NW,fg = "white",bg = "white").place(relx=0.695,rely=0.425,relwidth=0.13)

# Create two CTkButtons with text "DataBase" and "Extract" on f3 screen
# When clicked, these buttons will hide f3, delete the text in ImagePath entry widget, and show f5 or f2 screen respectively
ctk.CTkButton(master=f3,border_color="#3160DA",fg_color="#001B62",text="DataBase", border_width=1, font=("Calibri", round((width / 300) * 3.3)), corner_radius=12,command=lambda:[f3.place_forget(),ImagePath.delete(0,END),f5.place(relx=0,rely=0,relheight=1,relwidth=1)]).place(relx=0.56, rely=0.54,relwidth=0.095,relheight=0.045)
ctk.CTkButton(master=f3,border_color="#3160DA",fg_color="#001B62",text="Extract", border_width=1, font=("Calibri", round((width / 300) * 3.3)), corner_radius=12,command=lambda:[f3.place_forget(),ImagePath.delete(0,END),f2.place(relx=0,rely=0,relheight=1,relwidth=1)]).place(relx=0.67, rely=0.54,relwidth=0.095,relheight=0.045)

# Create a Label widget with a white background, and place it on f3 screen
# This Label widget will be used to display an image later
img2_f3 = Label(f3, anchor=NW,fg = "white",bg = "white")
img2_f3.place(relx=0.225,rely=0.14,relwidth=0.3)


# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________

# Create the loading screen window and place the image and text labels
f1.place(relx=0, rely=0, relwidth=1, relheight=1)
Label(f1, image=logoNxn1, bg="#ffffff").place(relx=0, rely=0.1, relwidth=1)
Label(f1, text="International Collaboration Fund PLUS (ICF PLUS)\nApplication Form Extractor", fg="#003271", font=("Calibri", round((height / 250) * 5), 'italic'), bg="#ffffff").place(relx=0, rely=0.8, relwidth=1, relheight=0.1)
Label(f1, text="LOADING...", fg="#003271", font=("Calibri", round((height / 250) * 6), 'italic'), bg="#ffffff").place(relx=0, rely=0.7, relwidth=1, relheight=0.1)

# Define the pb function that will be called after one second
def pb():
    # Hide the loading screen and display the next screen
    f1.place_forget()
    f3.place(relx=0, rely=0, relwidth=1, relheight=1)
    return

# Schedule the pb function to run after one second using the after method of the main window
master.after(3000, pb)

# Start the main loop of the application
master.mainloop()
