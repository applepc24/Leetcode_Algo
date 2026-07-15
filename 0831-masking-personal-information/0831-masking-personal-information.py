class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')

            return f"{name[0]}*****{name[-1]}@{domain}"
        
        else:
            digits = "".join(char for char in s if char.isdigit())

            last4 = digits[-4:]

            if len(digits) == 10:
                return f"***-***-{last4}"
            else:
                country_code_len = len(digits) -10
                return f"+{"*" * country_code_len}-***-***-{last4}"