def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a number. It's a string")


input1 = input("Enter your Age ")
check_user_input(input1)

input2 = input("Enter any number ")
check_user_input(input2)

input2 = input("Enter the last number ")
check_user_input(input2)
