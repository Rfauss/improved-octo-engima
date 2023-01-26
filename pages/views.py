from django.views.generic import TemplateView, DetailView
from django.shortcuts import render

# import openai

# Create your views here.

# openai.api_key = "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"


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


# def getResponse(request):
#     if request.method == "POST":
#         animal = request.form["animal"]
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=generate_prompt(animal),
#             temperature=0.6,
#         )
#     return render(request, "about.html", response.choices[0].text)
