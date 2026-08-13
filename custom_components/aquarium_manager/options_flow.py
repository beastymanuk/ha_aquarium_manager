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

    async def async_step_init(
        self,
        user_input=None,
    ):
        if user_input is not None:
            return self.async_create_entry(
                title="",
                data=user_input,
            )

        return self.async_show_form(
            step_id="init",
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