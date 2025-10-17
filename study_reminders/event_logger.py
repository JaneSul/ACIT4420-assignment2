import logging


def setup_logging():
    """
    Configure logging for the study_reminders package.

    Sets up logging to both console and file with appropriate formatting.
    """
    # Configure root logger
    logger = logging.getLogger('study_reminders')
    logger.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(console_format)

    # File handler
    file_handler = logging.FileHandler('automation.log')
    file_handler.setLevel(logging.INFO)
    file_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_format)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# Get logger instance
logger = setup_logging()


def log_reminder_generated(name, course):
    """Log when a reminder is generated.

     Args:
        name (str): Full name of the student receiving the reminder.
        course (str): Name of the course the reminder pertains to.
    """
    logger.info(f"Reminder generated for {name} - Course: {course}")


def log_reminder_sent(email, name):
    """Log when a reminder is sent.

     Args:
        name (str): Full name of the student receiving the reminder.
        email (str): Email of the student receiving the reminder.
    """
    logger.info(f"Reminder sent to {email} - Student: {name}")


def log_scheduler_started(student_count):
    """Log when the scheduler is started.

     Args:
        student_count (int): Number of students to remind.
    """
    logger.info(f"Scheduler started with {student_count} scheduled reminders")


def log_scheduler_job_executed(name, course):
    """Log when a scheduled job is executed.

     Args:
        name (str): Full name of the student receiving the reminder.
        course (str): Name of the course the reminder pertains to.
    """
    logger.info(f"Scheduled job executed for {name} - Course: {course}")


def log_error(component, error_message):
    """Log system errors.

    Args:
        component (str): Component of the error.
        error_message (str): Error message.
    """
    logger.error(f"Error in {component}: {error_message}")