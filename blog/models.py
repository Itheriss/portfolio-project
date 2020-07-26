from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    image =models.ImageField(upload_to="images/")
    body = models.TextField()
    bodyWords = []
    def summary(self):
        self.bodyWords = self.body.split()
        self.bodyWordsLim = self.bodyWords[:20]

        return ' '.join(self.bodyWordsLim) + ' ...'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
