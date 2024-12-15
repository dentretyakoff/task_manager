from exceptions.base import BackendError


class ApplicationNotFoundError(BackendError):
    """Не найдена заявка с указанным id."""
