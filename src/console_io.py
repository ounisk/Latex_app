class ConsoleIO:
    def write(self, value):
        print(value)

    def read(self, prompt):
        return input(f"{prompt:80}")
