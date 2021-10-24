class FilterModule(object):

    def filters(self):
        return {
            'build_report': self.build_report,
        }
    
    def build_report(self, flows):
        report = list()

        if isinstance(flows,list):
            for each in flows:
                interface = dict()
                if 'multi-routing-engine-results' in each['parsed_output']:
                    flows = each['parsed_output']['multi-routing-engine-results']['multi-routing-engine-item']
                    node0 = flows[0]['security-flow-information']['flow-session-information']['displayed-session-count']
                    node1 = flows[1]['security-flow-information']['flow-session-information']['displayed-session-count']
                    interface['flows'] = int(node0) + int(node1)
                    interface['interface'] = each['kwargs']['interface']
                    report.append(interface)
                elif 'security-flow-information' in each['parsed_output']:
                    interface['flows'] = each['parsed_output']['security-flow-information']['flow-session-information']['displayed-session-count']
                    interface['interface'] = each['kwargs']['interface']
                    report.append(interface)

        return report
