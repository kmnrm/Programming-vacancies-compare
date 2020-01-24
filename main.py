import os
from dotenv import load_dotenv
from terminaltables import AsciiTable
import stats_utils

URL_SJ = 'https://api.superjob.ru/2.0/vacancies/'
URL_HH = 'https://api.hh.ru/vacancies/'

LANGUAGES = [
    'Java',
    'JavaScript',
    'Python',
    'Ruby',
    'PHP',
    'C++',
    'C#',
    'Swift'
]

def draw_job_stats_table(job_stats, title=None):
    table = [
        ['\n'+'Language', 'Jobs'+'\n'+'Found', 'Handled'+'\n'+'Positions', 'Average'+'\n'+'Salary']
    ]
    table_title = title
    for (language, stats) in job_stats.items():
        new_row = [language]
        for stat_value in stats.values():
            new_row.append(stat_value)
        table.append(new_row)
    ascii_table = AsciiTable(table, table_title)
    print(ascii_table.table)


def main():
    superjob_stats = stats_utils.fetch_languages_vacancies_stats(URL_SJ, LANGUAGES, superjob_secret_key)
    headhunter_stats = stats_utils.fetch_languages_vacancies_stats(URL_HH, LANGUAGES, secret_key=None)
    draw_job_stats_table(superjob_stats, title='SuperJob.ru [Moscow, RU]')
    draw_job_stats_table(headhunter_stats, title='HH.ru [Moscow, RU]')


if __name__ == "__main__":
    load_dotenv()
    superjob_secret_key = os.getenv("SUPERJOB_SECRETKEY")
    main()
