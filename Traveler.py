class Traveler:
    # import cv2
    from getpass import getpass

    name = "Mickey"
    surname = "Mouse"
    username = "mickeymouse"
    
    birthdate = "03/04/1998"
    telephone = "6969696969"
    email = "mickeymouse@upatras.com"
    # profilePicture = cv2.imread('mickeyspicture.png')
    enableTraveling = False
    travelBuddies = ['Donald Duck', 'Goofy']

    def EnterPassword():
        password = "123456789"

        i = 1
        while i <= 3:
            enteredPassword = input("Παρακαλώ πληκτρολογήστε τον κωδικό χρήστη σας:")
            if (enteredPassword == password):
                print("Καλωσήλθατε")
                break
            else:
                print("Λάθος κωδικός πρόσβασης. Έχεις", 3 - i, "προσπάθειες ακόμα")
            i += 1
            # print ("Πληκτρολόγησες λάθος κωδικό 3 φορές. Έαν έχετε ξεχάσει τον κωδικό σας κάντε ανάκτηση εδώ.")

    EnterPassword()

    # def SelectPendingTravels():
    # def PasswordVerification():

    # def EditInfo():

    # def DisplayInfo():

    # def Delete Account():

    # def DeactivateAccount():

    # def ReasonSelection():

    # def PostReview():
