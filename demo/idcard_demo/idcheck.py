# coding: utf-8
from __future__ import unicode_literals

import sys

import region


def get_region_name(region_code):
    return region.REGION_MAP.get(region_code)


def main():
    idcard = sys.argv[1]
    region_name = get_region_name(idcard[:6])
    print(region_name)

    birthday = idcard[6:14]
    print('生日: {}'.format(birthday))

    gender = '女' if int(idcard[16]) % 2 == 0 else '男'
    print('性别: {}'.format(gender))


if __name__ == '__main__':
    main()
