from lmdeploy import TurbomindEngineConfig

class TurbomindConfig:
    def __init__(self, model_name, model_format, cache_max_entry_count):
        self.model_name = model_name
        self.model_format = model_format
        self.cache_max_entry_count = cache_max_entry_count

    def get_config(self):
        return TurbomindEngineConfig(
            model_name=self.model_name,
            model_format=self.model_format,
            cache_max_entry_count=self.cache_max_entry_count,
        )
