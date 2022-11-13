def fun(s):
    # return True if s is a valid email, else return False
    if '@' not in s:
        return False
    if s.count('@') > 1:
        return False
    a, b = s.split('@')

    if '.' not in b:
        return False

    b1, b2 = b.split('.')

    if not b1.isalnum():
        return False
    if len(b2) > 3 or not b2.isalpha():
        return False

    if a.isalnum():
        return True
    elif '_' in a or '-' in a:
        if '_' in a:
            a = a.replace("_", '')
            if not a.isalnum():
                return False
        if '-' in a:
            a = a.replace("-", '')
            if not a.isalnum():
                return False
    elif len(a) == 0:
        return False
    else:
        return False

    return True


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
