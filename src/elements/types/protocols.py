from typing import Protocol


class SupportsClose(Protocol):
    def close(self) -> None: ...


class Resource:
    def close(self) -> None:
        print("Resource closed")


def close_all(resources: list[SupportsClose]) -> None:
    for resource in resources:
        resource.close()


res = Resource()
close_all([res])  # Output: Resource closed
