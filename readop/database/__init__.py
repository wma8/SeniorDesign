from .engine import Engine
from .models.base import Base

# import each model to initialize engine
from .models.access_pattern import AccessPattern
from .models.operation import Operation
from .models.storage_unit import StorageUnit
from .models.system_description import SystemDescription
from .models.workload_description import WorkloadDescription


Base.metadata.create_all(bind=Engine)
