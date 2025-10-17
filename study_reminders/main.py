from event_logger import log_error
from students_manager import StudentsManager
from reminder_generator import generate_reminder
from reminder_sender import send_reminder
from logger import log_reminder


def run_automation(manual_trigger=True):
    """Runs the full automation system

    Args:
        manual_trigger (bool, optional): whether to manually trigger all reminders. Defaults to True.
    """
    try:
        print("Initializing Study Reminders Automation System...")

        manager = StudentsManager()
        print("\nLoaded Students:")
        manager.list_students()

        if manual_trigger:
            print("\nManually triggering reminders...\n")

            for student in manager.get_students():
                reminder = generate_reminder(student['name'], student['course'])
                send_reminder(student['email'], reminder)
                log_reminder(student, reminder)

            print("\nAll reminders sent successfully.")
        else:
            from scheduler import schedule_reminders
            schedule_reminders(manager, generate_reminder, send_reminder, log_reminder)

    except Exception as e:
        log_error("main", str(e))
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    run_automation(manual_trigger=True)