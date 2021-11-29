import turtle


class Particle:
    """
    An elementary particle made to be a super class to more specific compounds such as
    carbon dioxide and methane.
    """
    def __init__(self, name, color='black'):
        # Global Turtle Config
        self.name = name
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.resizemode('user')
        self.turtle.shape('circle')
        self.turtle.shapesize(0.25, 0.25)

        # Turtle Specific Config
        if self.name == 'CO2':
            self.turtle.color('grey')
        elif self.name == 'methane' or self.name == 'chemical symbol for methane':
            self.turtle.color('green')

    def move(self):
        self.turtle.showturtle()
        self.turtle.fd(50)

