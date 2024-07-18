from django.db import models

# Create your models here.


class Skill_Cards(models.Model):
    """ 
        Skill Card Images
    """

    name = models.CharField(max_length=20)
    friendly_name = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_friendly(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = 'Skill Card Images'

class Offerings(models.Model):
    """
        What can I do for you
    """

    name = models.CharField(max_length=20)
    friendly_name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_friendly(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = 'What I Offer'

class Current_Projects(models.Model):
    """
        Current projects/clients
    """

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=250, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    git_link = models.CharField(max_length=100, blank=True, null=True)
    live_site = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_friendly(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = 'Current Projects'

class Work_History(models.Model):
    """
        Work History/CV/Resume
    """

    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(max_length=200)
    dates = models.TextField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Work History'