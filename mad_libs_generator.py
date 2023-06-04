# Take information from user and fit it into story

name = input("What is your name? ").title()
city = input("What is your favorite city? ").title()
animal = input("What is your favorite animal? ")
place = input ("What's your favorite hiding place? ")
activity = input("What is your favorite activity? ")
mood = input ("What is your mood? ")
with_who = input ("Who is the most annoying celebrity? ").title()
punish = input ("What is your favorite punishment tool? ")


story = (f"\nI'am {name}. I'am living in {city} with {with_who}. It really feels {mood}. "
         f"\nI lost my {animal} today while doing {activity}. I called {with_who} "
         f"and {with_who} said that kidnapped my {animal} because was hungry "
         f"and was going to eat my {animal}. \nI caught {with_who} at {place}. "
         f"I decided to punish {with_who} with {punish} and I saved my {animal}.")

print (story)
