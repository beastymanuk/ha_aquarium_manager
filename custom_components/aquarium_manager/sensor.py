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
            AquariumManagerAgeSensor(entry),
            AquariumManagerDaysSinceWaterTestSensor(entry),
            AquariumManagerDaysSinceFilterCleanSensor(entry),
            AquariumManagerDaysSinceFilterMaintenanceSensor(entry),
            AquariumManagerDaysSincePartialWaterChangeSensor(entry),
            AquariumManagerDaysSinceHungryDaySensor(entry),
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

class AquariumDaysSinceSensor(SensorEntity):

    _attr_has_entity_name = True

    def __init__(
        self,
        entry: ConfigEntry,
        name: str,
        unique_suffix: str,
        icon: str,
        date_field: str,
    ):
        self._entry = entry
        self._date_field = date_field

        self._attr_name = name
        self._attr_unique_id = (
            f"{entry.entry_id}_{unique_suffix}"
        )
        self._attr_icon = icon

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={
                (
                    DOMAIN,
                    self._entry.entry_id,
                )
            }
        )

    @property
    def native_value(self):

        stored_date = self._entry.data.get(
            self._date_field
        )

        if not stored_date:
            return None

        date_value = datetime.strptime(
            stored_date,
            "%Y-%m-%d"
        ).date()

        return (
            datetime.now().date()
            - date_value
        ).days

class AquariumManagerDaysSinceWaterTestSensor(
    AquariumDaysSinceSensor
):
    def __init__(self, entry):
        super().__init__(
            entry,
            "Days Since Water Test",
            "days_since_water_test",
            "mdi:test-tube",
            "last_water_test_date",
        )

class AquariumManagerDaysSinceFilterCleanSensor(
    AquariumDaysSinceSensor
):
    def __init__(self, entry):
        super().__init__(
            entry,
            "Days Since Filter Clean",
            "days_since_filter_clean",
            "mdi:air-filter",
            "last_filter_clean_date",
        )

class AquariumManagerDaysSinceFilterMaintenanceSensor(
    AquariumDaysSinceSensor
):
    def __init__(self, entry):
        super().__init__(
            entry,
            "Days Since Filter Maintenance",
            "days_since_filter_maintenance",
            "mdi:wrench",
            "last_filter_maintenance_date",
        )

class AquariumManagerDaysSincePartialWaterChangeSensor(
    AquariumDaysSinceSensor
):
    def __init__(self, entry):
        super().__init__(
            entry,
            "Days Since Partial Water Change",
            "days_since_partial_water_change",
            "mdi:water-sync",
            "last_partial_water_change_date",
        )

class AquariumManagerDaysSinceHungryDaySensor(
    AquariumDaysSinceSensor
):
    def __init__(self, entry):
        super().__init__(
            entry,
            "Days Since Hungry Day",
            "days_since_hungry_day",
            "mdi:fish-off",
            "last_hungry_day_date",
        )