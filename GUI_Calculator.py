import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        
    # Variables
        self.expression = ""
        self.history = []
        self.dark_mode = False
        
        # Define color schemes
        self.light_bg = "#f0f0f0"  # Light background
        self.dark_bg = "#000000"   # Dark background (pure black)
        self.light_fg = "#000000"  # Light foreground
        self.dark_fg = "#ffffff"   # Dark foreground
        self.button_bg_light = "#e0e0e0"  # Light button background
        self.button_bg_dark = "#333333"   # Dark button background
        self.button_fg = "#000000"        # Button text color
        self.clear_button_color = "#ff4d4d"  # Red color for clear button
        self.equal_button_color = "#4d94ff"  # Blue color for equal button
        
        # Set initial theme to light mode
        self.current_bg = self.light_bg
        self.current_fg = self.light_fg
        self.current_button_bg = self.button_bg_light
        
        # Create UI components
        self.create_widgets()    
    

