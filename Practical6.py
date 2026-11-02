from itertools import product

# Example: KB = [R -> W, R]; Query = W

def implies(p, q):
    return (not p) or q

def knowledge_base(R, W):
    return implies(R, W) and R

variables = ['R', 'W']

truth_assignments = list(
    product([True, False], repeat=len(variables))
)

print("Truth Table Approach:")

entailment = True

for assignment in truth_assignments:
    R, W = assignment

    kb_val = knowledge_base(R, W)
    query_val = W

    print(f"R={R}, W={W} | KB: {kb_val}, Query: {query_val}")

    if kb_val and not query_val:
        entailment = False
        print("--> Counterexample found: KB is true but Query is false")
        break

if entailment:
    print("KB entails Query (W is always true if KB is true)")
else:
    print("KB does NOT entail Query")

print("\nResolution Example (hand-simulated):")

print("KB: (~R OR W), R")
print("Query: W, so use ~W for resolution")

print("Resolution Steps:")
print("1. (~R OR W) and ~W resolve to ~R")
print("2. R and ~R resolve to empty clause (contradiction)")
print("=> KB entails Query using resolution.")
