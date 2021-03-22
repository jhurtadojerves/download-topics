"""Import base views"""

# Django
from django.views.generic import FormView
from django.shortcuts import render

# Forms
from .forms import DownloadForm

# Third party integration
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class DownloadView(FormView):
    """View to download html file"""

    form_class = DownloadForm
    template_name = "index.html"

    def form_valid(self, form):
        url_base = form.cleaned_data["url"]
        initial_page = form.cleaned_data["initial_page"]
        end_page = form.cleaned_data["end_page"]
        name_list = url_base.split("/")[-2:][:-1]
        name = "".join(name_list)
        data = ""
        for page in range(initial_page, end_page + 1):
            data += f"<br><br><br><h2>Página {page} de {end_page} </h2><br><br><br>"
            url = url_base if page == 1 else f"{url_base}page-{page}"
            response = requests.get(url, allow_redirects=True)
            html = BeautifulSoup(response.text, features="html.parser")
            posts = html.select(".post_wrap")
            for post in posts:
                data += str(post)
            data += ""
        return render(self.request, "download.html", {"data": data, "name": name},)
