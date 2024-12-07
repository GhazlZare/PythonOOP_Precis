class CustomTuple(tuple):
    def __new__(cls, *args):
        unique_elements = set(args)
        return super().__new__(cls, unique_elements)
    
    def __add__(self, other):
        if not isinstance(other, tuple):
            raise TypeError("Can only merge with another tuple.")
        return CustomTuple(*(set(self) | set(other)))
    
    def sum(self):
        return sum(item for item in self if isinstance(item, (int, float)))

#checking the code
if __name__ == "__main__":
    t1 = CustomTuple(13, 14, 15, 27, 4, 13)
    print(t1)  

    t2 = CustomTuple(13, 4, 22, 25, 15)
    print(t2)  

    merged = t1 + t2  
    print(merged)  

    print(t1.sum())  
    print(t2.sum())  