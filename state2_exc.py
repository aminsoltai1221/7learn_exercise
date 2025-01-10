from abc import ABC,abstractmethod


class Text():
    def __init__(self,text):
        self.text = text


    def sametext(self):
        r = Same(self)
        return r.same()
        
    
    
    def reversetext(self):
        r = Reverse(self)
        return r.reverse()


class Same():
    def __init__(self, textobject):
        self.text = textobject.text

    def same(self):
        return self.text

class Reverse():
    def __init__(self, textobject):
        self.text = textobject.text

    def reverse(self):
        return self.text[::-1]


text1 = Text("hi everyone, hello my friends")
print(text1.sametext())

print(text1.reversetext())
