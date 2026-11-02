# ============================================================
# Certainty Factor Calculation
# Medical Diagnosis - Flu Detection
# ============================================================

def combine_cf(cf1, cf2):
    """
    Combine two certainty factors using standard CF combination rules.
    """

    if cf1 > 0 and cf2 > 0:
        # Both positive
        return cf1 + cf2 - (cf1 * cf2)

    elif cf1 < 0 and cf2 < 0:
        # Both negative
        return cf1 + cf2 + (cf1 * cf2)

    else:
        # Opposite signs
        denominator = 1 - min(abs(cf1), abs(cf2))

        if denominator == 0:
            return 0

        return (cf1 + cf2) / denominator

def calculate_combined_cf(cf_list):
    """
    Calculate combined certainty factor for multiple rules.
    """

    if not cf_list:
        return 0

    combined = cf_list[0]
    print(f"Starting CF: {combined}")

    for i in range(1, len(cf_list)):
        print(
            f"\nCombining CF{i-1} = {combined} "
            f"with CF{i} = {cf_list[i]}"
        )

        combined = combine_cf(combined, cf_list[i])

        print(f"Result: {combined:.4f}")

    return combined

# ============================================================
# Example 1: Medical Diagnosis - Flu Detection
# ============================================================

print("=" * 50)
print("Medical Diagnosis: Certainty Factor Calculation")
print("=" * 50)

print("\nRules:")
print("1. IF fever THEN flu [CF = 0.7]")
print("2. IF cough THEN flu [CF = 0.6]")
print("3. IF body ache THEN flu [CF = 0.5]")

print("\n" + "=" * 50)

cf_values = [0.7, 0.6, 0.5]

final_cf = calculate_combined_cf(cf_values)

print("\n" + "=" * 50)
print(f"Final Combined CF for Flu: {final_cf:.4f}")
print(f"Confidence Level: {final_cf * 100:.2f}%")
print("=" * 50)

# ============================================================
# Example 2: Mixed Evidence
# ============================================================

print("\n\nExample 2: Mixed Evidence (Positive and Negative)")
print("=" * 50)

cf_mixed = [0.8, -0.3, 0.5]

print(f"CF values: {cf_mixed}")

final_mixed = calculate_combined_cf(cf_mixed)

print("\n" + "=" * 50)
print(f"Final Combined CF: {final_mixed:.4f}")
print("=" * 50)
