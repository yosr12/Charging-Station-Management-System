from datetime import datetime, timedelta

from ChargingPort import ChargingPort
class ChargingStation:
    def __init__(self, numPorts):
        self.chargingPorts = []
        for i in range(numPorts):
            port = ChargingPort(i+1)
            self.chargingPorts.append(port) 
    
    def listChargingPorts(self):
        for port in self.chargingPorts:
            print(port)

    def getAvailablePorts(self):
        availablePorts = []
        for port in self.chargingPorts:
            if port.is_available:
                availablePorts.append(port)
        return availablePorts

    def getPortsWithEstimated(self, minCharge):
        portsWithCharge = []
        for port in self.chargingPorts:
            if port.estimatedCharge is not None and port.estimatedCharge >= minCharge:
                portsWithCharge.append(port)
        return portsWithCharge               

    filePath = 'car_1_profile.csv'


    def loadData(self,filePath):
        #main for test from datasets
        print('main')
        with open(filePath, 'r') as file:
            reader = csv.reader(file, delimiter=';')
        for row in reader:
            if len(row) >= 4:
                port_id = int(row[0])
                availability = int(row[1])
                estimatedCharge = row[2] if row[2] else None
                charge_requirements = row[3] if row[3] else None
                if 1 <= port_id <= len(self.charging_ports):
                    port = self.charging_ports[port_id - 1]
                    port.available = bool(availability)
                    port.estimatedCharge = estimatedCharge
                    port.chargeRequirements = chargeRequirements




