def sclar_vector_product(scalar, vector):
    result = []
    for value in vector:
        result.append(scalar * value)
    return result


iteration_max = 10000

vector = list(range(iteration_max))
scalar = 2

for _ in range(iteration_max):
    sclar_vector_product(scalar, vector)
