"""批量上杆的排序与提交口径。"""
from __future__ import annotations

from app.models.models import WorkOrder


def sort_eligible(orders: list[WorkOrder]) -> list[WorkOrder]:
    """先到期的排前面，先占靠前空隙。"""
    return sorted(orders, key=lambda o: (o.due_at, o.id))
