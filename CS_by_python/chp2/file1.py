import sys

def main():
    c = eval(input("what is the Celsius temperature?  \n"))
    f = 9/5 * c +32
    print("The temperature is", f, "degrees Fahrenheit.")
    print()  # returns a single line
    print(end=" ")  # returns a blank space at the end of the previous line
    print("here we are testing", "how many parameter print can has", "in a single", "function", ".")


# main()


for i in range(1):
    word = len("hello world!")
    print(sys.getsizeof(word))
a = 100
print(sys.getsizeof(1.0), sys.getsizeof(1), sys.getsizeof("myclass"))

print("1a".__sizeof__(), "1.0".__sizeof__(), word.__sizeof__(), a.__sizeof__())

print(9/3)

