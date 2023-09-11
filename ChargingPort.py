class ChargingPort:
    def __init__(self, portId):
        self.portId = portId
        self.available = True
        self.estimatedCharge = None
        self.chargeRequirements = None

    def getPortInfo(self): 
        return {
            "port_id": self.port_id,
            "is_available": self.is_available,
            "estimated_charge": self.estimated_charge,
            "charge_requirements": self.charge_requirements
        }


    def get_available(self):
        return self.available
    def get_estimatedCharge(self):
        return self.estimatedCharge
    def get_chargeRequirements(self):
        return self.chargeRequirements
