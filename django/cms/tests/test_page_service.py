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
import json

from mezzanine.pages.models import RichTextPage

from cms.management.commands import import_pages
from cms.tests.test_base_entity import TestBaseEntity


class PageServiceTestCase(TestBaseEntity):

    def childSetup(self):
        print("======================= "
              "PageServiceTestCase "
              "=======================")
        import_pages_command = import_pages.Command()
        import_pages_command.handle()

        self.documentation_page = \
            RichTextPage.objects.get(title="Documentation")
        self.base_page_content = "baseContentOfPage"
        self.base_page_title = "baseTitle"
        self.search_url = self.urlPrefix + 'pages/search/?keyword={keyword}'

        page = RichTextPage.objects.get_or_create(
            title=self.base_page_title,
            defaults={
                'content': self.base_page_content,
                'login_required': False}
        )
        print("Created basic page under documentation page:%s" % page[0].title)

    def testSearchPageByContent(self):
        response = self.c.get(self.search_url
                              .format(keyword=self.base_page_content))

        self.assertEqual(response.status_code, 200)
        self.console_print("Got 200 status from server, page search success")
        content = json.loads(response.content)

        self.assertEqual(len(content), 1)
        self.console_print("There is exactly one page that answers this query")
        self.assertEqual(content[0]['title'], self.base_page_title)
        self.console_print("The page is the requested one, test pass")

    def testSearchPageByTitle(self):
        response = self.c.get(self.search_url
                              .format(keyword=self.base_page_title))

        self.assertEqual(response.status_code, 200)
        self.console_print("Got 200 status from server, page search success")
        content = json.loads(response.content)

        self.assertEqual(len(content), 1)
        self.console_print("There is exactly one page that answers this query")
        self.assertEqual(content[0]['title'], self.base_page_title)
        self.console_print("The page is the requested one, test pass")

    def testSearchNotExistedPage(self):
        response = self.c.get(self.search_url
                              .format(keyword="pageNotExists"))

        self.assertEqual(response.status_code, 200)
        self.console_print("Got 200 status from server, page search success")
        content = json.loads(response.content)

        self.assertEqual(len(content), 0)
        self.console_print("There is no page that answers this query, "
                           "test pass")
