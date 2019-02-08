def get_user_data():
    '''retrieves user data from the command line
    Returns:
    [dictionary] of the form:
      {
        "name" : "user_name",
        "height": "user heigth in meters",
        "weight": "user weight in kilograms"'''
    name = input("Please enter username: ")
    height = float(input("Please enter your height in meters: ").replace(",","."))
    weight = float(input("Please enter your weight in kilos: ").replace(",","."))
    return {"name": name,
             "height": height,
             "weight": weight
             }


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
  print(bmi_category)

def cm_to_meters(cm):
  """converts centimetres to meters

  Arguments:
    cm {[int]}

  Returns:
    [float]
  """
  pass

user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = calc_BMI_category(bmi)
print_results(bmi_category)