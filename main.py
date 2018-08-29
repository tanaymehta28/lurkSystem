import random

print("Hello There! \nWelcome to the Safe and Secure Register and Login system.\n")

regId = str(input("Please Choose a username: \n"))
regPass = str(input("Please choose a strong Password: \n"))

random_seed = random.randint(88748,9879878794)


while len(regId) == 0 and len(regPass) < 8:
    while type(regId) == int:
        regId = str(input("Please choose a valid UserId: "))
        regPass = str(input("Please enter a valid Password: "))


#Generates a random seed to run everytime.

regId = hash(regId)*random_seed
regId = regId/57889

regPass = hash(regPass)*random_seed
regPass = regPass+7265374


print("Registration sucessfull. \n")

i = 0
while i < 20:
    print("Please wait ", i, " seconds before loging in! \n")
    i = i+1

logId = str(input("Please enter your Login-id: \n"))

logPass = str(input("Please enter your Login-Password: \n"))

logId = hash(logId)*random_seed
logId = logId/57889

logPass = hash(logPass)*random_seed
logPass = logPass+7265374

while logId != regId or logPass != regPass:
    print("Login Unsuccessfull: Wrong Id or Password or both")
    logId = str(input("Please enter your Login-id: \n"))
    logPass = str(input("Please enter your Login-Password: \n"))

    logId = hash(logId) * random_seed
    logId = logId / 57889

    logPass = hash(logPass) * random_seed
    logPass = logPass + 7265374

print("Login Sucessfull! \n")



