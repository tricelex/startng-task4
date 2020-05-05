print("Welcome to PyBank!!")
print("1 Staff Login")
print("2 Close App\n")
choice = int(input(''))
running = True


def login():
	username = input("What is your username: ")
	password = input("What is your password: ")

	staff_file = open("staff.txt", "r")
	staff = eval(staff_file.read())
	staff_file.close()

	exist = False
	for count in range(len(staff)):
		if username == staff[count][0]:
			exist = True
			if password == staff[count][1]:
				print("Logged in")
			else:
				print("Incorrect Password")
				login()
	if not exist:
		print("Invalid Username")
		login()


while running:
	if choice == 2:
		running = False
		print('exit while loop')
		exit()
	print('Hello my name is chuckz')
	login()
