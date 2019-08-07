from readop.database.models.operation import Operation
from readop.models.parameters import Parameters


def _calculate_permutations(values_list: list) -> list:
    permutations = []

    # print('values_list[0]')
    # print(values_list[0])

    for x in values_list[0]:
        for y in values_list[1]:
            for z in values_list[2]:
                permutations.append([x, y, z])

    return permutations


def _calculate_values_from_bounds(bounds: list, factors: int) -> list:
    # print('=' * 50)
    # print('calculating values')

    value_range = bounds[1] - bounds[0]

    increment_size = value_range / factors

    values = []

    for i in range(1, factors + 1):
        values.append(int(bounds[0] + increment_size * i))

    # print('values')
    # print(values)

    return values


def generate_operation_list(
        bounds: list,
        factors: list,
        access_pattern_id: int,
        storage_unit_id: int,
        system_description_id: int
) -> list:
    # print('=' * 50)

    # print('bounds')
    # print(bounds)

    # print('factors')
    # print(factors)

    if len(bounds) != len(factors):
        raise ValueError

    values_list = []

    for i in range(len(bounds)):
        values_list.append(_calculate_values_from_bounds(bounds[i], factors[i]))

    # print('values_list')
    # print(values_list)

    permutations = _calculate_permutations(values_list)

    # for p in permutations:
    #     # print(p)

    operation_list = []

    for p in permutations:
        operation_list.append(Operation(
            access_pattern_id,
            storage_unit_id,
            system_description_id,
            True,
            Parameters(
                apd_access_seq_threshold=p[0],
                apd_access_random_threshold=p[1],
                apd_access_random_inc_threshold=p[2]
            )
        ))
    
    return operation_list


def generate_operation_list_from_ranges(
        ranges: list,
        factors: list,
        access_pattern_id: int,
        storage_unit_id: int,
        system_description_id: int
) -> list:
    bounds = []
    for r in ranges:
        bounds.append([r.min_value, r.max_value])

    return generate_operation_list(
        bounds,
        factors,
        access_pattern_id,
        storage_unit_id,
        system_description_id
    )
