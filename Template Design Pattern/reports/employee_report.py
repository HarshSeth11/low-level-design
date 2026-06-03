from reports.report import Report

class EmployeeReport(Report):

    def fetch_data(self):
        print("Data fetched for employee report.")

    def process_data(self):
        print("Data processed for employee report.")

    def generate_report(self):
        print("Employee report generated.")