# 🥤 Vending Machine System (LLD)

A console-based Vending Machine implementation built using multiple Low-Level Design (LLD) concepts and Design Patterns.

## 🚀 Features

- Display available products
- Select product and quantity
- Inventory management
- Multiple payment methods
  - UPI
  - Card
  - Cash
- Payment validation
- Product dispensing
- State transitions
- Extensible architecture

---

## 📌 Design Patterns Used

### 1. State Pattern
The vending machine changes its behavior based on its current state.

States:

- IdleState
- PaymentState
- DispenseState

Flow:

```text
Idle State
    ↓
Payment State
    ↓
Dispense State
    ↓
Idle State
```

---

### 2. Strategy Pattern

Used for different payment methods.

```text
PaymentStrategy
    ├── UPIPayment
    ├── CardPayment
    └── CashPayment
```

Allows adding new payment methods without modifying existing code.

---

### 3. Factory Pattern

Used for:

- Product Selection
- Payment Method Selection

Factories:

- ProductFactory
- PaymentFactory

---

## 📂 Project Structure

```text
vending_machine/

├── main.py
│
├── machine/
│   └── vending_machine.py
│
├── states/
│   ├── vending_machine_state.py
│   ├── idle_state.py
│   ├── payment_state.py
│   └── dispense_state.py
│
├── strategies/
│   ├── payment_strategy.py
│   ├── upi_payment.py
│   ├── cash_payment.py
│   └── card_payment.py
│
├── factories/
│   ├── product_factory.py
│   └── payment_factory.py
│
├── inventory/
│   └── inventory.py
│
├── models/
│   └── product.py
│
└── README.md
```

---

## 🏗️ System Workflow

### Step 1: Display Products

```text
Available Products

ID: 1 | Name: Coke | Price: 40 | Qty: 10
ID: 2 | Name: Diet Coke | Price: 40 | Qty: 7
ID: 3 | Name: Chips | Price: 50 | Qty: 7
ID: 4 | Name: Kurkure | Price: 70 | Qty: 8
```

---

### Step 2: Select Product

```text
Enter product id: 1
Enter quantity: 5
```

Machine validates inventory availability.

---

### Step 3: Select Payment Method

```text
1. UPI
2. Cash
3. Card

Enter choice: 1
```

---

### Step 4: Payment Processing

```text
200 rupee is successfully paid via UPI
```

---

### Step 5: Product Dispensing

```text
Dispensing 5 - Coke
```

---

## 🧩 Core Classes

### Product

Represents a product inside the machine.

Attributes:

```python
id
name
price
quantity
```

---

### Inventory

Maintains all products available in the machine.

Responsibilities:

- Add Product
- Remove Product
- Check Availability
- Fetch Product

---

### VendingMachine

Main controller class.

Attributes:

```python
current_state
inventory
selected_product
selected_quantity
payment_strategy
```

Responsibilities:

- Manage state transitions
- Coordinate inventory
- Handle payment
- Dispense products

---

## 🔄 State Transitions

```text
IdleState
    |
    | Product Selected
    v
PaymentState
    |
    | Payment Success
    v
DispenseState
    |
    | Product Dispensed
    v
IdleState
```

---

## 💳 Payment Strategies

### UPI Payment

```python
UPIPayment.pay(amount)
```

### Card Payment

```python
CardPayment.pay(amount)
```

### Cash Payment

```python
CashPayment.pay(amount)
```

All strategies implement:

```python
PaymentStrategy.pay(amount)
```

---

## ▶️ Running the Project

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to project folder:

```bash
cd vending_machine
```

Run:

```bash
python main.py
```

---

## 📚 Concepts Practiced

- Low Level Design (LLD)
- SOLID Principles
- State Pattern
- Strategy Pattern
- Factory Pattern
- Object-Oriented Programming
- Dependency Injection
- Separation of Concerns

---

## 🔮 Future Enhancements

- Admin Mode
- Restocking Products
- Transaction History
- Refund Support
- Coupon System
- Multi-Vendor Inventory
- Database Integration
- GUI Version
- REST API Version using Django/FastAPI

---

## 👨‍💻 Author

**Harsh Seth**

Senior Software Developer | Learning Low Level Design, System Design, AI Engineering, and Backend Development.