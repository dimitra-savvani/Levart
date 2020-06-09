import tkinter
from PIL import ImageTk, Image

window = tkinter.Tk()
# to rename the title of the window
window.title("Ρυθμίσεις")
window.geometry("1500x1500")
window.configure(background='blanched almond')
# pack is used to show the object in the window
path1 = "logo.png"
path2 = ("footer.png")
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path1))
img2 = ImageTk.PhotoImage(Image.open(path2))
# You will first create a division with the help of Frame class and align them on TOP and BOTTOM with pack() method.
top_frame = tkinter.Frame(window).pack()

label = tkinter.Label(window, image = img1)
label.pack()


button_widget = tkinter.Button(window,text="Προσωπικά στοιχεία \nΕπεξεργαστείτε τα προσωπικά σας στοιχεία").pack()


button_widget = tkinter.Button(window, text = "Είσοδος και Προστασία \nΕπεξεργαστείτε τον κωδικό προσβασης σας").pack()


button_widget = tkinter.Button(window, text = "Ειδοποιήσεις\n Επεξεργαστείτε τον κωδικό προσβασης σας").pack()


button_widget = tkinter.Button(window, text = "Ιδιωτικότητα\n Επεξεργαστείτε τον κωδικό προσβασης σας").pack()



button_widget = tkinter.Button(window, text = "Γλώσσα \nΕπεξεργαστείτε τον κωδικό προσβασης σας").pack()


button_widget = tkinter.Button(window, text = "Panic Button \nΕπεξεργαστείτε τον κωδικό προσβασης σας").pack()

label = tkinter.Label(window, image = img2)
label.place(x=500 , y=700)




window.mainloop()