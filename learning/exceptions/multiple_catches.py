"""
Catching multiple exceptions and handling them separately
"""

print "Starting the code"

try:
    raise IOError("This is the exception you expect to handle")
except ValueError as error:
    print("ValueError - Caught this error: " + repr(error))
except IOError as error:
    print("IOError - Caught this error: " + repr(error))
except SystemExit as error:
    print("SystemExit - Caught this error: " + repr(error))

print
print "Executing this line"
