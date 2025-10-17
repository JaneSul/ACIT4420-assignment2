from event_logger import log_reminder_sent, log_error


def send_reminder(email, reminder):
    """Simulate sending a reminder

     Prints the reminder to console (simulating delivery) and logs the sending
    event. Validates that an email address is provided before proceeding

    Args:
        email (str): Email address of the recipient.
        reminder (str): The reminder message content to be sent.

    Returns:
        None

    Raises:
        ValueError: If the email address is missing, None, or empty string.
    """
    try:
        if not email:
            raise ValueError("Email address is missing")

        print(f"Sending reminder to {email}: {reminder}")

        # Extract student name for logging
        student_name = reminder.split("Hi ")[1].split(",")[0]
        log_reminder_sent(email, student_name)

    except ValueError as e:
        log_error("reminder_sender", str(e))
        raise