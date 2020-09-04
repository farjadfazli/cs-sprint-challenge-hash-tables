def get_indices_of_item_weights(weights, length, limit):

    if (length == 2) and (weights[0] + weights[1] == limit):
        return [1, 0]
    elif (length == 2):
        return None

    hash_table = {weight:index for index, weight in enumerate(weights)}

    output = []

    for weight in weights:
        if (limit - weight) in hash_table:
            output.append(hash_table[limit-weight])
    
    if len(output) < 2:
        return None
    else:
        return output