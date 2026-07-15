class delhi:
    def __init__(self):
        print("This is from Delhi.")

class mumbai(delhi):
    def __init__(self):
        super().__init__()
        print('This is from Mumbai.')

class kolkata(delhi):
    def __init__(self):
        super().__init__()
        print("This is from Kolkata.")

place = kolkata()
# fyi super() keyword helps to execute function of parent class.
