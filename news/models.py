from django.db import models
## file for creating pre-table

class Information(models.Model):
    title = models.CharField('Name', max_length=5, default='None')  ## what would be, if field is empty
    intro = models.CharField('Anons', max_length=250)  ## field - for small volume of texts (less then 250 signs)
    full_text = models.TextField('Article')  ## field - for huge volume of texts
    date = models.DateTimeField('Date')  ## field - for date

    def __str__(self):
        """i don't know for what"""
        return self.title

    class Meta:
        """class for meta params (and name changing)"""
        verbose_name = 'Information'
        verbose_name_plural = 'Information'
