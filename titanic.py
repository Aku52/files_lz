import pyarrow.parquet as pq

table = pq.read_table("titanic.parquet")
df = table.to_pandas()
df