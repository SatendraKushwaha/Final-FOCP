#program to create email.
import sys
import random

#function to create email.
def create_email(id , name):
  # Split the names
  parts = name.split(",")
  surname = parts[0]
  forenames = parts[1]
  
  # Removes any non-alphabetic letter characters from the suname.
  surname = ''.join([c.lower() for c in surname if c.isalpha()])
  
  # splits the initials of forenames.
  initials = ".".join([f[0].lower() for f in forenames.split()])
  
  # Creates random four digits.
  digits = "".join([str(random.randint(0, 9)) for _ in range(4)])
  
  # Concatenates to create a email.
  email = f"{initials}.{surname}{digits}@poppleton.ac.uk"

  return email

# Check if a file name was provided as a command-line argument.
if (len(sys.argv)) < 2:
  print("Error: Missing command-line argument.")
  sys.exit()

# Trying to open file if exists.
try:
  with open(sys.argv[1], "r") as f:
    # Reads a file line by line.
     for line in f:
      # Splits a line into id and name and strip() removes unwanted spaces.
      id=line.strip().split()[0]
      name = line.strip()[1:]
      # Creating an email
      email = create_email(id, name)
      
      # print the results to the output file "emails.txt"
      with open("emails.txt", "a") as out:
        out.write(f"{id} {email}\n").as_integer_ratio
except IOError:
  print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.")
