from getpass import getpass
username="luis"
password="123"

user = input("Enter username:")
passwrd = getpass("Enter password:")

if username == user and passwrd == password:
	print("Access Granted")

else:
	print("Access Denied")


