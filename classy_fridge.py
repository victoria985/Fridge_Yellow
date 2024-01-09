import os

class Smart_Fridge:
    def __init__(self, user_name, pin_code, temperature=5):
        self.user_name = user_name
        self.__pin = pin_code
        self.__temperature = temperature

    # String representation of a class for checks
    def __str__(self):
        return f'{self.user_name}:{self.__pin}:{self.__temperature}'

    # User input function to get user name and pin code
    @staticmethod
    def get_user_input():
        user_name = input("Enter your username: ")
        while True:
            pin_code = input("Enter your 4-digit PIN code: ")
            if pin_code.isdigit() and len(pin_code) == 4:
                break
            else:
                print("Invalid PIN code. Please enter a 4-digit number.")
        return user_name, pin_code

    # Function to save user information localy
    def write_user_data_to_file(self):
        with open('user_data.txt', 'w') as file:
            file.write(f"user_name = {self.user_name}\n")
            file.write(f"pin_code = {self.__pin}")

    # Read and extract user data from storage
    def read_user_data_from_file(self):
        user_name = None
        pin_code = None
        with open('user_data.txt', 'r') as file:
            for line in file:
                if line.startswith('user_name'):
                    user_name = line.split('=')[1].strip()
                elif line.startswith('pin_code'):
                    pin_code = line.split('=')[1].strip()
        return user_name, pin_code

    # Function to change class values to user information
    def set_attributes_from_input(self):
        user_name, pin_code = self.get_user_input()
        self.user_name = user_name
        self.__pin = pin_code

    # Pin code check
    def confirm_pin(self):
        while True:
            confirm_pin = input("Please confirm your PIN code: ")
            if confirm_pin == self.__pin:
                print("PIN code confirmed.")
                break
            else:
                print("PIN code does not match. Please try again.")

    def main(self):
        if os.path.isfile('user_data.txt'):
            print("User data file already exists.")
            user_name, pin_code = self.read_user_data_from_file()
            self.user_name = user_name
            self.__pin = pin_code
            self.confirm_pin()
        else:
            print("User data file does not exist.")
            self.set_attributes_from_input()
            self.write_user_data_to_file()
            print("User data has been saved to user_data.txt")


if __name__ == "__main__":
    fridge = Smart_Fridge("", "")
    fridge.main()
    print(fridge)
