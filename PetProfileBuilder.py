class Pet:
    print("🐾 Welcome to the Pet Profile Builder! 🐾")

pet_object = Pet()

class PetProfile:

    category = "🐾 Pet"

    def __init__(self, name, animal_type, age, favourite_food, personality):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favourite_food = favourite_food
        self.personality = personality

    def introduce(self):
        print("\n" + "🌸" * 25)
        print("       🐾 PET PROFILE 🐾")

        print(f"💖 Name: {self.name}")
        print(f"🐶 Animal: {self.animal_type}")
        print(f"🎂 Age: {self.age} years old")
        print(f"🍖 Favourite food: {self.favourite_food}")
        print(f"✨ Personality: {self.personality}")
        print(f"🏷️ Category: {self.category}")

        print("\n💬 Meet {0}! {0} is a {1} who loves {2}!".format(
            self.name, self.animal_type, self.favourite_food
        ))


pet1 = PetProfile(
"Rio",
"Dog",
4,
"Biscuits",
"Energetic"
)

pet2 = PetProfile(
"Milo",
"Cat",
3,
"Fish",
"Sleepy"
)

pet3 = PetProfile(
"Luna",
"Rabbit",
2,
"Carrots",
"Sweet"
)

pet1.introduce()
pet2.introduce()
pet3.introduce()


print("\n🏷️ CLASS ATTRIBUTE")
print("{} belongs to the {} category.".format(pet1.name, pet1.category))
print("{} also belongs to the {} category.".format(pet2.name, pet2.category))

print("\n💕 QUICK PET FACTS")

print("{} is a {} and is {} years old.".format(
pet1.name, pet1.animal_type, pet1.age
))
print("{}'s favourite food is {}.".format(
pet1.name, pet1.favourite_food
))

print("{} is a {} and is {} years old.".format(
pet2.name, pet2.animal_type, pet2.age
))
print("{}'s favourite food is {}.".format(
pet2.name, pet2.favourite_food
))

print("{} is a {} and is {} years old.".format(
pet3.name, pet3.animal_type, pet3.age
))
print("{}'s favourite food is {}.".format(
pet3.name, pet3.favourite_food
))

print("\n⭐ CHOOSE YOUR FAVOURITE PET ⭐")

print("1. 🐶 Buddy")
print("2. 🐱 Milo")
print("3. 🐰 Luna")

choice = input("\nWhich pet is your favourite? (1, 2, or 3): ")

if choice == "1":
    favourite_pet = pet1
elif choice == "2":
    favourite_pet = pet2
elif choice == "3":
    favourite_pet = pet3
else:
    favourite_pet = None
    print("❌ Please choose 1, 2, or 3!")

if favourite_pet:
    print("\n💖 Awww! Your favourite pet is {}! 🐾".format(favourite_pet.name))
    print("{} is a {} who is {}.".format(favourite_pet.name, favourite_pet.animal_type,favourite_pet.personality))
    print("🍖 Favourite food: {}".format(favourite_pet.favourite_food))
    print("✨ Great choice! {} is soo cute!! 🥰".format(favourite_pet.name))
