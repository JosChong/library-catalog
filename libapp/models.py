from django.db import models

from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse

from django.utils.text import slugify

# Create your models here.

numeric = RegexValidator(r'^[0-9]{13}$', 'Must be 13 digits with no hyphens')

class Book(models.Model):
    title = models.CharField(max_length = 50)
    page_count = models.PositiveIntegerField()
    author = models.CharField(max_length = 50)
    ISBN_number = models.CharField(primary_key = True, max_length = 13, validators=[numeric])
    publish_date = models.DateField(blank = True)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("book_detail_view", args = [self.ISBN_number])

class BookGenre(models.Model):
    book = models.ForeignKey(Book)
    genre = models.CharField(max_length = 50)

def image_upload_to(instance, filename):
    title = instance.book.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
    return "books/%s/%s" %(slug, new_filename)

class BookImage(models.Model):
    book = models.ForeignKey(Book)
    image = models.ImageField(upload_to = image_upload_to)
