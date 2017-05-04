import csv

mycsv = csv.reader(open('log.csv'))
locations = {}

for row in mycsv:
   loc = row[3] + " ," + row[4]
   if(locations.get(loc, False)):
        locations[loc].append(float(row[2]))
   else:
    locations[loc] = [float(row[2])]

points = {}
for key, value in locations.items():
    avg = sum(value) / len(value)
    if(avg > 5000):
        points[key] = "<default-dot>"
    elif (avg > 1000):
        points[key] = "<yellow-dot>"
    else:
        points[key] = "<green-dot>"


with open('points.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for key, value in points.items():
        writer.writerow([key] + [value])
