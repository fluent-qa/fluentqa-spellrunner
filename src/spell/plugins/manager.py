from typing import Any

import pluggy

from spell.plugins import PLUGIN_NAMESPACE
from spell.plugins.models import SpellPluginImpl, SpellPluginSpec, SpellPluginBaseSpec


class SpellPluginManager:

    def __init__(self):
        self.pm = pluggy.PluginManager(PLUGIN_NAMESPACE)
        self.pm.add_hookspecs(SpellPluginSpec)

    def register_spec(self, spec_type: type[SpellPluginBaseSpec]):
        self.pm.add_hookspecs(spec_type)
        return self

    def load_plugin(self, plugin: Any):
        self.pm.register(plugin)
        return self

    def load_plugin_from_module(self,
                                module_name: str,
                                hook_impl: type = SpellPluginImpl,
                                hook_spec=None):
        pass

    def invoke_plugin(self):
        pass