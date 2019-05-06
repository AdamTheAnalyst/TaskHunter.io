from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Master Model
# Handles Soft Deletes
class CommonModel(models.Model):

    created_by = models.ForeignKey(User,
                                   editable=False,
                                   related_name="+",
                                   on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User,
                                   editable=False,
                                   related_name="+",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(CommonModel, self).delete()


class Contact(CommonModel):

    name = models.CharField(max_length=255, blank=False)
    relation = models.CharField(max_length=255, blank=True)
    birthday = models.DateField()
    employer = models.TextField()

    def __str__(self):
        return "{}".format(self.name)


class ContactMethod(CommonModel):

    type = models.CharField(max_length=255,
                            blank=False,
                            choices=[
                                ("EMAIL", "Email"),
                                ("SLACK", "Slack"),
                                ("PHONE", "Phone"),
                                ("ADDRESS", "Address")
                            ])
    value = models.CharField(max_length=255)
    contact = models.ForeignKey(Contact,
                                related_name='contact_methods',
                                on_delete=models.CASCADE)


class ContactNote(CommonModel):

    type = models.CharField(max_length=255,
                            blank=False,
                            choices=[
                                ("GENERAL", "General"),
                                ("PERSONAL", "Personal"),
                                ("BUSINESS", "Business")
                            ])
    note = models.TextField(blank=False)
    contact = models.ForeignKey(Contact,
                                related_name='contact_notes',
                                on_delete=models.CASCADE)


class TaskType(CommonModel):
    value = models.CharField(max_length=15)

    def __str__(self):
        return "{}".format(self.value)


class Task(CommonModel):

    title = models.CharField(max_length=500)
    task_type = models.ForeignKey(TaskType, null=True, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
