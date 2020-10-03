from django.conf import settings
from django.contrib.auth import backends, get_user_model
from django.db.models import Q

from .models import Account


class PhoneBackend(backends.ModelBackend):

    def authenticate(username=None, input_OTP=None, actual_OTP=None, backend='PhoneBackend'):
        if username is None:
            return
        usermodel = get_user_model()
        try:
            user = Account.objects.get(phone=username)
            #print ("Phone backend found {} ".format(user))
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
