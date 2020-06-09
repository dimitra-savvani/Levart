import tkinter
from PIL import ImageTk, Image

window = tkinter.Tk()
# to rename the title of the window
window.title("Προφίλ χρήστη")
window.geometry("1500x1500")
window.configure(background='blanched almond')
# pack is used to show the object in the window
path1 = "logo.png"
path2 = ("footer.png")
path3 = ("foto.png")
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path1))
img2 = ImageTk.PhotoImage(Image.open(path2))
img3 = ImageTk.PhotoImage(Image.open(path3))
    
# You will first create a division with the help of Frame class and align them on TOP and BOTTOM with pack() method.
top_frame = tkinter.Frame(window).pack()

label = tkinter.Label(window, image = img1)
label.pack()

tkinter.Label(window, text = "Όνομα χρήστη: Mickey Mouse").pack()
tkinter.Label(window, text = "Nickname: Mickey the destroyer of worlds").pack()
tkinter.Label(window, text = "Περιγραφή \n Είμαι ο Mickey και μου αρέσει να ταξιδεύεω και να γνωρίζω τον κόσμο. Μαζί με τον καλύτερο μου φίλο τον Pluto και το Seat μου ταξιδεύουμε συχνά σε όλη την Ελλάδα στην αναζήτηση νέων εμπειριών και αναμνήσεων.").pack()




label = tkinter.Label(window, text="Ταξίδια που εκκρεμούν")
label.pack()
OptionList = [
"Ταξίδι 1",
"Ταξίδι 2",
"Ταξίδι 3",
"Ταξίδι 4",
"..."
] 





variable = tkinter.StringVar(window)
variable.set(OptionList[0])

opt = tkinter.OptionMenu(window, variable, *OptionList)
opt.config(width=10, font=('Helvetica', 10))
opt.pack()

label = tkinter.Label(window, text="Travel Buddies")
label.pack()
OptionList = [
"Άρης Ντούμι",
"Δήμητρά Σαββανή",
"Γιάννης Μπανιάς" ,
"Άγγελος Ντούμι"
] 

button_widget = tkinter.Button(window,text="Ανέβασμα φωτογραφίας")
button_widget.place(relx=0.5, rely=0.5, anchor= "center")

label = tkinter.Label(window, image = img3)
label.place(x=600 , y=400)

variable = tkinter.StringVar(window)
variable.set(OptionList[0])

opt = tkinter.OptionMenu(window, variable, *OptionList)
opt.config(width=13, font=('Helvetica', 9))
opt.pack()

label = tkinter.Label(window, image = img2)
label.place(x=500 , y=700)

label = tkinter.Label(window, text="Ιστορικό ταξιδιών")
label.pack()
OptionList = [
"Ο χρήστης ταξίδεψε απο Αθήνα προς Θεσσαλονίκη στις 19/02/2021",
"Ο χρήστης ταξίδεψε απο Θεσσαλονίκη προς Αθήνα στις 22/02/2021",
"Ο χρήστης ταξίδεψε απο Θεσσαλονίκη προς Πάτρα στις 25/02/2021",
"Ο χρήστης ταξίδεψε απο Πάτρα προς Θεσσαλονίκη στις 30/02/2021",
] 





variable = tkinter.StringVar(window)
variable.set(OptionList[0])

opt = tkinter.OptionMenu(window, variable, *OptionList)
opt.config(width=55, font=('Helvetica', 10))
opt.pack()

window.mainloop()