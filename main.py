# Реалізуйте функцію, яка ділить два числа, але обробляє помилку **`ZeroDivisionError`**,
# якщо друге число дорівнює нулю.

try:
    def division(num1, num2):

        result = int(num1) / int(num2)
        print(result)


    x = input("Enter your first number: ")
    y = input("Enter your second number: ")
    division(x, y)

except ZeroDivisionError:
    print("You can not divide by 0")