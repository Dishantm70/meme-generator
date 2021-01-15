from django.conf import settings
from django.db import models
from django_currentuser.middleware import get_current_user

from common.utils import generate_id


class Common(models.Model):
    id              = models.CharField(primary_key=True, default=generate_id,
                        max_length=22, editable=False, db_index=True)
    trash           = models.BooleanField(default=False, db_index=True)
    created_at      = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at     = models.DateTimeField(auto_now=True, editable=False)
    created_by      = models.ForeignKey(settings.AUTH_USER_MODEL,
                        null=True, editable=False, db_index=True,
                        on_delete=models.SET_NULL, related_name="%(class)s_created")
    modified_by     = models.ForeignKey(settings.AUTH_USER_MODEL,
                        null=True, editable=False, db_index=True,
                        on_delete=models.SET_NULL, related_name="%(class)s_modified")

    def save(self, *args, **kwargs):
        # get user from current request local thread
        user = get_current_user()

        if user and user.is_authenticated:
            self.modified_by = user

            # REF: https://stackoverflow.com/a/35647389/3016478
            # save created_by only if it's creating
            if self._state.adding:
                self.created_by = user

        # save the instance
        super().save(*args, **kwargs)

        # REF: https://stackoverflow.com/a/35647389/3016478
        # if update then only invalidate the cached property
        if not self._state.adding:
            self.refresh_from_db()