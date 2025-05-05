def diagnose(symptoms):
    if "fever" in symptoms and "cough" in symptoms and "fatigue" in symptoms and "loss of taste" in symptoms:
        return "You may have COVID-19."
    elif "fever" in symptoms and "cough" in symptoms and "body ache" in symptoms:
        return "You may have the Flu."
    elif "sneezing" in symptoms and "cough" in symptoms and "runny nose" in symptoms:
        return "You may have the Common Cold."
    elif "headache" in symptoms and "blurred vision" in symptoms:
        return "You may have a Migraine."
    else:
        return "Insufficient data to diagnose. Please consult a doctor."

def main():
    print("=== Medical Expert System ===")
    print("Enter your symptoms (comma-separated):")
    user_input = input("Symptoms: ").lower()
    symptoms = [s.strip() for s in user_input.split(",")]
    diagnosis = diagnose(symptoms)
    print("\nDiagnosis:", diagnosis)

if __name__ == "__main__":
    main()
