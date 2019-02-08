def get_float_from_user(msg):
    """
       Summary:
         Asks the user to enter a number and
         - if he/she entered no valid python's number value => print:
           "***Enter an number, please!" and ask again.
         - if any other error occurs => print:
           "***Oops, something went wrong! Try again!" and ask again

         Returns the user input, as float, when no errors occurred.

       Usage:
         user_number = get_float_from_user("the message to show to the user")

       Arguments:
         msg {[string]} - - [the message to show to the user]

       Returns:
         [float] - - [the number entered from user, converted to float]
     """
    float_number = 0
    while True:
        try:
            float_number = float(input(msg))
            return float_number
        except ValueError:
          #  float_number = float(input("Enter a number please: "))
            print("oops")


        except EOFError:
            float_number = float(input("***Oops, something went wrong! Try again: "))

        except KeyboardInterrupt:
            float_number = float(input("***Oops, something went wrong! Try again: "))

        # return float_number


user_height = get_float_from_user("Please share how tall you are in cm: ")
user_weight = get_float_from_user("Please enter your weight in kilos: ")
print("Thank you for sharing that your height is {} cm and your weight is {} kilos!".format(user_height,user_weight))