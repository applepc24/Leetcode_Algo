class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        t_index = 0

        for num in range(1, target[-1] + 1):
            if t_index == len(target):
                break

            operations.append("Push")

            if target[t_index] == num:
                t_index += 1
            else:
                operations.append("Pop")
        return operations