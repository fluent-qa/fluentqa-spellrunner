import pluggy

spell_hook_spec = pluggy.HookspecMarker("spell-plugin")
spell_hook_impl = pluggy.HookimplMarker("spell-plugin")


class SpellPluginImpl:
    pass


class SpellPluginSpec:

    @spell_hook_spec
    def pre_invoke(self, **input):
        pass

    @spell_hook_spec
    def invoke(self, **input):
        pass

    @spell_hook_spec
    def after_invoke(self, **input):
        pass



