import json 
from datetime import datetime, timedelta

class User:
    def __init__(self, userId,apartementNumber,carCapacity):
        self.userId = userId
        self.apartementNumber = apartementNumber
        self.carCapacity = carCapacity
        self.evSessions = []
        
    def chargingSession(self, startTime, endTime , capacity):
        if (endTime - startTime) > 15  : 
            session = {
                'start_Time' : startTime , 
                'end_Time' : endTime , 
                'desired_capacity' : capacity , 
                'charged_energy' : 0,
                'cost' : 0
            }
            if session['desired_capacity'] != None:
                session['charged_energy'] = session['desired_capacity']
            else :
                session['charged_energy'] = 1/2 * self.carCapacity
            if session['charged_energy'] <20 
                self.evSessions.append(session)
                return json.dumps(self.evSessions)
    
    def checkbatterycapacityrequirements(self, required_percentage, target_time):
        suitable_sessions = []
        for session in self.ev_sessions:
            remaining_charge = session.energy_consumed * (1 - session.charge_percentage)
            time_required = remaining_charge / session.charge_rate
            if time_required <= target_time and session.charge_percentage >= required_percentage:
                suitable_sessions.append(session)
        return suitable_sessions


    def get_evSessions(self):
        return self.get_evSessions
    def get_apartementNumber(self):
        return self.apartementNumber
    def get_userId(self) : 
        return self.userId       
