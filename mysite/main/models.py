from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name='department name')

    def __str__(self):
        return self.name


class Cabinet(models.Model):
    number = models.IntegerField(verbose_name='number')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='department')

    def __str__(self):
        return str(self.number)


class Doctor(models.Model):
    surname = models.CharField(max_length=50, verbose_name='doctor surname')
    name = models.CharField(max_length=50, verbose_name='doctor name')
    patronymic = models.CharField(max_length=50, verbose_name='doctor patronymic')
    position = models.CharField(max_length=50, verbose_name='doctor position')
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, verbose_name='cabinet')

    def __str__(self):
        return self.surname + ' ' + self.name


class Timetable(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='doctor')
    # day = models.ForeignKey(Day, on_delete=models.CASCADE, verbose_name='day of week')
    monstart = models.TimeField(default="00:00:00")
    monend = models.TimeField(default="00:00:00")
    tuestart = models.TimeField(default="00:00:00")
    tueend = models.TimeField(default="00:00:00")
    wedstart = models.TimeField(default="00:00:00")
    wedend = models.TimeField(default="00:00:00")
    thstart = models.TimeField(default="00:00:00")
    thnend = models.TimeField(default="00:00:00")
    frstart = models.TimeField(default="00:00:00")
    frend = models.TimeField(default="00:00:00")
    msatstart = models.TimeField(default="00:00:00")
    satend = models.TimeField(default="00:00:00")
    def __str__(self):
        return self.doctor.surname + ' ' + self.doctor.name


class Patient(models.Model):
    surname = models.CharField(max_length=50, verbose_name='patient surname', blank=True, null=True)
    name = models.CharField(max_length=50, verbose_name='patient name', blank=True, null=True)
    patronymic = models.CharField(max_length=50, verbose_name='patient patronymic', blank=True, null=True)
    login = models.CharField(max_length=100, verbose_name='login')
    password = models.CharField(max_length=100, verbose_name='password')
    policy = models.CharField(max_length=20, verbose_name='policy', blank=True, null=True)
    email = models.EmailField(blank=True, verbose_name='email')
    number = models.CharField(max_length=20, verbose_name='number', blank=True, null=True)
    date = models.DateField(verbose_name='patient date', blank=True, null=True)

    # def __str__(self):
    #     return self.surname + ' ' + self.name


class Record(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return self.patient.surname




