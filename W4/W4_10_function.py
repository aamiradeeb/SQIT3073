def calculate_monthly_installment(principal, interest_rate, loan_term):
    monthly_interest_rate = interest_rate / (12 * 100)
    monthly_installment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-loan_term))
    return monthly_installment

def calculate_accumulated_installment(monthly_installment, loan_term):
    return monthly_installment * loan_term

def check_dsr(income, monthly_installment, other_commitments):
    dsr_threshold = 0.3
    dsr = (monthly_installment + other_commitments) / income
    return dsr <= dsr_threshold, dsr

def display_menu():
    print("\n--- Housing Loan Calculator Menu ---")
    print("1. Calculate a new housing loan")
    print("2. Display all previous calculations")
    print("3. Exit")

def get_loan_details():
    principal = float(input("Enter the loan amount (principal): "))
    interest_rate = float(input("Enter the annual interest rate (in %): "))
    loan_term = int(input("Enter the loan term (in months): "))
    income = float(input("Enter your monthly income: "))
    other_commitments = float(input("Enter the total of other monthly financial commitments: "))
    return principal, interest_rate, loan_term, income, other_commitments

def main():
    loan_info_list = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                principal, interest_rate, loan_term, income, other_commitments = get_loan_details()

                monthly_installment = calculate_monthly_installment(principal, interest_rate, loan_term)
                accumulated_installment = calculate_accumulated_installment(monthly_installment, loan_term)
                eligible, dsr = check_dsr(income, monthly_installment, other_commitments)

                loan_info = {
                    'principal': principal,
                    'interest_rate': interest_rate,
                    'loan_term': loan_term,
                    'income': income,
                    'other_commitments': other_commitments,
                    'monthly_installment': monthly_installment,
                    'accumulated_installment': accumulated_installment,
                    'eligible': eligible,
                    'dsr': dsr
                }
                loan_info_list.append(loan_info)

                print(f"Monthly installment: {monthly_installment:.2f}")
                print(f"Total payment after {loan_term} months: {accumulated_installment:.2f}")
                if eligible:
                    print(f"Your DSR is {dsr:.2%}. You are eligible for the loan.")
                else:
                    print(f"Your DSR is {dsr:.2%}, which exceeds the threshold. You are not eligible for the loan.")

            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == '2':
            print("\nAll loan calculations:")
            for info in loan_info_list:
                print(info)

        elif choice == '3':
            print("Exiting the calculator. Thank you for using the service.")
            break
        else:
            print("Invalid option selected. Please try again.")

if __name__ == "__main__":
    main()
