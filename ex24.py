print("Let's practice all of the things.")
print("You\'ll need to know \ about escapes with \\ that do:")
print('\n new lines and \t tabs.')

poem = """
\t I don't wanna ruin your ballgown cause I'm not feeling lawbound. \n
You could probably coffee grind my body and mind\n
into a psychotropic compound.\n \n
\t An Ice Age will thaw before I'm able to play ball. \n
Your cryptic texts aint state law,\n
Yet you read like an algebraic scroll."""

print("----------")
print(poem)
print("----------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
