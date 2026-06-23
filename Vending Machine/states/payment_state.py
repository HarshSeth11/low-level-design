from states.vending_machine_state import VendingMachineState

class PaymentState(VendingMachineState):
    def make_payment(self, machine, payment_strategy):
        from states.dispense_state import DispenseState
        amount_to_pay = int(machine.selected_product.price)*int(machine.selected_quantity)
        payment_res = payment_strategy.pay(amount_to_pay)
        machine.current_state = DispenseState()
        return payment_res["status"] == "success"
    
    def cancel_transaction(self, machine):
        from states.idle_state import IdleState
        machine.selected_product = None
        machine.selected_quantity = 0

        machine.current_state = IdleState()

        
