class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list | None = None) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, distance_forward: int = 1) -> None:
        self.coords[1] += distance_forward

    def go_back(self, distance_backward: int = 1) -> None:
        self.coords[1] -= distance_backward

    def go_left(self, distance_left: int = 1) -> None:
        self.coords[0] -= distance_left

    def go_right(self, distance_right: int = 1) -> None:
        self.coords[0] += distance_right

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list | None = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        elif len(coords) != 3:
            raise ValueError("coords must contain exactly 3 values")
        super().__init__(name, weight, coords)

    def go_up(self, distance_up: int = 1) -> None:
        self.coords[2] += distance_up

    def go_down(self, distance_down: int = 1) -> None:
        self.coords[2] += -distance_down


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_load_weight: int,
                 coords: list | None = None,
                 current_load: Cargo | None = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, load: Cargo | None = None) -> None:
        if self.current_load is None and self.max_load_weight >= load.weight:
            self.current_load = load

    def unhook_load(self) -> None:
        self.current_load = None
