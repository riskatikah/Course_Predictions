from django.db import models

# Model untuk Student (Mahasiswa)
class Student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = "student"
        managed = False

    def __str__(self):
        return self.name


# Model untuk Course (Kursus)
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)

    class Meta:
        db_table = "course"
        managed = False

    def __str__(self):
        return self.course_name


# Model untuk Enrollment (Pendaftaran Kursus oleh Mahasiswa)
class Enrollment(models.Model):
    enroll_id = models.AutoField(primary_key=True)
    stu = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = (
            "stu",
            "course",
        )  # Correct field name here
        db_table = "enrollment"
        managed = False

    def __str__(self):
        return f"{self.stu.name} - {self.course.course_name}"


# Model untuk InterestType (Tipe Minat)
class InterestType(models.Model):
    interes_id = models.AutoField(primary_key=True)
    interes_name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "interes_type"
        managed = False

    def __str__(self):
        return self.interes_name


# Model untuk CourseActivity (Aktivitas Kursus)
class CourseActivity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=255)
    activity_start_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ("course_id",)
        db_table = "course_activity"
        managed = False

    def __str__(self):
        return f"{self.course_id.course_name} - {self.activity_name}"


# Model untuk StudentActivityLog (Log Aktivitas Mahasiswa)
class StudentActivityLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    stu_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    activity_id = models.ForeignKey(CourseActivity, on_delete=models.CASCADE)
    activity_start = models.DateTimeField(blank=True, null=True)
    activity_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "student_activity_log"
        managed = False

    def __str__(self):
        return f"Log by {self.stu_id.name} for activity."


# Model untuk ModelInfo (Informasi Model Machine Learning)
class ModelInfo(models.Model):
    model_name = models.CharField(max_length=100)
    model_file = models.FileField(upload_to="models/", blank=True, null=True)
    training_data = models.CharField(max_length=255)
    training_date = models.DateTimeField()
    model_summary = models.TextField(blank=True)

    def __str__(self):
        return f"{self.model_name} - {self.training_date.strftime('%Y-%m-%d %H:%M:%S')}"


# Model untuk UserInput (Input Pengguna untuk Prediksi)
class UserInput(models.Model):
    id = models.BigAutoField(primary_key=True)
    interes_name_1 = models.CharField(max_length=255, blank=True, null=True)
    interes_name_2 = models.CharField(max_length=255, blank=True, null=True)
    last_course_1 = models.CharField(max_length=255, blank=True, null=True)
    score_last_course_1 = models.FloatField(blank=True, null=True)
    last_course_2 = models.CharField(max_length=255, blank=True, null=True)
    score_last_course_2 = models.FloatField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = "Learnlytics_userinput"
        managed =  True

    def __str__(self):
        return f"Input ID: {self.id}"
