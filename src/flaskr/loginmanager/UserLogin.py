from flaskr.data_base.models import UserTypes

class UserLogin():
    
    def load_from_DB(self , user_id , dBase):
        self.__user = dBase.getUserById(user_id)
        return self
        
    def create(self , user):
        self.__user = user
        return self
    
    def is_authenticated(self) -> bool:
        return True
    
    def is_active(self) -> bool:
        return True
    
    def is_anonymous(self) -> bool:
        return False
    
    def get_id(self) -> str:
        return str(self.__user.id)
    
    def get_name(self) -> str:
        return self.__user.name

    def get_email(self) -> str:
        return self.__user.email
    
    def is_administrator(self) -> bool:
        if self.__user:
            return self.__user.type == UserTypes.administrator

        return False

    def get_type(self) -> UserTypes:
        return self.__user.type
    