import os

i = True

print("Welcome to the Kinematics calculator! - Select the area that your equation is in!")
print("1 - Core equations")
print("2 - Primary equations")

slct = int(input("Type the number of the part that you want to enter: "))
while i == True:
    if slct == 1:
        print("Select one of the equations down here:")
        print("1 - Average velocity")
        print("2 - Average acceleration")
        print("3 - Go back")
        cr_eq_slct = int(input("Type the equation you want to use: "))
        if cr_eq_slct == 1:
            xfinal = int(input("Type your final x in m(meters): "))
            xinitial = int(input("Type your initial x in m(meters): "))
            dX = xfinal - xinitial
            tfinal = int(input("Type your final time in s(seconds): "))
            tinitial = int(input("Type your initial time in s(seconds): "))
            dT = tfinal - tinitial
            aV = dX/dT
            aVk = aV*3.6
            print(f"Your average velocity is {aV}m/s(meters per second) and {aVk}km/h(kilometer per hour)")
        elif cr_eq_slct == 2:
            vfinal = int(input("Type your final velocity in m/s(meters per second): "))
            vinitial = int(input("Type your initial velocity in m/s(meters per second): "))
            dV = vfinal - vinitial
            tfinal = int(input("Type your final time in s(seconds): "))
            tinitial = int(input("Type your initial time in s(seconds): "))
            dT = tfinal - tinitial
            aAC = dV/dT
            print(f"Your average acceleration is {aAC}m/s²(meters per second squared)")
        else:
            print("1 - Core equations")
            slct = int(input("Type the number of the part that you want to enter: "))
    
    if slct == 2:
        print("1 - Velocity-Time")
        print("2 - Position-Time")
        print("3 - Velocity-Squared")
        print("4 - Average-Velocity")
        pr_eq_slct = int(input("Type the number of the equation you want to use: "))
        if pr_eq_slct == 1:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            a = int(input("Type your acceleration in m/s²(meters per second squared): "))
            t = int(input("Type your time in s(seconds)"))
            v = v0 + a * t
            print(f"Your velocity is {v}m/s(meters per second)")
        elif pr_eq_slct == 2:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            a = int(input("Type your acceleration in m/s²(meters per second squared): "))
            t = int(input("Type your time in s(seconds): "))
            dX = v0*t+(a*t^2)/2
            print(f"Your delta x is {dX}m(meters)")
        elif pr_eq_slct == 3:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            a = int(input("Type your acceleration in m/s²(meters per second squared): "))
            xfinal = int(input("Type your final x in m(meters): "))
            xinitial = int(input("Type your initial x in m(meters): "))
            dX = xfinal - xinitial
            v^2 = v0^2+2*a*dX
            print(f"Your velocity is {v}m/s(meters per second)")
        elif pr_eq_slct == 4:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            t = int(input("Type your time in s(seconds): "))
            v = int(input("Type your velocity in m/s(meters per second): "))
            dX = 0.5*(v0+v)*t
            print(f"Your delta x is {dX}m(meters)")
        else:
            print("1 - Core equations")
            slct = int(input("Type the number of the part that you want to enter: "))

            
