class Rectangle(object):
    """
    A class representing a rectangle
    """

    def __init__(self):
        '''
        Initialize the rectangle dimensions
        :return: None
        '''
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
    rect1 = Rectangle()
    rect1.width = float(input("Enter a width: "))
    rect1.height = float(input("Enter a height: "))

    rect2 = Rectangle()
    rect2.width = float(input("Enter a width: "))
    rect2.height = float(input("Enter a height: "))

    rect3 = Rectangle()
    rect3.width = float(input("Enter a width: "))
    rect3.height = float(input("Enter a height: "))

    print("The area of the rectangle is", get_area(rect1))
    print("The area of the rectangle is", get_area(rect2))
    print("The area of the rectangle is", get_area(rect3))

main()

