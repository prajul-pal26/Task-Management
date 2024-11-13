# basics
- django is the framework for building web application 
- with the help of django we can make API(application programming interface) ,which can connect with the client 

# features
- ORM object relational mapper
- the admin site
- caching 
- authentication 

# website

1 - front-end                                   2- Backend
-loaded on client machine                     - runs on a web server 
                                              - responsible for data processing 

# url - UNIFORM RESOURSE LOCATOR
  - LOCATE A  RESOURCE ON A INTERNET
  - RESOURCE - page
             - image 
             - video 
             - pdf
-----------------------------------------------------------------------------------------------------------------------------------

{        
[________url->_________browser->__________Browser_sends_a_request_to_web_server_which_hosted_a_website]
[server_take_this_request_process_it____________->return_response_back_to_the_client______]

## this data exchange is define by protocol called  -----HTTP(hyper text tranfer protocol)
# this define how server and client are communicate
}

-----------------------------------------------------------------------------------------------------------------------------------

# install
python -m venv myenv          [create_virtual_environment]
pip install django            [clone_django]
django-admin version          [version_check]
django-admin startproject deep .        [start_project]
py manage.py startapp playground        [start_app]

django-admin                            [to_check_all_the_commands_in_django]

django-admin runserver                  [if_setting_is_set]
python manage.py  runserver             [same_as_above_without_setting]
python manage.py migrations             [this_is_used_to_get_updated_in_the_database_and_dja_app]
python manage.py migrate app_name  
         



# connect to the database 
pip install psycopg2                   --this is known as driver  

# Playing with the API in shell
>>>py manage.py shell

>>>from polls.models import Choice, Question  
>>>from django.utils import timezone

>>> q=Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()

>>> q.id
>>> q.question_text
>>> q.pub_date

>>> Question.objects.all()

>>>Question.objects.filter(id=1)
   Question.objects.get(id=3)

>>>q=Question.objects.get(id=1) 
>>>q.choice_set.all()
>>>q.choice_set.count() 
>>>q.choice_set.create(choice_text="Not much", votes=0)
# create the superuser only with the name of database, and password as the laptop password
-----------------------------------------------------------------------------------------------------------------------------------
# model /forms (used for making authentication page)                                 [class()]
your database layout
To make a schema of the tables in the database,present in the app                     [def()]

# View section ,                                                              
-take a request and give a response
-request handler
-action [give main code from another one]
-web pages and other content are delivered by views.

# url   (add urls.py in app and call that where they needed)
map the url to the view funtion 
syntex-----path('',include('app_name.urls'))
            path('news/',def_name_in_views)

# templates      (add templates to the settings)             [define_in_app_and_create_folder] templates/polls/index.html
to return html content to the client(app)

# admin 
to register every thing in admin site [import_models]
>>>>>from .models import Question
>>>>>admin.site.register(Question)

# celery beats for schedule the task periodic
pip install django-celery-beat
- add to settings app

# how to add scheduled task using 
task.py
own_script.py
util.py
model.py


