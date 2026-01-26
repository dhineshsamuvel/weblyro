from .models import CMSContent

def cms_content(request):
    data = {}
    for item in CMSContent.objects.all():
        data[item.key] = item.value
    return {"content": data}
