from schemas.text_tab import TextTabBase
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_text_tab_by_id(db: Session, text_tab_id: int, password: str = None) -> TextTab | None:
    text_tab = db.query(TextTab).filter(TextTab.id == text_tab_id).first()

    if not text_tab:
        return None

    if text_tab.preferences and not text_tab.preferences.public:
        if not password:
            return None
        
        if text_tab.preferences.password_hash and verify_password(password, text_tab.preferences.password_hash):
            return text_tab
        else:
            return None
    
    return text_tab

def create_text_tab(db: Session, text_tab_data: TextTabCreate, user: User) -> TextTab:

    new_preferences = TextTabPreferences(
        created=datetime.utcnow(),
        public=True,
    )
    
    db.add(new_preferences)
    db.commit()
    db.refresh(new_preferences)
    
    new_text_tab = TextTab(
        title=text_tab_data.title,
        content=None,
        user_id=user.id,
        preferences_id=new_preferences.id,
    )
    
    db.add(new_text_tab)
    db.commit()
    db.refresh(new_text_tab)
    
    return new_text_tab
