import datetime, uuid, random

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class PhoneBackend(ModelBackend):

    def authenticate(phone=None, input_OTP=None, actual_OTP=None):
        if phone is None:
            return
        user = get_user_model()
        print (user)
        try:
            user = usermodel.objects.get(Q(phone__iexact=phone))
            if (actual_OTP==None):
                return user
            else:
                if (input_OTP==actual_OTP):
                    return user
        except Exception as e:
            pass

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
