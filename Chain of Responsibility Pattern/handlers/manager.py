from handlers.leave_handler import LeaveHandler

class Manager(LeaveHandler):

    def handle(self, request):
        if request.days <= 5:
            print(f"Manager approved {request.days} day(s) leave for {request.employee_name}.")
        elif self.next_handler:
            self.next_handler.handle(request)