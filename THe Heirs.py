class heirs():
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

        if "0" in family or "1" in family or "2" in family or "3" in family or "4" in family or "5" in family or "6" in family or "7" in family \
                or "8" in family or "9" in family or "!" in family or "@" in family or "#" in family or "%" in family or "^" in family \
                or "&" in family or "*" in family or "(" in family or ")" in family or "_" in family or "+" in family or "-" in family \
                or "=" in family or "~" in family or "`" in family or "" in family:
            Lie_detector[0] = 0
            print("PLEASE WRITE THE NAME")

        else:
            if "pass" in self.person[1]:
                The_share_of_the_heirs_per_person[0] = 0

            else:
                print(self.person[1] + " (Father) money :")
                print(20 / 100 * money_account[1])
                print("....................")
                The_share_of_the_heirs_per_person[0] = 20 / 100 * money_account[1]

            if "pass" in self.person[3]:
                The_share_of_the_heirs_per_person[1] = 0

            else:
                print(self.person[3] + " (Mother) money :")
                print(10 / 100 * money_account[1])
                print("....................")
                The_share_of_the_heirs_per_person[1] = 10 / 100 * money_account[1]

            if "pass" in self.person[5]:
                The_share_of_the_heirs_per_person[2] = 0

            else:
                print(self.person[5] + " (First Wife) money :")
                print(5 / 100 * money_account[1])
                print("....................")
                The_share_of_the_heirs_per_person[2] = 5 / 100 * money_account[1]

            if "pass" in self.person[7]:
                The_share_of_the_heirs_per_person[3] = 0

            else:
                print(self.person[7] + " (Second Wife) money :")
                print(5 / 100 * money_account[1])
                print("....................")
                The_share_of_the_heirs_per_person[3] = 5 / 100 * money_account[1]

            if "pass" in self.person[9]:
                The_share_of_the_heirs_per_person[4] = 0

            else:
                print(self.person[9] + " (Third Wife) money :")
                print(5 / 100 * money_account[1])
                print("....................")
                The_share_of_the_heirs_per_person[4] = 5 / 100 * money_account[1]

            if "pass" in self.person[11]:
                The_share_of_the_heirs_per_person[5] = 0
            else:
                print(self.person[11] + "(Third Wife) money :")
                print(5 / 100 * money_account[1])
                print("....................")
                The_share_of_the_heirs_per_person[5] = 5 / 100 * money_account[1]


Lie_detector = [None]

money_account = [print("Write the amount of the heirs :"), float(input()), print(".............."),
                 print("Write how many males :"), float(input()), print("..............."),
                 print("Write how many females :"), float(input())]

# jj Values
dad = float()  # [0]
mam = float()  # [1]
wife1 = float()  # [2]
wife2 = float()  # [3]
wife3 = float()  # [4]
wife4 = float()  # [5]
The_share_of_the_heirs_per_person = [float(dad), float(mam), float(wife1), float(wife2), float(wife3), float(wife4)]

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

your_heirs = heirs(family)
your_heirs.calculate_The_person_share_of_the_heirs()
ff = money_account[1] - (The_share_of_the_heirs_per_person[0] + The_share_of_the_heirs_per_person[1] + The_share_of_the_heirs_per_person[2] + The_share_of_the_heirs_per_person[3] + The_share_of_the_heirs_per_person[4] + The_share_of_the_heirs_per_person[5])


class son_daughter:
    def calculate_The_son_and_daughter_share_of_the_heirs(self):
        s = son * 2
        d = daughter
        gg = ff

        if Lie_detector[0] == 0:
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

ss = son_daughter()
ss.calculate_The_son_and_daughter_share_of_the_heirs()
