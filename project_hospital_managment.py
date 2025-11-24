import csv
import os
import datetime
import random

# This is the name of the Excel-compatible file
FILE_NAME = "hospital_records.csv"

class HospitalSystem:
    def __init__(self):
        self.check_and_create_file()

    def check_and_create_file(self):
        """
        Checks if the CSV file exists. 
        If not, it creates it and adds the Header Row (The column titles).
        """
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, mode='w', newline='') as file:
                writer = csv.writer(file)
                # These are your Excel Column Headers
                writer.writerow([
                    "Patient ID", "Name", "Age", "Sex", "Weight", 
                    "Date", "Type", "Department/Ward", "Doctor/Bed", 
                    "Medicine/Stay", "Emergency Contact"
                ])

    def save_patient_to_csv(self, data_list):
        """
        Writes a single patient's data to the bottom of the Excel sheet.
        """
        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data_list)
        print(f"\n[SAVED] Data successfully written to {FILE_NAME}")

    def read_excel_sheet(self):
        """
        Reads the Excel sheet and displays it in the Python console.
        """
        if not os.path.exists(FILE_NAME):
            print("\n[ERROR] No records found. Please register a patient first.")
            return

        print("\n--- READING EXCEL SHEET DATABASE ---")
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            # We convert the reader to a list to count rows
            rows = list(reader)
            
            if len(rows) <= 1:
                print("File exists but is empty.")
                return

            # Simple formatting to make it look like a table in Python
            # Using tabs (\t) to space it out
            for row in rows:
                print(f"{row[0]:<10} | {row[1]:<15} | {row[6]:<15} | {row[7]}")
        print("------------------------------------------------")
        print(f"Total Records: {len(rows) - 1}") # Subtract 1 for the header

    def get_basic_inputs(self):
        print("\n--- Enter Patient Vitals ---")
        p_id = f"P-{random.randint(1000, 9999)}" # Random ID
        name = input("Patient Name: ")
        age = input("Age: ")
        sex = input("Sex (M/F): ")
        weight = input("Weight (kg): ")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        return p_id, name, age, sex, weight, date

    def register_consultancy(self):
        print("\n>>> NEW CONSULTANCY (OPD) <<<")
        # 1. Get Basic Data
        p_id, name, age, sex, weight, date = self.get_basic_inputs()
        
        # 2. Get Specific Data
        dept = input("Department (e.g., General, ENT): ")
        doc = input("Assign Doctor: ")
        meds = input("Prescribed Medicine: ")
        
        # 3. Prepare Data for Excel (Order must match the Headers in check_and_create_file)
        # Columns: ID, Name, Age, Sex, Weight, Date, Type, Dept/Ward, Doc/Bed, Med/Stay, Contact
        patient_data = [
            p_id, name, age, sex, weight, 
            date, "OPD (Consultancy)", dept, doc, 
            meds, "N/A"
        ]
        
        # 4. Write to file
        self.save_patient_to_csv(patient_data)

    def register_admission(self):
        print("\n>>> NEW ADMISSION (IPD) <<<")
        # 1. Get Basic Data
        p_id, name, age, sex, weight, date = self.get_basic_inputs()
        
        # 2. Get Specific Data
        ward = input("Ward Type (General/Private): ")
        bed_num = f"Bed-{random.randint(1, 100)}"
        stay = input("Expected Days: ") + " Days"
        contact = input("Emergency Contact Number: ")
        
        # 3. Prepare Data for Excel
        patient_data = [
            p_id, name, age, sex, weight, 
            date, "IPD (Admission)", ward, bed_num, 
            stay, contact
        ]
        
        # 4. Write to file
        self.save_patient_to_csv(patient_data)

# --- MAIN LOOP ---
def main():
    system = HospitalSystem()
    
    while True:
        print("\n=========================================")
        print("   HOSPITAL EXCEL SYSTEM (Python)")
        print("=========================================")
        print("1. Register Consultancy (OPD)")
        print("2. Admit Patient (IPD)")
        print("3. Read Excel Sheet (View Records)")
        print("4. Exit")
        
        choice = input("\nSelect Option: ")
        
        if choice == '1':
            system.register_consultancy()
        elif choice == '2':
            system.register_admission()
        elif choice == '3':
            system.read_excel_sheet()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()