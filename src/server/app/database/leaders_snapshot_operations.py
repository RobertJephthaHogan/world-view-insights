from beanie import PydanticObjectId
from pydantic import ValidationError
from typing import List, Union
from bson import ObjectId


from app.models.LeadersSnapshot import LeadersSnapshot, UpdateLeadersSnapshotModel


leaders_snapshot_collection = LeadersSnapshot

class LeadersSnapshotOperations:

    async def add_leaders_snapshot(new_leaders_snapshot: LeadersSnapshot) -> LeadersSnapshot:
        new_leaders_snapshot.id = str(ObjectId())
        leaders_snapshot = await new_leaders_snapshot.create()
        return leaders_snapshot


    async def retrieve_all_leaders_snapshots() -> List[LeadersSnapshot]:
        leaders_snapshots = await leaders_snapshot_collection.all().to_list()
        return leaders_snapshots
    
    
    async def retrieve_most_recent_leaders_snapshot(self) -> Union[LeadersSnapshot, None]:
        most_recent_snapshot = await leaders_snapshot_collection.find().sort("-creationDate").limit(1).to_list()
        if most_recent_snapshot:
            return most_recent_snapshot[0]
        return None

    
    async def retrieve_leaders_snapshots_for_user(user_id) -> List[LeadersSnapshot]:
        leaders_snapshots = await leaders_snapshot_collection.find(LeadersSnapshot.createdByUserId == user_id).to_list()
        return leaders_snapshots


    async def retrieve_leaders_snapshot(id: LeadersSnapshot) -> LeadersSnapshot:
        leaders_snapshot = await leaders_snapshot_collection.get(str(id))
        if leaders_snapshot:
            return leaders_snapshot
        

    async def delete_leaders_snapshot(id: PydanticObjectId) -> bool:
        try:
            leaders_snapshot = await leaders_snapshot_collection.get(str(id))
        except ValidationError as e:
            print(e.json())
        if leaders_snapshot:
            await leaders_snapshot.delete()
            return True


    async def update_leaders_snapshot_data(id: PydanticObjectId, data: dict) -> Union[bool, LeadersSnapshot]:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        leaders_snapshot = await leaders_snapshot_collection.get(str(id))
        if leaders_snapshot:
            await leaders_snapshot.update(update_query)
            return leaders_snapshot
        return False

