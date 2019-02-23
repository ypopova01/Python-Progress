def get_user_data():
    '''retrieves user data from the command line
    Returns:
    [dictionary] of the form:
      {
        "name" : "user_name",
        "height": "user heigth in meters",
        "weight": "user weight in kilograms"'''

    def get_string_from_user(msg):
        """
            Summary:
              Asks the user to enter a string and
              - if any error occurs => print:
                "***Oops, something went wrong! Try again!" and ask again

              Returns the user input, as string, when no errors occurred.

            Usage:
              user_input = get_string_from_user("enter a user name: ")

            Arguments:
              msg {[string]} -- [the string to be displayed to the user,]

            Returns:
              [string] -- [the string entered from user]
          """
        try:
            name = input(msg)
        except EOFError:
            name = input("***Oops, something went wrong! Try again: ")
        except KeyboardInterrupt:
            name  = input("***Oops, something went wrong! Try again: ")
        return name



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

  #  user_height = get_float_from_user("Please share how tall you are in cm: ")



  #  user_height = get_float_from_user("Please share how tall you are in cm: ")
   # user_weight = get_float_from_user("Please enter your weight in kilos: ")
    #print(
     #   "Thank you for sharing that your height is {} cm and your weight is {} kilos!".format(user_height, user_weight))
    #user_weight = get_float_from_user("Please enter your weight in kilos: ")
    #print(
     #   "Thank you for sharing that your height is {} cm and your weight is {} kilos!".format(user_height, user_weight))

    name = get_string_from_user("Please enter a username: ")
    height = get_float_from_user("How tall are you? ")
    weight = get_float_from_user("Please enter your weight in kilos: ")
    return {"name": name,
                  "height": height,
                  "weight": weight
                  }

def validate_name(name):
    if len(name) >= 2:
        return name
    else:
        name = input("Please enter a valid username: ")
        return name

def validate_height(height):
    if 0.5 <= height <= 2.5:
        return height
    else:
        height = float(input("Please enter a valid height: "))
        return height

def validate_weight(weight):
    if weight in range(5,301):
        return weight
    else:
        weight = float(input("Please enter a valid weight: "))
        return weight

def calc_BMI(weight,height):
    """calculates the BMI

    Arguments:
    w {[float]} -- [weight]
    h {[float]} -- [height]

    Returns:
    [float] -- [calculated BMI = w / (h*h)]
      """
    calculated_BMI = weight/(height*height)
    return calculated_BMI



def calc_BMI_category(calculated_BMI):
  """Calculates the BMI category

  Arguments:
    BMI {[float]} -- [the bmi number index]

  Returns:
    [string] -- [bmi category]
  """
  if calculated_BMI <= 18.5:
      return "Underweight"
  elif 18.5 < calculated_BMI <= 24.9:
      return "Normal"
  elif 25 <= calculated_BMI <= 29.9:
      return "Overweight"
  else:  # BMI >= 30
      return "Obesity"


def print_results(bmi_category):
  """[Prints the BMI category to the user ]

  Arguments:
    bmi_category {[string]} -- []
  """
  print("Thanks for sharing details, {}.Your BMI category is {}".format(valid_name,bmi_category))

def cm_to_meters(cm):
  """converts centimetres to meters

  Arguments:
    cm {[int]}

  Returns:
    [float]
  """
  pass


