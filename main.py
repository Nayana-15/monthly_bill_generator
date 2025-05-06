from bill_generator import BillGenerator
from data.sample_data import sample_data

def main():
    generator = BillGenerator(sample_data)
    bill = generator.generate_bill_text()
    print(bill)
    generator.save_to_csv("monthly_bill.csv")
    print("\nBill saved as 'monthly_bill.csv'.")

if __name__ == "__main__":
    main()

