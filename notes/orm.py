class Student(model.model):
    name=model.CharField()
    age=model.IntegerField()

    student=Student.objects.all()