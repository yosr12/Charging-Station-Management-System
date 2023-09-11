from User import User
from datetime import datetime, timedelta

class BillingSystem : 
    def __init__(self,User) : 
        self.User = User
        self.sessionRecords = []

    def calculate_cost(self, energy_price_per_kwh):
        duration_hours = (self.User.evSessions['end_Time'] - self.User.evSessions['start_Time']).total_seconds() / 3600
        cost = self.User.evSessions['charged_energy'] * energy_price_per_kwh * duration_hours
        return cost

    def record_charging_session(self, energy_price_per_kwh):
        cost = self.calculate_cost(self.User.evSessions['end_Time'], self.User.evSessions['start_Time'], self.User.evSessions['charged_energy'], energy_price_per_kwh)
        session_record = [User.userId, self.User.evSessions['end_Time'],  self.User.evSessions['start_Time'], self.User.evSessions['charged_energy'], cost]
        self.session_records.append(session_record) 
        return session_record   


