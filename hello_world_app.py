import tkinter as tk
# tkinter is the standard GUI library for python
# different languages have different libraries for GUI
# but they usually work quite similarly
from tkinter import messagebox
# above we imported the general tkinter library,
# but we did not import any modules
# these large libraries are usually split into modules
# this allows programmers to only import the modules they need
# We are going to import the messagebox module, this creates the popup windows
# we will use this to show the user a message
import subprocess
import sys






# we are going to create a class to represent the application
# this is a good way to organize the code
# we will create a class for the application,
#  and then create an instance of the class
# This allows us to represent abstract ideas into code
# This is usually referred to as object-oriented programming (invented by java pretty much)
# This is called a class, and the instance of the class is called an object
class IhtiramsApp:
    # this is the constructor for the class
    # init is a special method that is called when an object is created
    # self is a reference to the object itself
    # root is the main window of the application
    # we will use this to create the main window
    def __init__(self, root):
        self.root = root
        self.root.title("Made with <3 for Ihtiram")
        self.root.geometry("600x400")
        
        # Center the window
        self.center_window()
        
        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(expand=True)
        
        # Create the Hello World button
        self.hello_button = tk.Button(
            self.button_frame,
            text="Hello World",
            font=("Arial", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="raised",
            padx=20,
            pady=10,
            command=self.show_popup
        )
        
        # Create the Firefox button
        self.firefox_button = tk.Button(
            self.button_frame,
            text="Open Firefox",
            font=("Arial", 14, "bold"),
            bg="#FF6B35",
            fg="white",
            relief="raised",
            padx=20,
            pady=10,
            command=self.open_firefox
        )
        
        # Pack the buttons with some spacing
        self.hello_button.pack(pady=10)
        self.firefox_button.pack(pady=10)
    
    # this is a method for the class
    # it is a function that is associated with the class
    # it is used to center the window
    # we will use this to center the window
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    

    # this is another method for the class object 'IhtiramsApp'
    # it is used to show a popup message
    # I hope you are starting to see the pattern here
    def show_popup(self):
        """Show the Hello World popup message"""
        messagebox.showinfo("hi ihtiram", "Hello World!\nhows it going?")
    
    def open_firefox(self):
        """Open Firefox browser or show error if not installed"""
        try:
            # Try to open Firefox
            # The command varies by operating system
            if sys.platform.startswith('win'):
                # Windows - try multiple possible Firefox locations
                firefox_paths = [
                    'firefox',  # If in PATH
                    r'C:\Program Files\Mozilla Firefox\firefox.exe',
                    r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe',
                    r'%APPDATA%\Mozilla\Firefox\firefox.exe'
                ]
                
                # Expand environment variables
                import os
                firefox_paths = [os.path.expandvars(path) for path in firefox_paths]
                
                # Try each path
                for path in firefox_paths:
                    try:
                        # Use Popen to start Firefox without waiting for it to close
                        subprocess.Popen([path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        return  # Successfully launched
                    except (subprocess.CalledProcessError, FileNotFoundError):
                        continue
                
                # If we get here, none of the paths worked
                raise FileNotFoundError("Firefox not found")
                
            elif sys.platform.startswith('darwin'):
                # macOS
                subprocess.run(['open', '-a', 'Firefox'], check=True)
            else:
                # Linux and other Unix-like systems
                subprocess.run(['firefox'], check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            # If Firefox is not found or fails to start, show angry popup
            messagebox.showerror("Firefox Not Found", "INSTALL FIREFOX >:(")

# this is the main function for the application
# This is what actually runs when you start the application
# we will use it to create the main window and start the application
def main():
    # Create the main window
    # root is an arbritary variable name
    # you could call it mainAppWindow or something like that
    # from the tkinter library we imported as tk, we call the Tk() function
    # the Tk() function initializes the main window
    root = tk.Tk()
    
    # Create the application
    # app is also an arbritary variable name
    # we are creating an instance of the IhtiramsApp class
    # and storing the reference to it locally in the app variable
    app = IhtiramsApp(root)
    
    # Start the main event loop
    # This is what keeps the window open
    # It is a loop that waits for events to happen
    # like a button being clicked or a key being pressed
    # It is what allows the user to interact with the application
    # It is what allows the application to run
    root.mainloop()

# this is the main entry point for the application
# the __name__ is a special variable that is set by the python interpreter
# it is set to the name of the module
# if you run the application directly, __name__ will be set to "__main__"
# if you import the application as a module, __name__ will be set to the name of the module
# dont worry too much about this for now
# this is just what allows the application to be run
# we will use it to call the main function
if __name__ == "__main__":
    main()
