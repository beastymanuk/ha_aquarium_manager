from datetime import datetime

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    async_add_entities(
        [
            AquariumManagerAgeSensor(
                entry.data["start_date"]
            )
        ]
    )


class AquariumManagerAgeSensor(SensorEntity):
    def __init__(self, start_date: str):
        self._start_date = start_date

        self._attr_name = "Aquarium Manager Age"
        self._attr_unique_id = "aquarium_manager_age"
        self._attr_icon = "mdi:fishbowl"

    @property
    def native_value(self):
        start = datetime.strptime(
            self._start_date,
            "%Y-%m-%d"
        ).date()

        days = (
            datetime.now().date() - start
        ).days

        years = days // 365
        months = (days % 365) // 30
        rem_days = (days % 365) % 30

        if years > 0:
            return f"{years} р. {months} міс. {rem_days} дн."

        if months > 0:
            return f"{months} міс. {rem_days} дн."

        return f"{days} дн."