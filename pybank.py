import random


def login(chk=1):
	if chk == 1:
		username = input("What is your username: ")
		password = input("What is your password: ")

		state = None
		staff_file = open("staff.txt", "r")
		staff = eval(staff_file.read())
		staff_file.close()

		exist = False
		for count in range(len(staff)):
			if username == staff[count][0]:
				exist = True
				if password == staff[count][1]:
					print("Logged in")
					state = True
				else:
					print("Incorrect Password try again")
					login()
					state = True
		if not exist:
			print("Invalid Username try again")
			login()
			state = True
		return state
	elif chk == 2:
		state = True
		return state


def create_bank_account():
	print("Please Enter the following details to create an account")
	account_name = input("Enter Account Name: ")
	opening_balance = input("Enter Opening Balance: ")
	account_type = input("Enter Account Type: ")
	account_email = input("Enter Account Email: ")
	account_number = generate_account_number()
	user_info = {
		'account_name': account_name,
		'account_number': account_number,
		'account_email': account_email,
		'account_type': account_type,
		'opening_balance': opening_balance
	}

	with open('customer.txt', 'w') as f:
		f.write(str(user_info))
	print(f'Account Number: {account_number}')


def generate_account_number():
	num = random.randint(1000000000, 9999999999)
	return num


def check_account_details():
	with open('customer.txt', 'r') as f:
		contents = eval(f.read())
	acc_number = int(input('Please enter account number: '))
	if contents['account_number'] == acc_number:
		print(contents)
	else:
		print('You have entered an invalid account number')


def show_menu():
	print("1 Create new bank account")
	print("2 Check Account Details")
	print("3 Logout")
	choice1 = int(input("Enter a value 1, 2 or 3: "))
	return choice1


def logout():
	print("Thank you for using pyBank!!")
	exit()


def main():
	print("Welcome to PyBank!!")
	print("1 Staff Login")
	print("2 Close App")
	choice = int(input("Enter a value 1 or 2: "))
	if choice == 1:
		if login():
			choice1 = show_menu()
			if choice1 == 1:
				create_bank_account()
			elif choice1 == 2:
				check_account_details()
			elif choice1 == 3:
				logout()
	elif choice == 2:
		logout()


# generate_account_number()
# check_account_details()

if __name__ == '__main__':
	main()
