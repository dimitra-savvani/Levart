import tkinter
from PIL import ImageTk, Image



window = tkinter.Tk()
# to rename the title of the window
window.title("Φόρμα Δημιουργίας Ταξιδιού")
window.geometry("1500x1500")
window.configure(background='blanched almond')
# pack is used to show the object in the window
path1 = "logo.png"
path2 = "footer.png"
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path1))
img2 = ImageTk.PhotoImage(Image.open(path2))
# You will first create a division with the help of Frame class and align them on TOP and BOTTOM with pack() method.
top_frame = tkinter.Frame(window).pack()

label = tkinter.Label(window, image = img1)
label.pack()

def toggle():

    if toggle_btn.config('relief')[-1] == 'sunken':
        toggle_btn.config(relief="raised")
        
    else:
        toggle_btn.config(relief="sunken")
        label1.visible = not label1.visible
        label2.visible = not label2.visible
        label3.visible = not label3.visible
        label4.visible = not label4.visible
        label5.visible = not label5.visible

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


variable = tkinter.StringVar(window)
variable.set(OptionList[0])

opt = tkinter.OptionMenu(window, variable, *OptionList)
opt.config(width=11, font=('Helvetica', 9))
opt.pack()

tkinter.Checkbutton(window, text = "Κατοικίδια").pack()
toggle_btn = tkinter.Button(text="Επιπλέον Επιλογές", width=12, relief="raised", command=toggle)
toggle_btn.pack(pady=5)


label1 = tkinter.Label(window, text='Τύπος αυτοκινήτου')
label1.visible = True
label1.pack()
OptionList = ['Sedan', 'SUV', 'VAN', 'Pickup', 'HatchBack', 'Coupe', 'Cabriolet']
variable = tkinter.StringVar(window)
variable.set(OptionList[0])

opt = tkinter.OptionMenu(window, variable, *OptionList)
opt.config(width=10, font=('Helvetica', 10))
opt.pack()

label2 = tkinter.Label(window, text='Μάρκα αυτοκινήτου')
label2.visible = True
label2.pack()
OptionList = ['Mercedes', 'BMW', 'Audi', 'Subaru', 'Suzuki', 'Toyota', 'Opel']
variable = tkinter.StringVar(window)
variable.set(OptionList[0])

opt = tkinter.OptionMenu(window, variable, *OptionList)
opt.config(width=10, font=('Helvetica', 10))
opt.pack()

label3 = tkinter.Label(window, text='Σασμάν')
label3.visible = True
label3.pack()
OptionList = ['Manual', 'Automatic']
variable = tkinter.StringVar(window)
variable.set(OptionList[0])

opt = tkinter.OptionMenu(window, variable, *OptionList)
opt.config(width=10, font=('Helvetica', 10))
opt.pack()

label4 = tkinter.Label(window, text='Καύσιμο')
label4.visible = True
label4.pack()
OptionList = ['Gas', 'Petroleum', 'Diesel', 'Electric']
variable = tkinter.StringVar(window)
variable.set(OptionList[0])

opt = tkinter.OptionMenu(window, variable, *OptionList)
opt.config(width=10, font=('Helvetica', 10))
opt.pack()

label5 = tkinter.Label(window, text='Κίνηση')
label5.visible = True
label5.pack()
OptionList = ['FWD', 'RWD', '4WD']
variable = tkinter.StringVar(window)
variable.set(OptionList[0])

opt = tkinter.OptionMenu(window, variable, *OptionList)
opt.config(width=10, font=('Helvetica', 10))
opt.pack()


button_widget = tkinter.Button(window,text="Αναζήτηση")
button_widget.pack()

label = tkinter.Label(window, image = img2)
label.pack(side='bottom')

window.mainloop()
