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
        string=input(msg)
    except EOFError:
        string = input("***Oops, something went wrong! Try again: ")
    except KeyboardInterrupt:
        string = input("***Oops, something went wrong! Try again: ")
    return string

username = get_string_from_user("Please enter a username: ")
user_location = get_string_from_user("Where are you from? ")
print("Hello, {}. How is the weather in {}?".format(username, user_location))



