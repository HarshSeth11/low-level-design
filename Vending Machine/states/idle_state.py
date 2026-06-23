from states.vending_machine_state import VendingMachineState
from factory.product_factory import ProductFactory


class IdleState(VendingMachineState):
    
    def select_product(self, machine):
        from states.payment_state import PaymentState

        ProductFactory.choose_product(machine)
        
        machine.current_state = PaymentState()
    