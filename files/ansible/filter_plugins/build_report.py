"""Compile a report to share.
(c) 2022 Calvin Remsburg <cremsburg.dev@gmail.com>
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


class FilterModule(object):  # pylint: disable=useless-object-inheritance
    """Return a report of interfaces with their sessions."""

    def filters(self):
        """Add this custom filter plugin to our list of Ansible's filters."""
        return {
            "build_report": self.build_report,
        }

    def build_report(self, flows):
        """Compile a report to share."""
        report = []

        if isinstance(flows, list):
            for each in flows:
                interface = dict()
                if "multi-routing-engine-results" in each["parsed_output"]:
                    flows = each["parsed_output"]["multi-routing-engine-results"][
                        "multi-routing-engine-item"
                    ]
                    node0 = flows[0]["security-flow-information"][
                        "flow-session-information"
                    ]["displayed-session-count"]
                    node1 = flows[1]["security-flow-information"][
                        "flow-session-information"
                    ]["displayed-session-count"]
                    interface["flows"] = int(node0) + int(node1)
                    interface["interface"] = each["kwargs"]["interface"]
                    report.append(interface)
                elif "security-flow-information" in each["parsed_output"]:
                    interface["flows"] = each["parsed_output"][
                        "security-flow-information"
                    ]["flow-session-information"]["displayed-session-count"]
                    interface["interface"] = each["kwargs"]["interface"]
                    report.append(interface)
                else:
                    pass

        return report
