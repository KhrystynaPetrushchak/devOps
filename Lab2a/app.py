
#2.i
#Виконуємо виведення констант
print("Перша константа", False)
print("Друга константа", True)
print("Третя константа", None)

print("  ")

#2.ii
#Обираємо будь-яку вбудовану константу та виконуємо звичайні базові приклади за допомогою констант 
#Моє прізвище починається P, тому демонструю  роботу функції pow() та інших функцій, яких я обрала
#pow()-повертає значенння числа х(в даному випадку=> 4) піднесеного до степення у(в даному випадку=> 5)
print(pow(4,5)) 
print(abs(-45))
print(bin(5))
print(all([1,2,3]))

print("  ")

#2.iii
#Ознайомлюємось з циклами та пишемо 3 своїх
words=["hello","world","school"]
for word in words:
	print(word + " ^_^ ")

print("  ")


for number in range(10):
    if number % 2 == 0:
        print(number)

print("  ")

a=5
while a<25:
	print(a)
	a=a+5



print("  ")
#2.iv
#Демонструємо роботу конструкції  try->except->finally

number1=0
number2=15
try:
   print("Поділимо 15 на 0, у результаті отримаємо: ",number2/number1)
except ZeroDivisionError:
	print("Помилка")
finally:
	print("На нуль ділити не можна!!!")

print("  ")
#2.v
#Робота контекст-менеджера with. Код з ним: 

with open("README.md", "r") as khrum:
    for line in khrum:
        print(line)

print("  ")
#2.vi
#Робота з Python lambdas

x=lambda a,b : a/b
print(x(6,2)) 

