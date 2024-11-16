# Advanced Calculator - GUI Application with Dark Mode and History Feature

## Project Overview

This project is an Advanced GUI Calculator built with Python’s tkinter library, designed to provide a simple and user-friendly interface for 
performing basic arithmetic calculations. In addition to standard calculator functions, this application offers Dark Mode and History Tracking 
features to enhance usability and accessibility.

The GUI design prioritizes simplicity and ease of use, with carefully selected color schemes and intuitive button layout.
This makes it suitable for everyday calculations, while the code provides a solid example of using tkinter to create customizable applications with advanced features.

## Features

### 1. Basic Calculator Functions:
- Supports fundamental operations: addition, subtraction, multiplication, and division.

- Also includes support for decimal points and parentheses for more complex calculations.

### 2. Dark Mode Toggle:
- A toggle button allows users to switch between light and dark modes.

- Dark mode provides a pure black background for a comfortable, eye-friendly experience in low-light environments.

- All components, including buttons, background, and margins, adapt to the selected mode for consistency.

### 3. Calculation History:
- A history section tracks previous calculations with results.

- Users can review their recent calculations without having to re-enter expressions.

- This feature is implemented using a list box widget that displays the history within the main application window.

### 4. Special Buttons:
- Clear Button (Red): Clears the entire expression.

- Delete Button: Removes the last character of the current expression, allowing for easy corrections.

- Equal Button (Blue): Computes the result and displays it instantly.

### 5. Enhanced Layout:
- The calculator’s buttons are arranged in a familiar layout, making it intuitive for any user.

- Buttons have been color-coded to differentiate standard operations from special functions.

## User Interface

The calculator’s layout consists of the following main sections:

### 1. Display Frame:
- Shows the current expression or result.

- Positioned at the top, with a larger font size for clear readability.

- Automatically updates with every button press.

### 2. History Section:
- Displays previous calculations with a scrollable list box, allowing users to track their recent operations.

- Includes a label for clarity and is aligned with the calculator’s main body.

### 3. Dark Mode Button:
- Located at the top right, allowing users to toggle dark mode.

- Changes the colors of the entire interface, including the display, buttons, and background margins, for a cohesive look in both light and dark themes.

### 4. Button Grid:
- Each calculator function and operation is mapped to a button arranged in a grid.

- Buttons are evenly spaced with appropriate padding to maintain a clean appearance.

- Buttons dynamically change color based on the selected mode, ensuring consistent styling.

## Code Structure

### 1. Initialization:
- The calculator application is instantiated by creating a CalculatorApp class, which initializes variables and defines color schemes.

- Sets up the layout by calling create_widgets() method, defining a layout with frames, labels, and buttons.

### 2. Mode Toggling:
- A function toggle_dark_mode manages switching between light and dark modes.

- Dynamically changes the background and foreground colors of all elements, ensuring that all components reflect the selected theme.

### 3. Event Handling:
- Buttons are assigned command functions for interactive operations.

- The on_button_click() method handles button presses, updating the display or performing the desired operation.



