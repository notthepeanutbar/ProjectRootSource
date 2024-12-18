# framework_start.py

framework_exists = False  # Start status: No framework

def build_framework():
    global framework_exists
    print("Building Framework...")
    if execute_framework():
        framework_exists = True
        rabbit_hole()
    else:
        raise Exception("FrameworkExecutionError")

def execute_framework():
    print("Framework EXECUTE successful.")
    return True

def rabbit_hole():
    print("ACTION: Go down the rabbit hole.")
