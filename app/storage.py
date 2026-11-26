from app.models import SampleResponse

_store: dict[int, SampleResponse] = {}
_counter = 0


def save(name: str, value: int) -> SampleResponse:
    global _counter
    _counter += 1
    item = SampleResponse(id=_counter, name=name, value=value, message="created")
    _store[_counter] = item
    return item


def get_all() -> list[SampleResponse]:
    return list(_store.values())
