from django.db import models
from django_mailer_plus import constants, managers
import datetime


PRIORITIES = (
    (constants.PRIORITY_HIGH, 'high'),
    (constants.PRIORITY_NORMAL, 'normal'),
    (constants.PRIORITY_LOW, 'low'),
)

RESULT_CODES = (
    (constants.RESULT_SENT, 'success'),
    (constants.RESULT_SKIPPED, 'not sent (blacklisted)'),
    (constants.RESULT_FAILED, 'failure'),
)

class Attachment(models.Model):
    """
    A message attachment
    """
    filename = models.CharField(max_length=200)

    class Meta:
        app_label = 'django_mailer_plus'

class Message(models.Model):
    """
    An email message.
    
    The ``to_address``, ``from_address`` and ``subject`` fields are merely for
    easy of access for these common values. The ``encoded_message`` field
    contains the entire encoded email message ready to be sent to an SMTP
    connection.
    
    """
    to_address = models.CharField(max_length=200)
    from_address = models.CharField(max_length=200)
    subject = models.CharField(max_length=255)
    attachment = models.ManyToManyField(Attachment)

    encoded_message = models.TextField()
    html_message = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ('date_created',)
        app_label = 'django_mailer_plus'

    def __unicode__(self):
        return '%s: %s' % (self.to_address, self.subject)

class QueuedMessage(models.Model):
    """
    A queued message.
    
    Messages in the queue can be prioritised so that the higher priority
    messages are sent first (secondarily sorted by the oldest message).
    
    """
    message = models.OneToOneField(Message, editable=False)
    priority = models.PositiveSmallIntegerField(choices=PRIORITIES,
                                            default=constants.PRIORITY_NORMAL)
    deferred = models.DateTimeField(null=True, blank=True)
    retries = models.PositiveIntegerField(default=0)
    date_queued = models.DateTimeField(default=datetime.datetime.now)

    objects = managers.QueueManager()

    class Meta:
        ordering = ('priority', 'date_queued')
        app_label = 'django_mailer_plus'

    def defer(self):
        self.deferred = datetime.datetime.now()
        self.save()


class Blacklist(models.Model):
    """
    A blacklisted email address.

    Messages attempted to be sent to e-mail addresses which appear on this
    blacklist will be skipped entirely.
    
    """
    email = models.EmailField(max_length=200)
    date_added = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'blacklisted e-mail address'
        verbose_name_plural = 'blacklisted e-mail addresses'
        app_label = 'django_mailer_plus'


class Log(models.Model):
    """
    A log used to record the activity of a queued message.
    
    """
    message = models.ForeignKey(Message, editable=False)
    result = models.PositiveSmallIntegerField(choices=RESULT_CODES)
    date = models.DateTimeField(default=datetime.datetime.now)
    log_message = models.TextField()

    class Meta:
        ordering = ('-date',)
        app_label = 'django_mailer_plus'
