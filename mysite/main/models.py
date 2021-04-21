from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name='department name')

    def __str__(self):
        return self.name


class Cabinet(models.Model):
    number = models.IntegerField(max_length=100, verbose_name='number')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='department')

    def __str__(self):
        return self.number


class Doctor(models.Model):
    surname = models.CharField(max_length=50, verbose_name='doctor surname')
    name = models.CharField(max_length=50, verbose_name='doctor name')
    patronymic = models.CharField(max_length=50, verbose_name='doctor patronymic')
    position = models.CharField(max_length=50, verbose_name='doctor position')
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, verbose_name='cabinet')

    def __str__(self):
        return self.surname + '' + self.direction


class Day(models.Model):
    DAY_CHOICES = (
        ("MON", "Понедельник"),
        ("Tuesday", "Вторник"),
        ("Wednesday", "Среда"),
        ("Thursday", "Четверг"),
        ("Friday", "Пятница")
    )
    name = models.CharField(max_length=10, choices=DAY_CHOICES, verbose_name='name')


class Timetable(models.Model):
    doctor = models.ForeignKey(Cabinet, on_delete=models.CASCADE, verbose_name='cabinet')
    day = models.ForeignKey(Day, on_delete=models.CASCADE, verbose_name='day of week')
    start = models.DateTimeField()
    end = models.DateTimeField()


class Patient(models.Model):
    surname = models.CharField(max_length=50, verbose_name='patient surname')
    name = models.CharField(max_length=50, verbose_name='patient name')
    patronymic = models.CharField(max_length=50, verbose_name='patient patronymic')
    login = models.CharField(max_length=100, verbose_name='login')
    password = models.CharField(max_length=100, verbose_name='password')
    policy = models.CharField(max_length=20, verbose_name='policy')
    email = models.CharField(max_length=50, verbose_name='email')
    date = models.DateField()
    number = models.CharField(max_length=20, verbose_name='number')

    def __str__(self):
        return self.surname + '' + self.name


class Record(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()





