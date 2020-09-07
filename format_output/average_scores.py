def names():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter you last name: ")

    full_name = first_name + " " + last_name
    return full_name

def average():
    score1 = int(input("Enter your first test score: "))
    score2 = int(input("Enter your second test score: "))
    score3 = int(input("Enter your third test score: "))

    sum = score1 + score2 + score3
    ave = sum / 3

    return ave

if __name__ == '__main__':
    print("Excellent", names(), "now...")
    print("Your average test score is", average())