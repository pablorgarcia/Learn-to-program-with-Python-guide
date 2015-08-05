# Functions - take an input(s) and return an output
# Examples


# Here are some examples of helpful functions. Feel free to
#   play around with the method calls to compute different
#   values.

# Area of a triangle

def area_of_triangle(base, height):
    return .5 * base * height

print "Triangle:", area_of_triangle(7, 4)
print

# Discriminant of the quadratic formula

def discriminant(a, b, c):
    d = b ** 2
    d -= 4 * a * c
    return d

print "Discriminant:", discriminant(1, 4, 3)
print

# Force

def force(mass, acceleration):
    return mass * acceleration

print "Force:", force(3.4, 9.8)
print

# Number of diagonals in a polygon

def num_diagonals(num_sides):
    ans = num_sides * (num_sides - 3) / 2
    return ans

print "Diagonals:", num_diagonals(7)
print

# Fat cat is Fat :)

def fat_cat(adjective):
    print adjective, "cat is", adjective
    
fat_cat("Fat")
fat_cat("Obvious")
print

# I love comp sci

def loves_cs(name):
    print name, "loves Computer Science!!! <3"

loves_cs("The cat")
loves_cs("The Terminator")
loves_cs("EVERYONE")


