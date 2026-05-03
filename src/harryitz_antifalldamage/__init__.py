from endstone import Player
from endstone.damage import DamageCause
from endstone.event import EventHandler, ActorDamageEvent
from endstone.plugin import Plugin

_DIMENSION_MAP: dict[str, str] = {
    "overworld": "Overworld",
    "nether": "Nether",
    "the_end": "TheEnd",
}

class AntiFallDamage(Plugin):
    name = "AntiFallDamage"
    version = "1.0.0"
    api_version = "0.5"
    description = (
        "Prevents fall damage for all players in configurable dimensions. "
        "No commands required — configure via config.yml."
    )
    authors = ["harryitz"]

    def on_enable(self) -> None:
        self.save_default_config()
        self._load_dimensions()
        self.server.plugin_manager.register_events(self, self)

    @EventHandler
    def on_actor_damage(self, event: ActorDamageEvent) -> None:
        if event.damage_source.cause != DamageCause.FALL:
            return
        if not isinstance(event.actor, Player):
            return
        if event.actor.dimension.name in self._protected_dimensions:
            event.cancel()

    def _load_dimensions(self) -> None:
        raw: list[str] = self.config.get("dimensions", list(_DIMENSION_MAP.keys()))
        self._protected_dimensions: set[str] = set()
        for entry in raw:
            mapped = _DIMENSION_MAP.get(entry.lower())
            if mapped is not None:
                self._protected_dimensions.add(mapped)
            else:
                self.logger.warning(
                    f"Unknown dimension '{entry}' in config — skipped. "
                    "Valid values: overworld, nether, the_end"
                )
