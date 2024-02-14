#Creating Entity
#update the entity
# entity represents a fundamental unit of data or functionality within the project
from dataclasses import dataclass
from pathlib import Path

#checking from config.yaml
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_URL : str
    local_data_file : Path
    unzip_dir : Path