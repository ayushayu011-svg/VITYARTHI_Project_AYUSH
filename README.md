# Hospital Excel System (Python)

This is a console-based Hospital Management mini-project in Python that stores patient records in an Excel-compatible CSV file. It allows users to register OPD consultations, admit IPD patients, and view all stored records from the CSV sheet.[attached_file:2]

## Features

- Automatic CSV file creation with proper column headers if the file does not exist.[attached_file:2]
- Register new patient for consultancy (OPD) with:
  - Auto-generated patient ID
  - Basic vitals: name, age, sex, weight
  - Department, assigned doctor, and prescribed medicine.[attached_file:2]
- Register new patient for admission (IPD) with:
  - Auto-generated patient ID
  - Ward type (General/Private)
  - Random bed number
  - Expected days of stay and emergency contact number.[attached_file:2]
- View all records from the CSV in a simple table-like format in the console, along with total record count.[attached_file:2]

## Technologies Used

- Language: Python 3.[attached_file:2]
- Modules:
  - `csv` – for reading and writing patient data in Excel-compatible format.
  - `os` – for checking file existence and creating the CSV file.
  - `datetime` – for storing date and time of registration.
  - `random` – for generating random patient IDs and bed numbers.[attached_file:2]

## File Structure

- `project.py`  
  Contains:
  - `HospitalSystem` class: CSV creation, saving records, reading records, registering OPD/IPD.
  - `main()` function: menu-driven loop for user interaction.[attached_file:2]
- `hospital_records.csv`  
  Generated automatically; stores all patient records row-wise.[attached_file:2]

## How to Run

1. Install Python 3 on your system.
2. Keep `project.py` in a folder where you want `hospital_records.csv` to be created.
3. Open terminal/command prompt in that folder.
4. Run:
