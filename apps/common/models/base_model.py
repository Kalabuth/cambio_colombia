from django.db.models import AutoField, BooleanField, DateTimeField, Model


class BaseModel(Model):
    id = AutoField(primary_key=True)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    SAVE_DELETED_DATA_TO_FILE = False

    class Meta:
        abstract = True

    def disable(self):
        self.is_active = False
        self.save()
