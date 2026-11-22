from django.core.management.base import BaseCommand
from jobs.models import Company, Job


class Command(BaseCommand):
    help = 'Adds demo Georgian and remote IT jobs.'

    def handle(self, *args, **options):
        if Job.objects.exists():
            self.stdout.write(self.style.WARNING('ვაკანსიები უკვე არსებობს — seed გამოტოვებულია.'))
            return

        companies = {}
        for name, site, loc, letters in [
            ('TBC Tech', 'https://www.tbcbank.ge', 'თბილისი', 'TB'),
            ('Space Int.', 'https://space.ge', 'თბილისი', 'SP'),
            ('Digital Area', 'https://example.com', 'თბილისი', 'DA'),
            ('CloudPeak', 'https://example.com', 'ევროპა / Remote', 'CP'),
            ('CodeBridge', 'https://example.com', 'საქართველო', 'CB'),
            ('Northstar Labs', 'https://example.com', 'Remote', 'NL'),
        ]:
            companies[name] = Company.objects.create(name=name, website=site, location=loc, logo_letter=letters)

        data = [
            dict(title='Senior Python / Django Developer', company='TBC Tech', location='თბილისი, საქართველო', level='senior', work_mode='hybrid', employment_type='full_time', salary_min=7000, salary_max=10000, currency='₾', skills='Python, Django, PostgreSQL, Redis, REST API', is_featured=True),
            dict(title='Frontend Developer — React', company='Space Int.', location='თბილისი, საქართველო', level='middle', work_mode='hybrid', employment_type='full_time', salary_min=4500, salary_max=7000, currency='₾', skills='React, TypeScript, Next.js, CSS, REST', is_featured=True),
            dict(title='Junior Python Developer', company='Digital Area', location='თბილისი, საქართველო', level='junior', work_mode='onsite', employment_type='full_time', salary_min=2000, salary_max=3200, currency='₾', skills='Python, Django, Git, SQL', is_featured=False),
            dict(title='Backend Engineer', company='CloudPeak', location='Remote — Europe', level='middle', work_mode='remote', employment_type='full_time', salary_min=3500, salary_max=5000, currency='€', skills='Node.js, PostgreSQL, Docker, AWS, TypeScript', is_featured=True),
            dict(title='Flutter Mobile Developer', company='CodeBridge', location='საქართველო', level='middle', work_mode='remote', employment_type='contract', salary_min=4000, salary_max=6500, currency='₾', skills='Flutter, Dart, REST API, Firebase', is_featured=False),
            dict(title='DevOps Engineer', company='Northstar Labs', location='Remote — Worldwide', level='senior', work_mode='remote', employment_type='full_time', salary_min=4500, salary_max=6500, currency='$', skills='AWS, Kubernetes, Docker, Terraform, CI/CD', is_featured=False),
            dict(title='QA Automation Engineer', company='Space Int.', location='თბილისი, საქართველო', level='middle', work_mode='hybrid', employment_type='full_time', salary_min=3500, salary_max=5200, currency='₾', skills='Playwright, Python, API Testing, CI/CD', is_featured=False),
            dict(title='UI/UX Product Designer', company='Digital Area', location='თბილისი, საქართველო', level='middle', work_mode='hybrid', employment_type='full_time', salary_min=3000, salary_max=5000, currency='₾', skills='Figma, Design Systems, UX Research, Prototyping', is_featured=False),
        ]

        desc = 'ვეძებთ მოტივირებულ პროფესიონალს, რომელიც იმუშავებს პროდუქტზე რეალურ გუნდთან ერთად. როლი მოიცავს ფუნქციონალის დაგეგმვას, განვითარებას, ხარისხის კონტროლს და გუნდთან კომუნიკაციას.'
        req = 'მინიმუმ შესაბამისი პრაქტიკული გამოცდილება; Git-ის ცოდნა; გუნდური მუშაობა; პასუხისმგებლობა და დამოუკიდებლად პრობლემების გადაჭრის უნარი.'
        ben = 'მოქნილი სამუშაო გრაფიკი; პროფესიული განვითარების ბიუჯეტი; თანამედროვე ტექნოლოგიური გარემო; ანაზღაურებადი შვებულება.'
        for row in data:
            company = companies[row.pop('company')]
            Job.objects.create(company=company, description=desc, requirements=req, benefits=ben, **row)

        self.stdout.write(self.style.SUCCESS(f'დაემატა {Job.objects.count()} დემო ვაკანსია.'))
