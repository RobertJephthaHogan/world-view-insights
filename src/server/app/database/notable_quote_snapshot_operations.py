from beanie import PydanticObjectId
from pydantic import ValidationError
from typing import List, Union
from bson import ObjectId
from datetime import datetime, timedelta


from app.models.NotableQuotesSnapshot import NotableQuotesSnapshot, UpdateNotableQuotesSnapshotModel


notable_quotes_snapshot_collection = NotableQuotesSnapshot

class NotableQuotesSnapshotOperations:

    async def add_notable_quotes_snapshot(new_notable_quotes_snapshot: NotableQuotesSnapshot) -> NotableQuotesSnapshot:
        new_notable_quotes_snapshot.id = str(ObjectId())
        notable_quotes_snapshot = await new_notable_quotes_snapshot.create()
        return notable_quotes_snapshot


    async def retrieve_all_notable_quotes_snapshots() -> List[NotableQuotesSnapshot]:
        notable_quotes_snapshots = await notable_quotes_snapshot_collection.all().to_list()
        return notable_quotes_snapshots


    async def retrieve_most_recent_nc_snapshot(self) -> Union[NotableQuotesSnapshot, None]:
        most_recent_snapshot = await notable_quotes_snapshot_collection.find().sort("-creationDate").limit(1).to_list()
        if most_recent_snapshot:
            return most_recent_snapshot[0]
        return None

    
    async def retrieve_notable_quotes_snapshots_for_user(user_id) -> List[NotableQuotesSnapshot]:
        notable_quotes_snapshots = await notable_quotes_snapshot_collection.find(NotableQuotesSnapshot.createdByUserId == user_id).to_list()
        return notable_quotes_snapshots


    async def retrieve_notable_quotes_snapshot(id: NotableQuotesSnapshot) -> NotableQuotesSnapshot:
        notable_quotes_snapshot = await notable_quotes_snapshot_collection.get(str(id))
        if notable_quotes_snapshot:
            return notable_quotes_snapshot
        

    async def delete_notable_quotes_snapshot(id: PydanticObjectId) -> bool:
        try:
            notable_quotes_snapshot = await notable_quotes_snapshot_collection.get(str(id))
        except ValidationError as e:
            print(e.json())
        if notable_quotes_snapshot:
            await notable_quotes_snapshot.delete()
            return True
        
    
    async def delete_old_entries(cutoff_hours_ago) -> None:
        # Calculate the threshold date: current time minus threshold
        threshold_date = datetime.now() - timedelta(hours=cutoff_hours_ago)
        # Delete documents older than threshold
        await NotableQuotesSnapshot.find(NotableQuotesSnapshot.creationDate < threshold_date).delete()


    async def update_notable_quotes_snapshot_data(id: PydanticObjectId, data: dict) -> Union[bool, NotableQuotesSnapshot]:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        notable_quotes_snapshot = await notable_quotes_snapshot_collection.get(str(id))
        if notable_quotes_snapshot:
            await notable_quotes_snapshot.update(update_query)
            return notable_quotes_snapshot
        return False

