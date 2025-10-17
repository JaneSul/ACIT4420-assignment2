from event_logger import log_scheduler_started, log_scheduler_job_executed, log_error
import schedule
import time


def schedule_reminders(students_manager, reminder_generator, reminder_sender, logger_func):
    """Schedule reminders with logging

    The scheduler continues running until interrupted (Ctrl+C), providing
    continuous automated reminder distribution capability.

    Args:
        students_manager (StudentsManager): Instance managing student data.
        reminder_generator (callable): Function to generate reminder messages.
                                           Signature: f(name: str, course: str) -> str
        reminder_sender (callable): Function to send reminders.
                                        Signature: f(email: str, reminder: str) -> None
        logger_func (callable): Function to log sent reminders.
                               Signature: f(student: dict, reminder: str) -> None

    Returns:
        None (runs indefinitely until interrupted)

    Raises:
        KeyboardInterrupt: When user interrupts execution (Ctrl+C).
        Exception: Any exception raised by scheduled job execution.
    """
    try:
        student_count = len(students_manager.get_students())
        log_scheduler_started(student_count)  # Log scheduler activation

        for student in students_manager.get_students():
            reminder = reminder_generator(student["name"], student["course"])
            schedule.every().day.at(student["preferred_time"]).do(
                lambda s=student, r=reminder: execute_reminder(
                    s, r, reminder_sender, logger_func
                )
            )

        while True:
            schedule.run_pending()
            time.sleep(60)

    except Exception as e:
        log_error("scheduler", str(e))
        raise


def execute_reminder(student, reminder, reminder_sender, logger_func):
    """Execute scheduled reminder with logging."""
    try:
        log_scheduler_job_executed(student["name"], student["course"])
        reminder_sender(student["email"], reminder)
        logger_func(student, reminder)
    except Exception as e:
        log_error("scheduler_job", str(e))
