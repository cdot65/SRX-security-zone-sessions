"""Clean up output from security zone information.
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
    """Return a dictionary of interfaces with their sessions."""

    def filters(self):
        """Add this custom filter plugin to our list of Ansible's filters."""
        return {
            "get_zone_interfaces": self.get_zone_interfaces,
        }

    def get_zone_interfaces(self, zones):
        """Retrieve the interfaces found in each security zone."""
        dmz_interfaces = []
        lan_interfaces = []
        wan_interfaces = []

        # ####################################################################
        # If the SRX is in cluster mode
        # ####################################################################
        if "multi-routing-engine-results" in zones:

            zone_information = zones["multi-routing-engine-results"][
                "multi-routing-engine-item"
            ]["zones-information"]["zones-security"]

            if isinstance(zone_information, list):
                for each in zone_information:
                    if each["zones-security-zonename"] == "DMZ":
                        if isinstance(
                            each["zones-security-interfaces"][
                                "zones-security-interface-name"
                            ],
                            list,
                        ):
                            for interface in each["zones-security-interfaces"][
                                "zones-security-interface-name"
                            ]:
                                dmz_interfaces.append(interface)
                        else:
                            dmz_interfaces.append(
                                each["zones-security-interfaces"][
                                    "zones-security-interface-name"
                                ]
                            )

                    elif each["zones-security-zonename"] == "LAN":
                        if isinstance(
                            each["zones-security-interfaces"][
                                "zones-security-interface-name"
                            ],
                            list,
                        ):
                            for interface in each["zones-security-interfaces"][
                                "zones-security-interface-name"
                            ]:
                                lan_interfaces.append(interface)
                        else:
                            lan_interfaces.append(
                                each["zones-security-interfaces"][
                                    "zones-security-interface-name"
                                ]
                            )

                    elif each["zones-security-zonename"] == "WAN":
                        if isinstance(
                            each["zones-security-interfaces"][
                                "zones-security-interface-name"
                            ],
                            list,
                        ):
                            for interface in each["zones-security-interfaces"][
                                "zones-security-interface-name"
                            ]:
                                wan_interfaces.append(interface)
                        else:
                            wan_interfaces.append(
                                each["zones-security-interfaces"][
                                    "zones-security-interface-name"
                                ]
                            )

                    else:
                        pass

            zone_ifaces = dict()
            zone_ifaces["dmz_interfaces"] = dmz_interfaces
            zone_ifaces["lan_interfaces"] = lan_interfaces
            zone_ifaces["wan_interfaces"] = wan_interfaces
            return zone_ifaces

        # ####################################################################
        # If the SRX is not in cluster mode
        # ####################################################################
        else:
            zone_information = zones["zones-information"]["zones-security"]

            if isinstance(zone_information, list):
                for each in zone_information:
                    if each["zones-security-zonename"] == "DMZ":
                        if isinstance(
                            each["zones-security-interfaces"][
                                "zones-security-interface-name"
                            ],
                            list,
                        ):
                            for interface in each["zones-security-interfaces"][
                                "zones-security-interface-name"
                            ]:
                                dmz_interfaces.append(interface)
                        else:
                            dmz_interfaces.append(
                                each["zones-security-interfaces"][
                                    "zones-security-interface-name"
                                ]
                            )

                    elif each["zones-security-zonename"] == "LAN":
                        if isinstance(
                            each["zones-security-interfaces"][
                                "zones-security-interface-name"
                            ],
                            list,
                        ):
                            for interface in each["zones-security-interfaces"][
                                "zones-security-interface-name"
                            ]:
                                lan_interfaces.append(interface)
                        else:
                            lan_interfaces.append(
                                each["zones-security-interfaces"][
                                    "zones-security-interface-name"
                                ]
                            )

                    elif each["zones-security-zonename"] == "WAN":
                        if isinstance(
                            each["zones-security-interfaces"][
                                "zones-security-interface-name"
                            ],
                            list,
                        ):
                            for interface in each["zones-security-interfaces"][
                                "zones-security-interface-name"
                            ]:
                                wan_interfaces.append(interface)
                        else:
                            wan_interfaces.append(
                                each["zones-security-interfaces"][
                                    "zones-security-interface-name"
                                ]
                            )

                    else:
                        pass

            zone_ifaces = dict()
            zone_ifaces["dmz_interfaces"] = dmz_interfaces
            zone_ifaces["lan_interfaces"] = lan_interfaces
            zone_ifaces["wan_interfaces"] = wan_interfaces
            return zone_ifaces
