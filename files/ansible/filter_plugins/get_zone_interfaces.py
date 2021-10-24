class FilterModule(object):

    def filters(self):
        return {
            'get_zone_interfaces': self.get_zone_interfaces,
        }
    
    def get_zone_interfaces(self, zones):
        dmz_lab_interfaces = list()
        home_interfaces = list()
        internet_interfaces = list()

        if 'multi-routing-engine-results' in zones:

            zone_information = zones['multi-routing-engine-results']['multi-routing-engine-item']['zones-information']['zones-security']

            if isinstance(zone_information,list):
                for each in zone_information:
                    if each['zones-security-zonename'] == "DMZ_LAB":
                        if isinstance(each['zones-security-interfaces']['zones-security-interface-name'],list):
                            for interface in each['zones-security-interfaces']['zones-security-interface-name']:
                                dmz_lab_interfaces.append(interface)
                        else:
                            dmz_lab_interfaces.append(each['zones-security-interfaces']['zones-security-interface-name'])

                    elif each['zones-security-zonename'] == "HOME":
                        if isinstance(each['zones-security-interfaces']['zones-security-interface-name'],list):
                            for interface in each['zones-security-interfaces']['zones-security-interface-name']:
                                home_interfaces.append(interface)
                        else:
                            home_interfaces.append(each['zones-security-interfaces']['zones-security-interface-name'])

                    elif each['zones-security-zonename'] == "INTERNET":
                        if isinstance(each['zones-security-interfaces']['zones-security-interface-name'],list):
                            for interface in each['zones-security-interfaces']['zones-security-interface-name']:
                                internet_interfaces.append(interface)
                        else:
                            internet_interfaces.append(each['zones-security-interfaces']['zones-security-interface-name'])

                    else:
                        pass

            zone_ifaces = dict()
            zone_ifaces['dmz_lab_interfaces'] = dmz_lab_interfaces
            zone_ifaces['home_interfaces'] = home_interfaces
            zone_ifaces['internet_interfaces'] = internet_interfaces
            return zone_ifaces

        elif 'zones-information' in zones:

            zone_information = zones['zones-information']['zones-security']

            if isinstance(zone_information,list):
                for each in zone_information:
                    if each['zones-security-zonename'] == "DMZ_LAB":
                        if isinstance(each['zones-security-interfaces']['zones-security-interface-name'],list):
                            for interface in each['zones-security-interfaces']['zones-security-interface-name']:
                                dmz_lab_interfaces.append(interface)
                        else:
                            dmz_lab_interfaces.append(each['zones-security-interfaces']['zones-security-interface-name'])

                    elif each['zones-security-zonename'] == "HOME":
                        if isinstance(each['zones-security-interfaces']['zones-security-interface-name'],list):
                            for interface in each['zones-security-interfaces']['zones-security-interface-name']:
                                home_interfaces.append(interface)
                        else:
                            home_interfaces.append(each['zones-security-interfaces']['zones-security-interface-name'])

                    elif each['zones-security-zonename'] == "INTERNET":
                        if isinstance(each['zones-security-interfaces']['zones-security-interface-name'],list):
                            for interface in each['zones-security-interfaces']['zones-security-interface-name']:
                                internet_interfaces.append(interface)
                        else:
                            internet_interfaces.append(each['zones-security-interfaces']['zones-security-interface-name'])

                    else:
                        pass

            zone_ifaces = dict()
            zone_ifaces['dmz_lab_interfaces'] = dmz_lab_interfaces
            zone_ifaces['home_interfaces'] = home_interfaces
            zone_ifaces['internet_interfaces'] = internet_interfaces
            return zone_ifaces

