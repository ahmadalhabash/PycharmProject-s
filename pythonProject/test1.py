class family:

    def __init__(self, family_data):
        self.family_dat = family_data


    def parents (self):
        print(" %s is a %s, and %s born in %s, and %s is %s years old" % ( self.family_dat[0], self.family_dat[1] , self.family_dat[0] , self.family_dat[2], self.family_dat[0], self.family_dat[3]))

    def son_and_daughter(self):
        print(" %s is the %s, and %s born in %s and %s is %s and %s years old Arrange it in the family is the %s " % (self.family_dat[0], self.family_dat[1], self.family_dat[0], self.family_dat[-3], self.family_dat[0], self.family_dat[-4], self.family_dat[-1], self.family_dat[-2]))




mohamad_al_habash = ["mohamad al habash","Dad", 1982, 39]
heba_shaheen = ["Heba shaheen" ,  "Mam", 1981, 40]
ahmad_al_habash = ["Ahmad al habash",  "Son" , " Tenth grade", 2006, "first", 15]
tala_al_habash = ["Tala al habash", "daughter","Eighth grade" ,2008, "second", 13]
hedaia_al_habash = [ "hedaia al habash", "daughter", "Sixth grade" , 2010, "third", 11]
noor_al_deen_al_habash = ["noor al deen al habash", "Son" , "First grade", 2014, "forth", 7]



family_data = family(mohamad_al_habash)
family_data.parents()

print("\n")

family_data = family(heba_shaheen)
family_data.parents()

print("\n")

family_dataa = family(ahmad_al_habash)
family_dataa.son_and_daughter()

print("\n")

family_dataa = family(tala_al_habash)
family_dataa.son_and_daughter()

print("\n")

family_dataa = family(hedaia_al_habash)
family_dataa.son_and_daughter()

print("\n")

family_dataa = family(noor_al_deen_al_habash)
family_dataa.son_and_daughter()