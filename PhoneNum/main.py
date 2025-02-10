import random
import argparse

# Dictionary of country codes and their respective area codes
country_area_codes = {
    'KZ': ['701', '702', '705', '721', '723', '731'],
    'AR': ['11', '221', '223', '261', '264', '341'],
    'AM': ['10', '91', '93', '94', '95', '96'],
    'BR': ['11', '21', '31', '41', '51', '61'],
    'CL': ['2', '32', '33', '41', '45', '51'],
    'CO': ['1', '2', '4', '5', '6', '7'],
    'EC': ['2', '3', '4', '5', '6', '7'],
    'EG': ['2', '3', '10', '11', '12', '13'],
    'GE': ['32', '34', '36', '37', '38', '39'],
    'IN': ['11', '22', '33', '44', '55', '66'],
    'ID': ['21', '22', '31', '61', '71', '81'],
    'MX': ['55', '33', '81', '656', '998', '614'],
    'PK': ['21', '42', '51', '61', '71', '81'],
    'PE': ['1', '44', '54', '64', '74', '84'],
    'UZ': ['71', '72', '73', '74', '75', '76']
}

# Function to generate phone numbers
def generate_phone_numbers(area_codes, count=10):
    phone_numbers = []
    for _ in range(count):
        area_code = random.choice(area_codes)
        local_number = random.randint(1000000, 9999999)  # Local 7-digit number
        phone_number = f"00{area_code}{local_number}"
        phone_numbers.append(phone_number)
    return phone_numbers

def main():
    parser = argparse.ArgumentParser(description="Generate phone numbers for a specified country")
    parser.add_argument('-c', '--country', type=str, required=True, help="Country code (e.g., KZ, AR, AM, etc.)")
    parser.add_argument('-n', '--number', type=int, default=10, help="Number of phone numbers to generate")
    args = parser.parse_args()

    country_code = args.country.upper()
    if country_code not in country_area_codes:
        print(f"Country code {country_code} is not supported.")
        return

    area_codes = country_area_codes[country_code]
    phone_numbers = generate_phone_numbers(area_codes, args.number)

    # Write phone numbers to a file named after the country code and number of phone numbers generated
    filename = f"{country_code}_{args.number}_phone_numbers.txt"
    with open(filename, 'w') as file:
        for number in phone_numbers:
            file.write(f"{number}\n")

    print(f"Generated phone numbers written to {filename}")

if __name__ == "__main__":
    main()
