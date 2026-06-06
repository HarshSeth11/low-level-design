from handlers.leave_handler import LeaveHandler

class Director(LeaveHandler):

    def handle(self, request):
        if request.days <= 10:
            print(f"Director approved {request.days} day(s) leave for {request.employee_name}.")
        elif self.next_handler:
            self.next_handler.handle(request)