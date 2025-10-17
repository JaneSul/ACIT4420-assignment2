from event_logger import log_reminder_generated

def generate_reminder(name, course):
    """Generate a personalized study reminder for the given name and course
     Args:
        name (str): Full name of the student receiving the reminder.
        course (str): Name of the course the reminder pertains to.

    Returns:
        str: A personalized reminder message incorporating the student's name
             and course information.

    Raises:
        None
    """
    log_reminder_generated(name, course)  # Log the event
    return f"Hi {name}, remember to review {course} materials before the deadline!"