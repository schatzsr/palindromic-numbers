from csv import writer, QUOTE_NONNUMERIC


def _is_palindrome(number, base):
    """
    :param number: An integer greater than or equal to 1.
    :param base: An integer greater than or equal to 2.
    :return: Returns True if the `number` given is a palindrome in the given `base`, and False otherwise.
    """
    digits = ''
    while number:
        digits += str(int(number % base))
        number /= base

    return digits == digits[::-1]


def _find_palindrome_base(number):
    """
    :param number: An integer greater than or equal to 1.
    :return: Returns the `number` given and the lowest base that number is a palindrome.
    """
    base = 2
    while True:
        if _is_palindrome(number, base):
            break
        base += 1

    return number, base


def generate_smallest_palindrome_bases(start_num, end_num):
    """
    :param start_num: An integer greater than or equal to 1.
    :param end_num: An integer greater than `start_num`.
    :return: Creates a csv file containing each integer between `start_num` and `stop_num` 
      and the lowest base each number is a palindrome.
    """
    if start_num < 1:
        raise ValueError('Must provide a "start_num" value greater than or equal to 1')
    if start_num >= end_num:
        raise ValueError('"end_num must" be greater than start_num')

    file_name = 'palindrome_bases_{}_to_{}.csv'.format(start_num, end_num)
    with open(file_name, 'w') as csv_file:
        wr = writer(csv_file, quoting=QUOTE_NONNUMERIC)

        wr.writerow(['decimal', 'smallest base in which the number is a palindrome'])
        for i in xrange(start_num, end_num + 1):
            number, base = _find_palindrome_base(i)
            row = [number, base]
            wr.writerow(row)

    print 'Created {}'.format(file_name)
