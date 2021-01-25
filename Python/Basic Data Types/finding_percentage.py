if __name__ == '__main__':
    n = 3
    student_marks = {
        'Krishna': [
            67,
            68,
            69, ],
        'Arjun': [
            70,
            98,
            63, ],
        'Malika': [
            52,
            56,
            60, ]
    }

    query_name = 'Malika'

    selected = student_marks[query_name]
    average = sum(selected) / len(selected)
    print('%.2f' % average)
