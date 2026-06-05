"""Python 3.10+ / Django 2.0 compatibility shims."""

import collections
import collections.abc

# 1. collections.Iterator etc. moved to collections.abc in Python 3.10+
for _name in ('Iterator', 'Iterable', 'Mapping', 'MutableMapping', 'Sequence'):
    if not hasattr(collections, _name):
        setattr(collections, _name, getattr(collections.abc, _name))

# 2. Python 3.11 removed 'codeset' kwarg from gettext.translation()
import gettext as _gettext
_orig_translation = _gettext.translation

def _patched_translation(*args, **kwargs):
    kwargs.pop('codeset', None)
    return _orig_translation(*args, **kwargs)

_gettext.translation = _patched_translation
