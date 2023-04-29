from models import db, Device

class Actuator(db.Model):
    __tablename__ = 'actuators'
    id = db.Column('id', db.Integer, db.ForeignKey(Device.id), primary_key=True)
    actuator_type = db.Column(db.String(50))

    """
    activations = db.Relationship("Activation", backref="actuators", lazy=True)

    def get_actuators():
        actuators = Actuator.query.join(Device, Device.id == Actuator.id)\
            .add_columns(Actuator.id, Device.name, Device.brand, Device.actuator_type, Device.description, Device.is_active,
                Device.model, Actuator.actuator_type).all()
        return actuators

    def save_actuators(name, brand, model, actuator_type, description, is_active):
        device = Device(name = name, brand = brand, model = model,
        actuator_type = actuator_type, description = description, is_active = is_active)

        actuator = Actuator(id = device.id, actuator_type = actuator_type)

        device.actuators.append(actuator)

        db.session.add(device)
        db.session.commit()
    """