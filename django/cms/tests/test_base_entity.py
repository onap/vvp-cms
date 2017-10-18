#
# ============LICENSE_START==========================================
# org.onap.vvp/engagementmgr
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
from abc import ABCMeta, abstractmethod
import http.client
import django
from django.test import TestCase
from django.test.client import Client
django.setup()


class TestBaseEntity(TestCase):
    __metaclass__ = ABCMeta

    def setUp(self):
        self.urlPrefix = "/api/"
        self.conn = http.client.HTTPConnection("127.0.0.1", 8000)
        self.c = Client()
        self.childSetup()

    def tearDown(self):
        self.conn.close()

    @abstractmethod
    def childSetup(self):
        pass

    def console_print(self, msg):
        print("======================= "
              "log from test "
              "=======================")
        print(msg)
        print("_____________________________________________________________")
