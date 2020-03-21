# coding: utf-8
"""app services."""
from faker import Faker

from app.consts import CAR_CITY_MAP, HTTP_CODES

import mmh3

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


FAKER = Faker('zh_CN')


def car_search(keyword):
    """车牌查询."""
    dataset = CAR_CITY_MAP

    return dataset.get(keyword.upper(), '未知')


def http_code_search(keyword):
    return HTTP_CODES.get(keyword, '未找到对应的 HTTP Code')


def get_random_email(count=1):
    return [FAKER.email() for i in range(count)]


def base62_encode(num, alphabet=ALPHABET):
    """Encode a number in Base X

    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base62_decode(string, alphabet=ALPHABET):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num


def get_short_url_code(url):
    hash_num = mmh3.hash(url)
    code = base62_encode(abs(hash_num))

    return code
