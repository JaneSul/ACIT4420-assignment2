# ACIT4420-assignment2

Sending personalized study reminder

The full report is available in [REPORT.md](REPORT.md)

# Study Reminders Package

This assignment creates a Python package named `study_reminders` to automate sending personalized study reminders.

## Features

- **Student Management**: Add, remove, and retrieve student information with JSON persistence
- **Personalized Reminders**: Generate context-specific study reminders incorporating student names and courses
- **Simulation and Logging**: Simulate reminder delivery with audit trail logging
- **Automated Scheduling**: Schedule reminders at student-specified preferred times
- **Modular Architecture**: Independent, reusable modules for each component

## Installation

### Prerequisites

- Python 3.9 or higher
- pip

### Local Installation

1. Clone or extract the package:
```bash
git clone https://github.com/JaneSul/ACIT4420-assignment2.git
cd study_reminders
```

2. Install the package in development mode:
```bash
pip install -e .
```

3. Or, install with dependencies:
```bash
pip install -r requirements.txt
```

## Package Structure

```
study_reminders/
├── __init__.py                 # Package initialization
├── students.py                 # Basic student management
├── students_manager.py         # JSON-based student data management
├── reminder_generator.py       # Reminder generation logic
├── reminder_sender.py          # Reminder delivery simulation
├── logger.py                   # Logging functionality
├── scheduler.py                # Automated scheduling
├── main.py                     # Main automation script
├── test.py                     # Unit tests
├── setup.py                    # Installation configuration
├── requirements.txt            # Dependency specifications
└── README.md                   # This file
```


## Testing

To execute the test suite:

```bash
python -m pytest test.py
```

Or run tests directly:

```bash
python test.py
```

## Logging

The system maintains a log file (`reminder_log.txt`) recording:
- Timestamp of reminder transmission
- Recipient student name
- Reminder message content


The system also maintains a full `automation.log` recording:
- Reminder generation
- Reminder scheduling
- Reminder sending