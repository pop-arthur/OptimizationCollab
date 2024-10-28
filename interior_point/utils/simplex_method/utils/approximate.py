from decimal import Decimal, ROUND_HALF_UP


def round_with_precision(value, precision):
    decimal_value = Decimal(value).quantize(Decimal(f"1.{'0' * precision}"), rounding=ROUND_HALF_UP)
    return float(decimal_value)


def round_table(table, apac):
    apac = int(apac)
    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            if isinstance(table[i][j], (int, float)):
                table[i][j] = round_with_precision(table[i][j], apac)
    return table