#CHAPTER 1

#x = 15
#price = 9.99

#discount = 0.2

#result = price * (1-discount)

#print(result)


#CHAPTER 2

#name = "Rolf"

#print(name)

#print(name * 2)

#a = 25

#b = a 

#print(a)
#print(b)

#b = 17

#print(a)
#print(b)


#CHAPTER 3

#name = "Bob"
#greeting = f"Hello, {name}"

#print(greeting)

#name = "Bob"
#greeting = "Hello,{}"
#with_name = greeting.format(name)
#with_name_two = greeting.format("Rolf")

#print(with_name)
#print(with_name_two)

#size_input = input("How big is your house (in square feet):")
#square_feet = int(size_input)
#square_meters = square_feet /10.8
#print(square_meters)


#CHAPTER 5

#user_age = input("Enter your age:")
#years = int(user_age)
#months = years * 12
#print(f"Your age, {years}, is equal to {months} months.")

#l = ["Bob", "Rolf", "Anne"]
#t = ("Bob", "Rolf", "Anne")
#s = {"Bob", "Rolf", "Anne"}

#print(l[0])
#print(t[0])

#l[0] = "Smith"

#print(l)
#print(t)


#CHAPTER 6

#l.append("Jen")
#print(l)

#s.add("Jen")
#print(s)


#CHAPTER 7

#s.add("Bob")
#print(s)

#friends = {"Bob", "Rolf", "Anne"}
#abroad = {"Bob", "Anne"}


#CHAPTER 8

#local = friends.difference(abroad)
#print(local)

#print(abroad.difference(friends)) 


#local = {"Rolf"}
#abroad = {"Bob", "Anne"}


#friends = local.union(abroad)
#print(friends)

#art = {"Bob", "Jen", "Rolf", "Charlie"}
#science = {"Bob", "Jen", "Adam", "Anne"}

#both = art.intersection(science)
#print(both)

#print(5 == 5)
#print(5 > 5)
#print(10 != 10)

#friends = ["Rolf", "Bob"]
#abroad = ["Rolf", "Bob"]

#print(friends == abroad)
#print(friends is abroad)



#day_of_week = input("What day of the week is it today? ")

#if day_of_week == "Monday":
    #print("Have a great start to your week!")
#elif day_of_week == "Friday":
    #print("It's ok to finish a bit early!")
#else:
   # print("Full speed ahead!")

#day_of_week = input("What day of the week is it today? ").lower()

#if day_of_week == "monday":
    #print("Have a great start to your week!")
#elif day_of_week == "friday":
    #print("It's ok to finish a bit early!")
#else:
    #print("Full speed ahead!")



#friends = ["Rolf", "Bob", "Jen"]
#print("Jen" in friends)

#movies_watched = {"The Gentlemen", "Grinch", "Transformers"}
#user_movie = input("Enter something you've watched recently: ")

#print(user_movie in movies_watched)




#movies_watched = {"The Gentlemen", "Transformers", "Grinch"}
#user_movie = input("Enter something you've watched recently: ")

#if user_movie in movies_watched:
   # print(f"I've watched {user_movie} too!")
#else:
    #print("I haven't watched that yet.")


#number = 7
#user_input = input("Enter 'y' if you would like to play: ")

#if user_input in ("y", "Y"):
    #user_number = int(input("Guess our number: "))
    #if user_number == number:
        #print("You guessed correctly!")
    #elif number - user_number in (1, -1):
        #print("You were off by 1.")
   # else:
        #print("Sorry, it's wrong!")


#number = 5
#user_input = input("Enter 'y' if you would like to play: ")

#if user_input.lower() == "y":
   # user_number = int(input("Guess our number: "))
    #if user_number == number:
       # print("You guessed correctly!")
    #elif abs(number - user_number) == 1:
        #print("You were off by 1.")
    #else:
       # print("Sorry, it's wrong!")


#CHAPTER 13

#number = 5
#play = input("Would you like to play? (Y/n) ")

#while play != "n":
    #user_number = int(input("Guess our number: "))
    #if user_number == number:
       #print("You guessed correctly!")
    #elif abs(number - user_number) == 1:
       # print("You were off by 1.")
   #else:
        #print("Sorry, it's wrong!")

    #play = input("Would you like to play? (Y/n) ")


#while True:
    #play = input("Would you like to play? (Y/n) ")

    #if play == "n":
       #break

    #user_number = int(input("Guess our number: "))
    #if user_number == number:
        #print("You guessed correctly!")
    #elif abs(number - user_number) == 1:
        #print("You were off by 1.")
    #else:
        #print("Sorry, it's wrong!")


#friends = ["Rolf", "Jen", "Bob", "Anne"]
#for friend in friends:
    #print(f"{friend} is my friend.")


#grades = [35, 67, 98, 100, 100]
#total = 0
#amount = len(grades)

#for grade in grades:
    #total += grade

#print(total / amount)

#grades = [35, 67, 98, 100, 100]
#total = sum(grades)
#amount = len(grades)

#print(total / amount)


#Chapter 14 - FOR loops

#numbers = [1, 3, 5]
#doubled = [x * 2 for x in numbers]

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)
print(friends)


#CHAPTER 15 - Dictionaries

#friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

#friend_ages["Bob"] = 20

#print(friend_ages)


#friends = [
   # {"name": "Rolf", "age": 24},
    #{"name": "Adam", "age": 30},
    #{"name": "Anne", "age": 27},
#]

#print(friends[1]["name"])


#CHAPTER 16 - variables

#t = 5, 11
#x, y = t

#print(x, y)


#people = [("Bob", 42, "Mecanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

#for name, age, profession in people:
    #print(f"Name:{name}, Age: {age}, Profession: {profession}")


#CHAPTER 17 - FUNCTIONS

#def hello():
    #print("HELLO!")

#hello()


#CHAPTER 18 - Function Arguments

#def add(x, y):
    #result = x + y
    #print(result)

#add(5, 3)

#CHAPTER 21 LAMBDA-FUNCTION

#add = lambda x, y: x + y

#print(add(5, 7))

#def double(x):
    #return x * 2

#sequence = [1, 3, 5, 9]
#doubled = list(map(lambda x: x * 2, sequence))