from abc import ABC, abstractmethod

class Report(ABC):

    def generate(self):
        self.fetch_data()
        self.process_data()
        self.generate_report()
        self.send_report()
    
    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def generate_report(self):
        pass

    def send_report(self):
        print("Report sent successfully.")