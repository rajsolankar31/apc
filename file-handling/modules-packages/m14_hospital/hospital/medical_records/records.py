records = {}
def add_record(pid, diagnosis): records.setdefault(pid, []).append(diagnosis)
def get_records(pid): return records.get(pid, [])
