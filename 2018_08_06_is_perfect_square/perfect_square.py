"""Initial solution to is_perfect_square exercise

08/06/2018
"""

import cmath
import math
import numbers

from decimal import Decimal, getcontext


PRECISION = 100


# The type 'complex' is getting clobbered by the keyword argument
# 'complex', so the type is being passed in as keyword argument
# 'complex_type' ... meh
def is_perfect_square(x, complex_type=complex, complex=False):
    if not isinstance(x, numbers.Number):
        raise TypeError("{} is not a numeric value".format(x))
    elif isinstance(x, complex_type) and complex is False:
        raise TypeError("x cannot be complex number if 'complex' "
                        "keyword argument is False")

    if not isinstance(x, complex_type) and x < 0 and complex is False:
        return False
    elif isinstance(x, complex_type) or x < 0:
        root = cmath.sqrt(x)
        return root.real.is_integer() and root.imag.is_integer()
    else:
        getcontext().prec = 100
        root = Decimal(x).sqrt()
        return root == int(root)
