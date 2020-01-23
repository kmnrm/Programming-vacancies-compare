# Programming-vacancies-compare
This program finds open vacancies for different languages programmers on Russian job search web-sites such as [HeadHunter](https://hh.ru/)  and [SuperJob](https://www.superjob.ru) and shows an average salary for each programming language position.

### How to install
Follow these steps before launching:
1. This program works with [HH.ru public API](https://dev.hh.ru/) and [SuperJob API](https://api.superjob.ru/), which requires Secret Key to work with.  To get Secret Key you need to register your application, which is not more than an ordinary sign up procedure. During signing up you may need to fill `Application website` field. If you do not have one, then just use any URL.  
2. Create a `.env` file in default directory and add your Secret Key from SuperJob in the format below:
```
SUPERJOB_SECRETKEY=your_secret_key
```
Do not use parenthesis, quotation marks or spaces, e.g:
```
SUPERJOB_SECRETKEY=v3.z.98765432.1this2is3just4an5example.6god7knows8how9it0really1looks2like
```

Preinstall Python3 to use this program.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### Getting started
This program collects eight popular programming languages vacancies.
```
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
```
You are more than welcome to add languages or remove ones you are not interested in.

### How to use
Running main.py script:
```
$ python3 main.py
```

The results are shown below:
```
$ python3 main.py
+SuperJob.ru [Moscow, RU]--------+---------+
|            | Jobs  | Handled   | Average |
| Language   | Found | Positions | Salary  |
+------------+-------+-----------+---------+
| Java       | 22    | 10        | 106500  |
| JavaScript | 30    | 19        | 107189  |
| Python     | 11    | 9         | 123000  |
| Ruby       | 2     | 1         | 180000  |
| PHP        | 41    | 23        | 97239   |
| C++        | 16    | 7         | 93000   |
| C#         | 15    | 9         | 132444  |
| Swift      | 1     | 1         | 120000  |
+------------+-------+-----------+---------+
+HH.ru [Moscow, RU]--+-----------+---------+
|            | Jobs  | Handled   | Average |
| Language   | Found | Positions | Salary  |
+------------+-------+-----------+---------+
| Java       | 1951  | 423       | 172152  |
| JavaScript | 2554  | 723       | 139646  |
| Python     | 1471  | 340       | 157647  |
| Ruby       | 206   | 69        | 164891  |
| PHP        | 1074  | 467       | 129048  |
| C++        | 132   | 54        | 133300  |
| C#         | 1045  | 326       | 147829  |
| Swift      | 252   | 76        | 189412  |
+------------+-------+-----------+---------+
```
### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
