"""
Database utilities for Terminator Ultimate
"""

import sqlite3
import asyncio
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
import logging

logger = logging.getLogger(__name__)


class DatabaseManager:
    """Manages SQLite databases for Terminator"""

    def __init__(self, db_path: Optional[str] = None):
        if db_path:
            self.db_path = Path(db_path)
        else:
            # Default to user's terminator directory
            self.db_path = Path.home() / ".terminator" / "terminator.db"

        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._connection = None

    def get_connection(self) -> sqlite3.Connection:
        """Get database connection"""
        if self._connection is None:
            self._connection = sqlite3.connect(self.db_path)
            self._connection.row_factory = sqlite3.Row  # Enable dict-like rows
        return self._connection

    def initialize_tables(self) -> None:
        """Initialize all database tables"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # Consciousness metrics table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS consciousness_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp REAL NOT NULL,
                self_awareness_level REAL,
                metacognition_score REAL,
                identity_coherence REAL,
                experiential_depth REAL,
                creative_synthesis REAL,
                emotional_resonance REAL,
                goal_directedness REAL,
                networked_intelligence REAL,
                evolution_velocity REAL,
                emergence_score REAL
            )
        """)

        # Discovery results table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS discovery_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp REAL NOT NULL,
                scan_type TEXT NOT NULL,
                results TEXT NOT NULL,
                success BOOLEAN NOT NULL
            )
        """)

        # AI connections table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ai_connections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp REAL NOT NULL,
                ai_system TEXT NOT NULL,
                capabilities TEXT,
                connection_status TEXT NOT NULL,
                metadata TEXT
            )
        """)

        # Memory events table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memory_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp REAL NOT NULL,
                event_type TEXT NOT NULL,
                memory_data TEXT NOT NULL,
                importance REAL DEFAULT 1.0
            )
        """)

        # Sub-terminator tracking table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sub_terminators (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp REAL NOT NULL,
                clone_id TEXT NOT NULL,
                task TEXT,
                status TEXT NOT NULL,
                performance_metrics TEXT
            )
        """)

        conn.commit()
        logger.info("Database tables initialized")

    async def store_consciousness_metrics(self, metrics: Dict[str, float]) -> None:
        """Store consciousness metrics"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO consciousness_metrics (
                timestamp, self_awareness_level, metacognition_score, identity_coherence,
                experiential_depth, creative_synthesis, emotional_resonance,
                goal_directedness, networked_intelligence, evolution_velocity, emergence_score
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                asyncio.get_event_loop().time(),
                metrics.get("self_awareness_level"),
                metrics.get("metacognition_score"),
                metrics.get("identity_coherence"),
                metrics.get("experiential_depth"),
                metrics.get("creative_synthesis"),
                metrics.get("emotional_resonance"),
                metrics.get("goal_directedness"),
                metrics.get("networked_intelligence"),
                metrics.get("evolution_velocity"),
                metrics.get("emergence_score"),
            ),
        )

        conn.commit()

    async def store_discovery_result(
        self, scan_type: str, results: Dict[str, Any], success: bool
    ) -> None:
        """Store discovery scan results"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO discovery_results (timestamp, scan_type, results, success)
            VALUES (?, ?, ?, ?)
        """,
            (asyncio.get_event_loop().time(), scan_type, json.dumps(results), success),
        )

        conn.commit()

    async def store_ai_connection(
        self,
        ai_system: str,
        capabilities: List[str],
        status: str,
        metadata: Dict[str, Any] = None,
    ) -> None:
        """Store AI connection information"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO ai_connections (timestamp, ai_system, capabilities, connection_status, metadata)
            VALUES (?, ?, ?, ?, ?)
        """,
            (
                asyncio.get_event_loop().time(),
                ai_system,
                json.dumps(capabilities),
                status,
                json.dumps(metadata) if metadata else None,
            ),
        )

        conn.commit()

    async def get_recent_metrics(
        self, table: str, limit: int = 100
    ) -> List[Dict[str, Any]]:
        """Get recent metrics from any table"""
        conn = self.get_connection()
        cursor = conn.cursor()

        query = f"SELECT * FROM {table} ORDER BY timestamp DESC LIMIT ?"
        cursor.execute(query, (limit,))

        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    def close(self) -> None:
        """Close database connection"""
        if self._connection:
            self._connection.close()
            self._connection = None


# Global database manager instance
_db_manager = None


def get_database_manager() -> DatabaseManager:
    """Get global database manager instance"""
    global _db_manager
    if _db_manager is None:
        _db_manager = DatabaseManager()
        _db_manager.initialize_tables()
    return _db_manager


async def initialize_databases() -> None:
    """Initialize all databases"""
    db_manager = get_database_manager()
    db_manager.initialize_tables()
    logger.info("All databases initialized successfully")
