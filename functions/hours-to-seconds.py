# Write a function total_seconds that takes three parameters hours, minutes and seconds
# and returns the total number of seconds for hours hours, minutes minutes and seconds seconds

# Hours, minutes, and seconds to seconds conversion formula
def total_seconds(hours, minutes, seconds):
    return (hours * 60 + minutes) * 60 + seconds

# Tests
def test(hours, minutes, seconds):
    print str(hours) + " hours, " + str(minutes) + " minutes, and",
    print str(seconds) + " seconds totals to",
    print str(total_seconds(hours, minutes, seconds)) + " seconds."

# Output
test(7, 21, 37)
test(10, 1, 7)
test(1, 0, 1)