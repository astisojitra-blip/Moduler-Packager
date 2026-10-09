from datetime import datetime
import time
import math
import random
import uuid
import string


# ==========================================
# 1.Datetime Operation
# ==========================================

def datetime_operation():

    while True:

        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate the difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            now = datetime.now()

            print("Current Date and Time:", now)
            print("================================")

        elif choice == 2:

            date1 = input("Enter the first date (YYYY-MM-DD): ")
            date2 = input("Enter the second date (YYYY-MM-DD): ")

            date1 = datetime.strptime(date1, "%Y-%m-%d")
            date2 = datetime.strptime(date2, "%Y-%m-%d")

            gap = date2 - date1

            print("Difference:", gap.days, "days")
            print("================================")

        elif choice == 3:

            date = input("Enter the date (YYYY-MM-DD): ")

            date = datetime.strptime(date, "%Y-%m-%d")

            custom_format = date.strftime("%d-%m-%Y")
        
            print("Formatted Date:", custom_format)
            
            print("1. DD/MM/YYYY :", date.strftime("%d/%m/%Y"))
            
            print("4. DD-MMM-YYYY       :", date.strftime("%d-%b-%Y"))
            
            print("5. Day Month, Year   :", date.strftime("%d %B, %Y"))
            
            print("6. Full Day & Date   :", date.strftime("%A, %d %B %Y"))
            
            print("7. Short Day & Date  :", date.strftime("%a, %d %b %Y"))
            print("================================")

        elif choice == 4:

            input("Press Enter to start the stopwatch...")

            start_time = time.time()

            input("Press Enter to stop the stopwatch...")

            end_time = time.time()

            elapsed_time = end_time - start_time

            print("Elapsed Time:", elapsed_time)
            print("================================")

        elif choice == 5:

            seconds = int(input("Enter number of seconds: "))

            while seconds > 0:

                print("Time remaining:", seconds, "seconds")

                time.sleep(1)

                seconds -= 1

            print("Time's up!")

        elif choice == 6:

            print("Back to Main Menu...")
            break

        else:

            print("Invalid choice. Please try again.")


# ==========================================
# 2.Math Operations
# ==========================================

def math_Operation():

    while True:

        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Logarithms calculations")
        print("6. Back to Main Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            num = int(input("Enter a number: "))

            print("Factorial:", math.factorial(num))

            print("================================")

        elif choice == 2:

            p = float(input("Enter Principal amount: "))
            r = float(input("Enter rate of interest (in %): "))
            t = float(input("Enter time (in years): "))

            amount = p * (1 + r / 100) ** t

            ci = amount - p

            print("Total Amount:", amount)
            print("Compound Interest:", ci)

            print("================================")

        elif choice == 3:

            angle = float(input("Enter angle in degrees: "))

            radians = math.radians(angle)

            print("Sin:", math.sin(radians))
            print("Cos:", math.cos(radians))
            print("Tan:", math.tan(radians))

            print("================================")

        elif choice == 4:

            r = float(input("Enter radius: "))
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            circle = math.pi * r * r

            rectangle = length * width

            triangle = 0.5 * base * height

            print("Area of Circle:", circle)
            print("Area of Rectangle:", rectangle)
            print("Area of Triangle:", triangle)

            print("================================")
            
        elif choice == 5:
            num = int(input("Enter number: "))

            print("Logarithm:", math.log(num))

        elif choice == 6:

            print("Back to Main Menu")

            break

        else:

            print("Invalid choice. Please try again.")


# ==========================================
# 3.Random Operations
# ==========================================

def random_Operation():

    while True:

        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            print("Random Number:", random.randint(1, 100))

        elif choice == 2:

            random_list = []

            for i in range(5):

                random_list.append(random.randint(1, 100))

            print("Random List:", random_list)

        elif choice == 3:
            # impoirt string
            length = int(input("Enter password length: "))
            characters =  string.ascii_letters + string.digits + "@#$!"
            
            password = ""

            for i in range(length):
                password += random.choice(characters)

            print("Generated Password:", password)

        elif choice == 4:

            otp = random.randint(100000, 999999)

            print("Generated OTP:", otp)

        elif choice == 5:

            print("Back to Main Menu")

            break

        else:

            print("Invalid choice. Please try again.")


# ==========================================
# 4.UUID Operations
# ==========================================

def uuid_operations():

    print("\nGenerate Unique Identifiers:")

    random_uuid = uuid.uuid4()

    print("Generated UUID:", random_uuid)

    print("=============================")


# ==========================================
# 5.File Operations
# ==========================================
from MyPackage import file_operations
def file_Operations():

    while True:

        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            file_operations.create_file()
        
        elif choice == 2:
            file_operations.write_file()
        
        elif choice == 3:
            file_operations.read_file()
            
        elif choice == 4:
            file_operations.append_file()
            
        elif choice == 5:
            print("Back to Main Menu")
            break
        
        else:
            print("Invalid choice.Please try again!")

        

# ==========================================
# 6.Explore Module Attributes
# ==========================================

def explore_module():

    print("\nExplore Module Attributes:")
    module_name = input("Enter module name to explore: ")
    if module_name == "math":
        print("Available Attributes in math module:")
        print(dir(math))
    
    elif module_name == "random":
            print("Available Attributes in random module:")
            print(dir(random))
        
    elif module_name == "datetime":
            print("Available Attributes in datetime module:")
            print(dir(datetime))
            
    elif module_name == "time":
            print("Available Attributes in time module:")
            print(dir(time))
            
    elif module_name == "uuid":
            print("Available Attributes in uuid module:")
            print(dir(uuid))
            
    elif module_name == "string":
            print("Available Attributes in string module:")
            print(dir(string))
            print("===============================")


# ==========================================
# Main Menu
# ==========================================

def main():

    print("===============================")
    print("Welcome to Multi-Utility Toolkit")
    print("================================")

    while True:

        print("\nChoose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("===============================")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            datetime_operation()

        elif choice == 2:

            math_Operation()

        elif choice == 3:

            random_Operation()

        elif choice == 4:

            uuid_operations()

        elif choice == 5:

            file_Operations()

        elif choice == 6:

            explore_module()

        elif choice == 7:

            print("============================")
            print("Thank you for using the Multi- Utility Toolkit!")
            print("============================")

            break

        else:

            print("Invalid choice. Please try again.")


# ==========================================
# Program Start
# ==========================================

if __name__ == "__main__":

    main()