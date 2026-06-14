from notification_template import NotificationTemplate

class NotificationTemplateFactory:
    _templates = {}

    @classmethod
    def get_template(cls, template_name):
        if template_name not in cls._templates:
            if template_name == "SUCCESS":
                cls._templates[template_name] = NotificationTemplate(
                    "Payment Successful",
                    "Your payment was successful."
                )
            elif template_name == "FAILED":
                cls._templates[template_name] = NotificationTemplate(
                    "Payment Failed",
                    "Your payment failed."
                )
        
        return cls._templates[template_name]
    