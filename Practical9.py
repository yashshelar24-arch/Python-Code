
class ExpertSystem:

    def __init__(self):
        self.facts = {}
        self.rules = []
        self.derived_facts = []

    def add_fact(self, fact, value):
        self.facts[fact] = value

    def add_rule(self, conditions, conclusion):
        self.rules.append({
            'conditions': conditions,
            'conclusion': conclusion
        })

    def check_rule(self, rule):
        for fact, value in rule['conditions'].items():
            if fact not in self.facts or self.facts[fact] != value:
                return False
        return True

    def forward_chain(self):
        print("\nFORWARD CHAINING INFERENCE ENGINE")
        print("=" * 50)

        changed = True

        while changed:
            changed = False

            for rule in self.rules:
                if self.check_rule(rule):
                    conclusion = rule['conclusion']

                    if conclusion not in self.derived_facts:
                        self.derived_facts.append(conclusion)
                        changed = True
                        print("Rule fired:", conclusion)

        print("Inference complete.")
        return self.derived_facts

    def display_diagnosis(self):
        print("\nDIAGNOSIS RESULTS")
        print("=" * 50)

        if self.derived_facts:
            for i, diagnosis in enumerate(self.derived_facts, 1):
                print(f"{i}. {diagnosis}")
        else:
            print("No matching diagnosis found.")


def add_medical_rules(system):

    system.add_rule(
        {'fever': True, 'cough': True, 'sore_throat': True},
        'Diagnosis: Common Cold'
    )

    system.add_rule(
        {
            'fever': True,
            'cough': True,
            'body_ache': True,
            'chills': True
        },
        'Diagnosis: Flu (Influenza)'
    )

    system.add_rule(
        {
            'fever': True,
            'cough': True,
            'shortness_of_breath': True,
            'chest_pain': True
        },
        'Diagnosis: Pneumonia'
    )

    system.add_rule(
        {'fever': True, 'cough': True},
        'Diagnosis: Possible Respiratory Infection'
    )

    system.add_rule(
        {'fever': True},
        'Recommendation: Monitor temperature closely'
    )

    system.add_rule(
        {'cough': True},
        'Recommendation: Drink warm liquids and rest'
    )


# Patient 1
print("\nMEDICAL DIAGNOSIS EXPERT SYSTEM")
print("=" * 50)

patient1 = {
    'fever': True,
    'cough': True,
    'sore_throat': True,
    'body_ache': False,
    'chills': False,
    'shortness_of_breath': False,
    'chest_pain': False
}

expert1 = ExpertSystem()
add_medical_rules(expert1)

print("\nPatient 1 Symptoms:")

for symptom, present in patient1.items():
    expert1.add_fact(symptom, present)
    print(f"{symptom}: {'Present' if present else 'Absent'}")

expert1.forward_chain()
expert1.display_diagnosis()


# Patient 2
print("\nPATIENT 2")
print("=" * 50)

patient2 = {
    'fever': True,
    'cough': True,
    'sore_throat': False,
    'body_ache': True,
    'chills': True,
    'shortness_of_breath': False,
    'chest_pain': False
}

expert2 = ExpertSystem()
add_medical_rules(expert2)

print("\nPatient 2 Symptoms:")

for symptom, present in patient2.items():
    expert2.add_fact(symptom, present)
    print(f"{symptom}: {'Present' if present else 'Absent'}")

expert2.forward_chain()
expert2.display_diagnosis()
