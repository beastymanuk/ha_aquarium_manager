from datetime import date

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers import selector


class AquariumManagerOptionsFlow(
    config_entries.OptionsFlow,
):
    def __init__(
        self,
        config_entry,
    ):
        self._config_entry = config_entry
        self._options_data = {}

    async def async_step_init(
        self,
        user_input=None,
    ):
        errors = {}

        if user_input is not None:

            if not user_input.get(
                "start_date"
            ):
                errors["start_date"] = (
                    "required_start_date"
                )

            start_date = user_input.get(
                "start_date"
            )

            if start_date:

                selected_date = (
                    date.fromisoformat(
                        start_date
                    )
                )

                if selected_date > date.today():
                    errors["start_date"] = (
                        "future_date"
                    )

            if not errors:

                self._options_data.update(
                    user_input
                )

                return await self.async_step_maintenance()

        return self.async_show_form(
            step_id="init",
            errors=errors,
            data_schema=vol.Schema(
                {
                    vol.Required(
                        "aquarium_name",
                        default=self._config_entry.data.get(
                            "aquarium_name",
                            "",
                        ),
                    ): str,

                    vol.Optional(
                        "start_date",
                        default=self._config_entry.data.get(
                            "start_date",
                        ),
                    ): selector.DateSelector(),
                }
            ),
        )

    async def async_step_maintenance(
        self,
        user_input=None,
    ):
        errors = {}

        if user_input is not None:

            today = date.today()

            date_fields = [
                "last_water_test_date",
                "last_filter_clean_date",
                "last_filter_maintenance_date",
                "last_partial_water_change_date",
                "last_hungry_day_date",
            ]

            for field in date_fields:

                value = user_input.get(
                    field
                )

                if value:

                    selected_date = (
                        date.fromisoformat(
                            value
                        )
                    )

                    if selected_date > today:
                        errors[field] = (
                            "future_date"
                        )

            if not errors:

                self._options_data.update(
                    user_input
                )

                return self.async_create_entry(
                    title="",
                    data=self._options_data,
                )

        return self.async_show_form(
            step_id="maintenance",
            errors=errors,
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        "last_water_test_date",
                        default=self._config_entry.data.get(
                            "last_water_test_date",
                        ),
                    ): selector.DateSelector(),

                    vol.Optional(
                        "water_test_interval",
                        default=self._config_entry.data.get(
                            "water_test_interval",
                        ),
                    ): int,

                    vol.Optional(
                        "last_filter_clean_date",
                        default=self._config_entry.data.get(
                            "last_filter_clean_date",
                        ),
                    ): selector.DateSelector(),

                    vol.Optional(
                        "filter_clean_interval",
                        default=self._config_entry.data.get(
                            "filter_clean_interval",
                        ),
                    ): int,

                    vol.Optional(
                        "last_filter_maintenance_date",
                        default=self._config_entry.data.get(
                            "last_filter_maintenance_date",
                        ),
                    ): selector.DateSelector(),

                    vol.Optional(
                        "filter_maintenance_interval",
                        default=self._config_entry.data.get(
                            "filter_maintenance_interval",
                        ),
                    ): int,

                    vol.Optional(
                        "last_partial_water_change_date",
                        default=self._config_entry.data.get(
                            "last_partial_water_change_date",
                        ),
                    ): selector.DateSelector(),

                    vol.Optional(
                        "partial_water_change_interval",
                        default=self._config_entry.data.get(
                            "partial_water_change_interval",
                        ),
                    ): int,

                    vol.Optional(
                        "last_hungry_day_date",
                        default=self._config_entry.data.get(
                            "last_hungry_day_date",
                        ),
                    ): selector.DateSelector(),

                    vol.Optional(
                        "hungry_day_interval",
                        default=self._config_entry.data.get(
                            "hungry_day_interval",
                        ),
                    ): int,
                }
            ),
        )