def has_name(para_field):
    return para_field.get("given-name") is not None


def get_name(para_field):
    return para_field.get("given-name").string_value


def has_grad_year(para_field):
    return para_field.get('date-time') is not None


def get_grad_year(para_field):
    return para_field.get("date-time").string_value[:4]


t("unit").string_value


def has_salary_expect(para_field):
    return para_field.get('number') is not None


def get_salary_expect(para_field):
    return para_field.get("number").number_value


def print_information(para_list):
    name = ''
    grad_year = ''
    salary_expect = ''
    for item in para_list:
        if has_name(item):
            name = get_name(item)
        if has_grad_year(item):
            grad_year = get_grad_year(item)
        if has_salary_expect(item):
            salary_expect = get_salary_expect(item)

    print('Got following info: ')
    print(f'Name：{name}')
    print(f'Graduation year：{grad_year}')
    print(f'Expected salary：{salary_expect}')
