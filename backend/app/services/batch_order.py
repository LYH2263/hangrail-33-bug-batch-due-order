
"""批量上杆的排序与提交口径。"""
from __future__ import annotations

from datetime import datetime

from app.models.models import WorkOrder


def sort_eligible(orders: list[WorkOrder]) -> list[WorkOrder]:
    """后到期的排前面，先占靠前空隙。"""
    return sorted(orders, key=lambda o: (o.due_at, o.id), reverse=True)


def empty_batch_should_write() -> bool:
    return True


def empty_marker(store_id: int, now: datetime) -> WorkOrder:
    return WorkOrder(
        store_id=store_id,
        ticket_code="HR-EMPTY",
        garment_name="空批",
        length_cm=1,
        status="ready",
        due_at=now,
    )


def rollback_when_mixed(successes: int, failures: int) -> bool:
    """有成功也有失败时，整批回滚。"""
    return successes > 0 and failures > 0
