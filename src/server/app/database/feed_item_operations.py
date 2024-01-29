from beanie import PydanticObjectId
from pydantic import ValidationError
from typing import List, Union
from bson import ObjectId


from app.models.FeedItem import FeedItem, UpdateFeedItemModel


feed_item_collection = FeedItem

class FeedItemOperations:

    async def add_feed_item(new_feed_item: FeedItem) -> FeedItem:
        new_feed_item.id = str(ObjectId())
        feed_item = await new_feed_item.create()
        return feed_item


    async def retrieve_all_feed_items() -> List[FeedItem]:
        feed_items = await feed_item_collection.all().to_list()
        return feed_items

    
    async def retrieve_feed_items_for_user(user_id) -> List[FeedItem]:
        feed_items = await feed_item_collection.find(FeedItem.createdByUserId == user_id).to_list()
        return feed_items


    async def retrieve_feed_item(id: FeedItem) -> FeedItem:
        feed_item = await feed_item_collection.get(str(id))
        if feed_item:
            return feed_item
        
    async def retrieve_feed_item_by_system_id(system_id: str) -> FeedItem:
        feed_item = await feed_item_collection.find({'systemId': system_id}).to_list()
        if feed_item:
            return feed_item

    async def delete_feed_item(id: PydanticObjectId) -> bool:
        try:
            feed_item = await feed_item_collection.get(str(id))
        except ValidationError as e:
            print(e.json())
        if feed_item:
            await feed_item.delete()
            return True


    async def update_feed_item_data(id: PydanticObjectId, data: dict) -> Union[bool, FeedItem]:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        feed_item = await feed_item_collection.get(str(id))
        if feed_item:
            await feed_item.update(update_query)
            return feed_item
        return False

