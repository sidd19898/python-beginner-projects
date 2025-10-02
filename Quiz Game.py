#print question no 1
#ask input(options)
#give conclusion if correct or not
#print question no 2
#ask input(options)
#give conclusion if correct or not


print("Question 1: What is the capital of France?\na) paris\nb) London\nc) Rome")
a = input("your answer: ")
if a == "a":
    print("correct!")
else:
    print("incorrect!")

print("Question 2: What is the largest planet in our solar system?\na) earth\nb) jupiter\nc) Mars")
b = input("your answer: ")
if b == "b":
    print("correct!")
else:
    print("incorrect!")

if a == "a" and b == "b":
    print("your final score 2/2")
elif a != "a" and b == "b":
    print("your final score 2/1")
elif a == "a" and b != "b":
    print("your final score 2/1")
elif a != "a" and b != "b":
    print("your final score 2/0")

