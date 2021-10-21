# Demo

It is a simple example for writting blogs or articles and guthering news in french language. It can be used for news in any other languages. I am working in Windows 10, and it is used Python 3.9.5

Follow this steps: 
- in the folder you will use for this project:
    - .../>git clone <clone link of this project> 
    
    - cd fr

or if you are using vs code: code . 

- .../> python -m venv env
- .../> pip install -r requirements.txt

Make chnages to settings.py: 
- create .env file (see .env_example)
In the browser, go to: https://newsapi.org/ 

- signup and get the link and API key:
for instance:
https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=your_api_key

- copy your api key from the newsapi link, and paste it in .env file
- also, put to .env file; the info required as in .env_example, then:

    - .../> py manage.py makemigrations
    - .../> py manage.py migrate
    - .../> py manage.py createsuperuser
    - .../> py manage.py collectstatic
    - .../> py manage.py runserver

Articles can posted, edited or deleted if registerd users are part of staff. Superadmin can activate a user if she/he is staff member.
Username: admin
Password: admin

    Try it and good luck!
