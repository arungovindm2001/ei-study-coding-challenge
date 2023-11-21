import os
import json
import argparse

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
            print("Creating JSON file..")
            with open("data.json",'w') as json_file:
                json.dump(self.data, json_file, indent=2)
            print("JSON file created")
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
            ask = input("File already exists. Do you want to overwrite [Y/N]:")
            if ask == "Y" or "yes" or "Yes":
                self.update_json(self.data)
            elif ask == "N" or "no" or "No":
                exit()
        else:
            with open("data.json", "w") as json_file:
                json.dump(self.data, json_file, indent=2)


    def add_classroom(self, args):
        """
        Adds a new classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Name of the classroom.

        Prints an error message and exits if the classroom already exists.
        """
        if args[0] in self.data["classrooms"].keys():
            print("Classroom already exists")
            exit()

        self.data["classrooms"][args[0]] = {"students":{}, "assignment":None}
        self.update_json(self.data)
        print(f"Classroom {args[0]} added")


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
            else:
                for classroom in self.data["classrooms"].keys():
                    print(classroom)
        except:
            print("Unknown error occurred")


    def remove_classroom(self, args):
        """
        Removes an existing classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Name of the classroom to be removed.

        Prints an error message if the classroom doesn't exist.
        """
        try:    
            self.data["classrooms"].pop(args[0])
            self.update_json(self.data)
            print(f"Classroom {args[0]} removed successfully")
        except KeyError:
            print(f"Classroom {args[0]} doesn't exist")


    def add_student(self, args):
        """
        Adds a student to a classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Student ID.
                args[1] (str): Name of the classroom.

        Prints an error message if the student is already enrolled or if the classroom doesn't exist.
        """
        try:
            if args[0] in self.data["classrooms"][args[1]]["students"].keys():
                print("Student already enrolled")
                exit()

            if self.data["classrooms"][args[1]]["assignment"] != None:
                self.data["classrooms"][args[1]]["students"][args[0]] = {"assignment_completed":False}
            else:
                self.data["classrooms"][args[1]]["students"][args[0]] = {"assignment_completed":None}

            self.update_json(self.data)
            print(f"Student {args[0]} has been enrolled in {args[1]}")
        except KeyError:
            print(f"Classroom {args[1]} doesn't exist")
        except IndexError:
            print("Classroom field missing")


    def list_students(self, args):
        """
        Lists all students in a classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Name of the classroom.

        Prints an error message if the classroom doesn't exist.
        """
        try:
            for classroom in self.data["classrooms"].keys():
                print(f"Classroom name: {classroom}")
                for student_id in self.data["classrooms"][classroom]["students"].keys():
                    print(student_id, ' ')
        except KeyError:
            print(f"Classroom {args[0]} doesn't exist")


    def schedule_assignment(self, args):
        """
        Schedules an assignment for a classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Name of the classroom.
                args[1:] (list): Details of the assignment.

        Prints an error message if the classroom doesn't exist.
        """
        try:
            self.data["classrooms"][args[0]]["assignment"] = ' '.join(args[1:])

            for student_id in self.data["classrooms"][args[0]]["students"]:
                self.data["classrooms"][args[0]]["students"][student_id]["assignment_completed"] = False

            self.update_json(self.data)
            print(f"Assignment for {args[0]} has been scheduled")
        except KeyError:
            print(f"Classroom {args[0]} doesnt exist for scheduling assignment")


    def submit_assignment(self, args):
        """
        Submits an assignment for a student in a classroom.

        Args:
            args (list): Command arguments.
                args[0] (str): Student ID.
                args[1] (str): Name of the classroom.
                args[2:] (list): Details of the assignment.

        Prints an error message if the assignment doesn't exist or if there is an unexpected error.
        """
        try:
            assignment_status = self.data["classrooms"][args[1]]["students"][args[0]]["assignment_completed"]
            if assignment_status == None:
                print(f"Assignment hasn't been given in {args[1]}")
            elif assignment_status == True:
                print("Assignment already submitted")
            elif assignment_status == False:
                self.data["classrooms"][args[1]]["students"][args[0]]["assignment_completed"] = True
                self.update_json(self.data)
                print(f"Assignment submitted by Student {args[0]} in {args[1]}")
        except KeyError:
            print("Assignment doesn't exist")
        except:
            print("Some error occurred")



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
    7) schedule_assignment <Class_Name> <Details>
    8) submit_assignment <Student_ID> <Class_Name> <Details>
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
        "schedule_assignment": manager.schedule_assignment,
        "submit_assignment": manager.submit_assignment,
    }

    if args.command in commands:
        commands[args.command](args.arguments)
    else:
        print(f"Invalid command: {args.command}\nLook up the list of commands with -h argument")



if __name__ == "__main__":
    main()