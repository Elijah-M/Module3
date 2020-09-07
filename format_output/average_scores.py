"""Author: Elijah Morishita
   elmorishita@dmacc.edu
   9/7/2020
   The Average Scores Program
   """

def names():
    """ gathers frist/last name as a string and returns a string """
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter you last name: ")

    full_name = last_name + "," + first_name + " age:"
    return full_name

def age():
    """ gathers age and returns an int"""
    age = int(input("Please enter your age: "))
    return age

def average():
    """ gathers score input, calculate an average, and returns an float"""
    score1 = float(input("Enter your first test score: "))
    score2 = float(input("Enter your second test score: "))
    score3 = float(input("Enter your third test score: "))

    sum = score1 + score2 + score3
    average_scores = sum / 3

    return average_scores

if __name__ == '__main__':
    print(names(), age(), "average grade:", average())

# the input works well unless you enter a char when gathering
# the score input, it will however accept floats and ints