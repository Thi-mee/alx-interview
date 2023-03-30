def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    stack = [0]
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key >= 0 and key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)
