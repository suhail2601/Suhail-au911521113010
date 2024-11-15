import random
import time

class WaterSystemSensors:
    def _init_(self):
        self.water_level = 50  
        self.water_pressure = 30 
        self.flow_rate = 10  
        self.is_leak_detected = False

    def read_sensors(self):
        
        self.water_level = random.randint(30, 90)
        self.water_pressure = random.randint(20, 60)
        self.flow_rate = random.randint(5, 20)
        self.is_leak_detected = random.choice([True, False])

        return {
            "water_level": self.water_level,
            "water_pressure": self.water_pressure,
            "flow_rate": self.flow_rate,
            "leak_detected": self.is_leak_detected,
        }

class SmartWaterSystem:
    def _init_(self, sensors):
        self.sensors = sensors
        self.valve_status = "Closed"
        self.pump_status = "Off"
        self.mode = "Manual"  

    def adjust_water_flow(self, desired_flow):
        print(f"Adjusting water flow to {desired_flow} GPM.")
        self.flow_rate = desired_flow

    def check_and_manage_system(self):
        sensor_data = self.sensors.read_sensors()

        if sensor_data["leak_detected"]:
            print("Leak detected! Shutting down pump and valves.")
            self.pump_status = "Off"
            self.valve_status = "Closed"
            return "Leak detected. System halted."

        if sensor_data["water_level"] < 40:
            self.pump_status = "On"
            print("Water level low, turning pump on.")
        elif sensor_data["water_level"] > 80:
            self.pump_status = "Off"
            print("Water level high, turning pump off.")

        if sensor_data["water_pressure"] < 25:
            self.valve_status = "Open"
            print("Water pressure too low, opening valves to increase pressure.")
        elif sensor_data["water_pressure"] > 50:
            self.valve_status = "Closed"
            print("Water pressure too high, closing valves.")

        return sensor_data

    def set_mode(self, mode):
        if mode in ["Manual", "Automatic"]:
            self.mode = mode
            print(f"System set to {mode} mode.")
        else:
            print("Invalid mode. Please choose 'Manual' or 'Automatic'.")

class AIWaterManagement:
    def _init_(self, system):
        self.system = system

    def optimize_system(self):
        print("AI is analyzing the water system...")
        sensor_data = self.system.check_and_manage_system()

        if sensor_data["water_level"] < 40:
            self.system.adjust_water_flow(15)  
        elif sensor_data["water_level"] > 80:
            self.system.adjust_water_flow(5)  


def main():
    sensors = WaterSystemSensors()
    system = SmartWaterSystem(sensors)
    ai_manager = AIWaterManagement(system)

    
    system.set_mode("Automatic")

    while True:
        ai_manager.optimize_system()
        time.sleep(5)  

if_name_ == "_main_":
    main()