x_end, y_end = map(int, input().split())

memo = {}

while True:
    try:
        x, y, direction = map(str, input().split())
        x = int(x)
        y = int(y)

        actions = input()

        for index, action in enumerate(actions):
            x0 = x
            y0 = y
        
            if direction == "N":
                if action == "F":
                    y += 1

                elif action == "R":
                    direction = "E"
                elif action == "L":
                    direction = "W"

            elif direction == "S":
                if action == "F":
                    y -= 1
                elif action == "R":
                    direction = "W"
                elif action == "L":
                    direction = "E"

            elif direction == "W":
                if action == "F":
                    x -= 1
                elif action == "R":
                    direction = "N"
                elif action == "L":
                    direction = "S"
        
            elif direction == "E":
                if action == "F":
                    x += 1
                elif action == "R":
                    direction = "S"
                elif action == "L":
                    direction = "N"

            # print("First", x, y, direction)

            if (0 > x or x > x_end) or (0 > y or y > y_end):
                if x0 in memo:
                    # print("x =", x, "y =", y)
                    # print("x0 =", x0, "y0 =", y0)
                    # print("memo[x0] =", memo[x0], "y0 =", y0)

                    if memo[x0] == {y0}:
                        # print("memo[x0] = y0")
                        # print("x =", x, "y =", y)
                        # print("x0 =", x0, "y0 =", y0)
                        x = x0
                        y = y0
                        continue

                print(x0, y0, direction, "LOST")
                memo[x0] = {y0}
                break

            # print("Sec", x, y, direction)


        if (0 <= x <= x_end) & (0 <= y <= y_end):
            print(x, y, direction)

    except EOFError:
        break