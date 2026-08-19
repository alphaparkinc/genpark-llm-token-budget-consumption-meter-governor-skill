from client import LlmTokenBudgetConsumptionMeterGovernorClient

def main():
    client = LlmTokenBudgetConsumptionMeterGovernorClient()
    res = client.check_and_govern_budget("tenant_enterprise_44", 1000.0)
    print(f"Budget Consumed: {res['budget_consumed_pct']}%")
    print(f"Is Throttled: {res['is_throttled']}")
    print(f"Projected Spend: ${res['projected_monthly_spend_usd']}")

if __name__ == "__main__":
    main()
