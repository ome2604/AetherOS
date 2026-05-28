from app.models.audit_log import (
    AuditLog,
)


class AuditService:

    @staticmethod
    def log_action(

        db,

        entity_type,

        entity_id,

        action,

        actor_id,

        metadata=None,
    ):

        log = AuditLog(

            entity_type=entity_type,

            entity_id=str(entity_id),

            action=action,

            actor_id=actor_id,

            event_metadata=metadata,
        )

        db.add(log)

        db.commit()

        return log