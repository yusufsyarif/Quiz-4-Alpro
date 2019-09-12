ListofGPA = [2.1,2.5,4,3]
def fbonus (GPA):
    bonus = 500000
    fbonus = GPA*bonus
    return fbonus

for GPA in ListofGPA:
    if GPA > 2.5:
        print("Congratulation! You win a Bonus : Rp", fbonus(GPA))
    else :
        print("Sorry, maybe next time!")