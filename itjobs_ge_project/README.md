# ITJobs.ge — Django MVP

ქართული IT ვაკანსიების პლატფორმის სამუშაო MVP. შექმნილია Django + Python + HTML + CSS + Vanilla JavaScript-ზე.

## ფუნქციები
- მთავარი გვერდი hero search-ით და რჩეული ვაკანსიებით
- ვაკანსიების სრული სია
- ძიება და ფილტრები: keyword, location, level, work mode, employment type
- ვაკანსიის დეტალის გვერდი
- კომპანიის მონაცემები და ტექნოლოგიური tags
- ვაკანსიის დამატების ფორმა
- Django Admin-იდან კომპანიებისა და ვაკანსიების მართვა
- Responsive დიზაინი desktop/tablet/mobile-ზე
- დემო მონაცემების seed command

## გაშვება Windows-ზე

```powershell
cd itjobs_ge_project
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_jobs
python manage.py createsuperuser
python manage.py runserver
```

შემდეგ გახსენი:
- საიტი: http://127.0.0.1:8000/
- ადმინი: http://127.0.0.1:8000/admin/

## შემდეგი ეტაპისთვის რეკომენდებული ფუნქციები
- მომხმარებლის/დამსაქმებლის რეგისტრაცია
- კანდიდატის პროფილი + CV ატვირთვა
- Saved jobs / განაცხადების ისტორია
- email alerts
- API/RSS importers საერთაშორისო ვაკანსიებისთვის
- წყაროების deduplication
- moderation queue
- PostgreSQL + Cloud Run deployment
- SEO JobPosting structured data

> შენიშვნა: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` production-ზე აუცილებლად გადაიტანე environment variables-ში.
