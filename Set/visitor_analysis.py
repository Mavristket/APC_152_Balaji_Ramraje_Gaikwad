
day1_visitors = {101, 102, 103, 104}
day2_visitors = {103, 104, 105, 106}

unique_visitors = day1_visitors.union(day2_visitors)


returning_visitors = day1_visitors.intersection(day2_visitors)


only_day1 = day1_visitors.difference(day2_visitors)


only_day2 = day2_visitors.difference(day1_visitors)


print("Day 1 Visitors:", day1_visitors)
print("Day 2 Visitors:", day2_visitors)
print("Unique visitors across both days:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors who came only on the first day:", only_day1)
print("Visitors who came only on the second day:", only_day2)
