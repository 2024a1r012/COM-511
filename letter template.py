name=input("Enter Your name:")
date=input("Enter Date:")
letter='''
Dear <name>
You are Selected!
<date>
'''
letter=letter.replace("<name>",name)
letter=letter.replace("<date>",date)
print(letter)