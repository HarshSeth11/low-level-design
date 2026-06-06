from handlers.leave_handler import LeaveHandler

class CEO(LeaveHandler):

    def handle(self, request):
        print(f"CEO approved {request.days} day(s) leave for {request.employee_name}.")