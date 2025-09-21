def maxmin_select(arr, inicio, fim):
    if inicio == fim:
        return arr[inicio], arr[inicio]

    elif fim - inicio == 1:
        if arr[inicio] < arr[fim]:
            return arr[inicio], arr[fim]
        else:
            return arr[fim], arr[inicio]

    else:
        meio = (inicio + fim) // 2

        min1, max1 = maxmin_select(arr, inicio, meio)
        min2, max2 = maxmin_select(arr, meio + 1, fim)

        min_total = min(min1, min2)
        max_total = max(max1, max2)

        return min_total, max_total


if __name__ == "__main__":
    arrays_teste = [
        [3, 1, 4, 1, 5, 9, 2, 6, 5],
        [64, 34, 25, 12, 22, 11, 90, 5],
        [10, 5, 8, 2, 7, 1, 9],
        [42],
        [7, 3]
    ]

    for arr in arrays_teste:
        print(f"Array: {arr}")
        min_val, max_val = maxmin_select(arr, 0, len(arr) - 1)
        print(f"Menor: {min_val}, Maior: {max_val}")
        print()