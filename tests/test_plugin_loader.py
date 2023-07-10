from spell.plugins.manager import SpellPluginManager
from spell.plugins.models import spell_hook_impl, SpellPluginImpl


class CustomPlugin(SpellPluginImpl):
    @spell_hook_impl
    def pre_invoke(self,**input):
        print("pre invoke")

    @spell_hook_impl
    def invoke(self, **input):
        print("invoke")

    @spell_hook_impl
    def after_invoke(self, **input):
        print("after invoke")


def test_load_plugin():
    spm = SpellPluginManager()
    spm.load_plugin(CustomPlugin())
    pm = spm.pm
    pm.hook.pre_invoke()
    pm.hook.invoke()
    pm.hook.after_invoke()
