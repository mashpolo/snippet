# coding: utf-8
from sqlalchemy import Column, DateTime, Index, JSON, String, Text, Time, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, SMALLINT, TINYINT
from app import db


class RegistryCenter(db.Model):
    __tablename__ = 'registry_center'
    __table_args__ = (
        Index('idx_project_app', 'project_code', 'module_code'),
    )

    id = Column(BIGINT(20), primary_key=True)
    project_code = Column(String(100, 'utf8mb4_general_ci'), nullable=False)
    module_code = Column(String(100, 'utf8mb4_general_ci'), nullable=False)
    instance_code = Column(String(100, 'utf8mb4_general_ci'), nullable=False)
    ip = Column(String(30, 'utf8mb4_general_ci'), nullable=False, index=True)
    host_name = Column(String(50, 'utf8mb4_general_ci'))
    http_port = Column(INTEGER(11))
    tcp_port = Column(INTEGER(11))
    monitor_port = Column(INTEGER(11))
    registry_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    heartbeat_time = Column(DateTime)
    startup_time = Column(DateTime)
    status = Column(INTEGER(11), nullable=False)
    env_science = Column(String(50, 'utf8mb4_general_ci'), nullable=False)
    token = Column(String(40, 'utf8mb4_general_ci'))
