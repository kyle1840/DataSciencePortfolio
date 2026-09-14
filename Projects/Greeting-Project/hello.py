# My first Python project in GitHub

def greet_user():
  name = input("Enter your name: ")
  interest = input("What area of Data Science interests you? ")
  experience = input("Have you used Python before? ").lower()
  
  print(f"Hello, {name}! Welcome to Data Science.")
  print(f"It's great that you're interested in {interest}.")

if experience == "yes":
  print("Nice! You already have some Python experience.")
else:
  print("That's okay! Python is a great language to start with.")

if __name__ == "__main__":
  greet_user()
