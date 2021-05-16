# Ticketing System (Django DRF + VueJS)
## Clone Repo
`git clone https://github.com/HarishJagtap/ticketing-system.git`<br><br>
Goto Git root directory<br>
`cd ticketing-system\`

## Setup Django Backend
Setup Virtual Environment<br>
`python -m venv env`<br>
`env\Scripts\activate`<br><br>

Goto Backend directory<br>
`cd ticketing_system\`<br><br>

Install Dependencies and Setup DB<br>
`pip install -r requirements.txt`<br>
`python manage.py makemigrations`<br>
`python manage.py migrate`<br><br>

Run Django Server<br>
`python manage.py runserver`<br><br>

Now Django Backend is running on port 8000.<br><br>

## Setup VueJS Frontend
Start from Git root directory<br>
`cd frontend`<br><br>

Install dependencies<br>
`npm install`<br><br>

Run VueJS Server<br>
`npm run serve`<br><br>

Now VueJS Fronend is running on port 8080.<br><br>
### Goto http://localhost:8080/ in the web-browser
