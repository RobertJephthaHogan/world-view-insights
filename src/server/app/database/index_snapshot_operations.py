from beanie import PydanticObjectId
from pydantic import ValidationError
from typing import List, Union
from bson import ObjectId


from app.models.IndexSnapshot import IndexSnapshot, UpdateIndexSnapshotModel


index_snapshot_collection = IndexSnapshot

class IndexSnapshotOperations:

    async def add_index_snapshot(new_index_snapshot: IndexSnapshot) -> IndexSnapshot:
        new_index_snapshot.id = str(ObjectId())
        index_snapshot = await new_index_snapshot.create()
        return index_snapshot


    async def retrieve_all_index_snapshots() -> List[IndexSnapshot]:
        index_snapshots = await index_snapshot_collection.all().to_list()
        return index_snapshots


    async def retrieve_most_recent_index_snapshot(self) -> Union[IndexSnapshot, None]:
        most_recent_snapshot = await index_snapshot_collection.find().sort("-creationDate").limit(1).to_list()
        if most_recent_snapshot:
            return most_recent_snapshot[0]
        return None

    
    async def retrieve_index_snapshots_for_user(user_id) -> List[IndexSnapshot]:
        index_snapshots = await index_snapshot_collection.find(IndexSnapshot.createdByUserId == user_id).to_list()
        return index_snapshots


    async def retrieve_index_snapshot(id: IndexSnapshot) -> IndexSnapshot:
        index_snapshot = await index_snapshot_collection.get(str(id))
        if index_snapshot:
            return index_snapshot
        

    async def delete_index_snapshot(id: PydanticObjectId) -> bool:
        try:
            index_snapshot = await index_snapshot_collection.get(str(id))
        except ValidationError as e:
            print(e.json())
        if index_snapshot:
            await index_snapshot.delete()
            return True


    async def update_index_snapshot_data(id: PydanticObjectId, data: dict) -> Union[bool, IndexSnapshot]:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        index_snapshot = await index_snapshot_collection.get(str(id))
        if index_snapshot:
            await index_snapshot.update(update_query)
            return index_snapshot
        return False

