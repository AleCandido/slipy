def switch_framework(framework, actions):
    try:
        return actions[framework]()
    except KeyError:
        raise ValueError("unknown framework selected")
