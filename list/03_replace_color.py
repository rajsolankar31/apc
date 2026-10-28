# Program 3: Create a list of colors. Replace the third color with user input and display

colors = ["Red", "Blue", "Green", "Yellow", "Purple"]
print("Original list:", colors)
new_color = input("Enter a new color to replace the third color: ")
colors[2] = new_color
print("Updated list:", colors)
