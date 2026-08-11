class Toggle:
    def __init__(self):
        self.active = False
    
    def switch(self):
        self.active = not self.active

        if self.active:
            print("Status: ACTIVE")
        else:
            print("Status: INACTIVE")

t = Toggle()
t.switch()
t.switch()
t.switch()
t.switch()