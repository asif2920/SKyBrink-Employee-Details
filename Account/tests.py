from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User
from Employee.models import Employee
from django.shortcuts import get_object_or_404

# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class SignupTests(SimpleTestCase):
    def test_signup_statuscode(self):
        response = self.client.get('/signupform/')
        self.assertEqual(response.status_code, 200)

    def test_signup_url(self):
        response = self.client.get(reverse('signupform'))
        self.assertEqual(response.status_code, 200)

    def test_signup_template(self):
        response = self.client.get(reverse('signupform'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'signupform.html')

class userTests(TestCase):
    @classmethod
    def setUp(cls):
        User.objects.create(username='shivani', password='admin1234')

    def test_text(self):
        user = User.objects.get(id=1)
        expected_username = user.username
        expected_password = user.password
        self.assertEqual(expected_username, 'shivani')
        self.assertEqual(expected_password, 'admin1234')

    def test_search(self):
        user = User.objects.get(username='shivani')
        expected_password = user.password
        self.assertEqual(expected_password, 'admin1234')

class EmployeeTests(TestCase):
    @classmethod
    def setUp(cls):
        Employee.objects.create(firstname='Shivani', lastname='Thakkar', designation='Manager',
                                department='HR', employeeid=100)

    def test_text(self):
        emp = Employee.objects.get(id=1)
        expected_fname = emp.firstname
        expected_lname = emp.lastname
        expected_designation= emp.designation
        expected_department = emp.department
        expected_employeeid = emp.employeeid

        self.assertEqual(expected_fname, 'Shivani')
        self.assertEqual(expected_lname,'Thakkar')
        self.assertEqual(expected_designation,'Manager')
        self.assertEqual(expected_department, 'HR')
        self.assertEqual(expected_employeeid, 100)

    def test_update(self):
        emp = Employee.objects.get(employeeid=100)
        emp.employeeid=90
        emp.firstname='Shivani'
        emp.lastname='Thakkar'
        emp.designation='Senior Executive'
        emp.department ='IT'
        emp.save()

        emp1 = Employee.objects.get(id=1)
        expected_fname = emp1.firstname
        expected_lname = emp1.lastname
        expected_designation= emp1.designation
        expected_department = emp1.department
        expected_employeeid = emp1.employeeid

        self.assertEqual(expected_fname, 'Shivani')
        self.assertEqual(expected_lname,'Thakkar')
        self.assertEqual(expected_designation,'Senior Executive')
        self.assertEqual(expected_department, 'IT')
        self.assertEqual(expected_employeeid, 90)
