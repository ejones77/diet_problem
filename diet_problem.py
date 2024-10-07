from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize
from pulp import PULP_CBC_CMD

def optimization(var_list, constraint_list, objective, min_or_max):
    if min_or_max == 'max':
        prob = LpProblem("problem", LpMaximize)
    elif min_or_max == 'min':
        prob = LpProblem("problem", LpMinimize)
    else:
        raise ('Choose min or max instead.')
    
    for constraint in constraint_list:
        prob += constraint

    prob += objective
    solver = PULP_CBC_CMD(msg=False)
    status = prob.solve(solver)
    LpStatus[status]

    for var in var_list:
        print(f"Optimal value for {var}: {value(var)}")

def main():
    H = LpVariable("H", lowBound=0)
    C = LpVariable("C", lowBound=0)
    L = LpVariable("L", lowBound=0)
    B = LpVariable("B", lowBound=0)
    F = LpVariable("F", lowBound=0)  

    var_list = [H,C,L,B,F]

    constraint_list_plain = [
        914.25*H+670*C+1196.5*L+720*B+277.13*F <= 35000,
        368*H+804.25*C+573*L+790*B+447.47*F >= 14000,
        40.04*H+60.86*C+22.85*L+30*B+54.53*F >= 350,
        20.88*H+.18*C+0*L+5.1*B+7.63*F >= 140,
        40.13*H+113.75*C+227.75*L+860*B+115.87*F >= 9100,
        2.15*H+3.82*C+3.6*L+5.6*B+3.17*F >= 126,
        1372.75*H+1682.25*C+517*L+960*B+1064.87*F >= 32900
    ]

    objective = 9.23*H + 8.19*C + 2.37*L + 3.51*B + 4.28*F

    print("PLAIN", '\n')
    optimization(var_list, constraint_list_plain, objective, 'min')

    nutritional_values = [
        (914.25*H+670*C+1196.5*L+720*B+277.13*F, "Sodium", "<=", 35000),
        (368*H+804.25*C+573*L+790*B+447.47*F, "Energy", ">=", 14000),
        (40.04*H+60.86*C+22.85*L+30*B+54.53*F, "Protein", ">=", 350),
        ( 20.88*H+.18*C+0*L+5.1*B+7.63*F, "Vitamin D", ">=", 140),
        (40.13*H+113.75*C+227.75*L+860*B+115.87*F, "Calcium", ">=", 9100),
        (2.15*H+3.82*C+3.6*L+5.6*B+3.17*F, "Iron", ">=", 126),
        (1372.75*H+1682.25*C+517*L+960*B+1064.87*F, "Potassium", ">=", 32900)
    ]
    print('\n')
    print("Nutritional Values:")
    for value, name, operator, limit in nutritional_values:
        print(f"{name}: {value.value():.2f} {operator} {limit}")
    print('\n')
    print("VARIETY", '\n')
    variety_list = [
        H >= 1,
        C >= 1,
        L >= 1,
        B >= 1,
        F >= 1,
        H + C + L + B + F <= 27
    ]

    constraint_list_variety = constraint_list_plain + variety_list
    optimization(var_list, constraint_list_variety, objective, 'min')

    nutritional_values = [
        (914.25*H+670*C+1196.5*L+720*B+277.13*F, "Sodium", "<=", 35000),
        (368*H+804.25*C+573*L+790*B+447.47*F, "Energy", ">=", 14000),
        (40.04*H+60.86*C+22.85*L+30*B+54.53*F, "Protein", ">=", 350),
        ( 20.88*H+.18*C+0*L+5.1*B+7.63*F, "Vitamin D", ">=", 140),
        (40.13*H+113.75*C+227.75*L+860*B+115.87*F, "Calcium", ">=", 9100),
        (2.15*H+3.82*C+3.6*L+5.6*B+3.17*F, "Iron", ">=", 126),
        (1372.75*H+1682.25*C+517*L+960*B+1064.87*F, "Potassium", ">=", 32900)
    ]
    print('\n')
    print("Nutritional Values:")
    for value, name, operator, limit in nutritional_values:
        print(f"{name}: {value.value():.2f} {operator} {limit}")

    

if __name__ == '__main__':
    main()