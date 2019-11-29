def float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Enter a number")


def user_kinetic_energy():
    print("This program calculates the kinetic energy of a moving object")
    mass = float_input("Enter the object's mass in kilograms: ")
    speed = float_input("Enter the object's speed in metres per second: ")
    print("The object has {:.1f} joules of kinetic energy.".format(0.5 * mass * speed ** 2))


if __name__ == "__main__":
    #user_kinetic_energy()
    print("print with \"quotes\". They're 'escaped'. These aren't.")
    print("what about \\n backslashes?")
    print("what about \rcarriage return?")


