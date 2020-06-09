import tkinter
from PIL import ImageTk, Image

window = tkinter.Tk()
# to rename the title of the window
window.title("Φόρμα αναζήτησης ταξιδιού")
window.geometry("1500x1500")
window.configure(background='blanched almond')
# pack is used to show the object in the window
path1 = ("logo.png")
path2 = ("footer.png")
path3 = ("person.png")
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path1))
img2 = ImageTk.PhotoImage(Image.open(path2))
img3 = ImageTk.PhotoImage(Image.open(path3))
# You will first create a division with the help of Frame class and align them on TOP and BOTTOM with pack() method.
top_frame = tkinter.Frame(window).pack()

label = tkinter.Label(window, image = img1)
label.pack()



tkinter.Label(window, text = "Αφετηρία").pack()
tkinter.Entry(window).pack()
tkinter.Label(window, text = "Προορισμός").pack()
tkinter.Entry(window).pack()
tkinter.Label(window, text = "Ημερομηνία").pack()
tkinter.Entry(window).pack()

label = tkinter.Label(window, text="Άτομα")
label.pack()
OptionList = [
"1",
"2",
"3",
"4"
] 





variable = tkinter.StringVar(window)
variable.set(OptionList[0])

opt = tkinter.OptionMenu(window, variable, *OptionList)
opt.config(width=10, font=('Helvetica', 10))
opt.pack()

label = tkinter.Label(window, text="Αποσκευές")
label.pack()
OptionList = [
"Σακίδιο πλάτης",
"Μικρή βαλίτσα",
"Μεσαία βαλίτσα",
"Μεγάλη βαλίτσα"
] 


label = tkinter.Label(window, image = img3)
label.place(x=940 , y=400)

variable = tkinter.StringVar(window)
variable.set(OptionList[0])

opt = tkinter.OptionMenu(window, variable, *OptionList)
opt.config(width=11, font=('Helvetica', 9))
opt.pack()

tkinter.Checkbutton(window, text = "Κατοικίδια").pack()



button_widget = tkinter.Button(window,text="Αναζήτηση")
button_widget.place(relx=0.5, rely=0.5, anchor= "center")

label = tkinter.Label(window, image = img2)
label.place(x=500 , y=700)

window.mainloop()