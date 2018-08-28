print("Hello There! \nWelcome to the Safe and Secure Register and Login system.\n")

regId = str(input("Please Choose a username: \n"))
regPass = str(input("Please choose a strong Password: \n"))

while len(regId) == 0 and len(regPass) < 8:
    while type(regId) == int:
        regId = str(input("Please choose a valid UserId: "))
        regPass = str(input("Please enter a valid Password: "))

regId = hash(regId)*83983973756
regId = regId/57889

regPass = hash(regPass)*939784868
regPass = regPass+7265374


print("Registration sucessfull. \n")

i = 0
while i < 20:
    print("Please wait ", i, " seconds before loging in! \n")
    i = i+1

logId = str(input("Please enter your Login-id: \n"))

logPass = str(input("Please enter your Login-Password: \n"))

logId = hash(logId)*83983973756
logId = logId/57889

logPass = hash(logPass)*939784868
logPass = logPass+7265374

while logId != regId or logPass != regPass:
    print("Login Unsuccessfull: Wrong Id or Password or both")
    logId = str(input("Please enter your Login-id: \n"))
    logPass = str(input("Please enter your Login-Password: \n"))

    logId = hash(logId) * 83983973756
    logId = logId / 57889

    logPass = hash(logPass) * 939784868
    logPass = logPass + 7265374

print("Login Sucessfull! \n")


