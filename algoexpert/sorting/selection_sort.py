from typing import List


def selection_sort(elements: List[int]) -> List[int]:
    for i in range(len(elements)):
        for j in range(i +1, len(elements)):
            if elements[j] < elements[i]:
                elements[j], elements[i] = elements[i], elements[j]
    return elements

def main():
    elements= [12,21, 1, 4,5,98,109]
    print(selection_sort(elements=elements))

if __name__ == "__main__":
    main()