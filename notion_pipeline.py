import dlt

from notion import notion_databases


def load_databases() -> None:
    """Loads all databases from a Notion workspace which have been shared with
    an integration.
    """
    pipeline = dlt.pipeline(
        pipeline_name="notion",
        destination='notion-to-bigquery@devus-ds-adventures-1.iam.gserviceaccount.com',
        dataset_name="Notion_to_bigquery",
    )

    data = notion_databases()

    info = pipeline.run(data)
    print(info)


if __name__ == "__main__":
    load_databases()
