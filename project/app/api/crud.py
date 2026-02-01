from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from typing import Union
from typing import List


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="dummy summary")

    await summary.save()
    return summary.id


async def get(id: int) -> Union[TextSummary, None]:
    return await TextSummary.filter(id=id).first()


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries
