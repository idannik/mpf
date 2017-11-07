"""Block Event Config Player."""
from mpf.core.config_player import ConfigPlayer


class BlockEventPlayer(ConfigPlayer):

    """Posts events based on config."""

    config_file_section = 'blocking'

    def play(self, settings, context, calling_context, priority=0, **kwargs):
        """Block event."""
        del kwargs
        print(settings)

    def validate_config_entry(self, settings: dict, name: str) -> dict:
        """Validate one entry of this player."""
        return settings

    def get_express_config(self, value):
        """Parse short config."""
        raise AssertionError()
