number = int(input("Enter your phone number like this: +998 12 345 67 89\n "))
if number.startswith("+998") and type(number)==int:
    if len(number) != 13:
        print("Raqam noto'g'ri kiritilgan")
    else:
        print("Raqam kiritildi")
print(f"Your phone number is{number}")