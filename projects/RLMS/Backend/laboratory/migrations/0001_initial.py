# Generated by Django 5.0.1 on 2024-02-03 20:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("company_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Supervisor",
            fields=[
                ("supervisor_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "rank",
                    models.CharField(
                        choices=[
                            ("Instructor", "Instructor"),
                            ("Assistant", "Assistant"),
                            ("Associate Professor", "Associate Professor"),
                            ("Professor", "Professor"),
                            ("Full Professor", "Full Professor"),
                        ],
                        default="Instructor",
                        max_length=100,
                    ),
                ),
                ("field", models.CharField(max_length=100)),
                ("salary", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                ("department_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("father_name", models.CharField(max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=100
                    ),
                ),
                ("address", models.CharField(max_length=500)),
                ("date_of_birth", models.DateField()),
                (
                    "picture",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("national_code", models.CharField(max_length=10, unique=True)),
                (
                    "user",
                    models.OneToOneField(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contact_Ways",
            fields=[
                (
                    "company_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="laboratory.company",
                    ),
                ),
                ("phone_number", models.CharField(max_length=11)),
                ("email_address", models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Degree",
            fields=[
                (
                    "supervisor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="laboratory.supervisor",
                    ),
                ),
                ("educational_degree", models.CharField(max_length=100)),
                ("university", models.CharField(max_length=100)),
                ("started_date", models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name="supervisor",
            name="department_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="laboratory.department"
            ),
        ),
        migrations.AddField(
            model_name="supervisor",
            name="person_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="laboratory.person",
                unique=True,
            ),
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                ("email_id", models.AutoField(primary_key=True, serialize=False)),
                ("email_address", models.EmailField(max_length=100)),
                (
                    "email_type",
                    models.CharField(
                        choices=[
                            ("Personal", "Personal"),
                            ("Work", "Work"),
                            ("University", "University"),
                        ],
                        default="Personal",
                        max_length=100,
                    ),
                ),
                (
                    "person_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="laboratory.person",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Phone",
            fields=[
                ("phone_id", models.AutoField(primary_key=True, serialize=False)),
                ("phone_number", models.CharField(max_length=11)),
                (
                    "person_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="laboratory.person",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Research",
            fields=[
                ("research_id", models.AutoField(primary_key=True, serialize=False)),
                ("research_code", models.CharField(max_length=10)),
                ("subject", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Ongoing", "Ongoing"),
                            ("Terminated", "Terminated"),
                            ("Suspand", "Suspand"),
                        ],
                        default="Pending",
                        max_length=100,
                    ),
                ),
                ("budget", models.IntegerField()),
                ("purpose", models.CharField(max_length=500)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "company_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="laboratory.company",
                    ),
                ),
                (
                    "department_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="laboratory.department",
                    ),
                ),
                (
                    "person_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="laboratory.person",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                ("room_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "department_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="laboratory.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Storage",
            fields=[
                ("storage_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "department_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="laboratory.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product_Info",
            fields=[
                ("product_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=500)),
                ("quantity", models.IntegerField()),
                ("creation_date", models.DateField()),
                ("expiration_date", models.DateField()),
                (
                    "storage_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="laboratory.storage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                ("student_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "educational_degree",
                    models.CharField(
                        choices=[
                            ("Associate", "Associate"),
                            ("Bachelor", "Bachelor"),
                            ("Master", "Master"),
                            ("PhD", "PhD"),
                        ],
                        max_length=100,
                    ),
                ),
                ("university", models.CharField(max_length=100)),
                ("gpa", models.FloatField()),
                ("field", models.CharField(max_length=100)),
                (
                    "person_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="laboratory.person",
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                ("course_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("platform", models.CharField(max_length=100)),
                ("subject", models.CharField(max_length=100)),
                ("session_number", models.IntegerField(null=True)),
                ("estimated_time", models.DurationField(null=True)),
                ("description", models.CharField(max_length=500)),
                ("price", models.IntegerField()),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="laboratory.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subscription_plan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField()),
                ("subscription_duration", models.DurationField()),
                ("price", models.IntegerField()),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="laboratory.student",
                    ),
                ),
            ],
        ),
    ]
