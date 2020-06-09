class Vehicle:
    def __init__(self,tupos,marka,sasman,kausimo,kinisi):
        self.tupos=tupos
        self.marka=marka
        self.sasman=sasman
        self.kausimo=kausimo
        self.kinisi=kinisi
    
    def VehicleForm(self):
        optionFill= ['Τύπος αυτοκινήτου', 'Μάρκα αυτοκινήτου', 'Σασμάν', 'Καύσιμο', 'Κίνηση']
        vehicleType= ['Sedan', 'SUV', 'VAN', 'Pickup', 'HatchBack', 'Coupe', 'Cabriolet']
        vehicleBrand= ['Mercedes', 'BMW', 'Audi', 'Subaru', 'Suzuki', 'Toyota', 'Opel']
        transmissionType= ['Manual', 'Automatic']
        fuelType= ['Gas', 'Petroleum', 'Diesel', 'Electric']
        driveTrain= ['FWD', 'RWD', '4WD']
        choice=999
        while choice != 9:
            for k,l in enumerate(optionFill):
                print(k,l)
            try:
                choice = int(input("Επιλογή πεδίου από 0 εως 4 αντίστοιχα, για έξοδο πατήστε 9: "))
                if choice==0:
                    a=999
                    for i, j in enumerate(vehicleType):
                        print(i, j)
                    while a<0 or a> len(vehicleType)-1:
                        try:
                            a = int(input ("Τύπος αυτοκινήτου: "))                                  ##Select vehicle type
                        except:
                            print ("Λάθος επιλογή δεν υπάρχει, προσπάθησε ξανά! \n") 
                    print(vehicleType[a])
                    print()
                    self.tupos=vehicleType[a]
                        
                elif choice==1:
                    b=999
                    for i, j in enumerate(vehicleBrand):
                        print(i, j)
                    while b<0 or b> len(vehicleBrand)-1:
                        try:
                            b = int(input ("Μάρκα αυτοκινήτου: "))                                  ##Select vehicle brand
                        except:                
                            print ("Λάθος επιλογή δεν υπάρχει, προσπάθησε ξανά! ")
                            print()
                    print(vehicleBrand[b])
                    print()
                    self.marka=vehicleBrand[b]
                    
                elif choice==2:
                    c=999
                    for i, j in enumerate(transmissionType):
                        print(i, j)
                    while c<0 or c> len(transmissionType)-1:
                        try:
                            c = int(input ("Σασμάν: "))                                             ##Select transmission type
                        except: 
                            print ("Λάθος επιλογή δεν υπάρχει, προσπάθησε ξανά! ")
                            print()              
                    print(transmissionType[c])
                    print()
                    self.sasman=transmissionType[c]
                                        
                elif choice==3:
                    d=999
                    for i, j in enumerate(fuelType):
                        print(i, j)
                    while d<0 or d> len(fuelType)-1: 
                        try:
                            d = int(input ("Καύσιμο: "))                                            ##Select fuel type
                        except:
                            print ("Λάθος επιλογή δεν υπάρχει, προσπάθησε ξανά! ")
                            print()
                    print(fuelType[d])
                    print()
                    self.kausimo=fuelType[d]
                        
                elif choice==4:
                    e=999
                    for i, j in enumerate(driveTrain):
                        print(i, j)
                    while e<0 or e> len(driveTrain)-1:
                        try:
                            e = int(input ("Κίνηση: "))                                             ##Select drivetrain
                        except:
                            print ("Λάθος επιλογή δεν υπάρχει, προσπάθησε ξανά! ")
                            print()
                    print(driveTrain[e])
                    print()
                    self.kinisi=driveTrain[e]  
                    
                elif choice==9:
                    break
                
                else:
                    print ("Λάθος επιλογή δεν υπάρχει, προσπάθησε ξανά! ","Διαλέξτε μεταξύ 0 και 4.")
                    
            except:
                print("Λάθος επιλογή! Διάλεξε μεταξύ 0 και 4.")
                print()
    def Display(self):
        print("Τύπος αυτοκινήτου: ",self.tupos,"\n","Μάρκα αυτοκινήτου: ",self.marka,"\n","Σασμάν: ",self.sasman,"\n","Καύσιμο: ",self.kausimo,"\n","Κίνηση: ",self.kinisi,"\n")
        
# veh=Vehicle('Unknown','Unknown','Unknown','Unknown','Unknown')
# veh.VehicleForm()
