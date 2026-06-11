from datetime import datetime

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []

        return cls._instance

    def _log(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_message = f"{timestamp} [{level.upper()}] {message}"

        self.logs.append(log_message)
        
        print(log_message)

    def info(self, message):
        self._log("info", message)

    def warning(self, message):
        self._log("warning", message)
    
    def error(self, message):
        self._log("error", message)

    def show_logs(self):
        for log in self.logs:
            print(log)