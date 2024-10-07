from pulp import LpMaximize, LpProblem, lpSum, LpVariable, LpMinimize

# Create the model
model = LpProblem(name="diet-problem", sense=LpMinimize)

# Initialize the variables
x1 = LpVariable(name="chicken_breast", lowBound=0)
x2 = LpVariable(name="quinoa_salad", lowBound=0)
x3 = LpVariable(name="lentil_soup", lowBound=0)
x4 = LpVariable(name="grilled_salmon", lowBound=0)
x5 = LpVariable(name="brown_rice", lowBound=0)

# Objective function
model += 3.50*x1 + 2.75*x2 + 2.25*x3 + 4.50*x4 + 1.50*x5

# Constraints
model += 250*x1 + 50*x2 + 400*x3 + 200*x4 + 2*x5 >= 2100  # Sodium
model += 165*x1 + 150*x2 + 230*x3 + 180*x4 + 110*x5 >= 2100  # Energy
model += 31*x1 + 8*x2 + 18*x3 + 35*x4 + 2*x5 >= 56  # Protein
model += 10*x4 >= 15  # Vitamin D
model += 10*x1 + 20*x2 + 70*x3 + 20*x4 + 10*x5 >= 1000  # Calcium
model += 1.5*x1 + 2.5*x2 + 6.5*x3 + 2.5*x4 + 1.5*x5 >= 8  # Iron
model += 450*x1 + 700*x2 + 1200*x3 + 500*x4 + 150*x5 >= 3500  # Potassium

# Solve the problem
status = model.solve()

# Print the solution
print("Solution:")
print("Chicken Breast:", x1.value())
print("Quinoa Salad:", x2.value())
print("Lentil Soup:", x3.value())
print("Grilled Salmon:", x4.value())
print("Brown Rice:", x5.value())
print("Total Cost: $", model.objective.value())
