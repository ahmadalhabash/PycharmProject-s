class heirs():
    def __float__(self, money):
        self.money = money
        heirs_s = self.money[1]
        son = self.money[4]
        daughter = self.money[7]
        wife = self.money[10]

    def __init__(self, person):
        self.person = person
        dad = self.person[1]
        mam = self.person[3]



    def calculate_The_person_share_of_the_heirs(self):
        if "0" in family or "1" in family or "2" in family or "3" in family or "4" in family or "5" in family or "6" in family or "7" in family \
                or "8" in family or "9" in family or "!" in family or "@" in family or "#" in family or "%" in family or "^" in family \
                or "&" in family or "*" in family or "(" in family or ")" in family or "_" in family or "+" in family or "-" in family \
                or "=" in family or "~" in family or "`" in family  or money_account[10] >4 or money_account[10] <0:
            Lie_detector[0] = 0
            print("PLEASE WRITE THE CORRECT INFORMATION")

        else:
            if "pass" in self.person[1] or "" == self.person[1] or " " == self.person[1] or "  " == self.person[1] or "   " == self.person[1] or "    " in self.person[1]:
                the_share_of_the_heirs_per_person[0] = 0

            else:
                print(self.person[1] + " (Father) money :")
                print(20 / 100 * money_account[1])
                print("....................")
                the_share_of_the_heirs_per_person[0] = 20 / 100 * money_account[1]

            if "pass" in self.person[3] or "" == self.person[3] or " " == self.person[3] or "  " == self.person[3] or "   " == self.person[3] or "    " in self.person[3]:
                the_share_of_the_heirs_per_person[1] = 0

            else:
                print(self.person[3] + " (Mother) money :")
                print(10 / 100 * money_account[1])
                print("....................")
                the_share_of_the_heirs_per_person[1] = 10 / 100 * money_account[1]


    def calculate_The_wife_share_of_the_heirs(self):
        if money_account[10] >4 or money_account[10] <0 or money_account[10] == 0:
            the_share_of_the_heirs_per_person[2] = 0
        else:
            print("wife share of the heirs :")
            print(5 / 100 * money_account[1])
            print("....................")
            the_share_of_the_heirs_per_person[2] = (5 / 100 * money_account[1]) * (money_account[10])




Lie_detector = [None]

money_account = [print("Write the amount of the heirs :"), float(input()), print(".............."),
                 print("Write how many males :"), float(input()), print("..............."),
                 print("Write how many females :"), float(input()) ,print("..............."), print("Write how many wifes :"), float(input())]

# jj Values
dad = float()  # [0]
mam = float()  # [1]
wif = float() # [2]

the_share_of_the_heirs_per_person = [float(dad), float(mam), float(wif)]

print("...............")

family = (print("Write the name of the father. If the father is not existent , write pass :"), input(),print("Write the name of the mother. If the mother is not existent , write pass:"), input())

print("\n")

print("peron money:")
print("...................")

your_heirs = heirs(family)

your_heirs.calculate_The_person_share_of_the_heirs()

w = heirs(money_account)
w.calculate_The_wife_share_of_the_heirs()

the_remainder_of_the_heirs_after_calculating_the_individual_s_share = money_account[1] - \
(the_share_of_the_heirs_per_person[0] + the_share_of_the_heirs_per_person[1] + the_share_of_the_heirs_per_person[2])

class son_daughter:
    def calculate_The_son_and_daughter_share_of_the_heirs(self):
        s = son * 2
        d = daughter

        if Lie_detector[0] == 0  :
            pass
        else:

            if s == 0 and d == 0:
                print("The bouns of the heirs :")
                print(the_remainder_of_the_heirs_after_calculating_the_individual_s_share)

            if s > 0 or d > 0:
                c = s + d
                x = the_remainder_of_the_heirs_after_calculating_the_individual_s_share / c
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

ss = son_daughter()
ss.calculate_The_son_and_daughter_share_of_the_heirs()
