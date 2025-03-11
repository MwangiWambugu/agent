from agency_swarm.tools import BaseTool
from pydantic import Field

class OrderStatusCheck(BaseTool):
    """Check status of customer orders"""
    
    order_id: str = Field(..., description="Customer's order ID to look up")

    def run(self):
        # Replace with actual API call to order system
        return f"Order {self.order_id} status: Shipped (Estimated delivery: July 15)"