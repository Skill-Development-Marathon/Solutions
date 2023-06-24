def defangIPaddr(address: str) -> str:
        return address.replace(".","[.]")
    
    
print(defangIPaddr("1.1.1.1.1"))