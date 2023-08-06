from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name



class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    join_date = models.DateField()

    def __str__(self):
        return "%s %s %s %s" %(self.first_name, self.last_name, self.dept, self.role)