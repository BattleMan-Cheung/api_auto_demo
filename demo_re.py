import re

from middleware.helper import Context


def replace_tag(target):
    """利用正则，动态替换属性"""
    re_pattern = r'#(.+?)#'
    while re.findall(re_pattern, target):
        key = re.findall(re_pattern, target)[0]
        target = re.sub(re_pattern, str(getattr(Context(), key)), target, 1)
    return target


if __name__ == '__main__':
    my_str = '{"token": "#token#", "mobile_phone_new": "#new_phone#", "mobile_phone_exist": "#exist_phone#"}'

    res = replace_tag(my_str)

    print(res)
