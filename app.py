# app.py
from flask import Flask, render_template, request, redirect
from models import Alumni
from controller import SystemController

app = Flask(__name__)
system = SystemController()

@app.route('/')
def home():
    # Pass the current alumni list from our JSON database to the HTML page
    return render_template('index.html', alumni_list=system.all_alumni)

@app.route('/add', methods=['POST'])
def add_alumni():
    name = request.form.get('name')
    year = request.form.get('year')
    degree = request.form.get('degree')
    company = request.form.get('company')
    email = request.form.get('email')

    if name and year:
        # Dynamically generate the next ID based on how many records exist
        next_id_num = len(system.all_alumni) + 101
        alumni_id = f"A{next_id_num}"
        
        # Create the object and save it permanently via the controller
        new_alumni = Alumni(alumni_id, name, year, degree, company, email)
        system.add_new_alumni(new_alumni)

    return redirect('/')

@app.route('/search', methods=['POST'])
def search_alumni():
    search_type = request.form.get('search_type')
    query = request.form.get('query')
    
    if search_type == 'year':
        results = system.search_by_year(query)
    else:
        results = system.search_by_company(query)
        
    # Show the results on the same webpage, highlighting the query used
    return render_template('index.html', alumni_list=results, search_query=query)

if __name__ == '__main__':
    app.run(debug=True)