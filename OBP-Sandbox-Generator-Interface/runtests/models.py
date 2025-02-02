# -*- coding: utf-8 -*-
"""
Models of runtests app
"""

from django.db import models
from django.conf import settings


class TestConfiguration(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Name',
        unique=True,
        help_text='Name of the configuration',
        blank=False,
        null=False,
    )
    api_version = models.CharField(
        max_length=255,
        verbose_name='API Version',
        help_text='Version of the API to test, e.g. 3.0.0',
        blank=False,
        null=False,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Owner',
        help_text='User who owns this configuration',
        blank=False,
        null=False,
        on_delete=models.DO_NOTHING
    )
    username = models.CharField(
        max_length=255,
        verbose_name='Username',
        help_text='Username',
        blank=True,
        null=True,
    )
    bank_id = models.CharField(
        max_length=255,
        verbose_name='Bank Id',
        help_text='Bank identifier',
        blank=True,
        null=True,
    )
    branch_id = models.CharField(
        max_length=255,
        verbose_name='Branch Id',
        help_text='Bank branch identifier',
        blank=True,
        null=True,
    )
    atm_id = models.CharField(
        max_length=255,
        verbose_name='ATM Id',
        help_text='ATM identifier',
        blank=True,
        null=True,
    )
    account_id = models.CharField(
        max_length=255,
        verbose_name='Account Id',
        help_text='Account identifier',
        blank=True,
        null=True,
    )
    other_account_id = models.CharField(
        max_length=255,
        verbose_name='Other Account Id',
        help_text='Account identifier of another account',
        blank=True,
        null=True,
    )
    view_id = models.CharField(
        max_length=255,
        verbose_name='View Id',
        help_text='View identifier',
        blank=True,
        null=True,
    )
    user_id = models.CharField(
        max_length=255,
        verbose_name='User Id',
        help_text='User identifier',
        blank=True,
        null=True,
    )
    provider_id = models.CharField(
        max_length=255,
        verbose_name='Provider Id',
        help_text='Provider identifier',
        blank=True,
        null=True,
    )
    customer_id = models.CharField(
        max_length=255,
        verbose_name='Customer Id',
        help_text='Customer identifier',
        blank=True,
        null=True,
    )
    transaction_id = models.CharField(
        max_length=255,
        verbose_name='Transaction Id',
        help_text='Transaction identifier',
        blank=True,
        null=True,
    )
    counterparty_id = models.CharField(
        max_length=255,
        verbose_name='Counterparty Id',
        help_text='Counterparty identifier',
        blank=True,
        null=True,
    )
    from_currency_code = models.CharField(
        max_length=255,
        verbose_name='From Currency Code',
        help_text='Currency code to convert from',
        blank=True,
        null=True,
    )
    to_currency_code = models.CharField(
        max_length=255,
        verbose_name='To Currency Code',
        help_text='Currency code to convert to',
        blank=True,
        null=True,
    )
    product_code = models.CharField(
        max_length=255,
        verbose_name='Product Code',
        help_text='Product code of a bank\'s product',
        blank=True,
        null=True,
    )
    meeting_id = models.CharField(
        max_length=255,
        verbose_name='Meeting Id',
        help_text='Meeting identifier of a bank\s meeting',
        blank=True,
        null=True,
    )
    consumer_id = models.CharField(
        max_length=255,
        verbose_name='Consumer Id',
        help_text='Consumer identifier of a registered app',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Test Configuration'
        verbose_name_plural = 'Test Configurations'

    def __str__(self):
        return self.name


class ProfileOperation(models.Model):
    profile_id = models.IntegerField(
        verbose_name="Profile id",
        help_text="Test Profile id"
    )
    operation_id = models.CharField(
        max_length=255,
        verbose_name="Operation id ",
        help_text="Test endpoint opreation id",
        blank=True,
        null=True
    )
    json_body = models.TextField(
        max_length=65535,
        verbose_name="Json body",
        help_text="The json body to the  test request",

    )
    order = models.IntegerField(
        verbose_name="Order",
        help_text="Test order",
        default=100
    )
    urlpath = models.CharField(
        max_length=255,
        verbose_name="The url",
        help_text="The url",
        blank=True,
        null=True,
    )

    replica_id = models.IntegerField(
        verbose_name="Replica id",
        help_text="Test Replica id",
        default= 1
    )

    remark = models.CharField(
        max_length=255,
        verbose_name="remark",
        help_text="remark",
        blank=True,
        null=True,
    )

    is_deleted = models.IntegerField(
        verbose_name="Deleted",
        help_text="Deleted",
        default=0,
        null=False
    )

    class Meta:
        verbose_name = 'Test Profile Operation'
        verbose_name_plural = 'Test Profile Operation'

    def __str__(self):
        return "profile_id:\t{}\noperationid:\t{}\n".format(self.profile_id,self.operation_id)

class User(models.Model):
    gender = models.CharField(
        max_length=25,
        verbose_name="Gender",
        help_text="Gender",
        default= 1
    )
    relationship_status = models.CharField(
        max_length=25,
        verbose_name="relationship_status",
        help_text="relationship_status",
        blank=True,
        null=True
    )

    employment_status = models.CharField(
        max_length=25,
        verbose_name="employment_status",
        help_text="employment_status",
        blank=True,
        null=True
    )

    highest_education_attained = models.CharField(
        max_length=25,
        verbose_name="highest_education_attained",
        help_text="highest_education_attained",
        blank=True,
        null=True
    )

    savings= models.CharField(
        max_length=25,
        verbose_name="savings",
        help_text="savings"
    )

    currents= models.CharField(
        max_length=25,
        verbose_name="currents",
        help_text="currents"
    )

    country=models.CharField(
        max_length=25,
        verbose_name="country",
        help_text="country"
    )

    behavior = models.TextField(
        max_length=65535,
        verbose_name="behavior",
        help_text="behavior",

    )

    replica_id = models.IntegerField(
        verbose_name="Replica id",
        help_text="Test Replica id",
        default= 1
    )

    remark = models.CharField(
        max_length=255,
        verbose_name="remark",
        help_text="remark",
        blank=True,
        null=True,
    )

    is_deleted = models.IntegerField(
        verbose_name="Deleted",
        help_text="Deleted",
        default=0,
        null=False
    )

    class Meta:
        verbose_name = 'Test Profile Operation'
        verbose_name_plural = 'Test Profile Operation'

    def __str__(self):
        return "profile_id:\t{}\noperationid:\t{}\n".format(self.profile_id,self.operation_id)

class Bank(models.Model):
    Bank_ID = models.CharField(
        max_length=25,
        verbose_name="Bank_ID",
        help_text="Bank_ID",
        default= 1
    )

    short_name = models.CharField(
        max_length=25,
        verbose_name="short_name",
        help_text="short_name",
        blank=True,
        null=True
    )

    full_name = models.CharField(
        max_length=25,
        verbose_name="full_name",
        help_text="full_name",
        blank=True,
        null=True
    )

    website = models.CharField(
        max_length=25,
        verbose_name="website",
        help_text="website",
        blank=True,
        null=True
    )

    logo= models.CharField(
        max_length=25,
        verbose_name="logo",
        help_text="logo"
    )

    currency= models.CharField(
        max_length=25,
        verbose_name="currency",
        help_text="currency"
    )

    replica_id = models.IntegerField(
        verbose_name="Replica id",
        help_text="Test Replica id",
        default= 1
    )

    remark = models.CharField(
        max_length=255,
        verbose_name="remark",
        help_text="remark",
        blank=True,
        null=True,
    )

    is_deleted = models.IntegerField(
        verbose_name="Deleted",
        help_text="Deleted",
        default=0,
        null=False
    )

    class Meta:
        verbose_name = 'Test Profile Operation'
        verbose_name_plural = 'Test Profile Operation'

    def __str__(self):
        return "profile_id:\t{}\noperationid:\t{}\n".format(self.profile_id,self.operation_id)

class Branch(models.Model):
    Name = models.CharField(
        max_length=25,
        verbose_name="Bank_ID",
        help_text="Bank_ID",
        default= 1
    )

    Address_1 = models.CharField(
        max_length=25,
        verbose_name="Address_1",
        help_text="Address_1",
        blank=True,
        null=True
    )

    Address_2 = models.CharField(
        max_length=25,
        verbose_name="Address_2",
        help_text="Address_2",
        blank=True,
        null=True
    )

    Address_3 = models.CharField(
        max_length=25,
        verbose_name="Address_3",
        help_text="Address_3",
        blank=True,
        null=True
    )

    City= models.CharField(
        max_length=25,
        verbose_name="City",
        help_text="City"
    )

    County= models.CharField(
        max_length=25,
        verbose_name="County",
        help_text="County"
    )

    State= models.CharField(
        max_length=25,
        verbose_name="State",
        help_text="State"
    )

    Postcode= models.CharField(
        max_length=25,
        verbose_name="Postcode",
        help_text="Postcode"
    )

    Country_code= models.CharField(
        max_length=25,
        verbose_name="Country_code",
        help_text="Country_code"
    )

    latitude= models.CharField(
        max_length=25,
        verbose_name="latitude",
        help_text="latitude"
    )

    longitude= models.CharField(
        max_length=25,
        verbose_name="longitude",
        help_text="longitude"
    )

    lobby= models.TextField(
        max_length=2555,
        verbose_name="lobby",
        help_text="lobby"
    )

    Drive_up=models.TextField(
        max_length=2555,
        verbose_name="Drive_up",
        help_text="Drive_up"
    )

    replica_id = models.IntegerField(
        verbose_name="Replica id",
        help_text="Test Replica id",
        default= 1
    )

    remark = models.CharField(
        max_length=255,
        verbose_name="remark",
        help_text="remark",
        blank=True,
        null=True,
    )

    is_deleted = models.IntegerField(
        verbose_name="Deleted",
        help_text="Deleted",
        default=0,
        null=False
    )

    class Meta:
        verbose_name = 'Test Profile Operation'
        verbose_name_plural = 'Test Profile Operation'

    def __str__(self):
        return "profile_id:\t{}\noperationid:\t{}\n".format(self.profile_id,self.operation_id)
