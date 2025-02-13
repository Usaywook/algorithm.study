import sys
sys.stdin = open('./input.txt', "r")

def solve(boxes):
    dp_boxes = []
    for (i, box) in enumerate(boxes):
        dp_boxes.append((box[0], box[1], box[2], i))
        dp_boxes.append((box[0], box[2], box[1], i))
        dp_boxes.append((box[1], box[2], box[0], i))
    dp_boxes = sorted(dp_boxes, key=lambda e: e[0] * e[1])

    piled = [{box[3]} for box in dp_boxes]
    depths = [box[2] for box in dp_boxes]
    for i in range(len(dp_boxes)):
        w, h, d, i_box = dp_boxes[i]        
        for j in range(i - 1, -1, -1):
            _w, _h, _d, j_box = dp_boxes[j]
            if not (_w <= w and _h <= h):
                continue
            if i_box in piled[j]:
                continue
            new_d = depths[j] + d
            if depths[i] < new_d:
                depths[i] = new_d
                piled[i] = piled[j].union([i_box])
    return max(depths)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    boxes = [tuple(sorted(map(int, input().split()))) for _ in range(N)]
    result = solve(boxes)
    print(f"#{t} {result}")
