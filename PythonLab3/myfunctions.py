from decimal import Decimal as dcm


def euler(func, x_init, t_fin, t_sampling, step_val = 0.0001):
    
    x_values = []
    t_values = []
    t = 0.0
    x = x_init

    while t<t_fin:
        
        if dcm(str(t)) % dcm(str(t_sampling))==0:
            t_values.append(round(t, 4))
            x_values.append(x)

        x = x + func(x)*step_val
        t+=step_val

        t = round(t, 4)

        if t==t_fin:
            t_values.append(round(t, 4))
            x_values.append(x) 

    return x_values, t_values
