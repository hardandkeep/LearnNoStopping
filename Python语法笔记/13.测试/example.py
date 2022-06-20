def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()


def gain_full_name(first_name, last_name, middle_name=''):
    if middle_name:
        name = first_name + "" + middle_name + "" + last_name
        return name.title()
    else:
        name = first_name + "" + last_name
        return name.title()


print(get_formatted_name("li", "xue"))


