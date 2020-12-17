class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_thanku():
    print("Thank u!")

@CountCalls
def say_goodMorning():
    print("good morning")

say_thanku()
say_goodMorning()
say_goodMorning()
say_goodMorning()
say_goodMorning()
