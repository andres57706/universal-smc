from django.db import models


class Search(models.Model):
    keywords = models.CharField(max_length=200, null=False)
    customer_ip = models.CharField(max_length=30, null=True)
    issued_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return f"{self.keywords} issued at: {self.issued_at.strftime('%Y-%m-%d %H-%M')}"
