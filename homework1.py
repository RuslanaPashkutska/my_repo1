from datetime import datetime


def get_days_from_today(date_str):
    given_date = None
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError ("Error!!!  Expected format YYYY-MM-DD")

    current_date = datetime.today().date()
    delta = current_date - given_date

    return delta.days

if __name__ == "__main__":
    try:
        days_difference = get_days_from_today("2027-01-02")
        print("Returned difference in days:", days_difference)
    except ValueError as error:
        print("Error:", error)