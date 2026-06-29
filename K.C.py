import math

i = True

sin_vals = {30: 1/2, 45: (2**0.5)/2, 60: (3**0.5)/2}
cos_vals = {30: (3**0.5)/2, 45: (2**0.5)/2, 60: 1/2}

while i == True:
    print("\nWelcome to the Kinematics calculator! - Select the area that your equation is in!")
    print("1 - Core equations")
    print("2 - Primary equations")
    print("3 - Projectile motion")
    print("4 - Circular movement")
    print("5 - Free fall")
    print("6 - Leave")

    slct = int(input("Type the number of the part that you want to enter: "))

    if slct == 1:
        print("\nSelect one of the equations down here:")
        print("1 - Average velocity")
        print("2 - Average acceleration")
        print("3 - Go back")
        cr_eq_slct = int(input("Type the equation you want to use: "))
        if cr_eq_slct == 1:
            xfinal = float(input("Type your final x in m(meters): "))
            xinitial = float(input("Type your initial x in m(meters): "))
            dX = xfinal - xinitial
            tfinal = float(input("Type your final time in s(seconds): "))
            tinitial = float(input("Type your initial time in s(seconds): "))
            dT = tfinal - tinitial
            aV = dX/dT
            aVk = aV*3.6
            print(f"Your average velocity is {aV}m/s and {aVk}km/h")
        elif cr_eq_slct == 2:
            vfinal = float(input("Type your final velocity in m/s: "))
            vinitial = float(input("Type your initial velocity in m/s: "))
            dV = vfinal - vinitial
            tfinal = float(input("Type your final time in s(seconds): "))
            tinitial = float(input("Type your initial time in s(seconds): "))
            dT = tfinal - tinitial
            aAC = dV/dT
            print(f"Your average acceleration is {aAC}m/s²")
        elif cr_eq_slct == 3:
            pass
        else:
            print("Invalid input")

    elif slct == 2:
        print("\n1 - Velocity-Time")
        print("2 - Position-Time")
        print("3 - Velocity-Squared")
        print("4 - Average-Velocity")
        print("5 - Go back")
        pr_eq_slct = int(input("Type the number of the equation you want to use: "))
        if pr_eq_slct == 1:
            v0 = float(input("Type your initial velocity in m/s: "))
            a = float(input("Type your acceleration in m/s²: "))
            t = float(input("Type your time in s(seconds): "))
            v = v0 + a * t
            print(f"Your velocity is {v}m/s")
        elif pr_eq_slct == 2:
            v0 = float(input("Type your initial velocity in m/s: "))
            a = float(input("Type your acceleration in m/s²: "))
            t = float(input("Type your time in s(seconds): "))
            dX = v0*t+(a*t**2)/2
            print(f"Your delta x is {dX}m")
        elif pr_eq_slct == 3:
            v0 = float(input("Type your initial velocity in m/s: "))
            a = float(input("Type your acceleration in m/s²: "))
            xfinal = float(input("Type your final x in m(meters): "))
            xinitial = float(input("Type your initial x in m(meters): "))
            dX = xfinal - xinitial
            v = (v0**2+2*a*dX)**0.5
            print(f"Your velocity is {v}m/s")
        elif pr_eq_slct == 4:
            v0 = float(input("Type your initial velocity in m/s: "))
            t = float(input("Type your time in s(seconds): "))
            v = float(input("Type your final velocity in m/s: "))
            dX = 0.5*(v0+v)*t
            print(f"Your delta x is {dX}m")
        elif pr_eq_slct == 5:
            pass
        else:
            print("Invalid input")

    elif slct == 3:
        print("\n1 - Horizontal and vertical components")
        print("2 - Horizontal range")
        print("3 - Maximum height")
        print("4 - Flight time")
        print("5 - Vertical position over time")
        print("6 - Horizontal position over time")
        print("7 - Vertical velocity over time")
        print("8 - Go back")
        pr_mo_slct = int(input("Type the equation you want to use: "))

        if pr_mo_slct == 1:
            print("\n1 - Y velocity")
            print("2 - X velocity")
            print("3 - Go back")
            pr_mo_slct_hv = int(input("Type the equation you want to use: "))
            if pr_mo_slct_hv == 1:
                v0 = float(input("Type your initial velocity in m/s: "))
                grau = int(input("Type theta in degrees (30, 45 or 60): "))
                if grau in sin_vals:
                    vY = sin_vals[grau]*v0
                    print(f"Your velocity for Y is {vY}m/s")
                else:
                    print("Invalid degree")
            elif pr_mo_slct_hv == 2:
                v0 = float(input("Type your initial velocity in m/s: "))
                grau = int(input("Type theta in degrees (30, 45 or 60): "))
                if grau in cos_vals:
                    vX = cos_vals[grau]*v0
                    print(f"Your velocity for X is {vX}m/s")
                else:
                    print("Invalid degree")
            elif pr_mo_slct_hv == 3:
                pass
            else:
                print("Invalid input")

        elif pr_mo_slct == 2:
            v0 = float(input("Type your initial velocity in m/s: "))
            grau = int(input("Type theta in degrees (30, 45 or 60): "))
            g = float(input("Type your gravity in m/s²: "))
            if grau in sin_vals:
                # R = v0² * sin(2θ) / g = v0² * 2*sin(θ)*cos(θ) / g
                r = (v0**2 * 2 * sin_vals[grau] * cos_vals[grau]) / g
                print(f"Your horizontal range is {r}m")
            else:
                print("Invalid degree")

        elif pr_mo_slct == 3:
            v0 = float(input("Type your initial velocity in m/s: "))
            grau = int(input("Type theta in degrees (30, 45 or 60): "))
            g = float(input("Type your gravity in m/s²: "))
            if grau in sin_vals:
                h = (v0**2 * sin_vals[grau]**2) / (2*g)
                print(f"Your maximum height is {h}m")
            else:
                print("Invalid degree")

        elif pr_mo_slct == 4:
            v0 = float(input("Type your initial velocity in m/s: "))
            grau = int(input("Type theta in degrees (30, 45 or 60): "))
            g = float(input("Type your gravity in m/s²: "))
            if grau in sin_vals:
                t = (v0 * 2 * sin_vals[grau]) / g
                print(f"Your flight time is {t}s")  # corrigido
            else:
                print("Invalid degree")

        elif pr_mo_slct == 5:
            v0 = float(input("Type your initial velocity in m/s: "))
            grau = int(input("Type theta in degrees (30, 45 or 60): "))
            g = float(input("Type your gravity in m/s²: "))
            t = float(input("Type your time in s(seconds): "))
            if grau in sin_vals:
                y = v0*sin_vals[grau]*t - (g*t**2)/2
                print(f"Your Y is {y}m")
            else:
                print("Invalid degree")

        elif pr_mo_slct == 6:
            v0 = float(input("Type your initial velocity in m/s: "))
            t = float(input("Type your time in s(seconds): "))
            grau = int(input("Type theta in degrees (30, 45 or 60): "))
            if grau in cos_vals:
                x = v0*cos_vals[grau]*t
                print(f"Your X is {x}m")
            else:
                print("Invalid degree")

        elif pr_mo_slct == 7:
            v0 = float(input("Type your initial velocity in m/s: "))
            grau = int(input("Type theta in degrees (30, 45 or 60): "))
            g = float(input("Type your gravity in m/s²: "))
            t = float(input("Type your time in s(seconds): "))
            if grau in sin_vals:
                vY = v0*sin_vals[grau] - g*t
                print(f"Your velocity for Y is {vY}m/s")
            else:
                print("Invalid degree")

        elif pr_mo_slct == 8:
            pass
        else:
            print("Invalid input")

    elif slct == 4:
        print("\n1 - Principles")
        print("2 - Main equations")
        print("3 - Go back")
        ci_mo_slct = int(input("Type the part that you want to go in: "))
        if ci_mo_slct == 1:
            print("\n1 - Period")
            print("2 - Frequency")
            print("3 - Angular Frequency")
            print("4 - Period-Frequency relation")
            print("5 - Go back")
            ci_mo_slct_pr = int(input("Type the equation you want to use: "))
            if ci_mo_slct_pr == 1:
                oo = float(input("Type your ω(omega) in rad/s: "))
                t = (2*math.pi)/oo
                print(f"Your period is {t}s")
            elif ci_mo_slct_pr == 2:
                t = float(input("Type your period in s(seconds): "))
                f = 1/t
                print(f"Your frequency is {f}Hz")
            elif ci_mo_slct_pr == 3:
                f = float(input("Type your frequency in Hz: "))
                oo = 2*math.pi*f
                print(f"Your ω(omega) is {oo}rad/s")
            elif ci_mo_slct_pr == 4:
                f = float(input("Type your frequency in Hz: "))
                t = 1/f
                print(f"Your period is {t}s")
            elif ci_mo_slct_pr == 5:
                pass
            else:
                print("Invalid input")

        elif ci_mo_slct == 2:
            print("\n1 - Angular velocity")
            print("2 - Linear velocity")
            print("3 - Linear-Angular relation")
            print("4 - Centripetal acceleration")
            print("5 - Go back")
            ci_mo_slct_me = int(input("Type the number of the equation you want to use: "))
            if ci_mo_slct_me == 1:
                tfinal = float(input("Type your final time in s(seconds): "))
                tinitial = float(input("Type your initial time in s(seconds): "))
                final0 = float(input("Type your final θ(theta) in radians: "))
                initial0 = float(input("Type your initial θ(theta) in radians: "))
                dT = tfinal-tinitial
                d0 = final0-initial0
                oo = d0/dT
                print(f"Your ω(omega) is {oo}rad/s")
            elif ci_mo_slct_me == 2:
                t = float(input("Type your period in s(seconds): "))
                r = float(input("Type your radius in m(meters): "))
                v = (2*math.pi*r)/t
                print(f"Your linear velocity is {v}m/s")
            elif ci_mo_slct_me == 3:
                r = float(input("Type your radius in m(meters): "))
                oo = float(input("Type your ω(omega) in rad/s: "))
                v = oo*r
                print(f"Your linear velocity is {v}m/s")
            elif ci_mo_slct_me == 4:
                print("\n1 - Linear")
                print("2 - Angular")
                print("3 - Go back")
                ci_mo_slct_me_ca = int(input("Type the number of the equation you want to use: "))
                if ci_mo_slct_me_ca == 1:
                    r = float(input("Type your radius in m(meters): "))
                    v = float(input("Type your velocity in m/s: "))
                    ac = v**2/r
                    print(f"Your centripetal acceleration is {ac}m/s²")
                elif ci_mo_slct_me_ca == 2:
                    r = float(input("Type your radius in m(meters): "))
                    oo = float(input("Type your ω(omega) in rad/s: "))
                    ac = oo**2*r
                    print(f"Your centripetal acceleration is {ac}m/s²")
                elif ci_mo_slct_me_ca == 3:
                    pass
                else:
                    print("Invalid input")
            elif ci_mo_slct_me == 5:
                pass
            else:
                print("Invalid input")

        elif ci_mo_slct == 3:
            pass
        else:
            print("Invalid input")

    elif slct == 5:
        print("\n1 - Velocity")
        print("2 - Height")
        print("3 - Velocity-Height")
        print("4 - Go back")
        fe_fa_slct = int(input("Type the number of the equation that you want to use: "))
        if fe_fa_slct == 1:
            g = float(input("Type your gravity in m/s²: "))
            t = float(input("Type your time in s(seconds): "))
            v = g*t
            print(f"Your velocity is {v}m/s")
        elif fe_fa_slct == 2:
            g = float(input("Type your gravity in m/s²: "))
            t = float(input("Type your time in s(seconds): "))
            h = (g*t**2)/2
            print(f"Your height is {h}m")
        elif fe_fa_slct == 3:
            g = float(input("Type your gravity in m/s²: "))
            h = float(input("Type your height in m(meters): "))
            v = (2*g*h)**0.5
            print(f"Your velocity is {v}m/s")
        elif fe_fa_slct == 4:
            pass
        else:
            print("Invalid input")

    elif slct == 6:
        print("Byee!")
        i = False
    else:
        print("Invalid input")