import csv
from datetime import datetime

class BillGenerator:
    def __init__(self, data):
        self.data = data

    def calculate_total(self):
        total = sum(item['amount'] for item in self.data)
        return total

    def generate_bill_text(self):
        lines = ["Monthly Bill Summary:"]
        for item in self.data:
            lines.append(f"{item['date']} - {item['description']} - ₹{item['amount']}")
        lines.append(f"\nTotal: ₹{self.calculate_total()}")
        return "\n".join(lines)

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["date", "description", "amount"])
            writer.writeheader()
            for item in self.data:
                writer.writerow(item)

