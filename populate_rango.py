import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    categories = {
        "Python": {"views": 128, "likes": 64, "pages": [
            {"title": "Official Python Tutorial", "url": "http://docs.python.org/3/tutorial/", "views" : "100"},
            {"title": "How to Think like a Computer Scientist", "url": "http://www.greenteapress.com/thinkpython/", "views" : "70"},
            {"title": "Learn Python in 10 Minutes", "url": "http://www.korokithakis.net/tutorials/python/", "views" : "65"},
        ]},
        "Django": {"views": 64, "likes": 32, "pages": [
            {"title": "Official Django Tutorial", "url": "https://docs.djangoproject.com/en/2.1/intro/tutorial01/", "views": "99"},
            {"title": "Django Rocks", "url": "http://www.djangorocks.com/", "views" : "30"},
            {"title": "How to Tango with Django", "url": "http://www.tangowithdjango.com/", "views" : "67"},
        ]},
        "Other Frameworks": {"views": 32, "likes": 16, "pages": [
            {"title": "Bottle", "url": "http://bottlepy.org/docs/dev/", "views" : "20"},
            {"title": "Flask", "url": "http://flask.pocoo.org", "views" : "18"},
        ]},
    }

    for category, category_data in categories.items():
        cat = add_category(category, category_data["views"], category_data["likes"])
        for page in category_data["pages"]:
            add_page(cat, page["title"], page["url"], page['views'])

def add_category(name, views, likes):
    category, created = Category.objects.get_or_create(name=name)
    category.views = views
    category.likes = likes
    category.save()
    return category

def add_page(category, title, url, views):
    page, created = Page.objects.get_or_create(category=category, title=title, url=url, views=views)
    page.save()
    return page

if __name__ == '__main__':
    print("Populating Rango database...")
    populate()
    print("Population complete!")
