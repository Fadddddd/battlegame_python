def Seattle():
    dogs = 1000
    print("Seattle has", dogs, "dogs")


def Bellevue():
    dogs = 2000
    print("Bellevue has", dogs, "dogs")


my_string = "set in global scope"


def main():
    global my_string
    my_string = "set in local scope"


main()
print(my_string)


def a_function(callback):
    print(callback(3))


a_function(lambda num: num**2)
