""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""
    read_file = open(filename)
    read_file_string = read_file.read()
    fruit_names = read_file_string.split('\n')
    return fruit_names

def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """

    # Write your code below.
    fruit_list = []
    for fruit in lst1:
        if fruit in lst2:
            # print fruit
            fruit_list.append(fruit)
    return fruit_list

    


# Call your functions at the bottom, after they've been defined.
print open_and_read_file("fruits_2.txt")
print open_and_read_file("fruits_1.txt")

fruits_1_list = open_and_read_file("fruits_1.txt")
fruits_2_list = open_and_read_file("fruits_2.txt")

print "\ncommon fruits are {}".format(compare(fruits_1_list, fruits_2_list))
# bekka = "awesome"


# def say_something(word):
#     return word

# print say_something("bekka")