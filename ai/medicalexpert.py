class ExpertSystem:
    def __init__(self):
        self.diseases = {
            "Flu": {
                "fever": True,
                "cough": True,
                "fatigue": True,
                "chills": True,
                "headache": False
            },
            "Cold": {
                "fever": False,
                "cough": True,
                "fatigue": True,
                "chills": False,
                "headache": True
            },
            "COVID-19": {
                "fever": True,
                "cough": True,
                "fatigue": True,
                "chills": True,
                "headache": True
            }
        }

    def ask_symptom(self, symptom):
        response = input(f"Do you have {symptom}? (yes/no): ").lower()
        return response == 'yes'

    def diagnose(self):
        # Ask the user about symptoms
        symptoms = ["fever", "cough", "fatigue", "chills", "headache"]
        patient_symptoms = {}

        for symptom in symptoms:
            patient_symptoms[symptom] = self.ask_symptom(symptom)

        # Check for diseases based on patient symptoms
        diagnosis = []
        for disease, disease_symptoms in self.diseases.items():
            match = True
            for symptom, is_present in disease_symptoms.items():
                if patient_symptoms[symptom] != is_present:
                    match = False
                    break
            if match:
                diagnosis.append(disease)

        # Provide diagnosis
        if diagnosis:
            print("\nBased on your symptoms, you might have the following conditions:")
            for disease in diagnosis:
                print(f"- {disease}")
        else:
            print("\nSorry, we couldn't match your symptoms to a known condition.")

# Example of using the expert system
if __name__ == "__main__":
    print("Welcome to the Medical Diagnosis Expert System!")
    expert_system = ExpertSystem()
    expert_system.diagnose()



