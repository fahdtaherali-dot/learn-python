phone_book = {
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla"
}
# دالة التحقق من صحة الرقم 
def is_valid_number(number):
    count = 0
    for char in number:
        count += 1
    if count != 10:
        return False
    for char in number:
        if char < '0' or char > '9':
            return False
    return True
# دالة البحث عن الاسم باستخدام الرقم 
def find_name_by_number():
    phone_number = input("Enter the phone number: ")
    if is_valid_number(phone_number):
        for number in phone_book:
            if phone_number == number:
                print(phone_book[phone_number])
                return
        print("Sorry, the number is not found")
    else:
        print("This is invalid number")


def find_number_by_name():
    name = input("Enter the name:")
    for number, owner in phone_book.items():
        if owner == name:
            print(number)
            return
    print("Sorry, the name is not found")



def add_new_contact():
    new_name = input("Add new name:")
    new_number = input("Add new number:")
    if is_valid_number(new_number):
        phone_book[new_number] = new_name
        print("Contact added successfully!")
    else:
        print("This is invalid number")



find_name_by_number()
find_number_by_name()
add_new_contact()