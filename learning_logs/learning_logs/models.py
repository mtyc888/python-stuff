from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the model"""
        return self.text
    
class Entry(models.Model):
    """Something specific learned about a topic"""

    # foreign key, tied to Topic. 'on_delete' means that when a topic is deleted, all relating entries will go as well
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # this is to tell django to use 'entries' for multiple Entry objects, or else it will use 'entrys'
        verbose_name_plural = 'entries'
    def __str__(self):
        """Returns a string representation of the model"""
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        else:
            return self.text 