"""
Avoid raising generic Exceptions.  To catch it, you'll have to catch all other more specific exceptions that subclass it
"""

print "Starting the code"

try:
    raise ValueError("Represents a hidden bug, do not catch this")
except Exception as error:
    print("Caught this error: " + repr(error))

print
print "Executing this line"
