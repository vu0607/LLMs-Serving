from backends.turbomind import TurbomindConfig
from backends.pytorch import PytorchConfig

class EngineConfigFactory:
    @staticmethod
    def get_engine_config(engine_type, model_name, model_format, cache_max_entry_count):
        if engine_type == "turbomind":
            return TurbomindConfig(model_name, model_format, cache_max_entry_count)
        elif engine_type == "pytorch":
            return PytorchConfig(model_name, model_format, cache_max_entry_count)
        else:
            raise ValueError(f"Unknown engine type: {engine_type}")
