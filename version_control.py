#Timothy Jin
def encode(password):
    pass_list = list(password)
    encode_str = ""
    for x in pass_list:
        encode_str += str(int(x)+3)
    return encode_str

def decode(password):
    pass

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
            pass
        elif option == 3:
            break
        print()
if __name__ == '__main__':
    main()