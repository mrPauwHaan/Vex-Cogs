"""
This type stub file was generated by pyright.
"""

from .core import InvokableApplicationCommand

__all__ = (
    "InvokableContextMenuCommand",
    "InvokableUserCommand",
    "InvokableMessageCommand",
    "user_command",
    "message_command",
)

class InvokableContextMenuCommand(InvokableApplicationCommand):
    def __init__(self, func, *, name=..., guild_ids=..., **kwargs) -> None: ...
    async def invoke(self, interaction): ...

class InvokableUserCommand(InvokableContextMenuCommand):
    def __init__(self, func, *, name=..., guild_ids=..., **kwargs) -> None: ...

class InvokableMessageCommand(InvokableContextMenuCommand):
    def __init__(self, func, *, name=..., guild_ids=..., **kwargs) -> None: ...

def user_command(*args, **kwargs):  # -> (func: Unknown) -> InvokableUserCommand:
    """
    A decorator that allows to build a user command, visible in a context menu.

    Parameters
    ----------
    name : :class:`str`
        name of the user command you want to respond to (equals to function name by default).
    guild_ids : :class:`List[int]`
        if specified, the client will register the command in these guilds.
        Otherwise this command will be registered globally.
    """
    ...

def message_command(*args, **kwargs):  # -> (func: Unknown) -> InvokableMessageCommand:
    """
    A decorator that allows to build a message command, visible in a context menu.

    Parameters
    ----------
    name : :class:`str`
        name of the user command you want to respond to (equals to function name by default).
    guild_ids : :class:`List[int]`
        if specified, the client will register the command in these guilds.
        Otherwise this command will be registered globally.
    """
    ...