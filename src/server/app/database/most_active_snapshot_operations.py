from beanie import PydanticObjectId
from pydantic import ValidationError
from typing import List, Union
from bson import ObjectId
from datetime import datetime, timedelta


from app.models.MostActiveSnapshot import MostActiveSnapshot, UpdateMostActiveSnapshotModel


most_active_snapshot_collection = MostActiveSnapshot

class MostActiveSnapshotOperations:

    async def add_most_active_snapshot(new_most_active_snapshot: MostActiveSnapshot) -> MostActiveSnapshot:
        new_most_active_snapshot.id = str(ObjectId())
        most_active_snapshot = await new_most_active_snapshot.create()
        return most_active_snapshot


    async def retrieve_all_most_active_snapshots() -> List[MostActiveSnapshot]:
        most_active_snapshots = await most_active_snapshot_collection.all().to_list()
        return most_active_snapshots


    async def retrieve_most_recent_most_active_snapshot(self) -> Union[MostActiveSnapshot, None]:
        most_recent_snapshot = await most_active_snapshot_collection.find().sort("-creationDate").limit(1).to_list()
        if most_recent_snapshot:
            return most_recent_snapshot[0]
        return None


    async def retrieve_most_active_snapshot(id: MostActiveSnapshot) -> MostActiveSnapshot:
        most_active_snapshot = await most_active_snapshot_collection.get(str(id))
        if most_active_snapshot:
            return most_active_snapshot
        

    async def delete_most_active_snapshot(id: PydanticObjectId) -> bool:
        try:
            most_active_snapshot = await most_active_snapshot_collection.get(str(id))
        except ValidationError as e:
            print(e.json())
        if most_active_snapshot:
            await most_active_snapshot.delete()
            return True


    async def delete_old_entries(cutoff_hours_ago) -> None:
        # Calculate the threshold date: current time minus threshold
        threshold_date = datetime.now() - timedelta(hours=cutoff_hours_ago)
        # Delete documents older than threshold
        await MostActiveSnapshot.find(MostActiveSnapshot.creationDate < threshold_date).delete()


    async def update_most_active_snapshot_data(id: PydanticObjectId, data: dict) -> Union[bool, MostActiveSnapshot]:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        most_active_snapshot = await most_active_snapshot_collection.get(str(id))
        if most_active_snapshot:
            await most_active_snapshot.update(update_query)
            return most_active_snapshot
        return False

