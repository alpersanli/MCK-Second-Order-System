##########################################
# Including libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import ctypes


##########################################
# Plotting data

def plot_func(tru_centered, t, title_f, ylabel_f, xlabel_f):

    # obtain screen resolution

    user32 = ctypes.windll.user32

    screen_s_width = user32.GetSystemMetrics(0)
    screen_s_height = user32.GetSystemMetrics(1)

    print("screen size" + str(screen_s_width) + " " + str(screen_s_height))

    plt.figure(figsize=(int(screen_s_width)/200, int(screen_s_height)/200))

    # for adding data
    plt.plot(t, tru_centered, 'r')
    plt.xlabel(xlabel_f)
    plt.ylabel(ylabel_f)
    plt.grid(True)
    plt.title(title_f)

    plt.show()

# plotting data
##########################################


##########################################
# difference solver function

def centered_difference_solver(t_initial, t_final, dt, f_x_pre, f_x_now, f_x_fut, x_0, x_dot_0, u, length_of_loop):

    tru = np.arange(t_initial, t_final, dt, dtype=float)

    # initial condition assigment
    tru[0] = x_0
    tru[1] = tru[0] + x_dot_0 * dt

    for i in range(1, length_of_loop - 1):
        tru[i+1] = (tru[i]*f_x_now + tru[i-1]*f_x_pre)/f_x_fut + u[i]/f_x_fut

    return tru
    
# difference solver function
##########################################


##########################################
# main function

def main():
    # define sampling period
    dt = 0.01

    t_initial = 0.0
    t_final = 10.0

    length_of_loop = int((t_final - t_initial)/dt)

    # initial conditions
    x_0 = 10
    x_dot_0 = 5

    t = np.arange(t_initial, t_final, dt, dtype=float)
    u = np.arange(t_initial, t_final, dt, dtype=float)

    for i in range(0, length_of_loop):
        u[i] = 4

    # define system parameters 
    f_x_fut = (1/(dt*dt) + 3/(2*dt))
    f_x_now = (2/(dt*dt) -2)
    f_x_pre = (3/(2*dt) - 1/(dt*dt))

    system_setting_parameters = [t_initial,
                                 t_final,
                                 dt,
                                 f_x_pre,
                                 f_x_now,
                                 f_x_fut,
                                 x_0,
                                 x_dot_0,
                                 u,
                                 length_of_loop,
                                 t ]
    
    return system_setting_parameters

# main function
##########################################


if __name__ == " __main__ ":
    system_parameters_main = main()
    tru_centered = centered_difference_solver(system_parameters_main[0],
                                              system_parameters_main[1],
                                              system_parameters_main[2],
                                              system_parameters_main[3],
                                              system_parameters_main[4],
                                              system_parameters_main[5],
                                              system_parameters_main[6],
                                              system_parameters_main[7],
                                              system_parameters_main[8],
                                              system_parameters_main[9])
    
    t = system_parameters_main[10]    #zaman parametresi
    plot_func(tru_centered, t, "MCK Second Order System", 
              "Position(m)", "Time(sec)" )
    

