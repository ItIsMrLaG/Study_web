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
* '"Shift+F5" - for cleaning cash'  
---  
## Starting new App
1. Do in terminal "python manage.py startapp NAME_OF_THE_APP"  
2. Log your app in "settings.py"  
3. Link page on your site with this app in "urls.py"  
4. Then link function from file "YOUR_APP/views.py" with your site-page of this app in "YOUR_APP/urls.py"  
---  
## Work with BD  
### Creating model  
1. Create table class in "YOUR_APP/models.py" (this class should be inherited from class models.Model)  
2. Create "__str__" func with return - self.title (for pretty output)  
3. Then do in terminal "python manage.py makemigrations"  
4. Then do in terminal "python manage.py migrate"  
5. Then you need to log in to your site on the page "YOUR_SITE/admin"  
  >* if you don't have an account  
  >1. Do in terminal "python manage.py createsuperuser"  
  >2. Imagine and mind your login and password (as 'admin' and 'geg')  
6. Register your table in file 'YOUR_APP/admin'  
7. For changing name of table in DB add new class 'Meta' inside the class of your table  
---  
### Adding info to the BD  
1. creating "<form method='post'>fields for info</form>"  
2. add inside form tag "{% csrf_token %}"  
3. add "<button type='submit'>...</button>" for creating request  
> then you should describe your form  
4. create file "YOUR_APP/forms.py"  
5. put your form in to the html  
6. send form to the bd  
---  
## Registration/login/logout  
### Registration  
1. pip install django-crispy-form  (app for pretty forms)
2. add 'crispy_forms' into 'settings.py' in 'INSTALLED_APP'
3. delete first point from 'settings.py' from 'AUTH_PASSWORD_VALIDATORS'  
4. add "CRISPY_TEMPLATE_PACK = 'bootstrap4'" into file 'settings.py'
5. create html-template (registration.html) where "info|crispy" - your form + crispy-filter 
> also add in the beginning of registration.html - '{% load crispy_forms_tags %}'
6. add new form in file 'YOUR_APP/forms.py'  
7. create def in file 'YOUR_APP/views.py'  and add path to this def  
8. add  in file 'settings.py' - "LOGIN_REDIRECT_URL = 'YOUR_URL'"  
---  
### Log in  
1. use method 'views.LoginView.as_view(template_name='YOUR.html')' from "django.contrib.auth"  
---  
### Log out  
1. use method 'views.LogoutView.as_view(template_name='YOUR.html')' from "django.contrib.auth"  
> to check now user inside .html you should write - "{{ user.username }}"  
---  
## Connecting djang with MySQL  
1. add new config in your 'settings.py' in 'DATABASES'  
> DATABASES = {  
>    'default': {  
>        'ENGINE': 'django.db.backends.mysql',  
>        'NAME': 'boosteam',  
>        'USER': 'root',  
>        'PASSWORD': '',  
>        'HOST': 'localhost',  
>        'PORT': '3306',  
>    }  
>}  
2. then try "pip install mysqlclient"  
> 1. if after this operation you have really huge and awful red 'error' you should install 'mysqlclient' manually  
> from https://pypi.org/project/mysqlclient/#files install file for your python version and then write in terminal - "pip install NAME_OF_THIS_FILE_WITH_PATH"  
> 2. if privious was useless for you and you have error - '.whl is not a supported wheel on this platform' take your 'mysqlclient.whl' from this site - 'https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient' (video - 'https://www.youtube.com/watch?v=8gSjvehTqAk')  
3. then write command 'makemigrations' and 'migrate'  
---
