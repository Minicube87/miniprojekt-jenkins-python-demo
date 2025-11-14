with open('numbers.txt') as f:
    lines = f.readlines()

    total = 0
    count = 0
    for entry in lines:
        cleaned = entry.strip()
        total += int(cleaned) 
        count += 1


average = total / count

with open("result.txt", "w") as r:
    r.write(f"totalme: {total}\n")
    r.write(f"Durchschnitt: {average}")
    