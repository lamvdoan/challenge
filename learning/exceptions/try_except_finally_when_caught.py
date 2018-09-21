"""
Catching multiple exceptions and handling them separately.  Exception caught.
"""

print "Starting the code"

try:
    raise IOError("Exception caught")
except ValueError as error:
    print("ValueError - Caught this error: " + repr(error))
except IOError as error:
    print("IOError - Caught this error: " + repr(error))
finally:
    print("Print this at the end")

print
print "Executing this line"
