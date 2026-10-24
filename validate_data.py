import sys
import pandas as pd
import great_expectations as gx
from great_expectations import expectations as gxe

df = pd.read_csv("data/customers.csv")

context = gx.get_context()
batch = (
    context.data_sources.add_pandas("pandas")
    .add_dataframe_asset("customers")
    .add_batch_definition_whole_dataframe("whole")
    .get_batch(batch_parameters={"dataframe": df})
)

cols = ["customer_id", "age", "tenure_months", "monthly_spend", "churn"]
checks = [gxe.ExpectTableColumnsToMatchOrderedList(column_list=cols)]
checks += [gxe.ExpectColumnValuesToNotBeNull(column=c) for c in cols]
checks += [
    gxe.ExpectColumnValuesToBeBetween(column="age", min_value=18, max_value=100),
    gxe.ExpectColumnValuesToBeBetween(column="tenure_months", min_value=0, max_value=600),
    gxe.ExpectColumnValuesToBeBetween(column="monthly_spend", min_value=0, max_value=10000),
    gxe.ExpectColumnValuesToBeInSet(column="churn", value_set=[0, 1]),
]

ok = True
for check in checks:
    result = batch.validate(check)
    ok = ok and result.success

print("Validation passed:", ok)
sys.exit(0 if ok else 1)