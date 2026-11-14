"""Domain exceptions for YT-RAG."""


class YTRAGBaseException(Exception):
    """Base exception for all YT-RAG errors."""

    def __init__(self, message: str, details: dict | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}


class InvalidYouTubeURLException(YTRAGBaseException):
    """Raised when a provided URL cannot be parsed into a valid YouTube video ID."""


class VideoNotFoundException(YTRAGBaseException):
    """Raised when a video is private, deleted, or does not exist."""


class TranscriptUnavailableException(YTRAGBaseException):
    """Raised when closed captions or transcripts cannot be retrieved from YouTube."""


class AudioDownloadError(YTRAGBaseException):
    """Raised when audio stream downloading via yt-dlp fails."""


class TranscriptionError(YTRAGBaseException):
    """Raised when speech-to-text processing fails."""


class VectorStoreError(YTRAGBaseException):
    """Raised when vector database indexing or query operations fail."""


class VideoNotIndexedError(YTRAGBaseException):
    """Raised when querying a video that has not yet been ingested/indexed."""


class LLMConfigurationError(YTRAGBaseException):
    """Raised when required API keys or LLM provider configs are missing or invalid."""


class LLMInferenceError(YTRAGBaseException):
    """Raised when an inference request to the LLM fails or is rate-limited."""


class RAGQueryError(YTRAGBaseException):
    """Raised when retrieval-augmented question answering fails."""

