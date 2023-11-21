# Ei Study Coding Challenge

## 1) Virtual Classroom Manager

https://github.com/arungovindm2001/ei-study-coding-challenge/assets/67337602/17cdbc86-6bdc-4626-baa4-00ee8c16816c

### Overview
A terminal-based Virtual Classroom Manager that handles class scheduling, student attendance, and assignment submissions. The data is stored in a json file which is created in the directory when the program is run.

### Initial State
- Number of Classrooms: 0
- Number of Students: 0
- Number of Assignments: 0

### Functional Requirements
- **Classroom Management:** Ability to add, list, and remove virtual classrooms. :white_check_mark:
- **Student Management:** Ability to enroll students into classrooms, and list students in each classroom. :white_check_mark:
- **Assignment Management:** Schedule assignments for classrooms and allow students to submit them. :white_check_mark:

---

## 2) Satellite Command System

https://github.com/arungovindm2001/ei-study-coding-challenge/assets/67337602/8c216bb2-38a5-4331-bb42-a6df84c9f438

### Overview

A Satellite Command System that simulates controlling a satellite in orbit. The system allows users to initialize a satellite, change its orientation, control the status of solar panels, and collect data.

### Functional Requirements

- **Initialize the Satellite:** Create a class or function that initializes the satellite's attributes to their initial state. :white_check_mark:
- **Rotate:** Implement a command called 'rotate' that takes a direction parameter (North, South, East, West) and sets the satellite's
orientation accordingly.:white_check_mark:<br>
Example: `rotate(North)` would set the orientation to "North".
- **Activate/Deactivate Solar Panels:** Implement commands called 'activatePanels' and 'deactivatePanels' to control the solar panels'
status.:white_check_mark:<br>
Example: `activatePanels()` would set the solar panels to "Active".
- **Collect Data:** Implement a command called 'collectData' that increments the 'Data Collected' attribute by 10 units, but only if the solar panels are "Active".:white_check_mark:<br>
Example: `collectData()` would set the data collected to 10 if the solar panels are "Active".

### Initial State

The satellite begins with the following attributes:
- Orientation: "North"
- Solar Panels: "Inactive"
- Data Collected: 0

### Usage

The series of commands should be executed in a sequential manner over the initial state, altering the satellite's state accordingly. You could execute them through function calls, or simulate a command-line interface where these commands can be entered.

Example:
```python
rotate("South")
activatePanels()
collectData()
```

After these commands, the satellite's state would be:
- Orientation: "South"
- Solar Panels: "Active"
- Data Collected: 10

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/arungovindm2001/ei-study-coding-challenge.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ei-study-coding-challenge
   ```
### For Satellite Command Center
3. Run the program or integrate the provided commands into your Python script.
   ```
   python satellite_command_center.py
   ```
### For Virtual Classroom Manager
3. Run the program or integrate the provided commands into your Python script.
   ```
   python classroom_manager.py <command> <arguments>
   ```

## Contributing

If you would like to contribute to this project, please fork the repository, create a new branch, and submit a pull request.
