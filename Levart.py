from LevartSettings import LevartSettings



class Levart:
    L = LevartSettings()
    language = L.LanguageSettings()
    
    companyInfo = ['261094735', '261094756', 'levart@info.gr']
    
    def __init__(self, language): 
        self.language = language
        self.travelCount = 0 #plithos taksidiwn pou exei pragmatatopoiisei o xristis

    
    
    def ComposeSMS(i):
        
        if i == 0:
            text = '\n Το όνομα μου είναι ΤΑΔΕ και δέχομαι σεξουαλική παρενόχληση στο ταξίδι που εκτελώ! Παρακάτω παραθέτονται πληροφορίες οι οποίες θα είναι χρήσιμες για την βοήθεια μου !'
            print(text)
        elif i == 1:   
            text = '\n Το όνομα μου είναι ΤΑΔΕ και έπεσα θύμα κλοπ΄΄ής στο ταξίδι που εκτελώ! Παρακάτω παρατίθενται πληροφορίες οι οποίες θα είναι χρήσιμες για την βοήθεια μου !'
            print(text)
        elif i == 2:   
            text = '\n Το όνομα μου είναι ΤΑΔΕ και ο συνταξηδιώτης μου με εγκατέληψε στο ταξίδι που εκτελώ! Παρακάτω παραθέτονται πληροφορίες οι οποίες θα είναι χρήσιμες για την βοήθεια μου !'
            print(text)
            
        elif i == 3: 
            text = '\n Το όνομα μου είναι ΤΑΔΕ και ο συνταξηδιώτης μου με παραπλάνησε και πάει σε διαφορετικό προορισμό απο τον προσκαθορισμένο στο ταξίδι που εκτελώ! Παρακάτω παραθέτονται πληροφορίες οι οποίες θα είναι χρήσιμες για την βοήθεια μου !'
            print(text)
        
    
    #def SendMessage():
