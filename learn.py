phone_book = {
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla"
}
def check_the_number(number):
     count = 0
     for char in number:
        count += 1
     if count != 10: 
        return False
     return True
def find_name_by_number():
    aaaq = input("Please enter the phone number: ")
    if check_the_number(aaaq):
        for number in phone_book:
            if number == aaaq:
                print(phone_book[aaaq])
                return
        print('Sorry, the number is not found')
    else:
             print("This is invalid number")
find_name_by_number()