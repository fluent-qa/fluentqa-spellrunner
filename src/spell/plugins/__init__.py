PLUGIN_NAMESPACE = "spell-plugin"

from .models import spell_hook_impl, spell_hook_spec,SpellPluginImpl,\
    SpellPluginSpec,SpellPluginBaseSpec
from .manager import SpellPluginManager

plugins_mgr = SpellPluginManager()
