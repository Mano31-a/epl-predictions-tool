"""
Application configuration using Pydantic Settings.

This module handles all environment-based configuration for the EPL Predictions Tool,
including database connections, CORS settings, API configuration, and other runtime settings.
"""

from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    
    Attributes:
        # Database Settings
        database_url: Database connection URL
        database_echo: Enable SQL query logging
        
        # CORS Settings
        cors_origins: List of allowed CORS origins
        cors_allow_credentials: Allow credentials in CORS requests
        cors_allow_methods: Allowed HTTP methods for CORS
        cors_allow_headers: Allowed headers for CORS requests
        
        # API Configuration
        api_title: Application title
        api_version: API version
        api_description: API description
        api_debug: Debug mode flag
        
        # Server Settings
        server_host: Server hostname/IP
        server_port: Server port number
        
        # Application Settings
        environment: Application environment (development, staging, production)
        log_level: Logging level
    """
    
    # Database Configuration
    database_url: str = "sqlite:///./test.db"
    database_echo: bool = False
    
    # CORS Configuration
    cors_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://localhost:8080",
    ]
    cors_allow_credentials: bool = True
    cors_allow_methods: List[str] = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"]
    cors_allow_headers: List[str] = ["*"]
    
    # API Configuration
    api_title: str = "EPL Predictions Tool API"
    api_version: str = "1.0.0"
    api_description: str = "API for predicting English Premier League match outcomes"
    api_debug: bool = False
    
    # Server Configuration
    server_host: str = "0.0.0.0"
    server_port: int = 8000
    
    # Application Settings
    environment: str = "development"
    log_level: str = "INFO"
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
    
    @property
    def database_url_connection(self) -> str:
        """
        Get the database URL for connection.
        
        Returns:
            str: The database connection URL
        """
        return self.database_url
    
    @property
    def is_debug(self) -> bool:
        """
        Check if debug mode is enabled.
        
        Returns:
            bool: True if in debug mode
        """
        return self.api_debug or self.environment == "development"
    
    def get_cors_middleware_config(self) -> dict:
        """
        Get CORS middleware configuration dictionary.
        
        Returns:
            dict: Configuration dictionary for CORS middleware
        """
        return {
            "allow_origins": self.cors_origins,
            "allow_credentials": self.cors_allow_credentials,
            "allow_methods": self.cors_allow_methods,
            "allow_headers": self.cors_allow_headers,
        }


# Create a singleton instance of settings
settings = Settings()
