from beanie import PydanticObjectId
from pydantic import ValidationError
from typing import List, Union
from bson import ObjectId
from datetime import datetime, timedelta


from app.models.LeadersTableSnapshot import LeadersTableSnapshot, UpdateLeadersTableSnapshotModel


leader_table_snapshot_collection = LeadersTableSnapshot

class LeadersTableSnapshotOperations:

    async def add_leader_table_snapshot(new_leader_table_snapshot: LeadersTableSnapshot) -> LeadersTableSnapshot:
        new_leader_table_snapshot.id = str(ObjectId())
        leader_table_snapshot = await new_leader_table_snapshot.create()
        return leader_table_snapshot


    async def retrieve_all_leader_table_snapshots() -> List[LeadersTableSnapshot]:
        leader_table_snapshots = await leader_table_snapshot_collection.all().to_list()
        return leader_table_snapshots


    async def retrieve_most_recent_leader_table_snapshot(self) -> Union[LeadersTableSnapshot, None]:
        most_recent_snapshot = await leader_table_snapshot_collection.find().sort("-creationDate").limit(1).to_list()
        if most_recent_snapshot:
            return most_recent_snapshot[0]
        return None


    async def retrieve_leader_table_snapshot(id: LeadersTableSnapshot) -> LeadersTableSnapshot:
        leader_table_snapshot = await leader_table_snapshot_collection.get(str(id))
        if leader_table_snapshot:
            return leader_table_snapshot
        

    async def delete_leader_table_snapshot(id: PydanticObjectId) -> bool:
        try:
            leader_table_snapshot = await leader_table_snapshot_collection.get(str(id))
        except ValidationError as e:
            print(e.json())
        if leader_table_snapshot:
            await leader_table_snapshot.delete()
            return True
        
    
    async def delete_old_entries(cutoff_hours_ago) -> None:
        # Calculate the threshold date: current time minus threshold
        threshold_date = datetime.now() - timedelta(hours=cutoff_hours_ago)
        # Delete documents older than threshold
        await LeadersTableSnapshot.find(LeadersTableSnapshot.creationDate < threshold_date).delete()


    async def update_leader_table_snapshot_data(id: PydanticObjectId, data: dict) -> Union[bool, LeadersTableSnapshot]:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        leader_table_snapshot = await leader_table_snapshot_collection.get(str(id))
        if leader_table_snapshot:
            await leader_table_snapshot.update(update_query)
            return leader_table_snapshot
        return False

