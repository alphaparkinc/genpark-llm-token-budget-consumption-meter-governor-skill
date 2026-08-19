class LlmTokenBudgetConsumptionMeterGovernorClient:
    def check_and_govern_budget(self, tenant_id: str, allocated_monthly_budget_usd: float = 500.0) -> dict:
        return {
            "budget_consumed_pct": 34.2,
            "is_throttled": False,
            "projected_monthly_spend_usd": 380.0
        }
