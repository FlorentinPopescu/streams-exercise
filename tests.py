"""
streams-exercise.tests.py

This file is intentionally written without the benefit of the Python
unittest library. This can be used to demonstrate in-class that unit testing
is a simple concept which benefits from the use of a library, but does not
require it.

Run with `python tests.py`. The return code will be the number of test failures.
"""

import io
import sys
from stream_exercise import StreamProcessor


failures = 0


value = "234761640930110349378289194"
expected = 5
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
failures += (not success)
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)


value = "03050403020309060707070708"
expected = 10
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
failures += (not success)
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)


value = "3"
expected = 0
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
failures += (not success)
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)


value = "2347"
expected = 2
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
failures += (not success)
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)


value = "23478"
expected = 2
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
failures += (not success)
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)



print("\n\nTest failures: {} ".format(failures))
sys.exit(failures)


#=======SAMPLE RUN=========================
# (base) C:\Users\Florentin\Desktop\UW3\L2\streams-exercise-master>python tests.py
# Testing "234761640930110349378289194", expected 5 got 5. SUCCESS
# Testing "03050403020309060707070708", expected 10 got 10. SUCCESS
# reached the end of stream
# Testing "3", expected 0 got 0. SUCCESS
# reached the end of stream
# Testing "2347", expected 2 got 2. SUCCESS
# reached the end of stream
# Testing "23478", expected 2 got 2. SUCCESS

# Test failures: 0     