import os
import random
import hashlib
import string
import enchant  # Rainbow tables with enchant
import cloud  # importing pi-cloud

def randomword(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

print('Author- Radhika Subramanian')

def mainroutine():
    engdict = enchant.Dict("en_US")
    fileb = open("password.txt", "a+")

    while True:
        randomword0 = randomword(6)
        if engdict.check(randomword0):
            randomkey0 = randomword0 + str(random.randint(0, 99))
        else:
            englist = engdict.suggest(randomword0)
            if len(englist) > 0:
                randomkey0 = englist[0] + str(random.randint(0, 99))
            else:
                randomkey0 = randomword0 + str(random.randint(0, 99))

        randomword3 = randomword(5)
        if engdict.check(randomword3):
            randomkey3 = randomword3 + str(random.randint(0, 99))
        else:
            englist = engdict.suggest(randomword3)
            if len(englist) > 0:
                randomkey3 = englist[0] + str(random.randint(0, 99))
            else:
                randomkey3 = randomword3 + str(random.randint(0, 99))
      
        randomkey1 = randomword(7)

        # Write data to the file within the loop
        whasher0 = hashlib.new("md5")
        whasher0.update(randomkey0.encode())
        whasher3 = hashlib.new("md5")
        whasher3.update(randomkey3.encode())
        whasher1 = hashlib.new("md5")
        whasher1.update(randomkey1.encode())
        fileb.write(randomkey0 + " + " + str(whasher0.hexdigest()) + "\n")
        fileb.write(randomkey3 + " + " + str(whasher3.hexdigest()) + "\n")
        fileb.write(randomkey1 + " + " + str(whasher1.hexdigest()) + "\n")
        fileb.flush()  # Flush the buffer to ensure data is written

# Commented out as it's not clear what it's doing
# jid = cloud.call(randomword)  # square(3) evaluated on PiCloud
# cloud.result(jid)

print('Value added to cloud')
print('Password added')
mainroutine()