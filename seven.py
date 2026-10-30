data = [
    "  python  ",
    "AI",
    "  Machine learning",
    "data Science  ",
    "",
    "deep learning"
]
data = [word.lower()for  word in data ]
data = [word.strip() for word in data]
data = [word.lstrip() for word in data]
data = [word.rstrip() for word in data]
data = [word for word in data if word]
print(data)
