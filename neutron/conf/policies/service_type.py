#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from oslo_policy import policy

from neutron.conf.policies import base


rules = [
    policy.DocumentedRuleDefault(
        'get_service_provider',
        base.RULE_ANY,
        'Get service providers',
        [
            {
                'method': 'GET',
                'path': '/service-providers',
            },
        ]
    ),
]


def list_rules():
    return rules
