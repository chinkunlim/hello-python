import datetime

print("Hello, I am chinkunlim! Welcome to my Python project.")

today = datetime.date.today()
print(f"Today's date: {today}")

# Pascal's triangle with rows equal to today's day (dd)
rows = today.day
print(f"\nPascal's Triangle ({rows} rows):")

triangle = []
for i in range(rows):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)
    print(" ".join(str(num) for num in row).center(rows * 4))
