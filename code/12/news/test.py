def get_inupt(text):
    return list(map(int,text.split()))

line_info = get_inupt("6 2")
map_list = []
map_list.append(get_inupt("3 3 3 3 3 3"))
map_list.append(get_inupt("2 3 3 3 3 3"))
map_list.append(get_inupt("2 2 2 3 2 3"))
map_list.append(get_inupt("1 1 1 2 2 2"))
map_list.append(get_inupt("1 1 1 3 3 1"))
map_list.append(get_inupt("1 1 2 3 3 2"))

check_road = []
for row_line in map_list:
    check_road.append(row_line)

for i in range(line_info[0]):
    column_line = []
    for x in range(line_info[0]):
        column_line.append(map_list[x][i])
    check_road.append(column_line)

count = 0
for line in check_road:
    if all([line[0] == value for value in line[1:]]):
        count += 1
    elif [value[i] <  for i in range(line_info[0]-1)]
