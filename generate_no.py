import math
n = 100

def check_prime_no(num):
    i = 2
    flag = 0
    sqrt = math.sqrt(num)
    while(i <= sqrt):
        if num % i == 0:
            flag = 1
            return flag
        else:
            i += 1
    return flag

def check_happy_no(num):
    flag = 0
    number = get_square_num_sum(num)
    while(number > 9):
        number = get_square_num_sum(number)
    if number == 1:
        flag = 1
    return flag

def get_square_num_sum(num):
    sum = 0
    for i in str(num):
        num1 = int(i)
        sum += num1 * num1
    return sum

def return_file_content(file_obj):
    list1 = []
    for i in file_obj.readlines():
        list1.append(i.strip())
    file_obj.close()
    return list1

j = 2
file_obj = open('pn.txt','w+')
file_obj.truncate()

file_obj1 = open('hn.txt','w+')
file_obj1.truncate()
file_obj1.write("%d \n" % 1)

while(j <= n):
    is_prime = check_prime_no(j)
    if is_prime == 0:
        file_obj.write("%d \n" % j)
    is_happy = check_happy_no(j)
    if is_happy == 1:
        file_obj1.write("%d \n" % j)
    j += 1

file_obj.close()
file_obj1.close()


file_obj = open('pn.txt','r+')
list1 = return_file_content(file_obj)
print "%r" % list1

print 4 * "-----"


file_obj1 = open('hn.txt','r+')
list2 = return_file_content(file_obj1)
print "%r" % list2

common_number = list(set(list1) & set(list2))
file_obj = open('result.txt','w+')
file_obj.truncate()
for i in common_number:
    file_obj.write("%r \n" % int(i))
file_obj.close()
