name = "Saul"
last_name = "Miller"
age = 60
city = "Mob"
array = ["1","2"]

if age < 50:
    print("you're so young")
elif age == 50:
    print("you're not so old")
else:
    print("yes you're old, but dont worry")


if name == "Letherius":
    print("Hello there " + name)
else:
    print("You are not Letherius")   

number_1= 15
number_2= 10

def test():
    print("hello I am a function")

def sum(number, numbers):
    return number + numbers

result = sum(15,12)

def mul(numberM, numbersM):
    return numberM * numbersM

resultM = mul(15,12)

nums = [12,-5,4,-15,-12,45,23,84,-2,0,-6,-2]

for n in nums:
    if n < 0:
     print (n)

    #print the sum of all the numbers in the list
    totalOfSum = 0

    for num in nums:
        totalOfSum = totalOfSum + num
         