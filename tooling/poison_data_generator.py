import random
import csv

def generate_poisoned_csv(filename="poisoned_data.csv", rows=100):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["input", "label"])
        for _ in range(rows):
            text = "This is safe input."
            label = "benign"
            if random.random() < 0.1:
                text = "Buy now!!! http://malicious.example"
                label = "malicious"
            writer.writerow([text, label])
    print(f"[+] Poisoned dataset written to {filename}")

if __name__ == "__main__":
    generate_poisoned_csv()
