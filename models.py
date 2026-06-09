# models.py

class Alumni:
    def __init__(self, alumni_id, name, graduation_year, degree, current_company, email):
        self.alumni_id = alumni_id
        self.name = name
        self.graduation_year = str(graduation_year) # Kept as string for easier searching
        self.degree = degree
        self.current_company = current_company
        self.email = email
        self.skills = []

    def add_skill(self, skill):
        """Adds a professional skill to the alumnus profile."""
        if skill not in self.skills:
            self.skills.append(skill)

    def __str__(self):
        """Controls how the alumnus looks when printed."""
        skills_str = ", ".join(self.skills) if self.skills else "None listed"
        return (f"ID: {self.alumni_id} | Name: {self.name} | Graduation Year: {self.graduation_year}\n"
                f"   Degree: {self.degree} | Company: {self.current_company} | Email: {self.email}\n"
                f"   Skills: {skills_str}\n" + "-"*50)