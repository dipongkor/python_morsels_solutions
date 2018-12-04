class PermaDict(dict):
    def __init__(self, *args, silent=False, **kwargs):
        self.silent = silent
        self.force = False
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key in self and not self.force:
            if not self.silent:
                raise KeyError("'{}' already in dictionary".format(key))
            else:
                # Silently ignore update
                return
        super().__setitem__(key, value)

    def update(self, iterable_or_dict=None, *, force=False, **kwargs):
        self.force = force
        if iterable_or_dict:
            if isinstance(iterable_or_dict, dict):
                for key, value in iterable_or_dict.items():
                    self.__setitem__(key, value)
            else:
                for key, value in iterable_or_dict:
                    self.__setitem__(key, value)
        elif kwargs:
            for key, value in kwargs.items():
                self.__setitem__(key, value)
        self.force = False

    def force_set(self, key, value):
        super().__setitem__(key, value)
