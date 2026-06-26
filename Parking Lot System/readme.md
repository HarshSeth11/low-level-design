# 🚗 Parking Lot System (Low-Level Design)

A console-based **Parking Lot System** implemented in **Python** following **Object-Oriented Programming (OOP)** principles and common **Low-Level Design (LLD)** patterns.

This project simulates a multi-floor parking lot where vehicles can enter, receive a parking ticket, be charged based on parking duration, and exit while freeing the occupied parking spot.

---

## ✨ Features

* 🚗 Supports multiple vehicle types

  * Bike
  * Car
  * Truck

* 🏢 Multi-floor parking lot

* 🅿️ Dedicated parking spots for different vehicle types

* 🎫 Automatic ticket generation

* ⏱️ Entry and exit time tracking

* 💰 Hourly pricing strategy

* ♻️ Reuse of freed parking spots

* 📦 Clean object-oriented architecture

---

## 📂 Project Structure

```text
parking_lot/

├── enums/
├── models/
│   ├── vehicle.py
│   ├── parking_spot.py
│   ├── floor.py
│   ├── parking_lot.py
│   └── ticket.py
│
├── services/
│   ├── parking_service.py
│   └── exit_service.py
│
├── strategies/
│   ├── pricing_strategy.py
│   └── hourly_pricing.py
│
└── main.py
```

---

## 🏗️ Design Overview

The system is designed using a layered architecture.

```text
                 main.py
                     │
        ┌────────────┴────────────┐
        │                         │
 ParkingService             ExitService
        │                         │
        └────────────┬────────────┘
                     │
                ParkingLot
                     │
                 Floors
                     │
              Parking Spots
```

---

## 🧩 OOP Concepts Used

* Abstraction
* Encapsulation
* Inheritance
* Polymorphism

---

## 🎯 Design Patterns Used

### Strategy Pattern

Pricing is implemented using the Strategy Pattern.

```text
PricingStrategy
        │
        └── HourlyPricing
```

This allows introducing additional pricing models in the future without modifying existing code.

Examples:

* Hourly Pricing
* Flat Pricing
* Weekend Pricing
* Premium Pricing

---

## 🚘 Parking Flow

```text
Vehicle Enters
        │
        ▼
ParkingService
        │
        ▼
ParkingLot
        │
        ▼
Find Available Floor
        │
        ▼
Allocate Parking Spot
        │
        ▼
Generate Ticket
```

---

## 🚪 Exit Flow

```text
Vehicle Exit
        │
        ▼
ExitService
        │
        ▼
Set Exit Time
        │
        ▼
Calculate Parking Fee
        │
        ▼
Free Parking Spot
        │
        ▼
Remove Ticket
```

---

## 🧱 Main Components

### Vehicle

Represents different vehicle types.

* Bike
* Car
* Truck

---

### Parking Spot

Represents a parking spot.

Responsibilities:

* Park vehicle
* Free spot
* Check availability

---

### Floor

Represents one parking floor.

Responsibilities:

* Maintain parking spots
* Allocate available spots
* Free occupied spots

---

### Parking Lot

Acts as the central model.

Maintains:

* Floors
* Active Tickets

---

### Ticket

Stores:

* Ticket ID
* Vehicle
* Entry Time
* Exit Time
* Floor
* Spot

---

### Parking Service

Responsible for:

* Parking vehicles
* Finding available spots
* Ticket generation

---

### Exit Service

Responsible for:

* Vehicle exit
* Fee calculation
* Freeing parking spots
* Removing completed tickets

---

## ▶️ Sample Output

```text
Floor added successfully

Vehicle - PB70-WQ-7635 is parked at #BIKE-10

Vehicle - PB70-WQ-7534 is parked at #CAR-20

$20 has been charged for Vehicle Number Plate: PB70-WQ-7534

Spot - #CAR-20 is free
```

---

## 🚀 Future Improvements

* Parking Spot Managers
* Entry & Exit Gates
* Payment Strategies (Cash, UPI, Card)
* Reservation System
* Electric Vehicle Parking
* VIP Parking
* Concurrency Support
* Database Integration
* REST API
* Unit Tests

---

## 📚 Learning Outcomes

Through this project, I practiced:

* Low-Level System Design
* SOLID Principles
* Object-Oriented Design
* Strategy Pattern
* Service Layer Architecture
* Responsibility Separation
* Designing Extensible Systems

---

## 🛠️ Tech Stack

* Python 3
* Object-Oriented Programming
* Design Patterns
* Low-Level Design (LLD)

---

## 📄 License

This project is created for learning and interview preparation purposes.
