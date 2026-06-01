from facade.order_facade import OrderFacade

def main():
    orderFacade = OrderFacade()
    orderFacade.place_order(200)

if __name__ == "__main__":
    main()
