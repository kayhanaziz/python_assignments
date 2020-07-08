name = "Kayhan"
password = "W@12345K"

int_name = input("Please enter your first name :").title()

if int_name == name:
    print("Hello, {}! The password is :{}".format(name, password))
else:
    print("Hello {}! See you later".format(int_name))

