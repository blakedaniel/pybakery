import types


def previewAttr(object):
    for attr in dir(object):
        if not attr.startswith('_'):
            try:
                result = getattr(object, attr)
                if isinstance(result, types.MethodType):
                    result = getattr(object, attr)()
                print(f'{attr}: {object} --> {result}')
            except Exception as e:
                print(f'{attr}: {e}')
                continue
