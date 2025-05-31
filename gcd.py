import.math
def start_game():
    while True:
     num1 = input("enter a number")

    if num1.lower() == 'exit':
        print("good")
        break

    num2 = input("enter an other number")
    if num2.lower() == 'exit':
       print("good")
       break

    if not num1.isdigit() or not num2.isdigit():
        print("enter numbers only")
        continue

    a = int(num1)
    b = int(num2)
    gcd = math.gcd(a,b)

    print(f"{gcd}")

start_game()



