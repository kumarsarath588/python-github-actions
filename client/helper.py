import uuid


def is_uuid(UUID):
    """
    This routine helps to determine given UUID is a valid uuid or not
    Args:
        UUID(str): UUID string
    Returns:
        (bool): returns True/False
    """
    try:
        uuid.UUID(UUID)
        return True
    except ValueError:
        return False
