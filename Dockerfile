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
FROM python:alpine

RUN apk add --no-cache \
    autoconf \
    gcc \
    git \
    jpeg-dev \
    libpq \
    linux-headers \
    musl-dev \
    postgresql-dev \
    zlib-dev \
    && :

COPY docker-entrypoint.sh /
COPY django /srv/

RUN ln -s -f /opt/configmaps/settings/__init__.py /srv/cms/settings/__init__.py; \
    ln -s -f /opt/configmaps/settings/storage.py /srv/cms/settings/storage.py

RUN pip install --upgrade setuptools && \
    pip install gunicorn && \
    pip install -r /srv/requirements.txt

#Git is required only for pulling the mezzanine api from forked project 
RUN apk del \
    autoconf \
    gcc \
    git \
    linux-headers \
    musl-dev \
    postgresql-dev \
    && :
ENTRYPOINT ["/docker-entrypoint.sh"]
