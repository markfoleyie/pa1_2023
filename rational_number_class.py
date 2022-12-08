"""
A simple Rational number class. This demonstrates operator overloading using the 'magic' methods such as '__add__'.
"""


class Rational:
    """
    Implements a simple Rational number. Note that not all possible methods are implemented. Only a sample of the
    'magic' methods which enable operator overloading are implemented.
    """

    def __init__(self, numer, denom=1):
        """
        Initializer method. This sets up the instance variables i.e. those prepended with 'self.'
        In this case we store the numerator & denominator, being the two elements that make up a
        rational number. An integer can be considered a rational in the form of itself over 1,
        hence the default.

        Your classes should always include an initializer method.
        """
        self.numer = numer
        self.denom = denom

    def __str__(self):
        """
        String representation for printing. When print(instance) is called this method is fired.
        Your classes should always have this method.
        """
        return f"{self.numer} / {self.denom}"

    def __repr__(self):
        """
        Representation of Rational number. This is the 'definitive' representation of an instance, usually a
        string representation of the code to make the instance.

        It's also acceptable, at this level, to just make this invoke the __str__ method.

        this method is invoked when you enter the instance name in an interactive editor such as IDLE or
        PyCharm console.

        Your classes should always have this method.
        """
        return f"{self.__class__.__name__}({self.numer}, {self.denom})"

    def __add__(self, f):
        """
        Add two Rationals, __add__ enables the '+' operator, thus overloading it.
        """
        if type(f) == int:
            # Make sure that the second object is a rational, if it's an int then convert it.
            f = Rational(f)
        if type(f) == Rational:
            # find the least common multiple (lcm)
            this_lcm = self.lcm(self.denom, f.denom)
            # multiply to make denominators the same, then add numerators
            this_sum = (this_lcm // self.denom * self.numer) + \
                       (this_lcm // f.denom * f.numer)
            return Rational(this_sum, this_lcm)
        else:
            raise TypeError(f"Invalid type. Cannot add rational and {type(f)}.")

    def __radd__(self, f):
        """
        Add two Rationals (reversed). Mapping is reversed: if "1 + x", x maps to self, and 1 maps to f. We then
        just call __add__ as in 'normal' addition.
        """
        return self.__add__(f)

    def __iadd__(self, i):
        '''
        Increment a rational. Implements rational += i.
        '''
        return self.__add__(i)

    def __sub__(self, f):
        """
        Subtract two Rationals. Subtraction is the same as addition with "+" changed to "-"
        """
        this_lcm = self.lcm(self.denom, f.denom)
        numerator_diff = (this_lcm // self.denom * self.numer) - \
                         (this_lcm // f.denom * f.numer)
        return Rational(numerator_diff, this_lcm)

    def reduce_rational(self, rational):
        """
        Return the reduced fractional value. Find the geatest common divisor (gcd) and then divide
        numerator and denominator by gcd.
        """
        this_gcd = self.gcd(rational.numer, rational.denom)
        return Rational(rational.numer // this_gcd, rational.denom // this_gcd)

    def __eq__(self, f):
        """
        Compare two Rationals for equality. Reduce both; then check that numerators and denominators are equal

        """
        f1 = self.reduce_rational(self)
        f2 = f.reduce_rational(f)
        return f1.numer == f2.numer and f1.denom == f2.denom

    @staticmethod
    def gcd(a, b):
        """
        Greatest common divisor. This is a utility method to calculate GCD of any rational number, so as such,
        it doesn't need to be in the class at all. It could be implemented as a function outside the class.
        However, it's convenient to store it in the class but it doesn't neet 'self'. We call this type of method a
        static method. We haven't covered these yet so don't worry if you don't understand the concept.
        """

        # Ensure that a > b, if it is not reverse a & b
        if not a > b:
            a, b = b, a

        print(f"Initial fraction is {a}/{b}")
        while b != 0:
            rem = a % b
            a, b = b, rem
            print(f"... {a}/{b}")

        print(f"GCD is {a}")
        return a

    @classmethod
    def lcm(cls, a, b):
        """
        Least common multiple (LCM). Also a utility method implemented as a 'class' method. It could be a static
        nethod but as it calls the gcd method it needs to know its own class. Note that, instead of 'self', we
        use 'cls'. Again, don't worry about not understanding this concept yet.
        """
        print(f"LCM is {a * b // cls.gcd(a, b)}")
        return (a * b // cls.gcd(a, b))


if __name__ == "__main__":
    rat1 = Rational(1, 2)
    rat2 = Rational(3, 4)
    rat6 = Rational(6, 8)
    rat3 = rat1 + rat2
    rat4 = rat1.__add__(rat2)
    rat5 = Rational.__add__(rat1, rat2)
    rat7 = rat2 - rat2


    print(rat1)
    print(rat2)

    print(f"{rat2} == {rat6} is {rat2 == rat6}")

    # Deliberate error
    rat8 = rat1 + 3.14
