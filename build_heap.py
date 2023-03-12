def build_heap(data):
    swaps = []

    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        swaps += sift_down(data, i)
    return swaps

def sift_down(data, i):
    swaps = []
    n = len(data)
    min_index = i

    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    if left_child_index < n and data[left_child_index] < data[min_index]:
        min_index = left_child_index

    if right_child_index < n and data[right_child_index] < data[min_index]:
        min_index = right_child_index

    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        swaps += sift_down(data, min_index)
    return swaps

def main():
    input_type = input().strip()

    if input_type == "I":
        n = int(input().strip())
        data = list(map(int, input().split()))
        assert len(data) == n

    elif input_type == "F":
        file_dir = input().strip()

        try:
            with open(f"./tests/{file_dir}") as f:
                contents = f.readlines()
        except:
            print("ERROR")

        n = int(contents[0].strip("\n"))
        data = list(map(int, contents[1].split()))
        assert len(data) == n

    else:
        print("ERROR")

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
