n = int(input())
queue = []

for _ in range(n):
    event = input().strip()
    
    if event.startswith("Кто последний?"):
        name = event.split(" - ")[1].strip(".")
        queue.append(name)

    elif event.startswith("Я только спросить!"):
        name = event.split(" - ")[1].strip(".")
        queue.insert(0,name)
    elif event == "Следующий!":
        if queue:
            print(f"Заходит {queue.pop(0)}!")
        else:
            print("В очереди никого нет")