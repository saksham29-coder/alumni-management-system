# controller.py
import json
import os
from models import Alumni

class SystemController:
    def __init__(self):
        self.file_path = "alumni_data.json"
        self.all_alumni = []
        self.load_data() # Load existing data automatically on startup

    def add_new_alumni(self, alumni_obj):
        """Appends a new alumni object to the master list and saves to file."""
        self.all_alumni.append(alumni_obj)
        self.save_data() # Permanent save!

    def search_by_year(self, year):
        """Loops through database and filters alumni by graduation year."""
        results = []
        for alumni in self.all_alumni:
            if alumni.graduation_year == str(year):
                results.append(alumni)
        return results

    def search_by_company(self, company_name):
        """Loops through database and filters alumni by current company."""
        results = []
        for alumni in self.all_alumni:
            if company_name.lower() in alumni.current_company.lower():
                results.append(alumni)
        return results

    # ================= BACKEND STORAGE LOGIC =================
    
    def save_data(self):
        """Converts Python objects into JSON format and writes to a file."""
        data_to_save = []
        for alumni in self.all_alumni:
            # Convert object attributes into a standard Python dictionary
            alumni_dict = {
                "alumni_id": alumni.alumni_id,
                "name": alumni.name,
                "graduation_year": alumni.graduation_year,
                "degree": alumni.degree,
                "current_company": alumni.current_company,
                "email": alumni.email
            }
            data_to_save.append(alumni_dict)
            
        with open(self.file_path, "w") as file:
            json.dump(data_to_save, file, indent=4)

    def load_data(self):
        """Reads the JSON file and converts data back into Python objects."""
        # If the file doesn't exist yet, create it with some starting dummy data
        if not os.path.exists(self.file_path):
            self.all_alumni = [
                Alumni("A101", "John Doe", "2024", "Computer Science", "Google", "john@gmail.com"),
                Alumni("A102", "Jane Smith", "2024", "Data Science", "Amazon", "jane@yahoo.com")
            ]
            self.save_data()
            return

        # If file exists, read it
        with open(self.file_path, "r") as file:
            try:
                loaded_data = json.load(file)
                self.all_alumni = []
                for item in loaded_data:
                    # Recreate the Alumni objects from the raw dictionary data
                    obj = Alumni(
                        item["alumni_id"], 
                        item["name"], 
                        item["graduation_year"], 
                        item["degree"], 
                        item["current_company"], 
                        item["email"]
                    )
                    self.all_alumni.append(obj)
            except json.JSONDecodeError:
                print("Error reading database file. Starting fresh.")