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
> from [site](https://pypi.org/project/mysqlclient/#files) install file for your python version and then write in terminal - "pip install NAME_OF_THIS_FILE_WITH_PATH"  
> 2. if privious was useless for you and you have error - '.whl is not a supported wheel on this platform' take your mysqlclient.whl - 'https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient, video - 'https://www.youtube.com/watch?v=8gSjvehTqAk'
3. then write command 'makemigrations' and 'migrate'  
---
## Connecting python with firebase Cloud  
* [Documentation](https://firebase.google.com/docs/firestore/quickstart#python_1)  
1. Create your 'Firestore Database'  
2. go to your "Project settings" > "Service account" and take SDK.json  
3. use this file in your config (like in firebase_cloud.py)  
   * for take an information from collection:  
   > information = db.collection('collection-name').get().to_dict()  
   * for take information from document from collection:  
   > information = db.collection('collection-name').document('doc-name').get().to_dict()  
   * for rewriting information:  
   > doc_ref = db.collection('userdata').document('just_check')  
     doc_ref.set({  
    ...  
    })  
   * for adding information:  
   > doc_ref = db.collection('userdata').document('just_check')  
     doc_ref.update({  
    ...  
    })  
---  
## Work with JS  
* JS.files are loaded anew (with the original parameters) every time the page is loaded (like html/css)  
* JS.files should be in YOUR_APP/static/YOUR_APP/js/YOUR_FILE.js  
* you can plug your JS.files to all HTML.templates (from all app)  
### Sending GET-request from JS to django  
1. plug to the HTML head jquery_library:  
> '<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>'  
2. then plug to the HTML head your JS.file:  
>  '<script type="text/javascript" src="{% static 'YOUR_APP/main.js' %}"></script>'  
3. create in the JS.file function for getting and handling response with information  
  * this function should have one parameter for information from response  
4. link this function with jquery.method:  
>  '$.getJSON("REQUEST_NAME", JS_FUNCTION);'  
  * without '()'  
5. create in YOUR_APP/urls.py ligament for handler of the path with 'REQUEST_NAME':  
>  'path('REQUEST_NAME', views.handler, name='config'),'  
6. in views "import json" and "from django.http import HttpResponse"  
7. in views.handler(request) return:  
>  'return HttpResponse(json.dumps(YOUR_DICT), content_type='REQUEST_NAME')'  
  * YOUR_DICT would be converted in json format  
---  
### Dynamic output of the code with JS  
* since HTML changes only on page reload, to make dynamic changes you need to use JS  
* ginger changes with HTML  
* all examples in 'js_work' app  
1. link HTML.element with JS.function  
  * for sending value-params to the JS.function:  
>  'on...="Func(this.value)'  
2. add special class to this element ('ELEMENT_CLASS')  
3. write JS.function-handler  
4. for changing some info in HTML inside this function:  
>  '$('.ELEMENT_CLASS').html(just a string);'  
  * the string can be whole html code  
---  
### Sending params from JS to Django  
1. create function like in previous paragraph  
2. write in this function:  
>  'fetch(string-with_params).then(function(response) {body of the func})'  
  * string_with_params = '?value='+ value + '&id=' + 1  (example)  
---  