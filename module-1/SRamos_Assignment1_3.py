# Stephanie Ramos
# June 1, 2025
# Module 1.3 Assignment
# On the Wall + Flowchart

# The purpose of this code is to count down bottles of beer from a user input
# and display the sing lyrics.

def song(bottles):
    if bottles <= 0:
        print ("No bottles of beer on the wall. Time to buy more beer.")
        return

    # Countdown loop
    while bottles >1:
      print (f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
      bottles -=1
      if bottles == 1:
          print("Take one down and pass it around, 1 bottle of beer on the wall. \n")
      else:
          print(f"Take one down and pass it around, {bottles} bottles of beer on the wall.\n")

    # Final bottle
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print(" Take one down and pass it around, no more bottles of beer on the wall.\n")
    print("Time to buy more bottles of beer.")

def main():
    try:
        bottles = int(input("Enter number of bottles: "))
        song(bottles)
    except ValueError:
        print("Please enter a valid number.")

# Run program
if __name__ == "__main__":
    main()
