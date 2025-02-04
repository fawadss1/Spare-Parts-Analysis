import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

car_models = [
    "Toyota Corolla", "Honda Civic", "Suzuki Mehran", "Suzuki Cultus", "Suzuki Alto",
    "Toyota Hilux", "Toyota Fortuner", "Honda City", "Suzuki Wagon R", "Kia Sportage",
    "Hyundai Tucson", "Toyota Yaris", "Suzuki Swift", "Kia Picanto", "Hyundai Elantra",
    "Toyota Prius", "Honda BR-V", "Suzuki Bolan", "Toyota Land Cruiser", "Nissan Sunny",
    "MG HS", "Changan Alsvin", "Hyundai Sonata", "Kia Sorento", "Toyota Vitz", "Truck"
]

car_spare_parts = [
    "Brake Pad", "Air Filter", "Spark Plug", "Oil Filter", "Headlight", 
    "Tail Light", "Radiator", "Alternator", "Battery", "Clutch Kit", "Fuel Pump", 
    "Shocck Absorber", "Steering Wheel", "Tire", "Wheel Rim", "Ignition Coil", "Thermostat", "Water Pump", 
    "Fuel Injector", "AC Compressor", "Radiator Fan", "Starter Motor","Fuel Tank", "Exhaust Pipe"
]

manufacturers = [
    "Toyota", "Honda", "Suzuki", "Hyundai", "Kia", "MG Motors", "Changan",
    "Ghandhara Nissan", "Hino Pak", "United Motors", "Nissan", "Proton", "Prince Motors",
]


def generate_spare_parts_dataset(num_records=10000, name="spare_parts.csv"):
    data = {
        "part_id": [fake.unique.random_number(digits=6) for _ in range(num_records)],
        "part_name": [fake.random_element(elements=car_spare_parts) for _ in range(num_records)],
        "manufacturer": [fake.random_element(elements=manufacturers) for _ in range(num_records)],
        "price": [round(np.random.uniform(10, 1000), 2) for _ in range(num_records)],
        "compatible_car_model": [fake.random_element(elements=car_models) for _ in range(num_records)],
    }
    df = pd.DataFrame(data)
    df.to_csv(name, index=False)
    return True


generate_spare_parts_dataset()
