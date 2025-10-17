import json


class StudentsManager:
    """Class to manage student data with JSON storage."""

    def __init__(self, file_path="students.json"):
        """Initialize the StudentsManager instance

        Loads student records from the specified JSON file. If the file does not
        exist, the manager initializes with default student data for
        testing and demonstration.

        Args:
            file_path (str, optional): Path to the JSON file for student data storage.
                                      Defaults to "students.json".
        """
        self.file_path = file_path
        self.students = self.load_students()

    def load_students(self):
        """Load student data from a JSON file.

        Returns:
            list: A list of dictionaries, each containing a student record with keys:
                  'name' (str), 'email' (str), 'course' (str), 'preferred_time' (str).

        Raises:
            json.JSONDecodeError: If the file contains malformed JSON
        """
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return [
                {
                    "name": "Alice",
                    "email": "alice@example.com",
                    "course": "Computerence",
                    "preferred_time": "21:37",
                },
                {
                    "name": "Bob",
                    "email": "bob@example.com",
                    "course": "Mathematics",
                    "preferred_time": "21:38",
                },
                {
                    "name": "Charlie",
                    "email": "charlie@example.com",
                    "course": "Physics",
                    "preferred_time": "21:39",
                },
            ]

    def add_student(self, name, email, course, preferred_time="08:00 AM"):
        """Add a student and save to the JSON file

        Args:
            name (str): Full name of the student.
            email (str): Email address for contact and reminder delivery.
            course (str): Name of the course the student is enrolled in.
            preferred_time (str, optional): Preferred time for reminders in HH:MM AM/PM format.
                                           Defaults to "08:00 AM".

        Returns:
            None

        Raises:
            IOError: If the file cannot be written.
        """
        student = {
            "name": name,
            "email": email,
            "course": course,
            "preferred_time": preferred_time,
        }
        self.students.append(student)
        self.save_students()

    def remove_student(self, name):
        """Remove a student by name and update the JSON file.

        Args:
            name (str): Full name of the student to remove.

        Returns:
            None

        Raises:
            IOError: If the file cannot be written.
        """
        self.students = [s for s in self.students if s["name"] != name]
        self.save_students()

    def save_students(self):
        """Save student data to the JSON file

        Returns:
            None

        Raises:
            IOError: If the file cannot be written or created.
        """
        with open(self.file_path, "w") as file:
            json.dump(self.students, file, indent=4)

    def get_students(self):
        """Returns the in-memory list of all student records currently managed
        by the system.

        Returns:
            list: A list of student dictionaries containing all student records
        """
        return self.students

    def list_students(self):
        """Print all students

        Returns:
            None
        """
        for student in self.students:
            print(
                f"Name: {student['name']}, Email: {student['email']}, Course:{student['course']}, Preferred Time: {student['preferred_time']}"
            )
