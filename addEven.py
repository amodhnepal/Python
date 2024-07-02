# Adding even numbers from 1 to 100
sum_num=0
for number in range(1,101):
    if number%2==0:
        sum_num+=number
print(sum_num)



# Also we can do in the following way
sum_num=0
for number in range(1,101,2):
    sum_num+=number
print(sum_num)