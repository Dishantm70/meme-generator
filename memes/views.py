from rest_framework.response import Response
from rest_framework.views import APIView

from memes.permissions import CookieConsentAcceptedPermission
from memes.utils import get_memes


class MemesView(APIView):
    permission_classes = [CookieConsentAcceptedPermission, ]

    def get(self, request):
        status_code, memes = get_memes()
        return Response(memes, status_code)

