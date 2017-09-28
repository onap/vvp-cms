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
import os

def envbool(key, default=False, unknown=True):
    """Return a boolean value based on that of an environment variable.

    Environment variables have no native boolean type. They are always strings, and may be empty or
    unset (which differs from empty.) Furthermore, notions of what is "truthy" in shell script
    differ from that of python.

    This function converts environment variables to python boolean True or False in
    case-insensitive, expected ways to avoid pitfalls:

        "True", "true", and "1" become True
        "False", "false", and "0" become False
        unset or empty becomes False by default (toggle with 'default' parameter.)
        any other value becomes True by default (toggle with 'unknown' parameter.)

    """
    return {
        'true': True, '1': True, # 't': True,
        'false': False, '0': False, # 'f': False.
        '': default,
        }.get(os.getenv(key, '').lower(), unknown)
