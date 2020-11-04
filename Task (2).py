# Start The Function to Show the Menu
def show_menu():
    print("\n\n\nPlease choose the operation you want from the following:")
    print("[0] Check the palindrome \t [1] Check if prime \n[99]Exit")
# End The Function to Show the Menu


# Start The Function to Check the Palindrome
def is_palindrome (word):
    word_after = word[::-1]     #The word after being reversed or the Number
    print(word_after)
    if (word == word_after):
        print(word, " is palindrome\n")
    else:
        print(word, " is not palindrome\n")
# End Start The Function to Check the Palindrome


# Start The Function to Check the Prime
def is_prime(num):
    if (num>1):
        for i in range (2,num):
            if (num%i == 0):
                print(num, " is not a prime number\n")
                break
        else:
            print(num, " is a prime number\n")
    else:
        print(num, " is not a prime number\n")
# End The Function to Check the Prime


entry_program = True
while(entry_program):
    print(show_menu())
    choice = int(input("\nEnter your choice: "))
    if (choice == 0):
        word = input("Enter the word or a number you want to check: ")
        print(is_palindrome(word))
    elif (choice == 1):
        num = int(input("Enter a Number to Check if the Number is Prime or Not: "))
        print(is_prime(num))
    elif (choice == 99):
        print("Thanks for Your Effort\n")
        entry_program = False
        break
    else:
        print("Invalid Choice, Please Try Again ...\n")