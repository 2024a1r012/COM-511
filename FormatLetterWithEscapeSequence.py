name=input("Enter your name:")
date=input("Enter Date:")

letter="Dear <name>\nYou are selected!!\n<date>"

letter=letter.replace("<name>",name)
letter=letter.replace("<date>",date)

print(letter)