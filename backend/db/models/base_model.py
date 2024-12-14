from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
import uuid
from datetime import datetime

Base = declarative_base()


class BaseModel:
    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True
    )

    @declared_attr
    def created_at(cls) -> Mapped[DateTime]:
        return mapped_column(
            DateTime,
            default=datetime.now()
        )

    @declared_attr
    def updated_at(cls) -> Mapped[DateTime]:
        return mapped_column(
            DateTime,
            default=datetime.now(),
            onupdate=datetime.now()
        )
