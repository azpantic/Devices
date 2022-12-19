from .db import db
from .models import Device, User, Operation
from datetime import datetime


class FDataBase():

    def getUserById(self, user_id: str) -> User:

        user = db.session.query(User).get(user_id)

        return user

    def getUserByEmail(self, email: str) -> User:

        users = db.session.query(User).where(User.email == email)

        if users.count() == 0:
            return None

        return list(users)[0]

    def addUser(self, newUser: User) -> None:

        db.session.add(newUser)
        db.session.commit()

    def registerNewOperation(self, newOperation: Operation) -> None:

        db.session.add(newOperation)
        db.session.commit()

    def getAllDevices(self) -> list[Device]:
        return list(db.session.query(Device).all())

    def addDevice(self, newDevice: Device) -> None:
        db.session.add(newDevice)
        db.session.commit()

    def getDeviceById(self, id: int) -> Device:
        return db.session.query(Device).get(id)

    def getDeviceByUID(self, uid: int) -> Device:
        devices = db.session.query(Device).where(Device.uid == uid)

        if devices.count() == 0:
            return None

        return list(devices)[0]

    def addNewOperation(self, newOperation: Operation) -> None:
        db.session.add(newOperation)
        db.session.commit()

    def getOperationById(self, operationId: int) -> Operation:
        return db.session.query(Operation).get(operationId)

    def deleteOperationById(self, operationId: int) -> None:
        db.session.query(Operation).filter(
            Operation.id == operationId).delete()
        db.session.commit()

    def getUserOperations(self, userId) -> list[Operation]:

        return list(db.session.query(Operation).where(Operation.userId == userId))

    def getItemOperationsHistory(self, deviceId: int) -> list[Operation]:

        return list(db.session.query(Operation).where(Operation.deviceId == deviceId))

    def getDeviceOperationOnDate(self,  deviceId: int, date: datetime):
        return list(db.session.query(Operation).where(Operation.deviceId == deviceId).where(datetime.strptime(Operation.startTime).date() == date.date()))


dBase: FDataBase = FDataBase()
