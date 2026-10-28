patients = {}
def add_patient(pid, name, age): patients[pid] = {"name": name, "age": age}; return patients[pid]
def get_patient(pid): return patients.get(pid)
