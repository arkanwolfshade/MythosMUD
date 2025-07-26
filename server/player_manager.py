import warnings


class PlayerManager:
    """
    Deprecated. Use PersistenceLayer from server.persistence instead.
    """

    def __init__(self, *args, **kwargs):
        warnings.warn("PlayerManager is deprecated. Use PersistenceLayer.", stacklevel=2)
        raise NotImplementedError("PlayerManager is deprecated. Use PersistenceLayer.")
