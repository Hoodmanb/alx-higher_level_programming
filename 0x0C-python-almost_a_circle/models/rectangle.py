class Base:
    """
    A class to manage all id attributes in
    other classes to avoid duplicating the
    same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        A constructor that takes two parameters id and self.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """
    Rectangle class that calculates the area of a rectangle.
    """

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter method (decorator)"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter method (decorator)"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter method (decorator)"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter method (decorator)"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter method (decorator)"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter method (decorator)"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter method (decorator)"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter method (decorator)"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """calculate the area of a rectangle and returns an int"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character."""
        for sy in range(self.y):
            print("")
        for h in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width, end="")
            print('')

    def update(self, *args, **kwargs):
        """a function that update the attributes
        through *args or **kwargs"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }


