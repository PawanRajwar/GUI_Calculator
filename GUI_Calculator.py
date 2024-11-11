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
    
    def create_widgets(self):
        # Display area
        self.display_frame = tk.Frame(self.root, bg=self.current_bg)
        self.display_frame.pack(expand=False, fill="both", padx=10, pady=(10, 0))
        
        self.display = tk.Label(self.display_frame, text="", anchor='e', font=("Arial", 20), bg=self.current_bg, fg=self.current_fg, height=2)
        self.display.pack(fill="both")
        
        # History area
        self.history_frame = tk.Frame(self.root, bg=self.current_bg)
        self.history_frame.pack(fill="both", padx=10, pady=(5, 0))
        
        self.history_label = tk.Label(self.history_frame, text="History", font=("Arial", 10), bg=self.current_bg, fg=self.current_fg)
        self.history_label.pack(anchor="w")
        
        self.history_box = tk.Listbox(self.history_frame, font=("Arial", 10), bg=self.current_bg, fg=self.current_fg, height=5, bd=0, highlightthickness=0)
        self.history_box.pack(fill="both")
        
        # Toggle dark mode button
        self.dark_mode_button = tk.Button(self.history_frame, text="Toggle Dark Mode", command=self.toggle_dark_mode, font=("Arial", 10), bg=self.current_button_bg, fg=self.current_fg)
        self.dark_mode_button.pack(anchor="e", pady=(5, 10))
        
        # Buttons area
        self.buttons_frame = tk.Frame(self.root, bg=self.current_bg)  # Match dark mode with background color
        self.buttons_frame.pack(expand=True, fill="both", padx=10, pady=(0, 10))
        
         # Define calculator buttons
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '(', ')',
            'C', 'Del', '=', '+'
        ]
        row = 0
        col = 0
        for button in buttons:
            if button == "C":
                button_bg = self.clear_button_color  # Red for Clear
            elif button == "=":
                button_bg = self.equal_button_color  # Blue for Equal
            else:
                button_bg = self.current_button_bg  # Default button color
            
            command = lambda x=button: self.on_button_click(x)
            tk.Button(self.buttons_frame, text=button, width=5, height=2, font=("Arial", 14),
                      bg=button_bg, fg=self.button_fg, command=command).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Make the buttons fill space evenly
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)
            self.buttons_frame.rowconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        elif char == "C":
            self.clear_display()
        elif char == "Del":
            self.delete_last()   
        else:
            self.expression += str(char)
            self.update_display()
    
    def calculate(self):
        try:
            result = eval(self.expression)
            self.history.append(f"{self.expression} = {result}")
            self.history_box.insert(tk.END, f"{self.expression} = {result}")
            self.expression = str(result)
            self.update_display()
        except Exception:
            self.expression = "Error"
            self.update_display()
            self.expression = ""

    def clear_display(self):
        self.expression = ""
        self.update_display()