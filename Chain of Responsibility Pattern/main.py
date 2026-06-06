from handlers.ceo import CEO
from handlers.director import Director
from handlers.manager import Manager
from handlers.team_lead import TeamLead

from models.leave_requests import LeaveRequest

def main():
    # Create handlers
    ceo = CEO()
    director = Director()
    manager = Manager()
    team_lead = TeamLead()

    # Set up the chain of responsibility
    team_lead.set_next_handler(manager)
    manager.set_next_handler(director) 
    director.set_next_handler(ceo)
    
    # Create leave requests
    leave_request_1 = LeaveRequest(employee_name="Alice", days=2)
    leave_request_2 = LeaveRequest(employee_name="Bob", days=4)
    leave_request_3 = LeaveRequest(employee_name="Charlie", days=8)
    leave_request_4 = LeaveRequest(employee_name="David", days=25)

    # Process leave requests
    print("Processing leave request 1:")
    team_lead.handle(leave_request_1)
    print("\nProcessing leave request 2:")
    team_lead.handle(leave_request_2)
    print("\nProcessing leave request 3:")
    team_lead.handle(leave_request_3)
    print("\nProcessing leave request 4:")
    team_lead.handle(leave_request_4)

if __name__ == "__main__":
    main()