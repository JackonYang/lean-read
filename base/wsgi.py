#-*- coding:utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")

import sys
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.append(current_dir)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
