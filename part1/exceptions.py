# Reference Article: https://www.python-course.eu/python3_exception_handling.php
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Please enter an integer: "))
            print("The number is read as {}".format(n))
            break
        except ValueError:
            print("The input is not an integer. Try Again!")
