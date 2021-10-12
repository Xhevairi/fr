# Demo

It is a simple example for writting blogs or articles and guthering news in french language. It can be used for news in any other languages. I am working in Windows 10, and it is used Python 3.9.5

Follow this steps: - in the folder you will use for this project:
.../>git clone <clone link of this project> - cd fr
or if you are using vs code: code . - .../> python -m venv <venv of your project> - .../> pip install -r requirements.txt

Make chnages to settings.py: - put your sceret key: SECRET_KEY = <your_secret_key>
In the browser, go to: https://newsapi.org/ - signup and get the API key:
https://newsapi.org/v2/everything?q=tesla&from=2021-09-07&sortBy=publishedAt&apiKey=<your_api_key>
In your project, open settings.py: - copy <your api key> from the newsapi link, and paste it:
API_KEY = <your_api_key>

    - .../> py manage.py makemigrations
    - .../> py manage.py migrate
    - .../> py manage.py createsuperuser
    - .../> py manage.py collectstatic
    - .../> py manage.py runserver

    Try it and good luck!
