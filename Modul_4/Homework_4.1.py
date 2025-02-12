def total_salary(path):
    try:
        with open (path, 'r', encoding='utf-8') as file:
            salaries = []

            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 2:
                    print (f'Incorrect format: {line.strip()}')
                    continue
                try:
                    salary = int(parts[1])
                    salaries.append(salary)
                except ValueError:
                    print (f'Invalid salary value: {parts[1]} in line {line.strip() }')
                    continue
        if not salaries:
            return 0, 0

        total = sum(salaries)
        average = total / len(salaries) if salaries else 0

        return total, average

    except FileNotFoundError:
        print(f"File not found.")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

print(total_salary("salaries.txt"))