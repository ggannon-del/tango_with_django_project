import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    categories = {
        "Python": {"views": 128, "likes": 64, "pages": [
            {"title": "Official Python Tutorial", "url": "http://docs.python.org/3/tutorial/"},
            {"title": "How to Think like a Computer Scientist", "url": "http://www.greenteapress.com/thinkpython/"},
            {"title": "Learn Python in 10 Minutes", "url": "http://www.korokithakis.net/tutorials/python/"},
        ]},
        "Django": {"views": 64, "likes": 32, "pages": [
            {"title": "Official Django Tutorial", "url": "https://docs.djangoproject.com/en/2.0/intro/tutorial01/"},
            {"title": "Django Rocks", "url": "http://www.djangorocks.com/"},
            {"title": "How to Tango with Django", "url": "http://www.tangowithdjango.com/"},
        ]},
        "Other Frameworks": {"views": 32, "likes": 16, "pages": [
            {"title": "Bottle", "url": "http://bottlepy.org/docs/dev/"},
            {"title": "Flask", "url": "http://flask.pocoo.org/"},
        ]},
    }

    for category, category_data in categories.items():
        cat = add_category(category, category_data["views"], category_data["likes"])
        for page in category_data["pages"]:
            add_page(cat, page["title"], page["url"])

def add_category(name, views, likes):
    category, created = Category.objects.get_or_create(name=name)
    category.views = views
    category.likes = likes
    category.save()
    return category

def add_page(category, title, url):
    page, created = Page.objects.get_or_create(category=category, title=title, url=url)
    page.save()
    return page

if __name__ == '__main__':
    print("Populating Rango database...")
    populate()
    print("Population complete!")
