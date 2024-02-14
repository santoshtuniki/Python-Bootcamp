# Global Scope
enemies = 1


def increase_enemies():
    #   Global scope
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

'''
enemies inside function: 2
enemies outside function: 2
'''