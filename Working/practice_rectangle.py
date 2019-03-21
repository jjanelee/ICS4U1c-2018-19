# https://github.com/StRobertCHSCS/ICS4U1c-2018-19/blob/master/Masters/OOP/practice_rectangle.md

class Rectangle():
    '''
    A class modelling width and height
    '''

    def __init__(self):
        self.width = 0
        self.height = 0


def get_area(rec):
    """
    Computes the area of a rectangle
    :param rec: a Rectangle object
    :return: area of rec
    """
    area = rec.width * rec.height
    return area


def main():
    # create an instance of a rectangle

    user_width = float(input("Enter a width: "))
    user_height = float(input("Enter a height: "))

    rect1 = Rectangle()
    rect1.width = user_width
    rect1.height = user_height

    print("The area of the rectangle is", get_area(rect1))

main()