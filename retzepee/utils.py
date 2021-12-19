from typing import Optional, Type

from django.test import TestCase
from django.urls import resolve
from django.views import View


def coerce_bool_from_string(string: str) -> bool:
    if string in ('1', 'true', 'True', 'y', 'Y', 'yes', 'Yes'):
        return True
    return False


class RetzepeeTestCase(TestCase):
    def assertURLResolvesToView(self, url: str, view_cls: Type[View], msg: Optional[str] = None):
        resolved = resolve(url)
        resolved_cls = resolved.func.view_class

        if resolved_cls != view_cls:
            msg = self._formatMessage(msg, '%s resolved to %s, expected %s' % (url, repr(resolved_cls), repr(view_cls)))
            raise self.failureException(msg)
