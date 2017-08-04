
![][py2x] [![GitHub forks][forks]][network] [![GitHub stars][stars]][stargazers] [![GitHub license][license]][lic_file]
> Disclaimer: This project is intended to study the Scrapy Spider Framework and the MongoDB database, it cannot be used for commercial or other personal intentions. If used improperly, it will be the individuals bear.


## Environment, Architecture

Language: Python2.7

Database: MongoDB

## Instructions for use

### Pre-boot configuration

* Install MongoDB and start without configuration
* Install Python dependent modules： `pip install -r requirements.txt` (best in virtualenv)
* Modify the configuration by needed, such as the interval time, the number of threads, etc.

### Start up

* python start.py

## Database description

The table in the database that holds the data is MixFunds. The following is a field description:

#### MixFunds table：

    name              : fund name
    code              : fund code
    ftype             : fund type
    unit_price        : unit price
    last_1month       : performance last month
    last_3month       : performance last 3 month
    last_6month       : performance last 6 month
    last_1year        : performance last 1 year
    last_2year        : performance last 2 year
    last_3year        : performance last 3 year
    size              : fund size
    fund_create_time  : fund create time
    manager_name      : fund manager name
    manage_fund_number: the number of funds what the fund manager managed
    manage_time       : how long the fund manager managed
    fund_comp_name    : which fund compony


[py2x]: https://img.shields.io/badge/python-2.x-brightgreen.svg
[issues_img]: https://img.shields.io/github/issues/bulatie/myfundbot.svg
[issues]: https://github.com/bulatie/myfundbot/issues

[forks]: https://img.shields.io/github/forks/bulatie/myfundbot.svg
[network]: https://github.com/bulatie/myfundbot/network

[stars]: https://img.shields.io/github/stars/bulatie/myfundbot.svg
[stargazers]: https://github.com/bulatie/myfundbot/stargazers

[license]: https://img.shields.io/badge/license-MIT-blue.svg
[lic_file]: https://raw.githubusercontent.com/bulatie/myfundbot/master/LICENSE
