from states.vending_machine_state import VendingMachineState


class DispenseState(VendingMachineState):
    
    def dispense_product(self, machine):
        from states.idle_state import IdleState
        print(f"Dispensing {machine.selected_quantity} - {machine.selected_product.name}")
        machine.selected_product.quantity -= (
            machine.selected_quantity
        )

        machine.selected_product = None
        machine.selected_quantity = 0

        machine.current_state = IdleState()