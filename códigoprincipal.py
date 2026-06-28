import os

i = True

print("Welcome to the Kinematics calculator! - Select the area that your equation is in!")
print("1 - Core equations")
print("2 - Primary equations")
print("3 - Projectile motion")
print("4 - Circular movement")

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
        elif cr_eq_slct == 3:
            print("1 - Core equations")
            print("2 - Primary equations")
            print("3 - Projectile motion")
            print("4 - Circular movement")
            slct = int(input("Type the number of the part that you want to enter: "))
        else:
                print("Invalid input")
    
    if slct == 2:
        print("1 - Velocity-Time")
        print("2 - Position-Time")
        print("3 - Velocity-Squared")
        print("4 - Average-Velocity")
        print("5 - Go back")
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
        elif pr_eq_slct == 5:
            print("1 - Core equations")
            print("2 - Primary equations")
            print("3 - Projectile motion")
            print("4 - Circular movement")
            slct = int(input("Type the number of the part that you want to enter: "))
        else:
            print("Invalid input")

    if slct == 3:
        print("1 - Horizontal and vertical components")
        print("2 - Horizontal range")
        print("3 - Maximum height")
        print("4 - Flight time")
        print("5 - Vertical position over time")
        print("6 - Horizontal position over time")
        print("7 - Vertical velocity over time")
        print("8 - Go back")
        pr_mo_slct = int(input("Type the equation you want to use: "))

        if pr_mo_slct == 1:
            print("1 - Y velocity")
            print("2 - X velocity")
            pr_mo_slct_hv = int(input("Type the equation you want to use: "))
            
            if pr_mo_slct_hv == 1:
                v0 = int(input("Type your initial velocity in m/s(meters per second: )"))
                sin0 = int(input("Type the sine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
                if sin0 == 30 or "30°":
                    sin0 = 1/2
                    vY = sin0*v0
                    print(f"Your velocity for Y is {vY}m/s(meters per second)")
                elif sin0 == 45 or "45°":
                    sin0 = 2^0.5
                    vY = sin0*v0
                    print(f"Your velocity for Y is {vY}m/s(meters per second)")
                elif sin0 == 60 or "60°":
                    sin0 = 3^0.5
                    vY = sin0*v0
                    print(f"Your velocity for Y is {vY}m/s(meters per second)")
                else:
                    print("Invalid degree")
            elif pr_mo_slct_hv == 2:
                v0 = int(input("Type your initial velocity in m/s(meters per second: )"))
                cos0 = int(input("Type the cossine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
                if cos0 == 30 or "30°":
                    cos0 = (3^0.5)/2
                    vX = cos0*v0
                    print(f"Your velocity for X is {vX}m/s(meters per second)")
                elif cos0 == 45 or "45°":
                    cos0 = (2^0.5)/2
                    vX = cos0*v0
                    print(f"Your velocity for X is {vX}m/s(meters per second)")
                elif cos0 == 60 or "60°":
                    cos0 = 1/2
                    vX = cos0*v0
                    print(f"Your velocity for X is {vX}m/s(meters per second)")
                else:
                    print("Invalid degree")
            else:
                print("Invalid input")
        elif pr_mo_slct == 2:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            sin0 = int(input("Type the sine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
            g = int(input("Type your gravity in m/s²(meters per second squared): "))
            if sin0 == 30 or "30°":
                sin0 = 1/2
                r = (v0^2*sin0*2)/g
                print(f"Your horizontal range is {r}m(meters)")
            elif sin0 == 45 or "45°":
                sin0 = 2^0.5
                r = (v0^2*sin0*2)/g
                print(f"Your horizontal range is {r}m(meters)")
            elif sin0 == 60 or "60°":
                sin0 = 3^0.5
                r = (v0^2*sin0*2)/g
                print(f"Your horizontal range is {r}m(meters)")
            else:
                print("Invalid degree")
        elif pr_mo_slct == 3:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            sin0 = int(input("Type the sine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
            g = int(input("Type your gravity in m/s²(meters per second squared): "))
            if sin0 == 30 or "30°":
                sin0 = 1/2
                h = (v0^2*sin0^2)/2*g
                print(f"Your maximum height is {h}m(meters)")
            elif sin0 == 45 or "45°":
                sin0 = 2^0.5
                h = (v0^2*sin0^2)/2*g
                print(f"Your maximum height is {h}m(meters)")
            elif sin0 == 60 or "60°":
                sin0 = 3^0.5
                h = (v0^2*sin0^2)/2*g
                print(f"Your maximum height is {h}m(meters)")
            else:
                print("Invalid degree")
        elif pr_mo_slct == 4:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            sin0 = int(input("Type the sine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
            g = int(input("Type your gravity in m/s²(meters per second squared): "))
            if sin0 == 30 or "30°":
                sin0 = 1/2
                t = (v0*2*sin0)/g
                print(f"Your maximum height is {t}m(meters)")
            elif sin0 == 45 or "45°":
                sin0 = 2^0.5
                t = (v0*2*sin0)/g
                print(f"Your maximum height is {t}m(meters)")
            elif sin0 == 60 or "60°":
                sin0 = 3^0.5
                t = (v0*2*sin0)/g
                print(f"Your maximum height is {t}m(meters)")
            else:
                print("Invalid degree")
        elif pr_mo_slct == 5:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            sin0 = int(input("Type the sine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
            g = int(input("Type your gravity in m/s²(meters per second squared): "))
            t = int(input("Type your time in s(seconds): "))
            if sin0 == 30 or "30°":
                sin0 = 1/2
                y = v0*sin0*t-(g*t^2)/2
                print(f"Your Y is {y}m(meters)")
            elif sin0 == 45 or "45°":
                sin0 = 2^0.5
                y = v0*sin0*t-(g*t^2)/2
                print(f"Your Y is {y}m(meters)")
            elif sin0 == 60 or "60°":
                sin0 = 3^0.5
                y = v0*sin0*t-(g*t^2)/2
                print(f"Your Y is {y}m(meters)")
            else:
                print("Invalid degree")
        elif pr_mo_slct == 6:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            t = int(input("Type your time in s(seconds): "))
            cos0 = int(input("Type the cossine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
            if cos0 == 30 or "30°":
                cos0 = (3^0.5)/2
                x = v0*cos0*t
                print(f"Your X is {x}m(meters)")
            elif cos0 == 45 or "45°":
                cos0 = (2^0.5)/2
                x = v0*cos0*t
                print(f"Your X is {x}m(meters)")
            elif cos0 == 60 or "60°":
                cos0 = 1/2
                x = v0*cos0*t
                print(f"Your X is {x}m(meters)")
            else:
                print("Invalid degree")
        elif pr_mo_slct == 7:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            sin0 = int(input("Type the sine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
            g = int(input("Type your gravity in m/s²(meters per second squared): "))
            t = int(input("Type your time in s(seconds): "))
            if sin0 == 30 or "30°":
                sin0 = 1/2
                vY = v0*sin0-g*t
                print(f"Your velocity for Y is {vY}m/s(meters per second)")
            elif sin0 == 45 or "45°":
                sin0 = 2^0.5
                vY = v0*sin0-g*t
                print(f"Your velocity for Y is {vY}m/s(meters per second)")
            elif sin0 == 60 or "60°":
                sin0 = 3^0.5
                vY = v0*sin0-g*t
                print(f"Your velocity for Y is {vY}m/s(meters per second)")
            else:
                print("Invalid degree")
        elif pr_mo_slct == 8:
            print("1 - Core equations")
            print("2 - Primary equations")
            print("3 - Projectile motion")
            print("4 - Circular movement")
            slct = int(input("Type the number of the part that you want to enter: "))
        else:
            print("Invalid input")





















            
    else:
         print("Invalid input")

            
