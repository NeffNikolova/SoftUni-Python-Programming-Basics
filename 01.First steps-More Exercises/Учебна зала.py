w = float(input())
h = float(input())

usable_h = h - 1

nr_tables_h = usable_h // 0.7

nr_tables_w = w // 1.2

nr_tables_total = nr_tables_w * nr_tables_h - 3

print(int(nr_tables_total))
