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
                }
            ),
        )