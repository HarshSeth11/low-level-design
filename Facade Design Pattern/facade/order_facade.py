from subsystems.delivery_service import DeliveryService
from subsystems.payment_service import PaymentService
from subsystems.inventory_service import InventoryService
from subsystems.notification_service import NotificationService
from subsystems.restaurant_service import RestaurantService

class OrderFacade:
    def __init__(self):
        self.delivery_service = DeliveryService()
        self.payment_service = PaymentService()
        self.inventory_service = InventoryService()
        self.notification_service = NotificationService()
        self.restaurant_service = RestaurantService()

    def place_order(self, amount):
        # Check inventory
        self.inventory_service.check_inventory()

        # Payment Service
        self.payment_service.process_payment(amount)

        # Restrurant Service
        self.restaurant_service.prepare_order()

        # Notification Service
        self.notification_service.send_notification()

        # Delivery Service 
        self.delivery_service.assign_delivery_partner()
