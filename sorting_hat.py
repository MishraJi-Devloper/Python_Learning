print("=====================================================")
print("        Kindly answer the following questions.      ")
print("                    Thank You!!                     ")
print("-----------------------------------------------------")

# Initialize scores
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# Question 1
print("\nQ1) Do you like Dawn or Dusk?")
print("    1) Dawn")
print("    2) Dusk")

q1 = int(input("Your answer (1 or 2): "))

if q1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif q1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")

# Question 2
print("\nQ2) When I’m dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")

q2 = int(input("Your answer (1–4): "))

if q2 == 1:
    hufflepuff += 2
elif q2 == 2:
    slytherin += 2
elif q2 == 3:
    ravenclaw += 2
elif q2 == 4:
    gryffindor += 2
else:
    print("Wrong input.")

# Question 3
print("\nQ3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")

q3 = int(input("Your answer (1–4): "))

if q3 == 1:
    slytherin += 4
elif q3 == 2:
    hufflepuff += 4
elif q3 == 3:
    ravenclaw += 4
elif q3 == 4:
    gryffindor += 4
else:
    print("Wrong input.")

# Final Scores
print("\n================= RESULTS =================")
print(f"🦁 Gryffindor: {gryffindor}")
print(f"🦅 Ravenclaw: {ravenclaw}")
print(f"🦡 Hufflepuff: {hufflepuff}")
print(f"🐍 Slytherin: {slytherin}")

# Determine the house with the most points
max_points = max(gryffindor, ravenclaw, hufflepuff, slytherin)
print("\n🏆 The Sorting Hat has made its decision!")

if gryffindor == max_points:
    print("You belong in 🦁 Gryffindor!")
elif ravenclaw == max_points:
    print("You belong in 🦅 Ravenclaw!")
elif hufflepuff == max_points:
    print("You belong in 🦡 Hufflepuff!")
elif slytherin == max_points:
    print("You belong in 🐍 Slytherin!")
