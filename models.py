from tortoise.models import Model
from tortoise import fields


class UserBirthday(Model):
    id = fields.IntField(primary_key=True)
    uid = fields.CharField(max_length=30)
    birthday = fields.DateField()


class GiveawayEvent(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=100)
    closeoff_date = fields.DatetimeField()
    draw_date = fields.DatetimeField()
    timezone = fields.CharField()


class GiveawayParticipant(Model):
    id = fields.IntField(primary_key=True)
    uid = fields.CharField(max_length=30)
    hoyo_uid = fields.CharField(max_length=30)
    gift_received = fields.BooleanField(null=True)


class GiveawayVolunteer(Model):
    id = fields.IntField(primary_key=True)
    uid = fields.CharField(max_length=30)
    gift_sent = fields.DatetimeField(null=True)
    gift_verified = fields.BooleanField(null=True)


class GiveawayBan(Model):
    id = fields.IntField(primary_key=True)
    uid = fields.CharField(max_length=30)
    reason = fields.TextField()


class GiveawayLog(Model):
    id = fields.IntField(primary_key=True)
    uid = fields.CharField(max_length=30)
