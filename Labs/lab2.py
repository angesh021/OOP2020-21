# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 02-10-2020
# purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: " + message)


        # Enter your own print statements below:
        aa = ("He said “that’s fantastic”!")
        print(aa)

        # print only first and last of the sentence:
        print("First character: " + message[0])
        print("Last character: " + message[-1])

        # use slice notation:
        print("Print up to position 5: " + message[:5])
        print("Print from position 3: " + message[3:])
        print("Print everything via slice: " + message[:])

        # escaping a character:
        print(aa[0:28:2])
        print("He said \“that\’s fantastic\”!")

        # find all a's in the input word and count how many there are:
        print(message.find("a"))
        print(message.count("a"))


        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        message = message.replace('a', '*')
        print(message)


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: " + message)

        # hand the input string to a list and print it out:
        my_list = list(message.split(" "))
        print(my_list)

        # append a new element to the list and print:
        my_list.append("that's all")
        print("Updated List: ", my_list)

        # remove from the list in 3 ways:
        print(my_list.pop())
        #print(my_list.remove("cake"))
        del my_list[-1:-2]
        print(my_list)



        # check if the word cake is in your input list:
        sub_str = "cake"
        print(message.__contains__(sub_str))

        # reverse the items in the list and print:
        my_list.reverse()
        None
        print("The reverse is: ", my_list)


        # reverse the list with the slicing trick:
        my_list[::-1]
        print("Reverse with slicing trick: ", my_list)

        # print the list 3 times by using multiplication:
        print(my_list * 3)


tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()
