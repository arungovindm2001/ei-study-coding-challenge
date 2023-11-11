# Ei Study Coding Challenge

## Satellite Command System

### Overview

This project implements a Satellite Command System that simulates controlling a satellite in orbit. The system allows users to initialize a satellite, change its orientation, control the status of solar panels, and collect data.

### Functional Requirements

#### 1. Initialize the Satellite

Create a class or function that initializes the satellite's attributes to their initial state.

#### 2. Rotate

Implement a command called 'rotate' that takes a direction parameter (North, South, East, West) and sets the satellite's orientation accordingly.

Example:
```python
rotate("North")
```

#### 3. Activate/Deactivate Solar Panels

Implement commands called 'activatePanels' and 'deactivatePanels' to control the solar panels' status.

Example:
```python
activatePanels()
```

#### 4. Collect Data

Implement a command called 'collectData' that increments the 'Data Collected' attribute by 10 units, but only if the solar panels are "Active".

Example:
```python
collectData()
```

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

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/arungovindm2001/ei-study-coding-challenge.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ei-study-coding-challenge
   ```

3. Run the program or integrate the provided commands into your Python script.
   ```
   python3 satellite_command_center.py
   ```


## Contributing

If you would like to contribute to this project, please fork the repository, create a new branch, and submit a pull request.