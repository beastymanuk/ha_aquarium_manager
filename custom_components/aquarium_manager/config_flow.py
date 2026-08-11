import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers.selector import (
    DateSelector,
    NumberSelector,
    NumberSelectorConfig,
)

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
                    ): DateSelector(),

                    vol.Optional(
                        "last_water_test_date",
                    ): DateSelector(),

                    vol.Optional(
                        "water_test_interval",
                    ): NumberSelector(
                        NumberSelectorConfig(
                            min=1,
                            max=365,
                            step=1,
                        )
                    ),

                    vol.Optional(
                        "last_filter_clean_date",
                    ): DateSelector(),

                    vol.Optional(
                        "filter_clean_interval",
                    ): NumberSelector(
                        NumberSelectorConfig(
                            min=1,
                            max=365,
                            step=1,
                        )
                    ),

                    vol.Optional(
                        "last_filter_maintenance_date",
                    ): DateSelector(),

                    vol.Optional(
                        "filter_maintenance_interval",
                    ): NumberSelector(
                        NumberSelectorConfig(
                            min=1,
                            max=365,
                            step=1,
                        )
                    ),

                    vol.Optional(
                        "last_partial_water_change_date",
                    ): DateSelector(),

                    vol.Optional(
                        "partial_water_change_interval",
                    ): NumberSelector(
                        NumberSelectorConfig(
                            min=1,
                            max=365,
                            step=1,
                        )
                    ),

                    vol.Optional(
                        "last_hungry_day_date",
                    ): DateSelector(),

                    vol.Optional(
                        "hungry_day_interval",
                    ): NumberSelector(
                        NumberSelectorConfig(
                            min=1,
                            max=365,
                            step=1,
                        )
                    ),
                }
            ),
        )