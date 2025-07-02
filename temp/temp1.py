MEMORY_FILE = "Vilnius.txt"

with open(MEMORY_FILE, "r", encoding="utf-8") as f:
    content = f.read().strip()

print(content)