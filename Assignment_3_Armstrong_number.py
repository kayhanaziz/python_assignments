num = input("Please enter a positive number :")
num_list = list(num)
power = len(list(num))
armstrong_num = 0
if num.isdigit() > 0:
    for i in num_list:
        armstrong_num += int(i) ** power
        
    if armstrong_num == int(num):
        print("{} is an Armstrong number".format(int(num)))
    else:
        print("{} is not an Armstrong number".format(int(num)))
else:
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")


