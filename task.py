def digitSum(val):
    sum = 0
    while val:
        sum += val % 10
        val //= 10
    return sum

# Не ясно, требуется напечатать результат или вернуть его в виде структуры данных?

def displayGroups(groupData):
    for group, n in groupData.items():
        print(f'Число клиентов в группе {group} - {n}')

def getCustGroups(n_customers: int) -> dict:
    data = {}
    for id in range(0, n_customers):
        group = digitSum(id)
        if data.get(group):
            data[group] += 1
        else:
            data[group] = 1
    # displayGroups(data)
    return data

def getCustGroupsID(n_first_id: int, n_customers: int) -> dict:
    data = {}
    for id in range(n_first_id, n_first_id + n_customers):
        group = digitSum(id)
        if data.get(group):
            data[group] += 1
        else:
            data[group] = 1
    # displayGroups(data)
    return data