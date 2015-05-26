#!/usr/bin/env python
"""Helps to deprecate your old code."""
from functools import wraps
import warnings

warnings.simplefilter('always', DeprecationWarning)


def deprecate(replacement=None):
    """Prints a deprecation warning when a function is called.

    Argument:
      replacement (str): The func which replaces the deprecated func.

    Usage:
      >>> from deprecator import deprecate
      >>> @deprecate(replacement=bar)
      >>> def foo():
      >>>     print "hello"
      >>> foo()
      DeprecationWarning: foo is deprecated; use bar instead.
      hello
    """
    def outer(fun):
        msg = "{} is deprecated".format(fun.__name__)
        if replacement is not None:
            msg += "; use {} instead.".format(replacement.__name__)
        if fun.__doc__ is None:
            fun.__doc__ = msg

        @wraps(fun)
        def inner(*args, **kwargs):
            warnings.warn(msg, category=DeprecationWarning, stacklevel=2)
            return fun(*args, **kwargs)
        return inner
    return outer


if __name__ == "__main__":
    print((deprecate.__doc__))
