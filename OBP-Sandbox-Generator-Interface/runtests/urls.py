# -*- coding: utf-8 -*-
"""
URLs for runtests app
"""

from django.conf.urls import url

from .views import (
    IndexView,
    RunView,
    TestConfigurationCreateView,
    TestConfigurationUpdateView,
    TestConfigurationDeleteView,
    UserCreateView,
    DataImportView,
    BankCreateView,
    BranchCreateView,
    GenerateJsonView,
    CounterpartyUpdateView,
    GenerateFile,
    ImportJson,
    ImportCounterparty,
    ImportCustomer,
    saveJsonBody,
    copyJsonBody, deleteJsonBody)




urlpatterns = [
    url(r'^$',
        IndexView.as_view(),
        name='runtests-index'),
    url(r'^(?P<testconfig_pk>[0-9]+)',
        IndexView.as_view(),
        name='runtests-index-testconfig'),
    url(r'^run/(?P<testmethod>\w+)/(?P<testpath>.+)/(?P<testconfig_pk>[0-9]+)/(?P<operation_id>.+)',
        RunView.as_view(),
        name='runtests-run'),

    url(r'import_data/$',
        DataImportView.as_view(),
        name='import-data'),

    url(r'generate_file$',
        GenerateFile,
        name='generate-file'),

    url(r'import_json$',
        ImportJson,
        name='import-json'
    ),

    url(r'import_counterparty$',
        ImportCounterparty,
        name='import-counterparty'
        ),

    url(r'import_customer$',
        ImportCustomer,
        name='import-customer'
        ),

    url(r'generate_json/$',
        GenerateJsonView.as_view(),
        name='generate-json'),

    url(r'user/add/$',
        UserCreateView.as_view(),
        name='runtests-user-add'),

    url(r'bank/add/$',
        BankCreateView.as_view(),
        name='runtests-bank-add'),

    url(r'branch/add/$',
        BranchCreateView.as_view(),
        name='runtests-branch-add'),

    url(r'counterparty/update/$',
        CounterpartyUpdateView.as_view(),
        name='runtests-counterparty-update'),

    url(r'testconfig/add/$',
        TestConfigurationCreateView.as_view(),
        name='runtests-testconfig-add'),
    url(r'testconfig/(?P<pk>[0-9]+)/$',
        TestConfigurationUpdateView.as_view(),
        name='runtests-testconfig-update'),
    url(r'testconfig/(?P<pk>[0-9]+)/delete/$',
        TestConfigurationDeleteView.as_view(),
        name='runtests-testconfig-delete'),
    url(r'save/json_body', saveJsonBody,
        name='runtests-save-json_body'),
    url(r'copy/json_body', copyJsonBody,
        name='runtests-copy-json_body'),
    url(r'delete/json_body', deleteJsonBody,
        name='runtests-delete-json_body'),

]
