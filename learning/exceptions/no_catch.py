"""
Too specific won't catch the general exception
"""

try:
    raise Exception('general exceptions not caught by specific handling')
except ValueError as e:
    print('we will not catch exception: Exception' + repr(e))

print
print "Executing this line"
