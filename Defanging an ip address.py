class Solution:
    def defangIPaddr(self, address: str) -> str:
        for i in range(len(address)+6):
            if address[i]=='.' and address[i-1]!='[' :
                address=address[:i]+'[.]'+address[i+1:]
        return address
                
        