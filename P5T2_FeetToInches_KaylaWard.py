# Feet to Inches
# 1 Oct 2018
# CTI-110 P5T2_FeetToInches 
# Kayla Ward
#

# Constant for the number of inches per foot.
inches_per_foot = 12

# Main Function
def main():
    # Get a number of feet from the user.
    feet = int(input("Enter a number of feet: "))

    # Convert that to inches.
    print(feet, "equals", feet_to_inches(feet), "inches.")

# The feet_to_inches function convets feet to inches.
def feet_to_inches(feet):
    return feet * inches_per_foot

# Call the min function.
main()
