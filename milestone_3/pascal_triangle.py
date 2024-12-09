def get_triangle(rows: int):
    triangle = []

    for i in range(rows):
        coef = 1
        row = []

        for j in range(i + 1):
            row.append(coef)
            coef = coef * (i - j) // (j + 1)

        triangle.append(row)


    max_ = len(" ".join(map(str, triangle[-1])))

    for i in range(rows):
        row_str = " ".join(map(str, triangle[i]))
        print(row_str.center(max_))

get_triangle(8)