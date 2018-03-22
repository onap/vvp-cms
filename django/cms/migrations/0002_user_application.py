# ============LICENSE_START==========================================
# org.onap.vvp/cms
# ===================================================================
# Copyright © 2017 AT&T Intellectual Property. All rights reserved.
# ===================================================================
#
# Unless otherwise specified, all software contained herein is licensed
# under the Apache License, Version 2.0 (the “License”);
# you may not use this software except in compliance with the License.
# You may obtain a copy of the License at
#
#             http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
#
# Unless otherwise specified, all documentation contained herein is licensed
# under the Creative Commons License, Attribution 4.0 Intl. (the “License”);
# you may not use this documentation except in compliance with the License.
# You may obtain a copy of the License at
#
#             https://creativecommons.org/licenses/by/4.0/
#
# Unless required by applicable law or agreed to in writing, documentation
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ============LICENSE_END============================================
#
# ECOMP is a trademark and service mark of AT&T Intellectual Property.
from __future__ import unicode_literals
from django.db import migrations
from django.contrib.auth import get_user_model
from oauth2_provider.models import get_application_model

from django.conf import settings

# This migration file creates default admin user for the mezzanine server
# and default EM client app and default categories

DEFAULT_USERNAME = settings.CMS_APP_USER
DEFAULT_PASSWORD = settings.CMS_APP_USER_PASSWORD
DEFAULT_EMAIL = settings.CMS_APP_USER_MAIL
DEFAULT_CLIENT_ID = settings.CMS_APP_CLIENT_ID
DEFAULT_CLIENT_SECRET = settings.CMS_APP_CLIENT_SECRET
CMS_APP_NAME = settings.CMS_APP_NAME

'''
Create the admin user for the CSM server
'''


def create_emuser(apps, schema_editor):
    User = get_user_model()
    args = (DEFAULT_USERNAME, DEFAULT_EMAIL, DEFAULT_PASSWORD)
    try:
        User.objects.get(username=DEFAULT_USERNAME)
    except Exception:
        User.objects.create_superuser(*args)


'''
Create the EM application which acts as a client to the CSM server
'''


def create_emapp(apps, schema_editor):

    Application = get_application_model()
    application = None
    try:
        application = Application.objects.get(client_id=DEFAULT_CLIENT_ID)
    except Exception:
        # If client_secret and client_id not supplied, a unique one will be
        # generated
        application = Application.objects.create(
            name=CMS_APP_NAME,
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_CLIENT_CREDENTIALS,
            client_secret=DEFAULT_CLIENT_SECRET,
            client_id=DEFAULT_CLIENT_ID,
        )
    print("Created ICE application=" + str(application))


class Migration(migrations.Migration):

    dependencies = [('cms', '0001_initial'),
                    ('twitter', '0001_initial'),
                    ('oauth2_provider', '0004_auto_20160525_1623'),
                    ]

    operations = [
        migrations.RunPython(create_emapp),
        migrations.RunPython(create_emuser),
    ]
