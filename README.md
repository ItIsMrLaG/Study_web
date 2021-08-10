# Study_web  
---  
## Commands:  
* "django-admin startproject NAME_OF_YOUR_PROJECT" - starting new project 
* "python manage.py runserver" - starting web testing  
* "python manage.py startapp NAME_OF_THE_APP" - creating new app  
* "python manage.py makemigrations" - creating migraation for bd  
* "python manage.py migrate" - making migration  
* "python manage.py createsuperuser" - creating a admin account
---
## Organization:
* "all .html should be in directory with name 'templates' + (developers recommends put all this html in a directory with same name as this app (django knows that 
all .html leaves in "template" because of that you should write path to file from 'templates'(exemp - main/index.html)))"  
* "all static sources (css, images, js-scripts) should be in directory with name 'static' (developers recommends put all 
this html in a directory with same name as this app)"  
---
## Starting new App
1. Do in terminal "python manage.py startapp NAME_OF_THE_APP"  
2. Log your app in "settings.py"  
3. Link page on your site with this app in "urls.py"  
4. Then link function from file "YOUR_APP/views.py" with your site-page of this app in "YOUR_APP/urls.py"  
---
## Work with BD  
1. Create table class in "YOUR_APP/models.py" (this class should be inherited from class models.Model)  
2. Create "__str__" func with return - self.title  
3. Then do in terminal "python manage.py makemigrations"  
4. Then do in terminal "python manage.py migrate"  
5. Then you need to log in to your site on the page "YOUR_SITE/admin"  
  * if you don't have an account  
  1. Do in terminal "python manage.py createsuperuser"  
  2. Imagine and mind your login and password (as 'admin' and 'geg')  
6. Register your table in file 'YOUR_APP/admin'  
7. For changing name of table in DB add new class 'Meta' inside the class of your table  