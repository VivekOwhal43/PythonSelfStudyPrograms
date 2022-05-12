# function for getting name from user and displaying it on console
def helloUser():
    print("Welcome to User Name Program")
    name = input("Please enter your name:")
    nameLength = len(name)
    if nameLength<3:
        print("User name length must be greater than or equal to 3")
    # print(nameLength)
    else:
        print("Hello "+name, "How Are You?\n")

def main():
    helloUser()
    helloUser()

if __name__ == "__main__":
    main()