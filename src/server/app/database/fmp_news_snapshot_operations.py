from beanie import PydanticObjectId
from pydantic import ValidationError
from typing import List, Union
from bson import ObjectId


from app.models.FmpNewsSnapshot import FmpNewsSnapshot, UpdateFmpNewsSnapshotModel


fmp_news_snapshot_collection = FmpNewsSnapshot

class FmpNewsSnapshotOperations:

    async def add_fmp_news_snapshot(new_fmp_news_snapshot: FmpNewsSnapshot) -> FmpNewsSnapshot:
        new_fmp_news_snapshot.id = str(ObjectId())
        fmp_news_snapshot = await new_fmp_news_snapshot.create()
        return fmp_news_snapshot


    async def retrieve_all_fmp_news_snapshots() -> List[FmpNewsSnapshot]:
        fmp_news_snapshots = await fmp_news_snapshot_collection.all().to_list()
        return fmp_news_snapshots


    async def retrieve_most_recent_fmp_news_snapshot(self) -> Union[FmpNewsSnapshot, None]:
        most_recent_snapshot = await fmp_news_snapshot_collection.find().sort("-creationDate").limit(1).to_list()
        if most_recent_snapshot:
            return most_recent_snapshot[0]
        return None


    async def retrieve_fmp_news_snapshot(id: FmpNewsSnapshot) -> FmpNewsSnapshot:
        fmp_news_snapshot = await fmp_news_snapshot_collection.get(str(id))
        if fmp_news_snapshot:
            return fmp_news_snapshot
        

    async def delete_fmp_news_snapshot(id: PydanticObjectId) -> bool:
        try:
            fmp_news_snapshot = await fmp_news_snapshot_collection.get(str(id))
        except ValidationError as e:
            print(e.json())
        if fmp_news_snapshot:
            await fmp_news_snapshot.delete()
            return True


    async def update_fmp_news_snapshot_data(id: PydanticObjectId, data: dict) -> Union[bool, FmpNewsSnapshot]:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        fmp_news_snapshot = await fmp_news_snapshot_collection.get(str(id))
        if fmp_news_snapshot:
            await fmp_news_snapshot.update(update_query)
            return fmp_news_snapshot
        return False

