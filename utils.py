# utils.py
def validate_input(prompt, validation_function):
   while True:
       try:
           value = input(prompt)
           if validation_function(value):
               return value
           else:
               print("Invalid input. Please try again.")
       except ValueError:
           print("Invalid input. Please enter a valid value.")
def convert_to_number(value):
    try:
        return float(value)
    except ValueError:
        return None
