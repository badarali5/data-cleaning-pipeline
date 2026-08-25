import json

FILE_PATH = "data/cleaned/healthcare_clean.json"


def read_patients():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def write_patients(patients):
    with open(FILE_PATH, "w") as file:
        json.dump(patients, file, indent=4)


def get_all_patients():
    return read_patients()


def get_patient(patient_id):
    patients = read_patients()

    if patient_id < 0 or patient_id >= len(patients):
        return None

    return patients[patient_id]


def create_patient(patient):
    patients = read_patients()

    patients.append(patient)

    write_patients(patients)

    return patient


def update_patient(patient_id, updated_patient):
    patients = read_patients()

    if patient_id < 0 or patient_id >= len(patients):
        return None

    patients[patient_id] = updated_patient

    write_patients(patients)

    return updated_patient


def delete_patient(patient_id):
    patients = read_patients()

    if patient_id < 0 or patient_id >= len(patients):
        return None

    deleted_patient = patients.pop(patient_id)

    write_patients(patients)

    return deleted_patient