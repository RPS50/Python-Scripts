# build a basic whiteboard app using Python and Tkinter.
#  will open a modal to select RGB color combinations
import tkinter as tk
from tkinter.colorchooser import askcolor

# then we create a function to start drawing

def start_drawing(event):  # This line defines a function named start_drawing that takes an event as its parameter. In GUI programming, events are actions or occurrences (like mouse clicks, key presses and so on) that trigger specific functions when they happen.
    global is_drawing, prev_x, prev_y # This line declares that the variables is_drawing, prev_x, and prev_y are global variables. In Python, global variables are accessible from anywhere in the code and can be modified within functions. This line ensures that these variables are accessible within the function.
    is_drawing = True  # This line sets the is_drawing variable to True. This variable is typically used to indicate whether a drawing action is in progress. By setting it to True, the function signals that a drawing action has started.
    prev_x, prev_y = event.x, event.y # This line captures the current coordinates of the mouse cursor when the start_drawing function is called. It assigns the x and y coordinates of the mouse cursor at that moment to the prev_x and prev_y variables. These variables are used to track the starting point of the drawing action.

def draw(event):    # A drawing is essentially a combination of points filled with colors, functioning as a vector. To work as a vector, it needs to have a starting and ending point. 
    global is_drawing, prev_x, prev_y
    if is_drawing:
        current_x, current_y = event.x, event.y
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill=drawing_color, width=line_width, capstyle=tk.ROUND, smooth=True)
        prev_x, prev_y = current_x, current_y
       
# after creating a function to start drawing, I need a function to stop drawing
def stop_drawing(event):
    global is_drawing
    is_drawing = False

#   Now that I have the primary drawing functionality, the next step is to implement the color-changing function. This is a simple function that calls the askcolor module, which is already part of Tkinter.
def change_pen_color():
    global drawing_color
    color = askcolor()[1]
    if color:
        drawing_color = color

#   Then I need a function to adjust the line width, allowing me to choose the thickness of my lines. 

def change_line_width(value):
    global line_width
    line_width = int(value)

""" Not done yet!  I need some other stuff:
A title for the app.
A white blank canvas for drawing.
A frame to hold the controls of the app in the same line.
A color button.
A clear canvas button to erase all the work and start drawing again.
A slider to select the line width.
"""
# I'm going to start by creating a window with a title and a white canvas:
root = tk.Tk()  #   This line creates the main application window. It initializes a Tkinter application and assigns it to the variable root. This window serves as the container for all the graphical elements of the whiteboard application.
root.title("Whiteboard App")    #    This sets the title of the application window to "Whiteboard App." The title appears in the title bar of the window and provides a name for the application.

canvas = tk.Canvas(root, bg="white")    #   This line creates a drawing canvas within the main application window. The canvas is a white rectangular area where users can draw. It is initialized with a white background color. The canvas is assigned to the variable canvas.
canvas.pack(fill="both", expand=True)   #   This configures the canvas to fill both the horizontal and vertical space of the application window. It allows the canvas to expand and occupy the entire window.

is_drawing = False  #   This initializes a variable is_drawing to False. It's typically used to track whether the user is currently drawing or not. When the user starts drawing, this variable is set to True to indicate an ongoing drawing action.
drawing_color = "black" #   This initializes a variable drawing_color to "black." It specifies the color that will be used for drawing on the canvas. Change this color as needed to draw with different colors with the functions (still to be written)
line_width = 2  #   This initializes a variable line_width to 2. It specifies the width of the lines or strokes used for drawing. You can adjust this value to change the thickness of the lines.

root.geometry("800x600")    #   This sets the initial size of the application window to 800 pixels in width and 600 pixels in height. It defines the dimensions of the window when it is first displayed but you can resize your window and with it, your canvas space.

# create a frame to hold the buttons or controls in the same line. This is the most comfortable way to have buttons, and it's kind of a navbar.

controls_frame = tk.Frame(root)
controls_frame.pack(side="top", fill="x")

#  create two buttons and give them default fixed position
color_button = tk.Button(controls_frame, text="Change Color", command=change_pen_color)
clear_button = tk.Button(controls_frame, text="Clear Canvas", command=lambda: canvas.delete("all"))

color_button.pack(side="left", padx=5, pady=5)  #   padx=5: It adds horizontal padding of 5 pixels around the label, creating some spacing. 
clear_button.pack(side="left", padx=5, pady=5)  # pady=5: It adds vertical padding of 5 pixels around the label, creating spacing.

# The last control i need to create is a slider for the line width function
line_width_label = tk.Label(controls_frame, text="Line Width:") #   This line creates a label widget with the text "Line Width." The label is intended to display text to describe the purpose of the following slider (which controls the line width). It is placed within the controls_frame widget.
line_width_label.pack(side="left", padx=5, pady=5)  #   This line configures the label's placement within the controls_frame.

line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient="horizontal", command=lambda val: change_line_width(val))   #   This line creates a horizontal slider widget (Scale widget) that allows the user to select a line width. The slider ranges from a minimum value of 1 (from_=1) to a maximum value of 10 (to=10). The command option is set to call the change_line_width function with the selected value whenever the slider position changes.
line_width_slider.set(line_width)   #  This sets the initial position of the slider to the value stored in the line_width variable, which is initialized earlier in the code. This ensures that the slider starts at the default line width. 
line_width_slider.pack(side="left", padx=5, pady=5) # This line configures the slider's placement within the controls_frame. It is placed on the left side, and padding is added to create spacing around the slider.

#   I still need to bind or "link" the functions i coded at the beginning with the buttons and controls 

canvas.bind("<Button-1>", start_drawing)    #   When the left mouse button is clicked on the canvas, it triggers the start_drawing function.
canvas.bind("<B1-Motion>", draw)    #   While the left mouse button is held down and the mouse is moved on the canvas, it triggers the draw function.
canvas.bind("<ButtonRelease-1>", stop_drawing)  #   When the left mouse button is released (button released event), it triggers the stop_drawing function.

root.mainloop() #   starts the main loop of the application, allowing it to respond to user interactions and events.