from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import JobPostForm
from .models import Job


def home(request):
    qs = Job.objects.filter(is_active=True).select_related('company')
    context = {
        'featured_jobs': qs.filter(is_featured=True)[:3],
        'latest_jobs': qs[:6],
        'job_count': qs.count(),
        'company_count': qs.values('company').distinct().count(),
        'remote_count': qs.filter(work_mode='remote').count(),
    }
    return render(request, 'jobs/home.html', context)


def jobs_list(request):
    jobs = Job.objects.filter(is_active=True).select_related('company')
    q = request.GET.get('q', '').strip()
    level = request.GET.get('level', '').strip()
    work_mode = request.GET.get('work_mode', '').strip()
    employment_type = request.GET.get('employment_type', '').strip()
    location = request.GET.get('location', '').strip()

    if q:
        jobs = jobs.filter(
            Q(title__icontains=q) |
            Q(company__name__icontains=q) |
            Q(skills__icontains=q) |
            Q(description__icontains=q)
        )
    if level:
        jobs = jobs.filter(level=level)
    if work_mode:
        jobs = jobs.filter(work_mode=work_mode)
    if employment_type:
        jobs = jobs.filter(employment_type=employment_type)
    if location:
        jobs = jobs.filter(location__icontains=location)

    return render(request, 'jobs/jobs_list.html', {
        'jobs': jobs,
        'q': q,
        'level': level,
        'work_mode': work_mode,
        'employment_type': employment_type,
        'location': location,
        'level_choices': Job.LEVEL_CHOICES,
        'work_choices': Job.WORK_CHOICES,
        'employment_choices': Job.EMPLOYMENT_CHOICES,
    })


def job_detail(request, pk):
    job = get_object_or_404(Job.objects.select_related('company'), pk=pk, is_active=True)
    related = Job.objects.filter(is_active=True).exclude(pk=pk).filter(
        Q(level=job.level) | Q(work_mode=job.work_mode)
    ).select_related('company')[:3]
    return render(request, 'jobs/job_detail.html', {'job': job, 'related_jobs': related})


def post_job(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save()
            messages.success(request, 'ვაკანსია წარმატებით დაემატა.')
            return redirect(job.get_absolute_url())
    else:
        form = JobPostForm()
    return render(request, 'jobs/post_job.html', {'form': form})


def for_developers(request):
    return render(request, 'jobs/for_developers.html')


def for_employers(request):
    return render(request, 'jobs/for_employers.html')


def about(request):
    return render(request, 'jobs/about.html')
