from reports.report import Report

class InventoryReport(Report):

    def fetch_data(self):
        print("Data fetched for inventory report.")

    def process_data(self):
        print("Data processed for inventory report.")

    def generate_report(self):
        print("Inventory report generated.")