
def bayes_theorem(prior_h, likelihood_e_given_h, likelihood_e_given_not_h):
    """
    Calculate posterior probability using Bayes' Theorem.
    """

    # Calculate total probability of evidence P(E)
    p_e = (
        likelihood_e_given_h * prior_h
        + likelihood_e_given_not_h * (1 - prior_h)
    )

    # Apply Bayes' Theorem
    posterior = (likelihood_e_given_h * prior_h) / p_e

    return posterior, p_e


def display_result(hypothesis, prior, likelihood_yes, likelihood_no, posterior):
    """Display results in a readable format."""

    print("\n" + "=" * 60)
    print(f"Bayes Theorem Calculation: {hypothesis}")
    print("=" * 60)

    print(f"Prior Probability P(H): {prior:.4f}")
    print(f"Likelihood P(E|H): {likelihood_yes:.4f}")
    print(f"Likelihood P(E|not H): {likelihood_no:.4f}")
    print(f"Prior Probability P(not H): {1 - prior:.4f}")

    print("-" * 60)
    print(f"Posterior Probability P(H|E): {posterior:.4f}")
    print(f"Confidence Level: {posterior * 100:.2f}%")
    print("=" * 60)


# Example 1: Medical Diagnosis
print("\nEXAMPLE 1: Medical Diagnosis - Disease Detection")

hypothesis_1 = "Patient has the disease"
prior_1 = 0.01
sensitivity = 0.95
specificity = 0.90
false_positive_rate = 1 - specificity

posterior_1, p_evidence_1 = bayes_theorem(
    prior_1,
    sensitivity,
    false_positive_rate
)

display_result(
    hypothesis_1,
    prior_1,
    sensitivity,
    false_positive_rate,
    posterior_1
)

print("\nInterpretation:")
print(
    f"Given a positive test, the probability of disease is "
    f"{posterior_1 * 100:.2f}%."
)


# Example 2: Spam Email Detection
print("\nEXAMPLE 2: Spam Email Detection")

hypothesis_2 = "Email is spam"
prior_2 = 0.30
p_word_given_spam = 0.80
p_word_given_not_spam = 0.05

posterior_2, p_evidence_2 = bayes_theorem(
    prior_2,
    p_word_given_spam,
    p_word_given_not_spam
)

display_result(
    hypothesis_2,
    prior_2,
    p_word_given_spam,
    p_word_given_not_spam,
    posterior_2
)

print("\nInterpretation:")
print(
    f"If an email contains the word 'click', the probability "
    f"that it is spam is {posterior_2 * 100:.2f}%."
)


# Example 3: Weather Prediction
print("\nEXAMPLE 3: Weather Prediction - Rain Forecast")

hypothesis_3 = "It will rain tomorrow"
prior_3 = 0.20
p_cloudy_given_rain = 0.90
p_cloudy_given_no_rain = 0.30

posterior_3, p_evidence_3 = bayes_theorem(
    prior_3,
    p_cloudy_given_rain,
    p_cloudy_given_no_rain
)

display_result(
    hypothesis_3,
    prior_3,
    p_cloudy_given_rain,
    p_cloudy_given_no_rain,
    posterior_3
)

print("\nInterpretation:")
print(
    f"Given cloudy conditions, the probability of rain is "
    f"{posterior_3 * 100:.2f}%."
)


# Comparison Table
print("\n" + "=" * 60)
print("SUMMARY: Posterior Probabilities for All Examples")
print("=" * 60)

print(f"{'Example':<30} {'Prior':<12} {'Posterior':<12}")
print("-" * 60)

print(f"{'Disease Detection':<30} {prior_1:<12.4f} {posterior_1:<12.4f}")
print(f"{'Spam Detection':<30} {prior_2:<12.4f} {posterior_2:<12.4f}")
print(f"{'Rain Prediction':<30} {prior_3:<12.4f} {posterior_3:<12.4f}")

print("=" * 60)
