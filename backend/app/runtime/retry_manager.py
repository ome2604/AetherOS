class RetryManager:

    MAX_RETRIES = 3

    @staticmethod
    def should_retry(
        retry_count: int,
    ):

        return (
            retry_count
            < RetryManager.MAX_RETRIES
        )

    @staticmethod
    def increment_retry(
        retry_count: int,
    ):

        return retry_count + 1