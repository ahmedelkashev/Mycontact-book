# MyContactBook

'''
The program is for managing contacts from vcf files. On first launch it asks to open a vcf file, then parses it and displays
list of contacts with details.
For release version it is planned to make changes on the file and export of the data. 
'''

from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import ast # convert str to dic
 
# Create window, define the size and the title.
window = Tk()
window.title("Open")
window.geometry("200x150")

def open_file():
    # Open file, create new window and close initial window
    
    file = filedialog.askopenfile(mode='r', filetypes=[('vCard Files', '*.vcf')])
    if file:
        content = file.readlines()
        file.close()
        window_data = Tk()
        window_data.geometry('600x400')
        window_data.title("Contacts")
        window.destroy()
        list_contacts(content, window_data)
    else:
        messagebox.showwarning(message="Please select a file.")


def export_data():
   # exports the data into a VCF format
   return 0
    

def listingTodata():
    # converts the listing data into it's original csv format
    return 0

def list_contacts(content, window_data):
#shows the listing of the content
    
    lst = build_list(content)
   
    def showSelected(e):
        line = lb.get(ANCHOR)[0]
        line  = ast.literal_eval(line)
        contact_detail = ""
        for key, value in line.items():
            value = value.replace("type=", "").replace("type=", "").replace("CELL:", "").replace("HOME:", "")
            contact_detail += f"{key}: {value}\n"
        show.config(text=contact_detail)

    lb = Listbox(window_data, font=("Helvetica", 12), width='25')
    lb.index(0)
    lb.grid(column=0, row=0, sticky=N, padx=20, pady=20, ipadx=10, ipady=50)
    
    for i in range(len(lst)): # creates a list of tuples from list object
        lb.insert(i, [lst[i]])
       
    lb.bind('<<ListboxSelect>>', showSelected)

    show = Label(window_data, font=("Helvetica", 14), width='25', anchor='w')
    show.grid(column=1, row=0, sticky=N, padx=20, pady=20, ipadx=10, ipady=0)
    ttk.Button(window_data, text="Export", command=export_data).pack(pady=20)

def build_list(content):
    # parsesing the contant of the file, returns list object of contacts with dictionary - [{'Name': 'John Doe', 'Phone': '+1 202 555 1212'}, {'Name': 'Johnny Depp', 'Phone': '+1 202233 1212'}]
    lst = []
    print ("content", content)
    for line in content:
        line = line.strip()
        if line[0:2] == "N:":
            name_line = line.split(";")
            d = {}
            d["Name"] = f"{name_line[0][2:]} {name_line[1]}"
        if line[0:3] == "TEL":
            tel_line = line.split(";")
            d["TEL"] = tel_line[1]
        if line[0:5] == "EMAIL":
            tel_line = line.split(";")
            d["EMAIL"] = tel_line[1]
        if line == "END:VCARD":
            lst.append(d)
            d.clear
    return lst    

label_file = Label(window, text="Open vcf file:", font=("Arial", 12))
label_file.place(x=20, y=20)
label_file.pack(pady=20)
ttk.Button(window, text="Browse", command=open_file).pack(pady=20)

 
# Enter the main event loop
window.mainloop()
