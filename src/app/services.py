# coding: utf-8
"""app services."""
from faker import Faker

from app.consts import CAR_CITY_MAP, HTTP_CODES

FAKER = Faker('zh_CN')


def car_search(keyword):
    """车牌查询."""
    dataset = CAR_CITY_MAP

    return dataset.get(keyword.upper(), '未知')


def http_code_search(keyword):
    return HTTP_CODES.get(keyword, '未找到对应的 HTTP Code')


def get_random_email(count=1):

    return [FAKER.email() for i in range(count)]
