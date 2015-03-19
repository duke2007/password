import random
#Create a tuple with random character from keyboard
inventory = ('axw@','bhg%s','sq$pc','dp{E#s','qw!e^J','xo%%$f',
			'kafg','w$Ula#','@Mpw*','K&sdf','@%Tsxc','alopw$','qp}@cx','!h#&m*S')
         
answer = 'No'
answer = input('You want to generate a password, uh? (Please hit Enter?) ')
#generate the password
#use str to transform object number in string object
password = random.choice(inventory) + str(random.randint(1, 10456))

#printing result
print("Your password is: ", password)
#Introduce a while loop. As long as user
#hit enter, a new password is generate.
#If user enter no or No program exit 
while answer !='No' and answer !='no':
    answer = input('You want another password? Hit Enter again (No/no to exit and a password gift..)')
    print("Your password is: ", random.choice(inventory) + str(random.randint(1, 10456)))
