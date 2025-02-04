from datetime import datetime


def get_days_from_today(date_str):
    given_date = None
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return "Error!!!  Expected format YYYY-MM-DD"

    current_date = datetime.today().date()
    delta = current_date - given_date

    return delta.days


if __name__ == "__main__":
   test_date = ["2019-08-23", "2026-09-05", "hello", "2023-16-02", "not-correct"]

   for test in test_date:
       print (f"Datos: {test} Resultado: {get_days_from_today(test)}")