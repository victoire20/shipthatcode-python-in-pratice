items = []
history = []
LIST_CMD = ['add', 'show', 'insert', 'remove', 'pop', 'reverse', 'sort', 'undo']

while True:
    try:
        n = input().strip()
    except EOFError:
        break

    parts = n.split() 

    if len(parts) != 0 and parts[0] in LIST_CMD:
        cmd = parts[0]
        args = parts[1:]

        if cmd == "show":
            if len(items) == 0:
                print("(empty)")
            else:
                print(" ".join(items))
        elif cmd == "add":
            items.append(" ".join(args))
            history.append(items.copy())
        elif cmd == "insert" and len(parts) >= 3:
            items.insert(int(parts[1]), " ".join(parts[2:]))
            history.append(items.copy())
        elif cmd == "remove":
            if " ".join(args) in items:
                items.remove(" ".join(args))
            history.append(items.copy())
        elif cmd == "pop":
            if len(items) > 0:
                items.pop()
            history.append(items.copy())
        elif cmd == "reverse":
            items.reverse()
            history.append(items.copy())
        elif cmd == "sort":
            items.sort()
            history.append(items.copy())
        elif cmd == "undo":
            if len(history) > 0:
                history.pop()
            if len(history) >= 1:
                items = history[-1].copy()
            else:
                items = []
