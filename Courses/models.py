from django.db import models


class Course(models.Model):
    Title = models.CharField('Title', max_length=100, unique=True)
    Description = models.TextField('Description')
    textChoices = [('AC', 'active'), ('IA', 'inactive'), ('MO', 'modifying')]
    Status = models.CharField('Status', max_length=2, choices=textChoices, default='IA')

    def __str__(self):
        return self.Title


class User(models.Model):
    Username = models.CharField('User\'s name', max_length=20)
    Email = models.EmailField('User email', max_length=255, unique=True)
    Password = models.CharField('User password', max_length=30)
    Courses = models.ManyToManyField(Course, through='UserCourse')

    def __str__(self):
        return self.Username


class UserCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Action = models.BooleanField('Created', default=False)

    def __str__(self):
        kk = 'enrolled'
        if self.Action:
            kk = 'Created'
        return self.course.Title + ' ' + self.user.Username + ' ' + kk


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Module_title = models.CharField('Title', max_length=100)
    Content = models.TextField('Content')

    def __str__(self):
        return self.Module_title

