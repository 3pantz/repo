#Timothy Jin
#encode function
def encode(password):
    pass_list = list(password)
    encode_str = ""
    for x in pass_list:
        encode_str += str((int(x)+3)%10)
    return encode_str

#Sephora Pierre-Louis
#decode function
def decode(password):
    password_list = list(password)
    encoded_list = []
    for item in password_list:
        item = int(item)
        item = (item + 7) % 10
        encoded_list.append(str(item))

    encoded_string = ''.join(encoded_list)

    return encoded_string

#main function
def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        print()
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            password = encode(password)
        elif option == 2:
            #Sephora Pierre-Louis
            print("The encoded password is " + password + ", and the original password is " + decode(password) + ".")

        elif option == 3:
            break
        print()
if __name__ == '__main__':
    main()