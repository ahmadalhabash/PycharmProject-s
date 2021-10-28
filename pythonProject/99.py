class moneey():
    def __float__(self, money):
        self.money = money
        bank = self.money[1]
        son = self.money[4]
        daughter = self.money[7]

    def __init__(self, person):
        self.person = person
        dad = self.person[1]
        mam = self.person[3]
        wife1 = self.person[5]
        wife2 = self.person[7]
        wife3 = self.person[9]
        wife4 = self.person[11]

    def calculate_The_person_share_of_the_heirs(self):

        if "0" in family or "1" in family or "2" in family or "3" in family or "4" in family or "5" in family or "6" in family or "7" in family or "8" in family or "9" in family or "!" in family or "@" in family or "#" in family or "%" in family or "^" in family or "&" in family or"*" in family or "(" in family or ")" in family or "_" in family or "+" in family or "-" in family or "=" in family or "~" in family or "`" in family or "" in family  :
            Lie_detector[0] = 0
            print("PLEASE WRITE THE NAME")

        else:
             if "pass" in self.person[1]:
                print("dad is not here:")
                dad_not_here = 0

                print("....................")
             else:
                print(self.person[1] + " (dad's) money :")
                print(20 / 100 * money_account[1])
                print("....................")

             if "pass" in self.person[3]:
                print("mom is not here")
                print("....................")

             else:
                print(self.person[3] + " (mam's) money :")
                print(10 / 100 * money_account[1])
                print("....................")

             if "pass" in self.person[5]:
                print("wife1 is not here")
                print("....................")

             else:
                print(self.person[5] + " (wife1's) money :")
                print(5 / 100 * money_account[1])
                print("....................")

             if "pass" in self.person[7]:
                print("wife2 is not here")
                print("....................")

             else :
                print(self.person[7] + " (wife2) money :")
                print(5 / 100 * money_account[1])
                print("....................")

             if "pass" in self.person[9]:
                print("wife3 is not here")
                print("....................")

             else:
                print(self.person[9] + " (wife3) money :")
                print(5 / 100 * money_account[1])
                print("....................")

             if "pass" in self.person[11]:
                print("wife3 is not here")
                print("....................")
             else:
                print(self.person[11] + " (wife4) money :")
                print(5 / 100 * money_account[1])
                print("....................")


Lie_detector = [None]

money_account = [print("Write the amount of the heirs :"), float(input()), print(".............."),
                 print("Write how many males :"), float(input()), print("..............."),
                 print("Write how many females :"), float(input())]

# jj Values
dad_not_here = 0
dad = 20 / 100 * money_account[1]
mam_not_Here = 0
mam = 10 / 100 * money_account[1]
wife1_not_here = 0
wife1 = 5 / 100 * money_account[1]
wife2_not_here = 0
wife2 = 5 / 100 * money_account[1]
wife3_not_here = 0
wife3 = 5 / 100 * money_account[1]
wife4_not_here = 0
wife4 = 5 / 100 * money_account[1]
jj = [dad_not_here, dad, mam_not_Here, mam, wife1_not_here, wife1, wife2_not_here, wife2, wife3_not_here, wife3,
      wife4_not_here, wife4]

print("...............")

family = (
    print("Write the name of the father. If the father is not existent , write pass :"), input(),
    print("Write the name of the mother. If the mother is not existent , write pass:"),
    input(), print("Write the name of the First Wife. If the First Wife is not existent , write pass :"), input(),
    print("Write the name of the Second Wife. If the Second Wife is not existent , write pass :"), input(),
    print("Write the name of the Third Wife. If the Third Wife is not existent , write pass :"), input(),
    print("Write the name of Forth Wife . If the Forth Wife is not existent , write pass :"), input())

print("\n")

print("peron money:")
print("...................")

your = moneey(family)
your.calculate_The_person_share_of_the_heirs()

ff = money_account[1] - (
            dad + dad_not_here + mam_not_Here + mam + wife1 + wife1_not_here + wife2 + wife2_not_here + wife3 + wife3_not_here + wife4 + wife4_not_here)


class sons:
    def sos(self):
        s = son * 2
        d = daughter
        gg = ff

        if Lie_detector[0] == 0 :
         pass
        else:

            if s == 0 and d== 0:
                print("The bouns of the heirs :")
                print(gg)


            if s > 0 or d > 0:
                c = s + d
                x = ff / c
                son1 = x * 2
                daughter1 = x
                if s > 0:
                    print("Male share of heirs   :")
                    print(son1)
                    print("..............")

                if d > 0:
                    print("The female's share of the heirs :")
                    print(daughter1)
                    print("..............")
            else:
              pass


son = money_account[4]
daughter = money_account[7]

ss = sons()
ss.sos()