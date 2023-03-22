from django.contrib.sites.models import Site
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny


class AccountConfirmEmailRedirectView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def redirect(self, request, *args, **kwargs):
        site = Site.objects.get_current()
        return redirect(
            f"https://{site.domain}/auth/account-confirm-email/?key={kwargs['key']}"
        )

    def get(self, request, *args, **kwargs):
        return self.redirect(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.redirect(request, *args, **kwargs)


class PasswordResetConfirmRedirectView(generics.GenericAPIView):
    def redirect(self, request, *args, **kwargs):
        site = Site.objects.get_current()
        return redirect(
            f"https://{site.domain}/auth/password-reset-confirm/?uid={kwargs['uid']}&token={kwargs['token']}"
        )

    def get(self, request, *args, **kwargs):
        return self.redirect(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.redirect(request, *args, **kwargs)
