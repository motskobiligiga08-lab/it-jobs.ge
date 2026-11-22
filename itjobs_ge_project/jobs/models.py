from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField('კომპანიის სახელი', max_length=120)
    website = models.URLField('ვებსაიტი', blank=True)
    location = models.CharField('ლოკაცია', max_length=120, blank=True)
    description = models.TextField('აღწერა', blank=True)
    logo_letter = models.CharField('ლოგოს ასო', max_length=2, default='IT')

    class Meta:
        verbose_name = 'კომპანია'
        verbose_name_plural = 'კომპანიები'
        ordering = ['name']

    def __str__(self):
        return self.name


class Job(models.Model):
    EMPLOYMENT_CHOICES = [
        ('full_time', 'სრული განაკვეთი'),
        ('part_time', 'ნახევარი განაკვეთი'),
        ('contract', 'კონტრაქტი'),
        ('internship', 'სტაჟირება'),
        ('freelance', 'ფრილანსი'),
    ]
    LEVEL_CHOICES = [
        ('intern', 'Intern'),
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
        ('lead', 'Lead'),
    ]
    WORK_CHOICES = [
        ('remote', 'დისტანციური'),
        ('hybrid', 'ჰიბრიდული'),
        ('onsite', 'ოფისიდან'),
    ]

    title = models.CharField('პოზიცია', max_length=180)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs', verbose_name='კომპანია')
    location = models.CharField('ლოკაცია', max_length=120, default='თბილისი, საქართველო')
    employment_type = models.CharField('დასაქმების ტიპი', max_length=20, choices=EMPLOYMENT_CHOICES, default='full_time')
    level = models.CharField('დონე', max_length=20, choices=LEVEL_CHOICES, default='middle')
    work_mode = models.CharField('სამუშაო ფორმატი', max_length=20, choices=WORK_CHOICES, default='hybrid')
    salary_min = models.PositiveIntegerField('ხელფასი მინ.', null=True, blank=True)
    salary_max = models.PositiveIntegerField('ხელფასი მაქს.', null=True, blank=True)
    currency = models.CharField('ვალუტა', max_length=8, default='₾')
    description = models.TextField('აღწერა')
    requirements = models.TextField('მოთხოვნები', blank=True)
    benefits = models.TextField('ბენეფიტები', blank=True)
    skills = models.CharField('ტექნოლოგიები', max_length=255, help_text='გამოყავი მძიმით: Python, Django, PostgreSQL')
    apply_url = models.URLField('აპლიკაციის ბმული', blank=True)
    source_name = models.CharField('წყარო', max_length=120, blank=True)
    source_url = models.URLField('წყაროს ბმული', blank=True)
    is_featured = models.BooleanField('რჩეული', default=False)
    is_active = models.BooleanField('აქტიური', default=True)
    created_at = models.DateTimeField('დამატების თარიღი', auto_now_add=True)

    class Meta:
        verbose_name = 'ვაკანსია'
        verbose_name_plural = 'ვაკანსიები'
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return f'{self.title} — {self.company.name}'

    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'pk': self.pk})

    @property
    def skill_list(self):
        return [s.strip() for s in self.skills.split(',') if s.strip()]

    @property
    def salary_display(self):
        if self.salary_min and self.salary_max:
            return f'{self.salary_min:,}–{self.salary_max:,} {self.currency}'
        if self.salary_min:
            return f'{self.salary_min:,}+ {self.currency}'
        return 'შეთანხმებით'
