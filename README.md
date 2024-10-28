# Phase 3 Final Project
## Author
Jacob Payne

## First Published
October 28, 2024

## Introduction

This document is a CLI ORM which takes input from a user and maps the input into objects which are then pushed into a database. It has 2 tables and 2 object classes.

## Jobs table and Object class
This table contains all of the jobs at the company. It contains the job name and ID.

The **job** class has methods to create a new job, delete a job, view all jobs, and find a job by ID.

## Applicants table and Object class
This table contains all of the applicants to the respective jobs. This contains the application ID, the applicant name and the job id they're applying to.

The **applicants** class has methods to add, delete or view all applicants. You can also find applicants by ID.

Note: The directory also includes two files named `CONTRIBUTING.md` and
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard or
delete the files if you want.

---

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## How to Use CLI

This application can be used and navigated via the command line interface. By pressing the corresponding command a user can:
1. Exit the program
2. Create a new job
3. View all jobs
    - See more info on a specific job
        - View applicants
        - Create new application
        - Delete Job
4. View all company applications at a glance

Additionally a user can go back to the main menu or exit the program at each completed step.
    
You can run the template CLI with `python lib/cli.py`.
---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
