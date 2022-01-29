from tkinter import *
from tkinter import messagebox
from OOP import PDF_Merger

def onclick():
    function_call = PDF_Merger.PDFmerger()
    messagebox.showinfo("", "PDF Merged")

main_window = Tk()
#Title
main_window.title("Merger more than one PDF in one PDF")
#labels
Label(main_window, text = "Enter the directory path :").grid(row = 0 , column = 0)
#Textbox = Entry
Entry(main_window, width= 50 ,borderwidth = 5).grid(row = 0, column = 1)
#button
Button(main_window, text = "OK", command= onclick).grid(row = 1, column = 1)
main_window.mainloop()



