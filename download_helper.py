from io import BytesIO
import pyarrow.parquet as pq

def download_processed_data(df, file_format):
    if file_format == "CSV":
        buffer = BytesIO()
        df.to_pandas().to_csv(buffer, index=False)
        buffer.seek(0)
        return buffer, "CSV"
    elif file_format == "Parquet":
        buffer = BytesIO()
        pq.write_table(df.to_arrow(), buffer)
        buffer.seek(0)
        return buffer, "Parquet"
