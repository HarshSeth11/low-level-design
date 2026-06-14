from notification_template_factory import NotificationTemplateFactory

success1 = NotificationTemplateFactory.get_template("SUCCESS")
success2 = NotificationTemplateFactory.get_template("SUCCESS")
failed1 = NotificationTemplateFactory.get_template("FAILED")
failed2 = NotificationTemplateFactory.get_template("FAILED")

print(success1 == success2)
print(failed1 == failed2)

print(success1 == failed1)

success1.send("Harsh")
failed1.send("Someone")