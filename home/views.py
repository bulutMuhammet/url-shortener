from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from home.models import ShortURL
from home.serializers import URLSerializer


class ShortenURL(APIView):
    serializer_class = URLSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        short_url_obj = serializer.save()
        short_url = f"{request.build_absolute_uri('/')}{short_url_obj.short_url}"
        original_url = short_url_obj.original_url
        return Response(status=status.HTTP_201_CREATED, data={
            "Original URL": original_url,
            "Short URL": short_url
        })


class RedirectURLView(APIView):

    def get(self, request, *args, **kwargs):
        short_code = kwargs['short_code']
        short_url_obj = get_object_or_404(ShortURL, short_url=short_code)
        return HttpResponseRedirect(redirect_to=short_url_obj.original_url)


class ShortenURLTemplateView(TemplateView):
    template_name = 'shorten_url.html'
    serializer_class = URLSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.POST)
        if serializer.is_valid():
            short_url_obj = serializer.save()
            short_url = f"{request.build_absolute_uri('/')}{short_url_obj.short_url}"
            original_url = short_url_obj.original_url
            context = {
                "original_url": original_url,
                "short_url": short_url
            }
        else:
            context = {
                "error": serializer.errors["original_url"][0]
            }

        return self.render_to_response(context)
