from django import forms
from .models import Company, Job


class JobPostForm(forms.ModelForm):
    company_name = forms.CharField(label='კომპანიის სახელი', max_length=120)
    company_website = forms.URLField(label='კომპანიის ვებსაიტი', required=False)

    class Meta:
        model = Job
        fields = [
            'title', 'location', 'employment_type', 'level', 'work_mode',
            'salary_min', 'salary_max', 'currency', 'skills', 'description',
            'requirements', 'benefits', 'apply_url'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6}),
            'requirements': forms.Textarea(attrs={'rows': 5}),
            'benefits': forms.Textarea(attrs={'rows': 4}),
        }

    def save(self, commit=True):
        company_name = self.cleaned_data['company_name']
        company_website = self.cleaned_data.get('company_website', '')
        company, _ = Company.objects.get_or_create(
            name=company_name,
            defaults={'website': company_website, 'logo_letter': company_name[:2].upper()}
        )
        if company_website and not company.website:
            company.website = company_website
            company.save(update_fields=['website'])
        instance = super().save(commit=False)
        instance.company = company
        instance.is_active = True
        if commit:
            instance.save()
        return instance
