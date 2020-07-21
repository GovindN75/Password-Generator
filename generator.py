import string
import random


if __name__ == "__main__":
    num_pass = int(input("How many passwords do you want? "))

    if num_pass == 0:
        pass_len = input("Seems like you don't want a password afterall. Go ahead, press enter to try again ")
        num_pass = int(input("How many passwords do you want? "))
    if num_pass == 1:
        pass_len = int(input("What should be the length of the password? "))
    else:
        pass_len = int(input("What should be the length of the passwords? "))
    characters = string.ascii_letters + string.digits + string.punctuation
    print("Your passwords are:")
    for i in range(num_pass):
        for j in range(pass_len):
            print(''.join(random.choice(characters)), end = "")
        print("\n")
        




    