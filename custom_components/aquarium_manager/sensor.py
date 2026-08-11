from datetime import datetime

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    async_add_entities(
        [
            AquariumManagerAgeSensor(
                entry
            )
        ]
    )


class AquariumManagerAgeSensor(SensorEntity):

    _attr_has_entity_name = True

    def __init__(
        self,
        entry: ConfigEntry,
    ):
        self._entry = entry
        self._start_date = entry.data["start_date"]

        self._attr_name = "Age"
        self._attr_unique_id = (
            f"{entry.entry_id}_age"
        )
        self._attr_icon = "mdi:fishbowl"

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={
                (
                    DOMAIN,
                    self._entry.entry_id,
                )
            },
            name=self._entry.data[
                "aquarium_name"
            ],
            manufacturer="Aquarium Manager",
            model="Aquarium",
        )

    @property
    def native_value(self):
        start = datetime.strptime(
            self._start_date,
            "%Y-%m-%d"
        ).date()

        days = (
            datetime.now().date()
            - start
        ).days

        years = days // 365
        months = (days % 365) // 30
        rem_days = (days % 365) % 30

        if years > 0:
            return (
                f"{years} р. "
                f"{months} міс. "
                f"{rem_days} дн."
            )

        if months > 0:
            return (
                f"{months} міс. "
                f"{rem_days} дн."
            )

        return f"{days} дн."