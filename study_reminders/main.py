
from study_reminders.students_manager import StudentsManager
from study_reminders.reminder_generator import generate_reminder
from study_reminders.reminder_sender import send_reminder
from study_reminders.logger import log_reminder


def run_automation(manual_trigger=False):
    print("Initializing Study Reminders Automation System...")
    print("-" * 60)

    manager = StudentsManager()

    print("\nLoaded Students:")
    manager.list_students()
    print("\n" + "-" * 60)

    if manual_trigger:
        print("\nManually triggering reminders for all students...")
        for student in manager.get_students():
            reminder = generate_reminder(student['name'], student['course'])
            send_reminder(student['email'], reminder)
            log_reminder(student, reminder)
        print("\n" + "-" * 60)
        print("All reminders sent and logged successfully.")
    else:
        from study_reminders.scheduler import schedule_reminders
        print("\nScheduler activated. Running in background...")
        schedule_reminders(manager, generate_reminder, send_reminder, log_reminder)


if __name__ == "__main__":
    run_automation(manual_trigger=True)