import fileinput
import math

input = [l.strip() for l in fileinput.input()]

register_a = int(input[0].split(": ")[1])
register_b = int(input[1].split(": ")[1])
register_c = int(input[2].split(": ")[1])

print(register_a, register_b, register_c)

opcodes = list(map(int, input[-1].split(": ")[1].split(",")))


pointer = 0


def combo_operand_lookup(operand):
    return {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: register_a,
        5: register_b,
        6: register_c,
    }[operand]


# Opcode 0. Writes to register a
def adv(register_a, operand):
    combo = combo_operand_lookup(operand)
    result = register_a / (2**combo)

    return math.trunc(result)


# Opcode 1. Writes to register b
def bxl(register_b, operand):
    return operand ^ register_b


# Opcode 2. Write to register b
def bst(operand):
    combo = combo_operand_lookup(operand)

    return combo % 8


# Opcode 3. Doesnt write to register
def jnz(register_a):
    if register_a == 0:
        return False

    return True


# Opcode 4. Store in register b
def bxc(register_b, register_c, operand):
    return register_b ^ register_c


# Opcode 5. Doesnt write to register
def out(operand):
    combo = combo_operand_lookup(operand)

    return combo % 8


# Opcode 6. Write to register b
def bdv(register_a, operand):
    combo = combo_operand_lookup(operand)
    result = register_a / (2**combo)

    return math.trunc(result)


# Opcode 7. Write to register c
def cdv(register_a, operand):
    combo = combo_operand_lookup(operand)
    result = register_a / (2**combo)

    return math.trunc(result)


console = []

while pointer < len(opcodes) - 1:
    opcode = opcodes[pointer]
    operand = opcodes[pointer + 1]

    match opcode:
        case 0:
            register_a = adv(register_a, operand)
            pointer += 2

        case 1:
            register_b = bxl(register_b, operand)
            pointer += 2

        case 2:
            register_b = bst(operand)
            pointer += 2

        case 3:
            advance = jnz(register_a)

            if advance:
                pointer = operand
            else:
                pointer += 2

        case 4:
            register_b = bxc(register_b, register_c, operand)
            pointer += 2

        case 5:
            output = out(operand)
            console.append(output)
            pointer += 2

        case 6:
            register_b = bdv(register_a, operand)
            pointer += 2

        case 7:
            register_c = cdv(register_a, operand)
            pointer += 2

print(f"Part 1: {','.join(str(x) for x in console)}")
