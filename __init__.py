def classFactory(iface):
    from .mainplugin import MainPlugin
    return MainPlugin(iface)
