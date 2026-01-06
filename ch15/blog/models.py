from django.db import models

# Models represent database tables
# Each class = one table
# Class name = table name (Student → student table)

class Student(models.Model):
    # name column (VARCHAR)
    name = models.CharField(max_length=100)

    # age column (INTEGER)
    age = models.IntegerField()

    # email column (must be unique)
    email = models.EmailField(unique=True)

    # enrollment_date column
    # auto_now_add=True → value set automatically when record is created
    enrollment_date = models.DateField(auto_now_add=True)

    # Optional: readable object representation
    def __str__(self):
        return self.name
