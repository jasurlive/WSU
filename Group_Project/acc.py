
#just wanted to create and import it 😸💡

def acc(a, b, c):
    result = {}
    for key, value in c.items():
        category = value[a] 
        total_value = value[b][2] 

        if category not in result:
            result[category] = 0

        result[category] += total_value

    return result
