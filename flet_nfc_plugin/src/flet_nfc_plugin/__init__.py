from flet.extension import register_extension
from .handler import NfcPlugin

def load(page):
    """
    Função obrigatória: o Flet chama `load(page)` automaticamente
    quando detecta este pacote como extensão.
    """
    # registra a classe de listener para eventos do plugin
    register_extension(NfcPlugin(page))
