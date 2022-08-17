import uuid

# this code was basically used to generate the random loan IDs
# which were entered manually into loans table in MySQL
loan_id = [str(uuid.uuid4()) for _ in range(20)]
for id in loan_id:
    print(id)
