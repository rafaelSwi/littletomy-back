import models as model
from schemas.text_tab_preferences import TextTabPreferencesBase
from sqlalchemy.orm import Session
from models import TextTab

async def get_preferences_by_tab_id(db: Session, text_tab_id: int) -> TextTabPreferencesBase:
    text_tab: TextTab = db.query(model.TextTab).filter_by(id=text_tab_id).first()
    return db.query(model.TextTabPreferences).filter(model.TextTabPreferences.id == text_tab.preferences_id).all()