class LevartSettings:
    ''' Needed procedure to verify user'''
    def Identification():# with T being an object of class Traveler      
        while True:
            try:
                changePic = int(input ('Πρόσθεσε νέα φωτογραφία προφίλ \n 1-->ΝΑΙ \n 0-->ΟΧΙ \n Επίλεξε:')) 
                if changePic==1:
                    print('Επιτυχής ταυτοποίηση στοιχείων, μπορείτε πλέον να Ταξιδέψετε μέσω της Levart\n')
                    False
                    break
                elif changePic==0:
                    print('Επιτυχής ταυτοποίηση στοιχείων, μπορείτε πλέον να Ταξιδέψετε μέσω της Levart\n')
                    False
                    break
                else:
                    print("Παρακαλώ επιλέξτε σύμφωνα με τις οδηγίες")
            except ValueError:
                 print("Παρακαλώ επιλέξτε σύμφωνα με τις οδηγίες")        
        #upload eggrafo
        #elegxos
        #upload fwtografia
        #elgxos
        #sugrisi
        #T.enableTraveling = True #if true, users are allowed to arrange travels through Levart
    def PanicButtonSettings(P):# with P being an object of class PanicButton
         typedEmergencyContacts = [6983775649, 6947789379]
         typedEnablePanicButton = True
         TypedAllowePictureCapture = True
         TypedAllowLocationCapture = True
         TypedAllowSendingMessage = True
         P.emergencyContacts = typedEmergencyContacts
         P.enablePanicButton = typedEnablePanicButton
         P.allowePictureCapture = TypedAllowePictureCapture
         P.allowLocationCapture = TypedAllowLocationCapture
         P.allowSendingMessage = TypedAllowSendingMessage
         
    def LanguageSettings():
        print('Διαλέξτε τη γλώσσα της επιλογής σας:')
        Languages = ['Greek', 'English', 'German', 'French', 'Russian','Έξοδος απο ρυθμίσεις γλώσσας']
        for i, j in enumerate(Languages):
            print(i, j)
        while True:
            try:
                langIndex = int(input ("Διάλεξε Γλώσσα: "))
                while langIndex > i :
                    langIndex = int(input ("Το νούμερο που διάλεξες δεν αντιστοιχεί σε διαθέσιμη γλώσσα, διάλεξε ξανά: "))
                if langIndex == i:
                    print('Έπιλέξατε έξοδο απο τις ρυθμίσεις γλώσσας')
                else:
                    print('Η γλώσσα τέθηκε σε',Languages[langIndex])
                break
            except ValueError:
                print("Αυτό το πεδίο δέχετε μόνο αριθμούς.")
        language = Languages[langIndex]
        return language
    

