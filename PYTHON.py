#Print a appropriate question for their personal info#
name = input ("What is your name")
age = input ("How old are you")
street_name = input ("At what street do you live in")
country = input ("What Country are you legally authorized")
House_Address = input ("What is you Houses location/address")

#Print a Correction statement If info is confirmed to be true#
Check = input("do you wish to see your answers Y/N")
If Check == "yes":
    print("ok")
else:   
    print("Too bad I have show it to you anyways")

#Print a Summary of input#
print("here is your Answers: ")
print("Name: " + name)
print("Age: " + age)
print("Street: " + street_name)
print("Country: " + country)
print("Address: " + House_Address)
