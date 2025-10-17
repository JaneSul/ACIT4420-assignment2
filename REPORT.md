# Report on the Development of the study_reminders Package

## 1. Introduction

This report presents the design, implementation, and testing of a Python package named study_reminders, developed to automate the generation and distribution of personalized study reminders for students. The package demonstrates a modular programming, file handling, and task scheduling. It integrates multiple modules responsible for managing student data, generating custom reminders, simulating message delivery, maintaining activity logs, and automating the entire process through scheduling. 

## 2. Methodology

### 2.1 Design Objectives

The development of the study_reminders package followed these main objectives:

1. Modularity: Each function (data management, message generation, sending, logging, scheduling) must be isolated in its own module for reuse and clarity.

2. Automation: The system must be capable of executing reminders automatically based on student preferences.

3. Persistence: Student data must be stored persistently using a structured file format (JSON).

4. Logging: Key events such as reminder generation, sending, and scheduling must be recorded in dedicated log files.

5. Testing and Maintainability: Include unit tests to verify functionality and ensure reliability.

### 2.2 Tools and Technologies

- Python 3.10 
- schedule (for task automation)
- json (for data persistence)
- datetime (for timestamps)
- logging (for system-level event tracking)
- unittest (for testing)

### 2.3 Workflow Overview

The workflow of the package can be summarized as follows:

1. Load student data from students.json or predefined defaults.
2. Generate a personalized reminder for each student. 
3. Simulate sending the reminder to their email. 
4. Log both the event details and timestamps in reminder_log.txt. 
5. Schedule reminders for daily automatic delivery using schedule.

## Implementation


### Package Structure

Each module performs a specific role: 

```shell
study_reminders/
├── students.py
├── students_manager.py
├── reminder_generator.py
├── reminder_sender.py
├── logger.py
├── scheduler.py
├── main.py
├── test.py
├── automation.log
└── reminder_log.txt
```

### 3.2 Logging Mechanism

Two levels of logging were implemented:

`reminder_log.txt:` Logs each individual reminder sent (timestamp, student name, message).

`automation.log:` Tracks system-level events such as initialization, loading students, generating reminders, sending, logging, and scheduling.


### 3.3 Main Program Integration

The main execution script main.py unifies all modules:

* Loads the student dataset through StudentsManager.

* Generates and sends reminders manually or via the scheduler.

* Writes detailed logs to both text files.

* Offers a parameter manual_trigger to control testing and automation modes.

Example usage:

`from study_reminders.main import run_automation
run_automation(manual_trigger=True)`

Or:

`run_automation(manual_trigger=False)
`

## Challenges

### Logging

Extending and integrating the logger for reminder generation was a challenge. 
It was not obvious what was the best way to approach this, as there are a number of ways it can be done:
- unify a single logging file using the logger passed to each of the modules
- keep separate logging files for each of the modules and events

There was also whether to use a single "generic" logging function which would be passed to each function,
or whether to create new logging function for each event and simply import it to the modules.

Ultimately I opted to maintain 2 separate log files and generate them with separate functions, as it seemed like a 
simpler solution in this context.
