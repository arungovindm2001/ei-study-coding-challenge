# Ei Study Coding Challenge

## Virtual Classroom Manager

https://github.com/arungovindm2001/ei-study-coding-challenge/assets/67337602/17cdbc86-6bdc-4626-baa4-00ee8c16816c

### Overview
A terminal-based Virtual Classroom Manager that handles class scheduling, student attendance, and assignment submissions. The data is stored in a json file which is created in the directory when the program is run. Logs each command you enter in a log file.

### Functional Abilities
- **Classroom Management:** Ability to add, list, and remove virtual classrooms. :white_check_mark:
   - `truncate_data`
   - `add_classroom <class_name>`
   - `list_classrooms` 
   - `remove_classroom <class_name>` 
- **Student Management:** Ability to enroll students into classrooms, and list students in each classroom. :white_check_mark:
   - `add_student <student_id>` 
   - `list_students <class_name>`
   - `list_students_overdue <class_name>`
- **Assignment Management:** Schedule assignments for classrooms and allow students to submit them. :white_check_mark:
   - `schedule_assignment <class_name> <details>`
   - `submit_assignment <student_id> <class_name> <details>`
   - `list_assignment <class_name>`
   - `remove_assignment <class_name>`

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
   python classroom_manager.py <command> <arguments>
   ```

## Contributing

If you would like to contribute to this project, please fork the repository, create a new branch, and submit a pull request.
