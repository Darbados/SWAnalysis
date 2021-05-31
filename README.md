# SWAnalysis

Steps to start the project:

1. Clone the repo
2. Within the repo folder add virtual environment
3. Activate the newly added environment
4. Run **pip install -r requirements.txt**
5. Run migrations. As the source folder of the Project is Site/, you
either need to run migrate as **Site/manage.py migrate**, or you'll go
   within Site/ and run **./manage.py migrate**
6. Run **Site/manage.py collectstatic** or **./manage.py collectstatic** from Site/   
7. Run the django web server **Site/manage.py runserver** or **./manage.py runserver** from Site/
8. You can directly access the webserver from localhost:<port of choice> where you'll hit the home page. You navigate from it.
9. I made a little start_project.sh withing the scripts/ where I placed the above commands and which could 
be easy used with **bash scripts/start_project.sh** from the repo directory. You should not be in activated virtual environment to use it.

The project is developed under Ubuntu 20.04. I saw some issues while testing it under Win 10. If you'll
test it under Win 10, you can message me to try to make it work smooth for you within Win 10.
