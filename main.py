from entities.car import Car
from entities.customer import Customer
from entities.seller import Seller
from entities.sales_contract import SalesContract
from entities.dealership import Dealership
from entities.maintenance_record import MaintenanceRecord
from repository.fake_repository import FakeRepository

# Create instances
car1 = Car("1HGCM82633A123456", "Honda", "Accord", 2020, "Black", 25000, 10000)
customer1 = Customer(1, "John Doe", "john.doe@example.com", "123 Main St")
seller1 = Seller(1, "Alice Smith", "alice.smith@example.com", "Sales Manager")
dealership1 = Dealership("AutoHub", "456 Elm St", "123-456-7890")
contract1 = SalesContract(1, "2024-11-25", 25000, car1, customer1, seller1)
maintenance1 = MaintenanceRecord(1, "2024-11-15", "Oil Change", 100, car1)

# Create repositories
car_repo = FakeRepository()
customer_repo = FakeRepository()
seller_repo = FakeRepository()
contract_repo = FakeRepository()
maintenance_repo = FakeRepository()

# Add data to repositories
car_repo.add(car1)
customer_repo.add(customer1)
seller_repo.add(seller1)
contract_repo.add(contract1)
maintenance_repo.add(maintenance1)

# Display data
print("All cars:", car_repo.get_all())
print("Find customer by ID:", customer_repo.find_by_id(1, "customer_id"))
