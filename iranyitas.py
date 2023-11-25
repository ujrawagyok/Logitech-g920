import pygame

pygame.init()


kontrollerek = pygame.joystick.get_count()
print(f"Az elérhető kontrolllerek száma: {kontrollerek}")

if kontrollerek > 0:
    wheel = pygame.joystick.Joystick(0)
    wheel.init()

steering = 1.0
throotle = 1.0
brake = 1.0
clutch = 1.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0: 
                steering = event.value
                print(f"kormany:{steering}   Kuplung:{clutch}   Fék: {brake}    Gáz:{throotle}")
            elif event.axis == 1: 
                throotle = event.value
                print(f"kormany:{steering}   Kuplung:{clutch}   Fék: {brake}    Gáz:{throotle}")
            elif event.axis == 2: 
                brake = event.value
                print(f"kormany:{steering}   Kuplung:{clutch}   Fék: {brake}    Gáz:{throotle}")
            elif event.axis == 3: 
                clutch = event.value
                print(f"kormany:{steering}   Kuplung:{clutch}   Fék: {brake}    Gáz:{throotle}")
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print("A")
            if event.button == 1:
                print("B")
            if event.button == 2:
                print("X")
            if event.button == 3:
                print("Y")
            if event.button == 4:
                print("RB")
            if event.button == 5:
                print("LB")
            if event.button == 6:
                print("Menu")
            if event.button == 7:
                print("Enter")
            if event.button == 8:
                print("RSB")
            if event.button == 9:
                print("LSB")
            if event.button == 10:
                print("Home")
            if event.button == 11:
                print("Reverse")
            if event.button == 12:
                print("1")
            if event.button == 13:
                print("2")
            if event.button == 14:
                print("3")
            if event.button == 15:
                print("4")
            if event.button == 16:
                print("5")
            if event.button == 17:
                print("6")
        elif event.type == pygame.JOYHATMOTION:
            print(event.value)