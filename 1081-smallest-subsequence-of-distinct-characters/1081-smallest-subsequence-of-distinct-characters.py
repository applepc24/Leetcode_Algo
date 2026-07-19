class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_position = {char: i for i, char in enumerate(s)}

        stack =[]
        seen = set()

        for i, char in enumerate(s):
            if char in seen:
                continue
            
            while stack and char < stack[-1] and i < last_position[stack[-1]]:
                popped_char = stack.pop()
                seen.remove(popped_char)
            
            stack.append(char)
            seen.add(char)
        return "".join(stack)