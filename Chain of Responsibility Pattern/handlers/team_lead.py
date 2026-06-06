from handlers.leave_handler import LeaveHandler

class TeamLead(LeaveHandler):

    def handle(self, request):
        if request.days <= 2:
            print(f"Team Lead approved {request.days} day(s) leave for {request.employee_name}.")
        elif self.next_handler:
            self.next_handler.handle(request)