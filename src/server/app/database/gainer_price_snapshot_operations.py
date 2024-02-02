from beanie import PydanticObjectId
from pydantic import ValidationError
from typing import List, Union
from bson import ObjectId


from app.models.GainerPriceSnapshot import GainerPriceSnapshot, UpdateGainerPriceSnapshotModel


gainer_price_snapshot_collection = GainerPriceSnapshot

class GainerPriceSnapshotOperations:

    async def add_gainer_price_snapshot(new_gainer_price_snapshot: GainerPriceSnapshot) -> GainerPriceSnapshot:
        new_gainer_price_snapshot.id = str(ObjectId())
        gainer_price_snapshot = await new_gainer_price_snapshot.create()
        return gainer_price_snapshot


    async def retrieve_all_gainer_price_snapshots() -> List[GainerPriceSnapshot]:
        gainer_price_snapshots = await gainer_price_snapshot_collection.all().to_list()
        return gainer_price_snapshots


    async def retrieve_most_recent_gainer_price_snapshot(self) -> Union[GainerPriceSnapshot, None]:
        most_recent_snapshot = await gainer_price_snapshot_collection.find().sort("-creationDate").limit(1).to_list()
        if most_recent_snapshot:
            return most_recent_snapshot[0]
        return None


    async def retrieve_gainer_price_snapshot(id: GainerPriceSnapshot) -> GainerPriceSnapshot:
        gainer_price_snapshot = await gainer_price_snapshot_collection.get(str(id))
        if gainer_price_snapshot:
            return gainer_price_snapshot
        

    async def delete_gainer_price_snapshot(id: PydanticObjectId) -> bool:
        try:
            gainer_price_snapshot = await gainer_price_snapshot_collection.get(str(id))
        except ValidationError as e:
            print(e.json())
        if gainer_price_snapshot:
            await gainer_price_snapshot.delete()
            return True


    async def update_gainer_price_snapshot_data(id: PydanticObjectId, data: dict) -> Union[bool, GainerPriceSnapshot]:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        gainer_price_snapshot = await gainer_price_snapshot_collection.get(str(id))
        if gainer_price_snapshot:
            await gainer_price_snapshot.update(update_query)
            return gainer_price_snapshot
        return False

