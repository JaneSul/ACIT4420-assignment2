import datetime


def log_reminder(student, reminder):
    """Log a sent reminder with a timestamp to a file
Records the details of a sent reminder (recipient name and message) along
    with the current timestamp to a text file. This provides a human-readable
    audit trail of all reminders transmitted.

    Args:
        student (dict): Dictionary containing student information, must include
                       the 'name' key for logging purposes.
        reminder (str): The content of the reminder message that was sent.

    Returns:
        None

    Raises:
        IOError: If the log file cannot be written.
        """
    with open("reminder_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {student['name']}:{reminder}\n")
