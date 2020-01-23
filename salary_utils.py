
def calculate_salary(salary_from, salary_to):
    if salary_from in (None, 0):
        return int(salary_to * 0.8)
    if salary_to in (None, 0):
        return int(salary_from * 1.2)
    return int((salary_from + salary_to) / 2)


def predict_vacancy_salary(vacancy, source):
    if source == 'superjob':
        salary_from = vacancy['payment_from']
        salary_to = vacancy['payment_to']
        currency = vacancy['currency']
    else:
        salary_from = vacancy['salary']['from']
        salary_to = vacancy['salary']['to']
        currency = vacancy['salary']['currency']
    if currency not in ('rub', 'RUR'):
        return None
    return calculate_salary(salary_from, salary_to)
