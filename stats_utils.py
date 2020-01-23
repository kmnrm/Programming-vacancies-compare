import os
from math import ceil
from itertools import count
import requests
import salary_utils


def get_payload(url, keywords_param='Программист '):
    source = url.split('.')[1]
    records_per_page = 100
    if source == 'superjob':
        moscow_id = 4
        catalogue_id = 48
        payload = {
            'town': moscow_id,
            'keyword': keywords_param,
            'count': records_per_page,
            'no_agreement': 1,              #ignore vacancies without stated salary
            'catalogues': catalogue_id 
        }
    else:
        moscow_id = 1
        payload = {
            'area': moscow_id,
            'text': keywords_param,
            'per_page': records_per_page,
            'only_with_salary': True
        }
    return payload


def get_found_vacancies_number(url, language, secret_key):
    target_job = 'Программист ' + language
    payload = get_payload(url, keywords_param=target_job)
    source = url.split('.')[1]
    if source == 'superjob':
        headers = {"X-Api-App-Id": secret_key}
        payload.pop('no_agreement')
    else:
        headers = {}
        payload['only_with_salary'] = False
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    vacancies = response.json()
    if source == 'superjob':
        return vacancies['total']
    return vacancies['found']


def fetch_vacancies(url, language, secret_key):
    vacanices_per_page = 100
    limit_for_pages = 19
    target_job = 'Программист {}'.format(language)
    headers = {}
    source = url.split('.')[1]
    if source == 'superjob':
        headers = {"X-Api-App-Id": secret_key}
    payload = get_payload(url, keywords_param=target_job)
    for page in count():
        payload['page'] = page
        page_response = requests.get(url, headers=headers, params=payload)
        page_response.raise_for_status()
        vacancies_page = page_response.json()
        if source == 'superjob':
            total_quantity = vacancies_page['total']
            fetched_vacancies = vacancies_page['objects']
        else:
            total_quantity = vacancies_page['found']
            fetched_vacancies = vacancies_page['items']
        pages_quantity = ceil(total_quantity / vacanices_per_page)
        if page >= pages_quantity or page >= limit_for_pages:
            break
        yield from fetched_vacancies


def get_stats(url, language, secret_key):
    salaries = []
    vacancies_processed_quantity = 0
    source = url.split('.')[1]
    for vacancy in fetch_vacancies(url, language, secret_key):
        salary = salary_utils.predict_vacancy_salary(vacancy, source)
        if salary is not None:
            salaries.append(salary)
            vacancies_processed_quantity += 1
    vacancies_quantity = get_found_vacancies_number(url, language, secret_key)
    avg_salary = int(sum(salaries) / len(salaries))
    return vacancies_quantity, vacancies_processed_quantity, avg_salary


def fetch_languages_vacancies_stats(url, languages, secret_key):
    all_languages_vacancies_stats = {}
    for language in languages:
        vacancies_stats = {}
        vacancies_quantity, vacancies_processed_quantity, avg_salary = get_stats(url, language, secret_key)
        vacancies_stats["vacancies_found"] = vacancies_quantity
        vacancies_stats["vacancies_processed"] = vacancies_processed_quantity
        vacancies_stats["average_salary"] = avg_salary
        all_languages_vacancies_stats[language] = vacancies_stats
    return all_languages_vacancies_stats
