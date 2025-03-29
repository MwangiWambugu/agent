from agency_setup import agency
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    while True:
        user_input = input("Customer: ")
        if user_input.lower() == "exit":
            break

        # Process through CEO agent
        response = agency.get_completion(user_input, recipient=agency.ceo)

        print("\nSupport Agent:", response)
        print("\n" + "-" * 50 + "\n")