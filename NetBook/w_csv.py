import csv

with open("test.csv", "w", newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow([1, 2, 3])
    writer.writerow([4, 5, 6])
