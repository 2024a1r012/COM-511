email=input("Enter Email address:")
index=email.find("@")
domain=email[index+1:]
print("Domain=",domain)