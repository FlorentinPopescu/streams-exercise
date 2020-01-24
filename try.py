"""
USAGE: `python try.py 123456`
"""

import io
import sys


from stream_exercise import StreamProcessor

value = sys.argv[1]

my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()
print("Processed {} and got {}".format(value, result))

# ----------------------------------------------------------


print("---additional tests---")
values = ["234761640930110349378289194", "03050403020309060707070708",
          "3", "2347", "23478"]

for value in values:
    my_stream_processor = StreamProcessor(io.StringIO(value))
    result = my_stream_processor.process()
    print("Processed {} and got {}".format(value, result))


#=======SAMPLE RUN=========================
# (base) C:\Users\Florentin\Desktop\UW3\L2\streams-exercise-master>python try.py 123456
# reached the end of stream
# Processed 123456 and got 3
# ---additional tests---
# Processed 234761640930110349378289194 and got 5
# Processed 03050403020309060707070708 and got 10
# reached the end of stream
# Processed 3 and got 0
# reached the end of stream
# Processed 2347 and got 2
# reached the end of stream
# Processed 23478 and got 2