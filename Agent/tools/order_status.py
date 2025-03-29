from agency_swarm.tools import BaseTool
from pydantic import Field

class OrderStatusCheck(BaseTool):
    """Check status of customer orders"""

    order_id: str = Field(..., description="Customer's order ID to look up")

    def run(self):
        # Replace with actual API call to order system
        # For MVP, using a simple mock response
        statuses = {
            "ORD123": "Processing (Est. shipping: 2 days)",
            "ORD124": "Shipped (Est. delivery: July 15)",
            "ORD125": "Delivered on July 1",
            "ORD126": "Back-ordered (Est. shipping: July 20)"
        }

        if self.order_id in statuses:
            return f"Order {self.order_id} status: {statuses[self.order_id]}"
        else:
            return f"Order {self.order_id} not found. Please verify the order number."