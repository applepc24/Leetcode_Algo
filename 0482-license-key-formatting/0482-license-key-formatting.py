class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned = s.replace('-', '').upper()

        if  not cleaned:
            return ""
        
        first_group_len = len(cleaned) % k

        parts = []
        
        if first_group_len > 0:
            parts.append(cleaned[:first_group_len])
        
        for i in range(first_group_len, len(cleaned), k):
            parts.append(cleaned[i : i+k])
        
        return "-".join(parts)