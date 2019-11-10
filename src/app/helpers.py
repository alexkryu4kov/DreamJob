def get_unique_list(array):
    return list(set(array))


def create_list_of_names(data: list) -> list:
    return get_unique_list([row['name'].lower() for row in data])
