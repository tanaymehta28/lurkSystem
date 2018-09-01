import random

print("Hello There! \nWelcome to the Safe and Secure Register and Login system.\n")

seedLogin = random.randrange(767648787805,343556677654756874685746587346584854853874568734568734658345347326457436535834579834759899)
seedPass = random.randrange(7368472368473827,9834093094839874376487346746256562669525155815132161168415216516538495652151651351)

regId = str(input("Please Choose a username: \n"))
regPass = str(input("Please choose a strong Password: \n"))

while len(regId) == 0 and len(regPass) < 8 and regId == regPass:
    while type(regId) == int:
        regId = str(input("Please choose a valid UserId: "))
        regPass = str(input("Please enter a valid Password: "))

regId = hash(regId)*seedLogin
regId = regId/57889

regPass = hash(regPass)*seedPass
regPass = regPass+7265374


print("Registration sucessfull. \n")

i = 100
while i != 0:
    print("Please wait ", i, " moments before loging in! \n")
    i = i-1

logId = str(input("Please enter your Login-id: \n"))

logPass = str(input("Please enter your Login-Password: \n"))

logId = hash(logId)*seedLogin
logId = logId/57889

logPass = hash(logPass)*seedPass
logPass = logPass+7265374

while logId != regId or logPass != regPass:
    print("Login Unsuccessfull: Wrong Id or Password or both")
    logId = str(input("Please enter your Login-id: \n"))
    logPass = str(input("Please enter your Login-Password: \n"))

    logId = hash(logId) * seedLogin
    logId = logId / 57889

    logPass = hash(logPass) * seedPass
    logPass = logPass + 7265374

print("Login Sucessfull! \n")


