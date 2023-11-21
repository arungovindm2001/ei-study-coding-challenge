import os
import json
import argparse
import logging

logging.basicConfig(filename='classroom.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class JSONHandler:
    """
    A class for handling JSON operations.

    Attributes:
        data (dict): The data dictionary to store and manipulate JSON data.

    Methods:
        __init__(): Initializes the JSONHandler object.
        update_json(data): Updates the JSON file with the provided data.
    """
    def __init__(self):
        """
        Initializes the JSONHandler object.

        If the 'data.json' file does not exist, it creates a new one with an initial data structure.
        If the file already exists, it loads the existing data.
        """
        self.data = { "classrooms": {} }
        if not os.path.exists("data.json"):
            logging.info("Creating JSON file..")
            with open("data.json",'w') as json_file:
                json.dump(self.data, json_file, indent=2)
            logging.info("JSON file created")
        else:
            with open("data.json", "r") as json_file:
                self.data = json.load(json_file)
                return self.data

    def update_json(self, data):
        """
        Updates the JSON file with the provided data.

        Args:
            data (dict): The data to be written to the JSON file.
        """
        with open("data.json",'w') as json_file:
            json.dump(data, json_file, indent=2)


class ClassroomManager(JSONHandler):
    """
    A class for managing virtual classrooms and student assignments.

    Methods:
        truncate_data(args): Truncates the data in 'data.json'.
        add_classroom(args): Adds a new classroom.
        list_classrooms(args): Lists all existing classrooms.
        remove_classroom(args): Removes an existing classroom.
        add_student(args): Adds a student to a classroom.
        list_students(args): Lists all students in a classroom.
        schedule_assignment(args): Schedules an assignment for a classroom.
        submit_assignment(args): Submits an assignment for a student in a classroom.
    """
    def __init__(self):
        """
        Initializes the ClassroomManager object by inheriting from JSONHandler.
        """
        super().__init__()

    def truncate_data(self, args):
        """
        Truncates the data in 'data.json'.

        If the file already exists, prompts the user for confirmation before truncating the data.

        Args:
            args (list): Command arguments.
        """
        self.data = { "classrooms": {} }
        if os.path.exists("data.json"):
            ask = input("File already exists. Do you want to overwrite [Y/N]:").lower()
            if ask in {"y", "yes"}:
                self.update_json(self.data)
                logging.info("Data truncated.")
            elif ask in {"n", "no"}:
                exit()
            else:
                print("Invalid input. Please enter 'Y' or 'N'")
        else:
            with open("data.json", "w") as json_file:
                json.dump(self.data, json_file, indent=2)


    def add_classroom(self, args):
        """
        Adds a new classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Name of the classroom.

        Prints an error message and exits if the classroom name is not provided or if it already exists.
        """
        if not args:
            print("Error: Classroom name not provided.")
            logging.error("Classroom name not provided.")
            exit()

        classroom_name = args[0]
        if classroom_name in self.data["classrooms"].keys():
            print("Error: Classroom already exists.")
            logging.error("Classroom already exists.")
            exit()

        self.data["classrooms"][classroom_name] = {"students": {}, "assignment": None}
        self.update_json(self.data)
        print(f"Classroom {classroom_name} added")
        logging.info(f"Classroom {classroom_name} added.")


    def remove_classroom(self, args):
        """
        Removes an existing classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Name of the classroom to be removed.

        Prints an error message if the classroom name is not provided or if it doesn't exist.
        """
        if not args:
            print("Error: Classroom name not provided.")
            logging.error("Classroom name not provided.")
            exit()

        classroom_name = args[0]
        try:
            self.data["classrooms"].pop(classroom_name)
            self.update_json(self.data)
            print(f"Classroom {classroom_name} removed successfully")
            logging.info(f"Classroom {classroom_name} removed successfully.")
        except KeyError:
            print(f"Error: Classroom {classroom_name} doesn't exist")
            logging.error(f"Classroom {classroom_name} doesn't exist.")

    def list_classrooms(self, args):
        """
        Lists all existing classrooms.

        Args:
            args (list): Command arguments (unused).

        Prints a message if there are no classrooms.
        """
        try:
            if len(self.data["classrooms"].keys()) == 0:
                print("No classrooms as of now. Try adding new classrooms with 'add_classroom' command")
                logging.info("No classrooms as of now. Try adding new classrooms with 'add_classroom' command")
            else:
                for classroom in self.data["classrooms"].keys():
                    print(classroom)
        except:
            print("Unknown error occurred")

    def add_student(self, args):
        """
        Adds a student to a classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Student ID.
                args[1] (str): Name of the classroom.

        Prints an error message if student ID or classroom name is not provided,
        if the student is already enrolled, or if the classroom doesn't exist.
        """
        if len(args) < 2:
            print("Error: Both student ID and classroom name are required.")
            logging.error("Both student ID and classroom name are required.")
            exit()

        student_id, classroom_name = args[0], args[1]

        if student_id in self.data["classrooms"].get(classroom_name, {}).get("students", {}).keys():
            print("Error: Student already enrolled.")
            logging.error("Student already enrolled.")
            exit()

        if classroom_name not in self.data["classrooms"].keys():
            print(f"Error: Classroom {classroom_name} doesn't exist.")
            logging.error(f"Classroom {classroom_name} doesn't exist.")
            exit()

        if self.data["classrooms"][classroom_name]["assignment"] is not None:
            self.data["classrooms"][classroom_name]["students"][student_id] = {"assignment_completed": False}
        else:
            self.data["classrooms"][classroom_name]["students"][student_id] = {"assignment_completed": None}

        self.update_json(self.data)
        print(f"Student {student_id} has been enrolled in {classroom_name}")
        logging.info(f"Student {student_id} enrolled in {classroom_name}.")


    def list_students(self, args):
        """
        Lists all students in a classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Name of the classroom.

        Prints an error message if the classroom name is not provided or if it doesn't exist.
        """
        if not args:
            print("Error: Classroom name not provided.")
            logging.error("Classroom name not provided.")
            exit()

        classroom_name = args[0]
        try:
            for student_id in self.data["classrooms"][classroom_name]["students"].keys():
                print(student_id, ' ')
        except KeyError:
            print(f"Error: Classroom {classroom_name} doesn't exist.")
            logging.error(f"Classroom {classroom_name} doesn't exist.")

    def list_students_overdue(self, args):
        """
        Lists all students who are due to submit assignment.

        Args:
            args (list): Command arguments.
                args[0] (str): Name of the classroom.

        Prints an error message if the classroom name is not provided or if it doesn't exist.
        """
        if not args:
            print("Error: Classroom name not provided.")
            logging.error("Classroom name not provided.")
            exit()

        classroom_name = args[0]
        try:
            flag = 0
            students = self.data["classrooms"][classroom_name]["students"]
            for student_id in students:
                if not students[student_id]["assignment_completed"]:
                    print(student_id)
                    flag = 1
            if not flag:
                print(f"All students completed their assignment in {classroom_name}")

        except KeyError:
            print(f"Error: Classroom {classroom_name} doesn't exist or there are no students in {classroom_name}")
            logging.error(f"Error: Classroom {classroom_name} doesn't exist or there are no students in {classroom_name}")
    
    def list_assignment(self, args):
        """
        Lists all assignments in a classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Name of the classroom.

        Prints an error message if the classroom name is not provided or if it doesn't exist.
        """
        if not args:
            print("Error: Classroom name not provided.")
            logging.error("Classroom name not provided.")
            exit()

        classroom_name = args[0]
        try:
            assignment = self.data["classrooms"][classroom_name]["assignment"]
            print(assignment)

        except KeyError:
            print(f"Error: Classroom {classroom_name} doesn't exist or there is no assignment in {classroom_name}")
            logging.error(f"Error: Classroom {classroom_name} doesn't exist or there is no assignment in {classroom_name}")


    def schedule_assignment(self, args):
        """
        Schedules an assignment for a classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Name of the classroom.
                args[1:] (list): Details of the assignment.

        Prints an error message if the classroom name is not provided or if it doesn't exist.
        """
        if not args:
            print("Error: Classroom name not provided.")
            logging.error("Classroom name not provided.")
            exit()

        classroom_name = args[0]
        try:
            self.data["classrooms"][classroom_name]["assignment"] = ' '.join(args[1:])

            for student_id in self.data["classrooms"][classroom_name]["students"]:
                self.data["classrooms"][classroom_name]["students"][student_id]["assignment_completed"] = False

            self.update_json(self.data)
            print(f"Assignment for {classroom_name} has been scheduled")
            logging.info(f"Assignment for {classroom_name} has been scheduled.")
        except KeyError:
            print(f"Error: Classroom {classroom_name} doesn't exist for scheduling assignment")
            logging.error(f"Classroom {classroom_name} doesn't exist for scheduling assignment.")
    
    def remove_assignment(self, args):
        """
        Removes an assignment for a classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Name of the classroom.

        Prints an error message if the classroom name is not provided or if it doesn't exist.
        """
        if not args:
            print("Error: Classroom name not provided.")
            logging.error("Classroom name not provided.")
            exit()

        classroom_name = args[0]
        try:
            assignment = self.data["classrooms"][classroom_name]["assignment"]
            if assignment != None:
                assignment = None

                for student_id in self.data["classrooms"][classroom_name]["students"]:
                    self.data["classrooms"][classroom_name]["students"][student_id]["assignment_completed"] = None

                self.update_json(self.data)
                print(f"Assignment of {classroom_name} removed successfully")
                logging.info(f"Assignment of {classroom_name} removed successfully")
            else:
                print(f"Error: There is no assignment scheduled in {classroom_name}")
                logging.error(f"There is no assignment scheduled in {classroom_name}")
        except KeyError:
            print(f"Classroom {classroom_name} doesn't exist")


    def submit_assignment(self, args):
        """
        Submits an assignment for a student in a classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Student ID.
                args[1] (str): Name of the classroom.
                args[2:] (list): Details of the assignment.

        Prints an error message if student ID, classroom name, or assignment details are not provided,
        if the assignment doesn't exist, or if there is an unexpected error.
        """
        if len(args) < 3:
            print("Error: Student ID, classroom name, and assignment details are required.")
            logging.error("Student ID, classroom name, and assignment details are required.")
            exit()

        student_id, classroom_name = args[0], args[1]

        try:
            assignment_status = self.data["classrooms"][classroom_name]["students"][student_id]["assignment_completed"]
            if assignment_status is None:
                print(f"Error: Assignment hasn't been given in {classroom_name}")
                logging.error(f"Assignment hasn't been given in {classroom_name}")
            elif assignment_status:
                print("Error: Assignment already submitted")
                logging.error("Assignment already submitted")
            elif not assignment_status:
                self.data["classrooms"][classroom_name]["students"][student_id]["assignment_completed"] = True
                self.update_json(self.data)
                print(f"Assignment submitted by Student {student_id} in {classroom_name}")
                logging.info(f"Assignment submitted by Student {student_id} in {classroom_name}.")
        except KeyError:
            print("Error: Assignment doesn't exist")
            logging.error("Assignment doesn't exist.")
        except Exception as e:
            print(f"Error: {str(e)}")
            logging.error(f"{str(e)}")


def main():
    """
    The main function to parse command-line arguments and execute corresponding commands.
    """
    parser = argparse.ArgumentParser(
    prog="Virtual Classroom Management System",
    description="A terminal-based Virtual Classroom Manager that handles class scheduling, student enrollment, and assignment submissions.",
    epilog="""
    Commands:
    1) truncate_data
    2) add_classroom <Class_Name>
    3) list_classrooms
    4) remove_classroom <Class_Name>
    5) add_student <Student_ID> <Class_Name>
    6) list_students <Class_Name>
    7) list_students_overdue <Class_Name>
    8) schedule_assignment <Class_Name> <Details>
    9) remove_assignment <Class_Name>
    10) list_assignment <Class_Name>
    11) submit_assignment <Student_ID> <Class_Name> <Details>
    """,
    )


    parser.add_argument("command", help="truncate_data add_classroom remove_classroom list_classrooms add_student list_students schedule_assignment submit_assignment")
    parser.add_argument("arguments", nargs="*", help="Add arguments for the command", type=str)

    args = parser.parse_args()

    manager = ClassroomManager()

    commands = {
        "truncate_data": manager.truncate_data,
        "add_classroom": manager.add_classroom,
        "remove_classroom": manager.remove_classroom,
        "list_classrooms": manager.list_classrooms,
        "add_student": manager.add_student,
        "list_students": manager.list_students,
        "list_students_overdue": manager.list_students_overdue,
        "schedule_assignment": manager.schedule_assignment,
        "remove_assignment": manager.remove_assignment,
        "list_assignment": manager.list_assignment,
        "submit_assignment": manager.submit_assignment,
    }

    if args.command in commands:
        commands[args.command](args.arguments)
    else:
        print(f"Invalid command: {args.command}\nLook up the list of commands with -h argument")

if __name__ == "__main__":
    main()
