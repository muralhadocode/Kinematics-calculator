import os

i = True

print("Welcome to the Kinematics calculator! - Select the area that your equation is in!")
print("1 - Core equations")
print("2 - Primary equations")
print("3 - Projectile motion")
print("4 - Circular movement")
print("5 - Free fall")
print("6 - Leave")

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
            print("5 - Free fall")

            slct = int(input("Type the number of the part that you want to enter: "))
        else:
                print("Invalid input")
    
    elif slct == 2:
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
            dX = v0*t+(a*t**2)/2
            print(f"Your delta x is {dX}m(meters)")
        elif pr_eq_slct == 3:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            a = int(input("Type your acceleration in m/s²(meters per second squared): "))
            xfinal = int(input("Type your final x in m(meters): "))
            xinitial = int(input("Type your initial x in m(meters): "))
            dX = xfinal - xinitial
            v = (v0**2+2*a*dX)**0.5
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
            print("5 - Free fall")

            slct = int(input("Type the number of the part that you want to enter: "))
        else:
            print("Invalid input")

    elif slct == 3:
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
            print("3 - Go back")
            pr_mo_slct_hv = int(input("Type the equation you want to use: "))
            
            if pr_mo_slct_hv == 1:
                v0 = int(input("Type your initial velocity in m/s(meters per second: )"))
                sin0 = int(input("Type the sine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
                if sin0 == 30 or sin0 == "30°":
                    sin0 = 1/2
                    vY = sin0*v0
                    print(f"Your velocity for Y is {vY}m/s(meters per second)")
                elif sin0 == 45 or sin0 == "45°":
                    sin0 = (2**0.5)/2
                    vY = sin0*v0
                    print(f"Your velocity for Y is {vY}m/s(meters per second)")
                elif sin0 == 60 or sin0 == "60°":
                    sin0 = (3**0.5)/2
                    vY = sin0*v0
                    print(f"Your velocity for Y is {vY}m/s(meters per second)")
                else:
                    print("Invalid degree")
            elif pr_mo_slct_hv == 2:
                v0 = int(input("Type your initial velocity in m/s(meters per second: )"))
                cos0 = int(input("Type the cossine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
                if cos0 == 30 or cos0 == "30°":
                    cos0 = (3**0.5)/2
                    vX = cos0*v0
                    print(f"Your velocity for X is {vX}m/s(meters per second)")
                elif cos0 == 45 or cos0 == "45°":
                    cos0 = (2**0.5)/2
                    vX = cos0*v0
                    print(f"Your velocity for X is {vX}m/s(meters per second)")
                elif cos0 == 60 or cos0 == "60°":
                    cos0 = 1/2
                    vX = cos0*v0
                    print(f"Your velocity for X is {vX}m/s(meters per second)")
                else:
                    print("Invalid degree")
            elif pr_mo_slct_hv == 3:
                print("1 - Horizontal and vertical components")
                print("2 - Horizontal range")
                print("3 - Maximum height")
                print("4 - Flight time")
                print("5 - Vertical position over time")
                print("6 - Horizontal position over time")
                print("7 - Vertical velocity over time")
                print("8 - Go back")
                pr_mo_slct = int(input("Type the equation you want to use: "))
            else:
                print("Invalid input")
        elif pr_mo_slct == 2:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            sin0 = int(input("Type the sine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
            g = int(input("Type your gravity in m/s²(meters per second squared): "))
            if sin0 == 30 or sin0 == "30°":
                sin0 = 1/2
                r = (v0**2*sin0*2)/g
                print(f"Your horizontal range is {r}m(meters)")
            elif sin0 == 45 or sin0 == "45°":
                sin0 = (2**0.5)/2
                r = (v0**2*sin0*2)/g
                print(f"Your horizontal range is {r}m(meters)")
            elif sin0 == 60 or sin0 == "60°":
                sin0 = (3**0.5)/2
                r = (v0**2*sin0*2)/g
                print(f"Your horizontal range is {r}m(meters)")
            else:
                print("Invalid degree")
        elif pr_mo_slct == 3:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            sin0 = int(input("Type the sine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
            g = int(input("Type your gravity in m/s²(meters per second squared): "))
            if sin0 == 30 or sin0 == "30°":
                sin0 = 1/2
                h = (v0**2*sin0**2)/(2*g)
                print(f"Your maximum height is {h}m(meters)")
            elif sin0 == 45 or sin0 == "45°":
                sin0 = (2**0.5)/2
                h = (v0**2*sin0**2)/(2*g)
                print(f"Your maximum height is {h}m(meters)")
            elif sin0 == 60 or sin0 == "60°":
                sin0 = (3**0.5)/2
                h = (v0**2*sin0**2)/(2*g)
                print(f"Your maximum height is {h}m(meters)")
            else:
                print("Invalid degree")
        elif pr_mo_slct == 4:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            sin0 = int(input("Type the sine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
            g = int(input("Type your gravity in m/s²(meters per second squared): "))
            if sin0 == 30 or sin0 == "30°":
                sin0 = 1/2
                t = (v0*2*sin0)/g
                print(f"Your maximum height is {t}m(meters)")
            elif sin0 == 45 or sin0 == "45°":
                sin0 = (2**0.5)/2
                t = (v0*2*sin0)/g
                print(f"Your maximum height is {t}m(meters)")
            elif sin0 == 60 or sin0 == "60°":
                sin0 = (3**0.5)/2
                t = (v0*2*sin0)/g
                print(f"Your maximum height is {t}m(meters)")
            else:
                print("Invalid degree")
        elif pr_mo_slct == 5:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            sin0 = int(input("Type the sine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
            g = int(input("Type your gravity in m/s²(meters per second squared): "))
            t = int(input("Type your time in s(seconds): "))
            if sin0 == 30 or sin0 == "30°":
                sin0 = 1/2
                y = v0*sin0*t-(g*t**2)/2
                print(f"Your Y is {y}m(meters)")
            elif sin0 == 45 or sin0 == "45°":
                sin0 = (2**0.5)/2
                y = v0*sin0*t-(g*t**2)/2
                print(f"Your Y is {y}m(meters)")
            elif sin0 == 60 or sin0 == "60°":
                sin0 = (3**0.5)/2
                y = v0*sin0*t-(g*t**2)/2
                print(f"Your Y is {y}m(meters)")
            else:
                print("Invalid degree")
        elif pr_mo_slct == 6:
            v0 = int(input("Type your initial velocity in m/s(meters per second): "))
            t = int(input("Type your time in s(seconds): "))
            cos0 = int(input("Type the cossine of 0(theta) in degrees(only for 30°, 45° and 60°): "))
            if cos0 == 30 or cos0 == "30°":
                cos0 = (3**0.5)/2
                x = v0*cos0*t
                print(f"Your X is {x}m(meters)")
            elif cos0 == 45 or cos0 == "45°":
                cos0 = (2**0.5)/2
                x = v0*cos0*t
                print(f"Your X is {x}m(meters)")
            elif cos0 == 60 or cos0 == "60°":
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
            if sin0 == 30 or sin0 == "30°":
                sin0 = 1/2
                vY = v0*sin0-g*t
                print(f"Your velocity for Y is {vY}m/s(meters per second)")
            elif sin0 == 45 or sin0 == "45°":
                sin0 = (2**0.5)/2
                vY = v0*sin0-g*t
                print(f"Your velocity for Y is {vY}m/s(meters per second)")
            elif sin0 == 60 or sin0 == "60°":
                sin0 = (3**0.5)/2
                vY = v0*sin0-g*t
                print(f"Your velocity for Y is {vY}m/s(meters per second)")
            else:
                print("Invalid degree")
        elif pr_mo_slct == 8:
            print("1 - Core equations")
            print("2 - Primary equations")
            print("3 - Projectile motion")
            print("4 - Circular movement")
            print("5 - Free fall")

            slct = int(input("Type the number of the part that you want to enter: "))
        else:
            print("Invalid input")

    elif slct == 4:
        print("1 - Principles")
        print("2 - Main equations")
        print("3 - Go back")
        ci_mo_slct = int(input("Type the part that you want to go in: "))
        if ci_mo_slct == 1:
            print("1 - Period")
            print("2 - Frequency")
            print("3 - Angular Frequency")
            print("4 - Period-Frequency relation")
            print("5 - Go back")
            ci_mo_slct_pr = int(input("Type the equation you want to use: "))
            if ci_mo_slct_pr == 1:
                oo = int(input("Type your ω(omega) in rad/s(radians per second): "))
                t = (2*3.14)/oo
                print(f"Your period is {t}s(seconds)")
            elif ci_mo_slct_pr == 2:
                t = int(input("Type your period in s(seconds): "))
                f = 1/t
                print(f"Your frequency is {f}Hz(hertz)")
            elif ci_mo_slct_pr == 3:
                f = int(input("Type your frequency in Hz(hertz): "))
                oo = 2*3.14*f
                print(f"Your ω(omega) is {oo}rad/s(radians per second)")
            elif ci_mo_slct_pr == 4:
                f = int(input("Type your frequency in Hz(hertz): "))
                t = 1/f
                print(f"Your period is {t}s(seconds)")
            elif ci_mo_slct_pr == 5:
                print("1 - Principles")
                print("2 - Main equations")
                print("3 - Go back")
                ci_mo_slct = int(input("Type the part that you want to go in: "))
        elif ci_mo_slct == 2:
            print("1 - Angular velocity")
            print("2 - Linear velocity")
            print("3 - Linear-Angular relation")
            print("4 - Centripetal acceleration")
            print("5 - Go back")
            ci_mo_slct_me = int(input("Type the number of the equation you want to use: "))
            if ci_mo_slct_me == 1:
                tfinal = int(input("Type your final time in s(seconds): "))
                tinitial = int(input("Type your initial time in s(seconds): "))
                final0 = int(input("Type your final 0(theta) in °(degrees without the little symbol)"))
                initial0 = int(input("Type your initial 0(theta) in "))
                dT = tfinal-tinitial
                d0 = final0-initial0
                oo = d0/dT
                print(f"Your ω(omega) is {oo}rad/s(radians per second)")
            elif ci_mo_slct_me == 2:
                t = int(input("Type your period in s(seconds): "))
                r = int(input("Type your radius in m(meters): "))
                v = (2*3.14*r)/t
                print(f"Your linear velocity is {v}m/s(meters per second)")
            elif ci_mo_slct_me == 3:
                r = int(input("Type your radius in m(meters): "))
                oo = int(input("Type your ω(omega) in rad/s(radians per second): "))
                v = oo*r
                print(f"Your linear velocity is {v}m/s(meters per second)")
            elif ci_mo_slct_me == 4:
                print("1 - Linear")
                print("2 - Angular")
                print("3 - Go back")
                ci_mo_slct_me_ca = int(input("Type the number of the equation you want to use"))
                if ci_mo_slct_me_ca == 1:
                    r = int(input("Type your radius in m(meters): "))
                    v = int(input("Type your velocity in m/s(meters per second): "))
                    ac = v**2/r
                    print(f"Your centripetal acceleration for the linear part is {ac}m/s²(meters per second squared)")
                elif ci_mo_slct_me_ca == 2: 
                    r = int(input("Type your radius in m(meters): "))
                    oo = int(input("Type your ω(omega) in rad/s(radians per second): "))
                    ac = oo**2*r
                    print(f"Your centripetal acceleration for the angular part is {ac}m/s²(meters per second squared)")
                elif ci_mo_slct_me_ca == 3:
                    print("1 - Angular velocity")
                    print("2 - Linear velocity")
                    print("3 - Linear-Angular relation")
                    print("4 - Centripetal acceleration")
                    print("5 - Go back")
                    ci_mo_slct_me_ca = int(input("Type the number of the equation you want to use: "))
                else:
                    print("Invalid input")
            elif ci_mo_slct_me == 5:
                print("1 - Principles")
                print("2 - Main equations")
                print("3 - Go back")
                ci_mo_slct = int(input("Type the part that you want to go in: "))
            else:
                print("Invalid input")
        elif ci_mo_slct == 3:
            print("1 - Core equations")
            print("2 - Primary equations")
            print("3 - Projectile motion")
            print("4 - Circular movement")
            print("5 - Free fall")

            slct = int(input("Type the number of the part that you want to enter: "))
        else:
            print("Invalid input")
    
    elif slct == 5:
        print("1 - Velocity")
        print("2 - Height")
        print("3 - Velocity-Height")
        print("4 - Go back")
        fe_fa_slct = int(input("Type the number of the equation that you want to use: "))
        if fe_fa_slct == 1:
            g = int(input("Type your gravity in m/s²(meters per second squared): "))
            t = int(input("Type your time in s(seconds): "))
            v = g*t
            print(f"Your velocity is {v}m/s(meters per second)")
        elif fe_fa_slct == 2:
            g = int(input("Type your gravity in m/s²(meters per second squared): "))
            t = int(input("Type your time in s(seconds): "))
            h = (g*t**2)/2
            print(f"Your height is {h}m(meters)")
        elif fe_fa_slct == 3:
            g = int(input("Type your gravity in m/s²(meters per second squared): "))
            h = int(input("Type your height in m(meters): "))
            v = (2*g*h)**0.5
            print(f"Your velocity is {v}m/s(meters per second)")
        elif fe_fa_slct == 4:
            print("1 - Core equations")
            print("2 - Primary equations")
            print("3 - Projectile motion")
            print("4 - Circular movement")
            print("5 - Free fall")

            slct = int(input("Type the number of the part that you want to enter: "))
    
    elif slct == 6:
        print("Byee!")
        i = False
    else:
         print("Invalid input")

            
