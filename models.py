from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Table
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Association Table: Many-to-Many (User <-> Permission)
user_permission_table = Table(
    "user_permission",
    Base.metadata,
    Column("user_id", ForeignKey("user_account.id", ondelete="CASCADE"), primary_key=True),
    Column("permission_id", ForeignKey("server_permission.id", ondelete="CASCADE"), primary_key=True)
)

# Models
class TextTabLogType(Base):
    __tablename__ = "text_tab_log_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String(16), nullable=False, unique=True)


class TextTabLog(Base):
    __tablename__ = "text_tab_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user_account.id", ondelete="SET NULL"))
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    type_id = Column(Integer, ForeignKey("text_tab_log_type.id", ondelete="SET NULL"))
    ip_address = Column(String(45))

    user = relationship("User", back_populates="text_tab_logs")
    type = relationship("TextTabLogType", backref="logs")


class TextTabPreferences(Base):
    __tablename__ = "text_tab_preferences"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    password_hash = Column(String(60), nullable=True)
    public = Column(Boolean, default=True, nullable=False)

    text_tabs = relationship("TextTab", back_populates="preferences")


class TextTab(Base):
    __tablename__ = "text_tab"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=True)
    title = Column(String(32), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("user_account.id", ondelete="SET NULL"))
    preferences_id = Column(Integer, ForeignKey("text_tab_preferences.id", ondelete="SET NULL"))

    preferences = relationship("TextTabPreferences", back_populates="text_tabs")
    user = relationship("User", back_populates="text_tabs")
    logs = relationship("TextTabLog", secondary="text_tab_log_link", backref="text_tabs")


# Association Table: TextTab <-> TextTabLog (Many-to-Many)
text_tab_log_link = Table(
    "text_tab_log_link",
    Base.metadata,
    Column("text_tab_id", ForeignKey("text_tab.id", ondelete="CASCADE"), primary_key=True),
    Column("log_id", ForeignKey("text_tab_log.id", ondelete="CASCADE"), primary_key=True)
)


class ServerPermission(Base):
    __tablename__ = "server_permission"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False, unique=True)

    users = relationship(
        "User",
        secondary=user_permission_table,
        back_populates="permissions"
    )


class User(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), nullable=False, unique=True, index=True)
    password_hash = Column(String(60), nullable=False)
    email_address = Column(String(255), nullable=True, unique=True)

    permissions = relationship(
        "ServerPermission",
        secondary=user_permission_table,
        back_populates="users"
    )

    text_tabs = relationship("TextTab", back_populates="user")
    text_tab_logs = relationship("TextTabLog", back_populates="user")