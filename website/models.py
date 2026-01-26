from django.db import models


class Lead(models.Model):
    SERVICE_CHOICES = [
        ("custom_website", "Custom Website Development"),
        ("shopify", "Shopify Store Development"),
        ("wordpress", "WordPress Website"),
        ("redesign", "Website Redesign"),
        ("maintenance", "Maintenance & Support"),
        ("seo", "SEO & Optimization"),
        ("other", "Other Services"),
    ]

    STATUS_CHOICES = [
        ("New", "New"),
        ("Contacted", "Contacted"),
        ("Closed", "Closed"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=150, blank=True)
    service = models.CharField(max_length=30, choices=SERVICE_CHOICES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="New")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.service})"


class Project(models.Model):
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=150)
    website_url = models.URLField()
    description = models.TextField()
    services = models.CharField(max_length=200)
    image = models.ImageField(upload_to="portfolio/")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class CMSContent(models.Model):
    page = models.CharField(max_length=50)
    key = models.CharField(max_length=100)
    value = models.TextField()

    class Meta:
        unique_together = ("page", "key")
        ordering = ("page", "key")

    def __str__(self):
        return f"{self.page} :: {self.key}"
