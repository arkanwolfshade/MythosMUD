"""
Combat messaging integration - composes base and broadcast mixins.

As noted in the Pnakotic Manuscripts, the transmission of forbidden knowledge
must reach all who bear witness to the cosmic horror unfolding.
"""

from server.services.combat_messaging.base import CombatMessagingBase
from server.services.combat_messaging.combat_broadcasts import CombatBroadcastMixin
from server.services.combat_messaging.player_broadcasts import PlayerBroadcastMixin


class CombatMessagingIntegration(CombatBroadcastMixin, PlayerBroadcastMixin, CombatMessagingBase):
    """
    Integrates combat messaging with the real-time messaging system.

    This service handles broadcasting combat messages to all players in a room
    using the existing real-time messaging infrastructure.
    """


combat_messaging_integration = CombatMessagingIntegration()
