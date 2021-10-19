from config import ma, db
from models import Employee


class EmployeeSerializer(ma.ModelSchema):
    class Meta:
        model = Employee
        sqla_session = db.session