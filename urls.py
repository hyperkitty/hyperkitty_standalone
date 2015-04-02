# -*- coding: utf-8 -*-
# Copyright (C) 1998-2012 by the Free Software Foundation, Inc.
#
# This file is part of HyperKitty.
#
# HyperKitty is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# HyperKitty is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# HyperKitty.  If not, see <http://www.gnu.org/licenses/>.

"""
The aim of this file is to give an example of a Django site where hyperkitty
would be a component, but not the only component. If you only want to run
HyperKitty, just set the ROOT_URLCONF to "hyperkitty.urls" in your settings.py
configuration file.
"""

from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

# Comment the next two lines to disable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('hyperkitty.views.index.index'))),
    #url(r'^postorius/', include('postorius.urls')),
    url(r'^hyperkitty/', include('hyperkitty.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social'), {"SSL": True}),
    url(r'', include('django_browserid.urls'), {"SSL": True}),
)
