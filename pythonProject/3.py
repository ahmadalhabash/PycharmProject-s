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

        if "0" in family or "1" in family or "2" in family or "3" in family or "4" in family or "5" in family or "6" in family or "7" in family or "8" in family or "9" in family or "!" in family or "@" in family or "#" in family or "%" in family or "^" in family or "&" in family or"*" in family or "(" in family or ")" in family or "_" in family or "+" in family or "-" in family or "=" in family or "~" in family or "`" in family or "/" in family  :
            Lie_detector[0] = 0
            print("PLEASE WRITE THE NAME")

        else:
            if "pass" in self.person[1]:
                jj[0] = 0
                jj[1] = 0

            else:
                print(self.person[1] + " (Father) money :")
                print(20 / 100 * money_account[1])
                print("....................")
                jj[0] = 20 / 100 * money_account[1]
                jj[1] = 0

            if "pass" in self.person[3]:
                jj[2] = 0
                jj[3] = 0

            else:
                print(self.person[3] + " (Mother) money :")
                print(10 / 100 * money_account[1])
                print("....................")
                jj[2] = 0
                jj[3] = 10 / 100 * money_account[1]

            if "pass" in self.person[5]:
                jj[4] = 0
                jj[5] = 0

            else:
                print(self.person[5] + " (First Wife) money :")
                print(5 / 100 * money_account[1])
                print("....................")
                jj[4] = 0
                jj[5] = 5 / 100 * money_account[1]

            if "pass" in self.person[7]:
                jj[6] = 0
                jj[7] = 0

            else:
                print(self.person[7] + " (Second Wife) money :")
                print(5 / 100 * money_account[1])
                print("....................")
                jj[6] = 0
                jj[7] = 5 / 100 * money_account[1]

            if "pass" in self.person[9]:
                jj[8] = 0
                jj[9] = 0

            else:
                print(self.person[9] + " (Third Wife) money :")
                print(5 / 100 * money_account[1])
                print("....................")
                jj[8] = 0
                jj[9] = 5 / 100 * money_account[1]

            if "pass" in self.person[11]:
                jj[10] = 0
                jj[11] = 0
            else:
                print(self.person[11] + "(Third Wife) money :")
                print(5 / 100 * money_account[1])
                print("....................")
                jj[10] = 0
                jj[11] = 5 / 100 * money_account[1]


Lie_detector = [None]

money_account = [print("Write the amount of the heirs :"), float(input()), print(".............."),
                 print("Write how many males :"), float(input()), print("..............."),
                 print("Write how many females :"), float(input())]

# jj Values
dad = float() # [0]
dad_not_here =float() # [1]
mam_not_Here = float() # [2]
mam = float() # [3]
wife1_not_here = float()# [4]
wife1 = float() # [5]
wife2_not_here = float()# [6]
wife2 =float()# [7]
wife3_not_here =float() # [8]
wife3 = float() # [9]
wife4_not_here =float()# [10]
wife4 = float()# [11]
jj = [float(dad) , float(dad_not_here), float(mam_not_Here), float(mam), float(wife1_not_here), float(wife1), float(wife2_not_here), float(wife2), float(wife3_not_here), float(wife3),
      float(wife4_not_here), float(wife4)]


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

ff = money_account[1] - (jj[0] + jj[1] + jj[2] + jj[3] + jj[4] + jj[5] + jj[6] + jj[7] + jj[8] + jj[9] + jj[10] + jj[11])

class sons:
    def sos(self):
        s = son * 2
        d = daughter
        gg = ff

        if Lie_detector[0] == 0 :
         pass
        else:

            if s == 0 and d == 0:
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