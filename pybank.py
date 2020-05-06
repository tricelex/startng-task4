import random

print("Welcome to PyBank!!")
print("1 Staff Login")
print("2 Close App\n")


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


def logout():
	pass


def main():
	pass


# generate_account_number()
check_account_details()
