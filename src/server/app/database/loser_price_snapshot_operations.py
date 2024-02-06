from beanie import PydanticObjectId
from pydantic import ValidationError
from typing import List, Union
from bson import ObjectId
from datetime import datetime, timedelta


from app.models.LoserPriceSnapshot import LoserPriceSnapshot, UpdateLoserPriceSnapshotModel


loser_price_snapshot_collection = LoserPriceSnapshot

class LoserPriceSnapshotOperations:

    async def add_loser_price_snapshot(new_loser_price_snapshot: LoserPriceSnapshot) -> LoserPriceSnapshot:
        new_loser_price_snapshot.id = str(ObjectId())
        loser_price_snapshot = await new_loser_price_snapshot.create()
        return loser_price_snapshot


    async def retrieve_all_loser_price_snapshots() -> List[LoserPriceSnapshot]:
        loser_price_snapshots = await loser_price_snapshot_collection.all().to_list()
        return loser_price_snapshots


    async def retrieve_most_recent_loser_price_snapshot(self) -> Union[LoserPriceSnapshot, None]:
        most_recent_snapshot = await loser_price_snapshot_collection.find().sort("-creationDate").limit(1).to_list()
        if most_recent_snapshot:
            return most_recent_snapshot[0]
        return None


    async def retrieve_loser_price_snapshot(id: LoserPriceSnapshot) -> LoserPriceSnapshot:
        loser_price_snapshot = await loser_price_snapshot_collection.get(str(id))
        if loser_price_snapshot:
            return loser_price_snapshot
        

    async def delete_loser_price_snapshot(id: PydanticObjectId) -> bool:
        try:
            loser_price_snapshot = await loser_price_snapshot_collection.get(str(id))
        except ValidationError as e:
            print(e.json())
        if loser_price_snapshot:
            await loser_price_snapshot.delete()
            return True


    async def delete_old_entries(cutoff_hours_ago) -> None:
        # Calculate the threshold date: current time minus threshold
        threshold_date = datetime.now() - timedelta(hours=cutoff_hours_ago)
        # Delete documents older than threshold
        await LoserPriceSnapshot.find(LoserPriceSnapshot.creationDate < threshold_date).delete()


    async def update_loser_price_snapshot_data(id: PydanticObjectId, data: dict) -> Union[bool, LoserPriceSnapshot]:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        loser_price_snapshot = await loser_price_snapshot_collection.get(str(id))
        if loser_price_snapshot:
            await loser_price_snapshot.update(update_query)
            return loser_price_snapshot
        return False

