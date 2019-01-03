# SKyBrink Employee Details

This is a simple application with django. This application has the feature of signup, sign in, insert employee information and perform basic crud operations. Technically, this application gives the flavor of Django restful API services and unit testing. Django version of 2.1 is used with built in database SQLite. For the beginner, this application can be a good source of learning.  
Requirement: 
Installation of python and django (pip install django)
Step-by-step demonstration:
1.	Creation of Project: at first, choose the directory, you want to create your project. Then type the following command: django-admin startproject EmployeeManagement (Name of the project)
2.	You can check the project creation by going to that folder. You can check your project by running from the project folder by typing: django manage.py runserver 
3.	It will show the default home page with welcome message. Now we have to load our template and home page. To do that, follow the instructions below:
4.	Create a folder templates in the root directory of the project which will keep all of the view files (html) files. To make this workable, add this line in the projects settings.py file: 
'DIRS': [os.path.join(BASE_DIR, 'templates')],  
5.	Create a static folder in the root directory which will contain all the CSS, JavaScript files.  To make it workable, add the following lines in the settings.py file.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

6.	Now it is time to add a new application: Account which will take care of the signup and sign in part. It can be done by: python manage.py startapp Account
7.	Next part is to create base.html file and home.html for the project and url configuration.
8.	base.html is created and added the required css files inside the static folder. Later, home.html is created and create a new urls.py file inside the Account application.
Inside the root projects urls.py, one line is added: path('', include('Account.urls')),  and new created urls.py, added one line is: path('', views.home, name='home'),
9.	Inside the views.py file, one method is created, which returns the home.html file and the code from this method is:
def home(request):
    context = {}
    return render(request, 'home.html', context) 
10.	Now it is time to sign up and sign in to go ahead with the app. For this, we have to create the super user for this project and test the cool feature of Django “Admin panel”. Before that, we have to do the migrations. python manage.py makemigrations and python manage.py migrate. Later create the super user by typing, python manage.py createsuperuser. Give necessary credentials for username and password. Now, you can log in to the admin panel by: http://localhost:8000/admin/
11.	After clicking on, sign up, one page will appear for user name and password. After giving those information, it will verify that password and confirm password are same or not, username has been existed in the data base or not. If everything is ok, it will register you and take you to the login page.
12.	After the successful login, it will take you to your dashboard and from there you can see the all employee details. This dashboard is implemented using django rest frame work.
13.	Now, you have the access to perform basic crud operation (Insert, Update and delete). For better understanding, check the code of GitHub repository. 
Unit Testing:
Case 1: SimpleTestCase class was imported for the following three test cases.
1.	Check for status code for a given url: 
At first, we checked for root url (‘/’), for this it is expected from this project to get a status code of 200 (success). Later, we checked for another url (‘/signup/’) and also observed when the tests failed. 
2.	Check for valid URL: Using reverse, we got the URL from name and then checked the status code for this case.
3.	“Check for valid template: Valid url is using the correct html file for viewing or not” is tested in this test case
Case 2: TestCase class was imported for the following test cases. We have two tables in this project. We tested insert, update and read operations for each of the tables.
1.	Insert: I inserted dummy data from the test.py file and later, checked that can I retrieve the data or not.
2.	Update: I updated the previous inserted value and checked that the is the update reflected in the present reading or not. The test will give ok if the change has been reflected.
3.	Read/Search: I inserted multiple values in the table and checked that I can search the entries or not.
During the unit test, I created 10 test cases and at the time of testing a default database was created by the program and after the test-cases, it was deleted. 


