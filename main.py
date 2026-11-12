items = []
history = []

while True:
    n = input().strip()

    LIST_CMD = ['add', 'show', 'insert', 'remove', 'pop', 'reverse', 'sort', 'undo']
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
            cp = items.copy()
            history.append(cp)
        elif cmd == "insert" and len(parts) >= 3:
            items.insert(int(parts[1]), ''.join(parts[2:]))
            cp = items.copy()
            history.append(cp)
        elif cmd == "remove":
            items.remove(''.join(args))
            cp = items.copy()
            history.append(cp)
        elif cmd == "pop":
            items.pop()
            cp = items.copy()
            history.append(cp)
        elif cmd == "reverse":
            items.reverse()
            cp = items.copy()
            history.append(cp)
        elif cmd == "sort":
            items.sort()
            cp = items.copy()
            history.append(cp)
        elif cmd == "undo":
            if len(history) > 0:
                history.pop()
            if len(history) >= 1:
                items = history[-1]
            else:
                items = []

