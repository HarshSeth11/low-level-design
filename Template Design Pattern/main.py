from reports.employee_report import EmployeeReport
from reports.inventory_report import InventoryReport
from reports.sales_report import SalesReport


def main():
    print("Generating Sales Report:")
    sales_report = SalesReport()
    sales_report.generate()

    print("\nGenerating Inventory Report:")
    inventory_report = InventoryReport()
    inventory_report.generate()

    print("\nGenerating Employee Report:")
    employee_report = EmployeeReport()
    employee_report.generate()

if __name__ == "__main__":
    main()