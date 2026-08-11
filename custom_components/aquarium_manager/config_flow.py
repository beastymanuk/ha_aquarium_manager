import voluptuous as vol

from homeassistant import config_entries

from .const import DOMAIN


class AquariumManagerConfigFlow(
    config_entries.ConfigFlow,
    domain=DOMAIN,
):
    VERSION = 1

    async def async_step_user(
        self,
        user_input=None,
    ):
        if user_input is not None:
            return self.async_create_entry(
                title=user_input["aquarium_name"],
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        "aquarium_name",
                        default="My Aquarium",
                    ): str,

                    vol.Required(
                        "start_date",
                        default="2025-01-01",
                    ): str,

                    vol.Optional(
                        "last_water_test_date",
                    ): str,

                    vol.Optional(
                        "water_test_interval",
                    ): int,

                    vol.Optional(
                        "last_filter_clean_date",
                    ): str,

                    vol.Optional(
                        "filter_clean_interval",
                    ): int,

                    vol.Optional(
                        "last_filter_maintenance_date",
                    ): str,

                    vol.Optional(
                        "filter_maintenance_interval",
                    ): int,

                    vol.Optional(
                        "last_partial_water_change_date",
                    ): str,

                    vol.Optional(
                        "partial_water_change_interval",
                    ): int,

                    vol.Optional(
                        "last_hungry_day_date",
                    ): str,

                    vol.Optional(
                        "hungry_day_interval",
                    ): int,
                }
            ),
        )