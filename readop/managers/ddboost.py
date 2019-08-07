from readop.protocols.ddboost import DDBStress
from readop.managers.database import DatabaseManager


class DDBoostManager:
    def execute(self, operation) -> int:
        dm = DatabaseManager()

        access_pattern = dm.get_access_pattern_by_id(operation.access_pattern_id)
        storage_unit = dm.get_storage_unit_by_id(operation.storage_unit_id)

        self.executedObj = DDBStress('/opt/dell/access_pattern_files/' + access_pattern.file_path, storage_unit.name)
        self.executedObj.stats.setOperationObject(operation)
        return 0

    def getStats(self):
        return self.executedObj.stats
    
    def getStatsJSON(self):
        return self.executedObj.stats.getJSON()
