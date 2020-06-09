import tkinter
from PIL import ImageTk, Image




window = tkinter.Tk()
# to rename the title of the window
window.title("Διαλέξτε Ταξίδι")
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

tkinter.Label(window, text = "Επιλογή Ταξιδιού").pack()

button_widget = tkinter.Button(window,text="Donald Duck\t\t\t\t\t\t\t\t\t\n26/03/2021\t\t\t\t\t\tΧωρητικότητα αποσκευών: 2\nΑπό Αθήνα προς Πάτρα\t\t\t\t\t\tΚατοικίδια: ΝΑΙ\n12:00 μ.μ\t\t\t\t\t\t Mazda, Αυτόματο, Πετρελαιοκίνητο.\nΧωρητικότητα ατόμων: 3\t\t\t\tΠροκαθορισμένη στάση στο Αίγιο").pack()


button_widget = tkinter.Button(window,text="Goofy\t\t\t\t\t\t\t\t\t\n27/03/2021\t\t\t\t\tΧωρητικότητα αποσκευών: 1\nΑπό Αθήνα προς Πάτρα\t\t\t\t\t\tΚατοικίδια: ΟΧΙ\n17:00 μ.μ\t\t\t\t\t Hyundai, Χειροκίνητο , Βενζινοκίνητο.\nΧωρητικότητα ατόμων: 1\t\t\tΔεν θα υπάρξουν στάσεις καθώς πρέπει\n\t\t\t\t\t να φτάσω Πάτρα το συντομότερο").pack()


button_widget = tkinter.Button(window,text="Mini Mouse\t\t\t\t\t\t\t\t\t\n26/03/2021\t\t\t\t\tΧωρητικότητα αποσκευών: 0\nΑπό Αθήνα προς Πάτρα\t\t\t\t\t\tΚατοικίδια: ΝΑΙ\n9:00 π.μ\t\t\t\t\t Mini Cooper, Αυτόματο, Βενζινοκίνητο.\nΧωρητικότητα ατόμων: 4\t\t\t\t\t\t\t\t").pack()



label = tkinter.Label(window, image = img2)
label.place(x=500 , y=700)




window.mainloop()