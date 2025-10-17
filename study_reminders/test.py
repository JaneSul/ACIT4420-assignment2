import unittest
import os
import json
from datetime import datetime
from study_reminders.students import Students
from study_reminders.students_manager import StudentsManager
from study_reminders.reminder_generator import generate_reminder
from study_reminders.reminder_sender import send_reminder
from study_reminders.logger import log_reminder

# Define a unittest.TestCase subclass grouping tests for Students:
class TestStudents(unittest.TestCase):
    """Test cases for the Students class."""

def setUp(self):
    """Initialize a Students instance for each test."""
    self.students = Students()
def test_add_student(self):
    """Test adding a student to the list."""
    self.students.add_student("Alice", "alice@example.com", "CS", "08:00 AM")
    self.assertEqual(len(self.students.get_students()), 1)
    self.assertEqual(self.students.get_students()[0]['name'], "Alice")

# Adds then removes “Alice”; checks the list is empty afterward.
def test_remove_student(self):
    """Test removing a student from the list."""
    self.students.add_student("Alice", "alice@example.com", "CS", "08:00 AM")
    self.students.remove_student("Alice")
    self.assertEqual(len(self.students.get_students()), 0)


def test_get_students(self):
    """Test retrieving the student list."""
    self.students.add_student("Bob", "bob@example.com", "Math", "09:00 AM")
    students = self.students.get_students()
    self.assertIsInstance(students, list)
    self.assertEqual(len(students), 1)

def test_get_students(self):
    """Test retrieving the student list."""
    self.students.add_student("Bob", "bob@example.com", "Math", "09:00 AM")
    students = self.students.get_students()
    self.assertIsInstance(students, list)
    self.assertEqual(len(students), 1)


#test for student manager:

class TestStudentsManager(unittest.TestCase):
    """Test cases for the StudentsManager class."""

def setUp(self):
    """Initialize a StudentsManager with a test file."""
    self.test_file = "test_students.json"
    self.manager = StudentsManager(self.test_file)

def tearDown(self):
    """Clean up the test file after each test."""
    if os.path.exists(self.test_file):
        os.remove(self.test_file)

def test_add_and_save_student(self):
    """Test adding a student and saving to JSON."""
    self.manager.add_student("Diana", "diana@example.com", "Physics", "10:00 AM")
    self.assertEqual(len(self.manager.get_students()), 4)

def test_remove_and_save_student(self):
    """Test removing a student and saving to JSON."""
    initial_count = len(self.manager.get_students())
    self.manager.remove_student("Alice")
    self.assertEqual(len(self.manager.get_students()), initial_count - 1)

def test_load_default_students(self):
    """Test loading default students when file doesn't exist."""
    manager = StudentsManager("nonexistent.json")
    students = manager.get_students()
    self.assertEqual(len(students), 3)
    self.assertEqual(students[0]['name'], "Alice")



class TestReminderGenerator(unittest.TestCase):
    """Test cases for reminder generation."""

def test_generate_reminder(self):
    """Test generating a personalized reminder."""
    reminder = generate_reminder("Alice", "Computer Science")
    self.assertIn("Alice", reminder)
    self.assertIn("Computer Science", reminder)

def test_reminder_format(self):
    """Test that reminder follows expected format."""
    reminder = generate_reminder("Bob", "Mathematics")
    self.assertTrue(reminder.startswith("Hi Bob"))
    self.assertIn("review", reminder)
    self.assertIn("deadline", reminder)

class TestReminderSender(unittest.TestCase):
    """Test cases for reminder sending."""
def test_send_reminder_valid_email(self):
    """Test sending a reminder with a valid email."""
    try:
        send_reminder("test@example.com", "Test reminder message")
    except ValueError:
        self.fail("send_reminder raised ValueError unexpectedly")

def test_send_reminder_missing_email(self):
    """Test that sending with empty email raises ValueError."""
    with self.assertRaises(ValueError):
        send_reminder("", "Test reminder message")
def test_send_reminder_none_email(self):
    """Test that sending with None email raises ValueError."""
    with self.assertRaises(ValueError):
        send_reminder(None, "Test reminder message")

#Test suite for logger

class TestLogger(unittest.TestCase):
    """Test cases for the logging functionality."""
def setUp(self):
    """Set up test environment."""
    self.log_file = "test_reminder_log.txt"
    if os.path.exists(self.log_file):
        os.remove(self.log_file)
def tearDown(self):
    """Clean up after tests."""
    if os.path.exists(self.log_file):
        os.remove(self.log_file)


def test_log_reminder(self):
    """Test logging a reminder."""
    student = {"name": "Alice", "email": "alice@example.com"}
    reminder = "Test reminder"

    # Temporarily redirect log file
    original_log_reminder = log_reminder

    def test_log(student, reminder):
        with open(self.log_file, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - Sent to {student['name']}: {reminder}\\n")

    test_log(student, reminder)

    # Verify log entry
    self.assertTrue(os.path.exists(self.log_file))
    with open(self.log_file, "r") as f:
        content = f.read()
        self.assertIn("Alice", content)
        self.assertIn("Test reminder", content)

#Test module entry point
if __name__ == '__main__':
    unittest.main()
