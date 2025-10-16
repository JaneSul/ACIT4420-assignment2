from setuptools import setup, find_packages

setup(
    name="study_reminders",
    version="0.1.0",
    author="Jeen",
    author_email="",
    description="Automates generation and distribution of personalized study reminders",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/JaneSul/ACIT4420-assignment2",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.9",
    install_requires=[
        "schedule>=1.1.0",
    ],
)
