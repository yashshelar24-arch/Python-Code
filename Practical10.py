
class FuzzyMembershipFunction:

    @staticmethod
    def triangular(x, a, b, c):
        """Calculate triangular membership value."""

        if x < a or x > c:
            return 0.0

        if x == b:
            return 1.0

        if x < b:
            return (x - a) / (b - a) if b != a else 1.0

        return (c - x) / (c - b) if c != b else 1.0


class FuzzyTemperatureController:

    def fuzzify_temperature(self, temp):
        cold = FuzzyMembershipFunction.triangular(temp, 0, 5, 15)
        warm = FuzzyMembershipFunction.triangular(temp, 10, 17.5, 25)
        hot = FuzzyMembershipFunction.triangular(temp, 20, 27.5, 35)

        return {
            'cold': cold,
            'warm': warm,
            'hot': hot
        }

    def fuzzify_humidity(self, humidity):
        low = FuzzyMembershipFunction.triangular(humidity, 0, 20, 40)
        medium = FuzzyMembershipFunction.triangular(humidity, 30, 50, 70)
        high = FuzzyMembershipFunction.triangular(humidity, 60, 80, 100)

        return {
            'low': low,
            'medium': medium,
            'high': high
        }

    def apply_rules(self, temp, humidity):
        """Apply fuzzy IF-THEN rules."""

        rules = [
            ('off', min(temp['cold'], humidity['low'])),
            ('low', min(temp['warm'], humidity['low'])),
            ('medium', min(temp['warm'], humidity['medium'])),
            ('low', min(temp['hot'], humidity['low'])),
            ('medium', min(temp['hot'], humidity['medium'])),
            ('high', min(temp['hot'], humidity['high']))
        ]

        return rules

    def defuzzify(self, rules):
        """Calculate crisp fan speed using weighted average."""

        centers = {
            'off': 0,
            'low': 30,
            'medium': 60,
            'high': 90
        }

        numerator = 0
        denominator = 0

        for level, strength in rules:
            numerator += centers[level] * strength
            denominator += strength

        if denominator == 0:
            return 0

        return numerator / denominator

    def control(self, temperature, humidity):
        temp_fuzzy = self.fuzzify_temperature(temperature)
        humidity_fuzzy = self.fuzzify_humidity(humidity)

        rules = self.apply_rules(temp_fuzzy, humidity_fuzzy)
        fan_speed = self.defuzzify(rules)

        return fan_speed, temp_fuzzy, humidity_fuzzy, rules


# Create the controller
controller = FuzzyTemperatureController()

print("=" * 65)
print("FUZZY LOGIC TEMPERATURE AND FAN SPEED CONTROLLER")
print("=" * 65)


# Test cases
test_cases = [
    (10, 30, "Cold room, low humidity"),
    (18, 45, "Warm room, medium humidity"),
    (28, 75, "Hot room, high humidity"),
    (5, 20, "Very cold, very dry"),
    (32, 90, "Very hot, very humid")
]

print("\nTEST RESULTS")
print("-" * 65)

print(f"{'Temp':<10}{'Humidity':<12}{'Fan Speed':<14}{'Scenario'}")
print("-" * 65)

for temp, humidity, scenario in test_cases:
    speed, _, _, _ = controller.control(temp, humidity)

    print(
        f"{temp:<10}{humidity:<12}{speed:<14.2f}{scenario}"
    )


# Detailed analysis
temperature = 28
humidity = 75

fan_speed, temp_fuzzy, humidity_fuzzy, rules = controller.control(
    temperature,
    humidity
)

print("\nDETAILED ANALYSIS")
print("-" * 40)

print(f"Temperature: {temperature} C")
print(f"Humidity: {humidity}%")

print("\nTemperature Membership Values:")

for name, value in temp_fuzzy.items():
    print(f"{name.capitalize()}: {value:.4f}")


print("\nHumidity Membership Values:")

for name, value in humidity_fuzzy.items():
    print(f"{name.capitalize()}: {value:.4f}")


print("\nRules Fired:")

for level, strength in rules:
    if strength > 0:
        print(f"{level.capitalize()}: {strength:.4f}")


print(f"\nFinal Fan Speed: {fan_speed:.2f}%")

if fan_speed < 20:
    status = "OFF"
elif fan_speed < 50:
    status = "LOW"
elif fan_speed < 80:
    status = "MEDIUM"
else:
    status = "HIGH"

print("Fan Status:", status)

print("=" * 65)
