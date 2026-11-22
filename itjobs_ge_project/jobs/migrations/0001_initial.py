# Generated for ITJobs.ge MVP
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='კომპანიის სახელი')),
                ('website', models.URLField(blank=True, verbose_name='ვებსაიტი')),
                ('location', models.CharField(blank=True, max_length=120, verbose_name='ლოკაცია')),
                ('description', models.TextField(blank=True, verbose_name='აღწერა')),
                ('logo_letter', models.CharField(default='IT', max_length=2, verbose_name='ლოგოს ასო')),
            ],
            options={'verbose_name': 'კომპანია', 'verbose_name_plural': 'კომპანიები', 'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180, verbose_name='პოზიცია')),
                ('location', models.CharField(default='თბილისი, საქართველო', max_length=120, verbose_name='ლოკაცია')),
                ('employment_type', models.CharField(choices=[('full_time','სრული განაკვეთი'),('part_time','ნახევარი განაკვეთი'),('contract','კონტრაქტი'),('internship','სტაჟირება'),('freelance','ფრილანსი')], default='full_time', max_length=20, verbose_name='დასაქმების ტიპი')),
                ('level', models.CharField(choices=[('intern','Intern'),('junior','Junior'),('middle','Middle'),('senior','Senior'),('lead','Lead')], default='middle', max_length=20, verbose_name='დონე')),
                ('work_mode', models.CharField(choices=[('remote','დისტანციური'),('hybrid','ჰიბრიდული'),('onsite','ოფისიდან')], default='hybrid', max_length=20, verbose_name='სამუშაო ფორმატი')),
                ('salary_min', models.PositiveIntegerField(blank=True, null=True, verbose_name='ხელფასი მინ.')),
                ('salary_max', models.PositiveIntegerField(blank=True, null=True, verbose_name='ხელფასი მაქს.')),
                ('currency', models.CharField(default='₾', max_length=8, verbose_name='ვალუტა')),
                ('description', models.TextField(verbose_name='აღწერა')),
                ('requirements', models.TextField(blank=True, verbose_name='მოთხოვნები')),
                ('benefits', models.TextField(blank=True, verbose_name='ბენეფიტები')),
                ('skills', models.CharField(help_text='გამოყავი მძიმით: Python, Django, PostgreSQL', max_length=255, verbose_name='ტექნოლოგიები')),
                ('apply_url', models.URLField(blank=True, verbose_name='აპლიკაციის ბმული')),
                ('source_name', models.CharField(blank=True, max_length=120, verbose_name='წყარო')),
                ('source_url', models.URLField(blank=True, verbose_name='წყაროს ბმული')),
                ('is_featured', models.BooleanField(default=False, verbose_name='რჩეული')),
                ('is_active', models.BooleanField(default=True, verbose_name='აქტიური')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='დამატების თარიღი')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobs.company', verbose_name='კომპანია')),
            ],
            options={'verbose_name': 'ვაკანსია', 'verbose_name_plural': 'ვაკანსიები', 'ordering': ['-is_featured','-created_at']},
        ),
    ]
