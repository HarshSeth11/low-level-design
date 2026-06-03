from reports.report import Report

class SalesReport(Report):

    def fetch_data(self):
        print("Data fetched for sales report.")

    def process_data(self):
        print("Data processed for sales report.")

    def generate_report(self):
        print("Sales report generated.")