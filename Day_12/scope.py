# Global Scope
enemies = 1


def increase_enemies():
    #   Local scope
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

'''
enemies inside function: 2
enemies outside function: 1
'''


if 9 > 7:
    # Global Scope & NOT Block scope
    enemies = 3
    print(f"enemies outside function: {enemies}")

print(f"enemies outside function: {enemies}")

'''
enemies outside function: 3
enemies outside function: 3
'''
