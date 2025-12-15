import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="Clients",   # replace with your database name
    user="postgres",       # replace with your PostgreSQL username
    password="Uhirwashami54."    # replace with your password
)

mycursor = conn.cursor()
mycursor.execute("CREATE TABLE Melissa (names varchar(255), school varchar(255),age int,location varchar(255))")
conn.commit()
print("Welcome to Java quiz")
score=0

# Question 1
print("Question 1: What is the default value of a boolean variable in Java?")
print("a) true")
print("b) false")
print("c) 0")
print("d) null")
print("Enter your answer:")
answer1 = input()
if answer1.lower() == "b":
    score += 1
else:
    print("The answer was incorrect")
    print("The correct answer was b")

# Question 2
print("\nQuestion 2: Which of the following is used to print output in Java?")
print("a) System.in.println(\"Hello\")")
print("b) System.out.println(\"Hello\")")
print("c) Print.out(\"Hello\")")
print("d) Console.print(\"Hello\")")
print("Enter your answer:")
answer2 = input()
if answer2.lower() == "b":
    score += 1
else:
    print("The answer was incorrect")
    print("The correct answer was b")

# Question 3
print("\nQuestion 3: Which data type would you use to store a single character in Java?")
print("a) String")
print("b) char")
print("c) int")
print("d) boolean")
print("Enter your answer:")
answer3 = input()
if answer3.lower() == "b":
    score += 1
else:
    print("The answer was incorrect")
    print("The correct answer was b")

# Question 4
print("\nQuestion 4: What is the correct syntax to start the main method in Java?")
print("a) public static void main(String args[])")
print("b) public void main(String[] args)")
print("c) main(String args[])")
print("d) static public main(String args[])")
print("Enter your answer:")
answer4 = input()
if answer4.lower() == "a":
    score += 1
else:
    print("The answer was incorrect")
    print("The correct answer was a")

# Question 5
print("\nQuestion 5: Which of the following is NOT a valid Java identifier?")
print("a) myVariable")
print("b) 2ndVariable")
print("c) _variable")
print("d) variable123")
print("Enter your answer:")
answer5 = input()
if answer5.lower() == "b":
    score += 1
else:
    print("The answer was incorrect")
    print("The correct answer was b")

# Final score
print("Your total score is:",score)