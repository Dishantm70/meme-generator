import base64
import uuid


def generate_uuid(key=None):
    try:
        return uuid.uuid5(uuid.NAMESPACE_DNS, str(key)) if key else uuid.uuid4()
    except:
        return uuid.uuid4()

def generate_id():
    uuid_val = generate_uuid()
    return base64.urlsafe_b64encode(uuid_val.bytes).decode('utf-8').strip('=')
