from django.shortcuts import render
from django.conf import settings
import markdown


def swagger_index(request):
    return render(request, 'swagger_index.html')


def markdown_index(request):
    with open(f"{settings.BASE_DIR}/README.md", "r", encoding="UTF-8") as md:
        html = markdown.markdown(
            md.read(),
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
    context = {'html': html}
    return render(request, 'markdown_index.html', context)
